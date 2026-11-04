"""Three independent readers from two vendors (Claude Sonnet 5.5, Claude Opus 5.5, Gemini 4 Argon), all blind to the
database value. Final verdict = majority (at least 2 of 3 readers agree); no majority -> unresolved.
Writes data/three_reader.csv and results/three_readers.json."""
import json, os, sys, csv, collections, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import DATA, RESULTS, wilson
from adjudicate import read, verdict
import re

def read_gemini(path):
    try: return json.loads(re.findall(r'\{[^{}]*\}', json.load(open(path))['text'], re.S)[-1])
    except Exception: return None

CATS = ['DB_error', 'label_misprint', 'unresolved']
def kappa(a, b):
    n = len(a); po = sum(x == y for x, y in zip(a, b)) / n
    pe = sum((a.count(c) / n) * (b.count(c) / n) for c in CATS); return (po - pe) / (1 - pe)
def fleiss(rows):
    n, k = len(rows), 3
    P = [(sum(r.count(c) ** 2 for c in CATS) - k) / (k * (k - 1)) for r in rows]
    p = [sum(r.count(c) for r in rows) / (n * k) for c in CATS]
    Pb, Pe = sum(P) / n, sum(x * x for x in p); return (Pb - Pe) / (1 - Pe)

flags = list(csv.DictReader(open(os.path.join(DATA, 'flags.csv')))); n_flags = collections.Counter(f['cls'] for f in flags)
rows = []
for sample, sdir, tag in [('sample_round1.json', 'sonnet_round1', 'a'), ('sample_round2.json', 'sonnet_round2', 'b')]:
    for k, f in enumerate(json.load(open(os.path.join(DATA, sample)))):
        key = f'{tag}{k}'
        v = {'sonnet': verdict(f, read(os.path.join(DATA, 'readers', sdir, f'{k}_{f["id"]}.json'))),
             'opus': verdict(f, read(os.path.join(DATA, 'readers', 'opus', f'{key}_{f["id"]}.json'))),
             'gemini': verdict(f, read_gemini(os.path.join(DATA, 'readers', 'gemini', f'{key}_{f["id"]}.json')))}
        c = collections.Counter(v.values()); top, cnt = c.most_common(1)[0]
        final = top if cnt >= 2 else 'unresolved'
        rows.append(dict(key=key, id=f['id'], cls=f['cls'], name=f['name'], amount=f['amount'], unit=f['unit'], pct=f['pct'],
                         target=f['target'], **v, final=final, unanimous=cnt == 3))
w = csv.DictWriter(open(os.path.join(DATA, 'three_reader.csv'), 'w', newline=''), fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

S = {}
for cls in ['unit_1000x', 'decimal_10x', 'all']:
    R = rows if cls == 'all' else [r for r in rows if r['cls'] == cls]
    res = {'n': len(R)}
    for a, b in itertools.combinations(['sonnet', 'opus', 'gemini'], 2):
        A, B = [r[a] for r in R], [r[b] for r in R]
        res[f'{a}-{b}'] = {'agree': sum(x == y for x, y in zip(A, B)), 'kappa': round(kappa(A, B), 3)}
    res['fleiss_kappa'] = round(fleiss([[r['sonnet'], r['opus'], r['gemini']] for r in R]), 3)
    res['unanimous'] = sum(r['unanimous'] for r in R)
    c = collections.Counter(r['final'] for r in R); res['final'] = dict(c)
    n = c['DB_error'] + c['label_misprint']
    if n:
        lo, hi = wilson(c['DB_error'], n); res['db_share'] = (c['DB_error'], n, c['DB_error'] / n, lo, hi)
        if cls in n_flags: res['extrapolated'] = (round(n_flags[cls] * lo), round(n_flags[cls] * c['DB_error'] / n), round(n_flags[cls] * hi))
    # each reader against the majority, on rows with a majority
    M = [r for r in R if r['final'] != 'unresolved']
    for m in ['sonnet', 'opus', 'gemini']:
        res[f'{m}_vs_majority'] = (sum(r[m] == r['final'] for r in M), len(M))
    S[cls] = res
json.dump(S, open(os.path.join(RESULTS, 'three_readers.json'), 'w'), indent=1)
for cls, res in S.items(): print(cls, json.dumps(res, indent=None))
