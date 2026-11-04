"""All numbers for the paper. Inputs: the database snapshot, data/flags.csv, data/three_reader.csv,
data/author_review.csv (author's review of disagreements) and data/author_spot30.csv (spot check)."""
import json, os, csv, math, re, collections, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import SNAPSHOT as SRC, DATA, RESULTS, wilson as wil
os.chdir(DATA)
S = {}
# per-label metadata
meta = {}
for f in os.listdir(SRC):
    if not f.endswith('.json'): continue
    d = json.load(open(f'{SRC}/{f}'))
    ss = (d.get('servingSizes') or [{}])[0]
    meta[str(d['id'])] = dict(year=(d.get('entryDate') or '')[:4], off=d.get('offMarket'), nh=bool(d.get('nhanesId')),
                              maxd=ss.get('maxDailyServings') or 1)
S['labels'] = len(meta); S['nhanes_labels'] = sum(m['nh'] for m in meta.values())
F = list(csv.DictReader(open('flags.csv')))
U = [f for f in F if f['cls'] == 'unit_1000x']
S['flag_rows'] = len(F); S['unit_rows'] = len(U); S['unit_labels'] = len({f['id'] for f in U})
S['unit_rows_adult'] = sum('Adults' in f['target'] for f in U)
S['cls'] = dict(collections.Counter(f['cls'] for f in F))
# per year rate per 1,000 labels
yl = collections.Counter(m['year'] for m in meta.values()); yu = collections.Counter(meta[i]['year'] for i in {f['id'] for f in U})
S['by_year'] = {y: (yl[y], yu.get(y, 0), round(1000*yu.get(y, 0)/yl[y], 2)) for y in sorted(yl) if yl[y] >= 500}
# on/off market
for k in ['0', '1']:
    n = sum(1 for m in meta.values() if str(int(bool(m['off']))) == k); u = sum(1 for i in {f['id'] for f in U} if str(int(bool(meta[i]['off']))) == k)
    S[f'market_{k}'] = (n, u, round(1000*u/n, 2))
S['nhanes_unit_labels'] = sum(meta[i]['nh'] for i in {f['id'] for f in U})
CNT = json.load(open('flags_counts.json'))
S['rows_checked'] = CNT['rows_checked']
nut = collections.Counter(f['group'] for f in U)
S['by_nutrient'] = sorted([(k, CNT['checked:'+k], nut[k], round(1000*nut[k]/CNT['checked:'+k], 2)) for k in nut], key=lambda x: -x[2])
# verification: three blind readers, majority vote (data/three_reader.csv, written by three_readers.py);
# rows reviewed by the author (data/author_review.csv, optional) replace the majority verdict
A = list(csv.DictReader(open('three_reader.csv')))
REV = {}
if os.path.exists('author_review.csv'):
    REV = {r['key']: r['final'] for r in csv.DictReader(open('author_review.csv'))}
for r in A: r['majority'] = r['final']; r['final'] = REV.get(r['key'], r['final'])
S['author_reviewed_rows'] = len(REV)
w = csv.DictWriter(open('final_verdicts.csv', 'w', newline=''), fieldnames=list(A[0].keys())); w.writeheader(); w.writerows(A)
CHILD = re.compile(r'Children less than 4|Infants')  # %DV target population of the row
def share(R):
    c = collections.Counter(r['final'] for r in R); n = c['DB_error'] + c['label_misprint']
    lo, hi = wil(c['DB_error'], n); return dict(c, n=len(R), resolved=n, share=c['DB_error']/n, lo=lo, hi=hi)
for cls in ['unit_1000x', 'decimal_10x']:
    R = [r for r in A if r['cls'] == cls]
    S[f'adj_{cls}'] = share(R)
    S[f'adj_{cls}_not_child_target'] = share([r for r in R if not CHILD.search(r['target'])])
    S[f'child_target_{cls}'] = sum(bool(CHILD.search(r['target'])) for r in R)
    S[f'unanimous_{cls}'] = sum(r['unanimous'] == 'True' for r in R)
    S[f'adj_{cls}_unanimous_only'] = share([r for r in R if r['unanimous'] == 'True'])
    # lone dissenter: the other two readers agree and this reader differs, by direction
    for m in ['sonnet', 'opus', 'gemini']:
        o = [x for x in ['sonnet', 'opus', 'gemini'] if x != m]
        S[f'lone_{m}_{cls}'] = dict(collections.Counter(f"{r[o[0]]}->{r[m]}" for r in R if r[o[0]] == r[o[1]] and r[m] != r[o[0]]))
    for a, b in [('sonnet', 'opus'), ('sonnet', 'gemini'), ('opus', 'gemini')]:
        S[f'agree_{a}_{b}_{cls}'] = sum(r[a] == r[b] for r in R)
U_ = S['adj_unit_1000x']
S['extrap_db_unit_rows'] = (round(S['unit_rows']*U_['lo']), round(S['unit_rows']*U_['share']), round(S['unit_rows']*U_['hi']))
# spot check: random sample (seed 20261104) of unanimous database-error rows, read by the author without the readers' outputs
if os.path.exists('author_spot30.csv'):
    SP = list(csv.DictReader(open('author_spot30.csv')))
    k = sum(r['final'] == 'DB_error' for r in SP); n = len(SP); lo, hi = wil(k, n)
    S['spot_unanimous_db'] = dict(confirmed=k, n=n, lo=lo, hi=hi, pool=sum(r['cls'] == 'unit_1000x' and r['unanimous'] == 'True' and r['majority'] == 'DB_error' for r in A))
    # worst case within the CI: the unconfirmed fraction (1 - lower bound) of unanimous DB errors are label misprints
    U2 = S['adj_unit_1000x']; pool = S['spot_unanimous_db']['pool']; moved = round(pool * (1 - lo))
    S['adj_unit_spot_lower'] = dict(moved=moved, share=(U2['DB_error'] - moved) / U2['resolved'])
# agreement statistics over three categories
CATS = ['DB_error', 'label_misprint', 'unresolved']
def kappa(R, a, b):
    n = len(R); po = sum(r[a] == r[b] for r in R)/n
    pe = sum((sum(r[a] == c for r in R)/n)*(sum(r[b] == c for r in R)/n) for c in CATS); return (po-pe)/(1-pe)
def fleiss(R):
    n, k = len(R), 3; rows = [[r['sonnet'], r['opus'], r['gemini']] for r in R]
    P = [(sum(x.count(c)**2 for c in CATS) - k)/(k*(k-1)) for x in rows]
    p = [sum(x.count(c) for x in rows)/(n*k) for c in CATS]; Pe = sum(q*q for q in p); return (sum(P)/n - Pe)/(1 - Pe)
for name, R in [('unit', [r for r in A if r['cls'] == 'unit_1000x']), ('all', A)]:
    S[f'fleiss_{name}'] = fleiss(R)
    for a, b in [('sonnet', 'opus'), ('sonnet', 'gemini'), ('opus', 'gemini')]: S[f'kappa_{a}_{b}_{name}'] = kappa(R, a, b)
# UL: applicability rules in ul_analysis.py, applied to verified unit errors
from ul_analysis import assess, per_day
FF = {(f['id'], f['name']): f for f in F}
DBerr = [r for r in A if r['cls'] == 'unit_1000x' and r['final'] == 'DB_error']
st = collections.Counter(); fl = collections.Counter()
for r in DBerr:
    f = FF[(r['id'], r['name'])]; rec = json.load(open(f'{SRC}/{r["id"]}.json'))
    s_, db, true, ul = assess(f, rec); st[s_] += 1
    if s_ != 'assessed': continue
    for basis, m in [('serving', 1.0), ('day', per_day(rec))]:
        d, t = db*m, true*m
        fl[(basis, 'db over, true under' if d > ul and t <= ul else 'db under, true over' if d <= ul and t > ul else 'same side')] += 1
S['ul_applicability'] = dict(st); S['ul_flips'] = {f'{b}: {k}': v for (b, k), v in fl.items()}
S['ul_not_assessable_units'] = dict(collections.Counter(FF[(r['id'], r['name'])]['unit'] for r in DBerr
                                    if assess(FF[(r['id'], r['name'])], json.load(open(f'{SRC}/{r["id"]}.json')))[0] == 'unit not assessable'))
S['db_direction_verified'] = dict(collections.Counter('DB 1000x too large' if float(FF[(r['id'], r['name'])]['ratio']) > 1 else 'DB 1000x too small' for r in DBerr))
byn = collections.defaultdict(collections.Counter)
for r in A:
    if r['cls'] == 'unit_1000x': byn[FF[(r['id'], r['name'])]['group']][r['final']] += 1
S['verified_by_nutrient'] = sorted([(k, v['DB_error'], v['DB_error'] + v['label_misprint']) for k, v in byn.items()], key=lambda x: -x[2])
# significance tests for differences reported in the paper (Pearson chi-square without continuity correction)
import numpy as np
from scipy.stats import chi2_contingency, norm
def c2(t):
    r = chi2_contingency(np.array(t), correction=False); return dict(chi2=round(float(r[0]), 2), df=int(r[2]), p=float(r[1]))
(n0, u0, _), (n1, u1, _) = S['market_0'], S['market_1']
S['test_market'] = c2([[u0, n0-u0], [u1, n1-u1]])
nh, NH, Nl, Ul = S['nhanes_unit_labels'], S['nhanes_labels'], S['labels'], S['unit_labels']
S['rate_non_nhanes'] = round(1000*(Ul-nh)/(Nl-NH), 2)
S['test_nhanes'] = c2([[nh, NH-nh], [Ul-nh, (Nl-NH)-(Ul-nh)]])
yrs = [y for y in sorted(S['by_year']) if 2012 <= int(y) <= 2025]
ta = [[S['by_year'][y][1], S['by_year'][y][0]-S['by_year'][y][1]] for y in yrs]
S['test_year_homogeneity_2012_2025'] = c2(ta)
x = np.array([int(y) for y in yrs], float); a = np.array([r[0] for r in ta], float); n = np.array([sum(r) for r in ta], float)
pp = a.sum()/n.sum(); T = np.sum(x*(a-n*pp)); Vv = pp*(1-pp)*(np.sum(n*x*x)-np.sum(n*x)**2/n.sum()); z = T/np.sqrt(Vv)
S['test_year_trend_2012_2025'] = dict(z=round(float(z), 2), p=float(2*norm.sf(abs(z))))  # Cochran-Armitage
y11 = S['by_year']['2011']; S['test_2011_vs_rest'] = c2([[y11[1], y11[0]-y11[1]], [a.sum(), n.sum()-a.sum()]])
VN = [v for v in S['verified_by_nutrient'] if v[2] >= 10]
S['test_share_by_nutrient'] = dict(c2([[v[1], v[2]-v[1]] for v in VN]), nutrients=len(VN))
uu, dd = S['adj_unit_1000x'], S['adj_decimal_10x']
S['test_unit_vs_10x_share'] = c2([[uu['DB_error'], uu['resolved']-uu['DB_error']], [dd['DB_error'], dd['resolved']-dd['DB_error']]])
json.dump(S, open(os.path.join(RESULTS, 'stats.json'), 'w'), indent=1, default=str)
for k, v in S.items(): print(k, ':', v)
