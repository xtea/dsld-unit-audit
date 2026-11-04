"""Upper-limit (UL) impact of verified database unit errors, with explicit applicability rules.

A verified error is assessed only when
  (1) the nutrient has an adult UL from the Institute of Medicine DRIs,
  (2) the UL applies to the declared form (rules below), and
  (3) the product targets adults: no target group names infants, children, girls or boys.
Rows that fail (2) because the form cannot be determined are counted as 'form undetermined'.

Form rules
  vitamin A   UL covers preformed vitamin A only. Assessed when every listed form is a retinol or
              retinyl ester; rows listing any carotenoid form, or no form, are not assessed.
  folate      UL covers synthetic folic acid only. Assessed when every listed form is folic acid;
              mcg DFE is converted to mcg folic acid by dividing by 1.7. Methylfolate or folinate: not assessed.
  magnesium   UL covers supplemental magnesium; every supplement form counts.
  niacin      UL covers supplemental nicotinic acid and nicotinamide; inositol hexanicotinate is not assessed.
  vitamin E   UL covers any form of supplemental alpha-tocopherol; only mg declarations are assessed.
  others      the UL applies to total intake and to any form.
Calcium uses 2,000 mg for products whose target groups name adults over 50, otherwise 2,500 mg.
"""
import json, os, csv, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import SNAPSHOT, DATA, RESULTS

UL = {'iodine': 1100, 'vitamin a': 3000, 'vitamin d': 100, 'vitamin c': 2000e3, 'niacin': 35e3, 'vitamin b6': 100e3,
      'folate': 1000, 'calcium': 2500e3, 'iron': 45e3, 'magnesium': 350e3, 'zinc': 40e3, 'selenium': 400, 'copper': 10e3,
      'manganese': 11e3, 'molybdenum': 2000, 'choline': 3500e3, 'vitamin e': 1000e3, 'phosphorus': 4000e3, 'chloride': 3600e3}
TO = {'mcg': 1, 'mg': 1e3, 'g': 1e6, 'mcgdfe': 1, 'mcgrae': 1, 'mgne': 1e3, 'mgate': 1e3}
CHILD = re.compile(r'child|infant|baby|girl|boy|teen|toddler', re.I)
OVER50 = re.compile(r'>50|over 50|senior|mature', re.I)

def forms_of(row):
    return [(f.get('name') or '').lower() for f in (row.get('forms') or [])]

def find_row(rec, name):
    def walk(rows):
        for r in rows:
            if r.get('name') == name: return r
            x = walk(r.get('nestedRows') or [])
            if x: return x
    return walk(rec.get('ingredientRows') or [])

def assess(flag, rec):
    """Return (status, db_amount_mcg, true_amount_mcg, ul_mcg) or (status, None, None, None)."""
    g = flag['group']
    if g not in UL: return ('no UL', None, None, None)
    if any(CHILD.search(t) for t in (rec.get('targetGroups') or [])): return ('not adult product', None, None, None)
    u = re.sub(r'[^a-z]', '', flag['unit'].lower())
    if u not in TO: return ('unit not assessable', None, None, None)
    row = find_row(rec, flag['name']) or {}
    fm = forms_of(row)
    db = float(flag['amount']) * TO[u]
    if g == 'vitamin a':
        if not fm or not all(re.search(r'retin', f) for f in fm): return ('form undetermined', None, None, None)
    if g == 'folate':
        if not fm or not all('folic acid' in f for f in fm): return ('form undetermined', None, None, None)
        if 'dfe' in u: db = db / 1.7
    if g == 'niacin' and any('inositol' in f for f in fm): return ('form undetermined', None, None, None)
    if g == 'vitamin e' and u != 'mg': return ('unit not assessable', None, None, None)
    ul = UL[g]
    if g == 'calcium' and any(OVER50.search(t) for t in (rec.get('targetGroups') or [])): ul = 2000e3
    true = db / 1000 if float(flag['ratio']) > 1 else db * 1000
    return ('assessed', db, true, ul)

def per_day(rec):
    ss = (rec.get('servingSizes') or [{}])[0]
    return float(ss.get('maxDailyServings') or 1)

if __name__ == '__main__':
    adj_file = sys.argv[1] if len(sys.argv) > 1 else os.path.join(DATA, 'final_verdicts.csv')
    flags = {(f['id'], f['name']): f for f in csv.DictReader(open(os.path.join(DATA, 'flags.csv')))}
    rows = [r for r in csv.DictReader(open(adj_file)) if r['cls'] == 'unit_1000x' and r['final'] == 'DB_error']
    status = collections.Counter(); flips = collections.Counter(); out = []
    for r in rows:
        f = flags[(r['id'], r['name'])]; rec = json.load(open(os.path.join(SNAPSHOT, f'{r["id"]}.json')))
        st, db, true, ul = assess(f, rec); status[st] += 1
        if st != 'assessed': continue
        for basis, m in [('serving', 1.0), ('day', per_day(rec))]:
            d, t = db * m, true * m
            k = 'db over, true under' if d > ul and t <= ul else 'db under, true over' if d <= ul and t > ul else 'same side'
            flips[(basis, k)] += 1
            out.append(dict(key=r['key'], id=r['id'], nutrient=f['group'], basis=basis, db_mcg=round(d, 3), true_mcg=round(t, 3), ul_mcg=ul, result=k))
    print('verified DB unit errors:', len(rows)); print('applicability:', dict(status))
    for basis in ['serving', 'day']:
        n = sum(v for (b, _), v in flips.items() if b == basis)
        print(basis, {k: v for (b, k), v in flips.items() if b == basis}, 'of', n)
    if out:
        w = csv.DictWriter(open(os.path.join(RESULTS, 'ul_assessment.csv'), 'w', newline=''), fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
