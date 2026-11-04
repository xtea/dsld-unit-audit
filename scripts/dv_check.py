"""%DV consistency check over the full database export. For each Supplement Facts row with a declared amount and %DV,
implied DV = amount / (%DV/100) is compared with FDA reference DVs (2016 set and pre-2016 set).
Rows >=5x away from every reference value are flagged and classed by magnitude:
~1000x -> unit (mg/mcg) error, ~10x -> decimal / %DV digit error, other -> unclassified.
Matching uses ingredientGroup (not the free-text name), which removes 'calcium D-pantothenate -> calcium'."""
import json, os, re, sys, math, csv, glob
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import SNAPSHOT, DATA
import argparse
ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument('--snapshot', default=SNAPSHOT)
ap.add_argument('--out', default=os.path.join(DATA, 'flags.csv'))
ap.add_argument('--dv-set', choices=['both', '2016'], default='both', help="'2016' = 2016 Daily Values only, no IU (sensitivity)")
args = ap.parse_args(); SRC = args.snapshot; OUT = args.out
TO_MCG = {'mcg': 1, 'µg': 1, 'μg': 1, 'ug': 1, 'mg': 1e3, 'g': 1e6, 'mcgdfe': 1, 'mcgrae': 1, 'mgne': 1e3, 'mgate': 1e3, 'mgαte': 1e3}
# (new 2016 DVs in mcg, pre-2016 DVs in mcg, pre-2016 IU DVs)
DV = {'vitamin a': ([900], [], [5000]), 'vitamin c': ([90e3], [60e3], []), 'vitamin d': ([20], [10], [400]),
      'vitamin e': ([15e3], [], [30]), 'vitamin k': ([120], [80], []), 'thiamin': ([1.2e3], [1.5e3], []),
      'riboflavin': ([1.3e3], [1.7e3], []), 'niacin': ([16e3], [20e3], []), 'vitamin b6': ([1.7e3], [2e3], []),
      'folate': ([400], [400], []), 'vitamin b12': ([2.4], [6], []), 'biotin': ([30], [300], []),
      'pantothenic acid': ([5e3], [10e3], []), 'calcium': ([1300e3], [1000e3], []), 'iron': ([18e3], [18e3], []),
      'iodine': ([150], [150], []), 'magnesium': ([420e3], [400e3], []), 'zinc': ([11e3], [15e3], []),
      'selenium': ([55], [70], []), 'copper': ([900], [2000], []), 'manganese': ([2.3e3], [2e3], []),
      'chromium': ([35], [120], []), 'molybdenum': ([45], [75], []), 'chloride': ([2300e3], [3400e3], []),
      'potassium': ([4700e3], [3500e3], []), 'phosphorus': ([1250e3], [1000e3], []), 'choline': ([550e3], [], [])}
def key(g):
    n = (g or '').lower().replace('-', ' ').strip()
    n = re.sub(r'^vitamin b ?1\b.*|^thiamine?\b.*', 'thiamin', n); n = re.sub(r'^vitamin b ?2\b.*', 'riboflavin', n)
    n = re.sub(r'^vitamin b ?3\b.*', 'niacin', n); n = re.sub(r'^vitamin b ?5\b.*', 'pantothenic acid', n)
    n = re.sub(r'^vitamin b ?9\b.*|^folic acid.*', 'folate', n); n = re.sub(r'^vitamin b ?6\b.*', 'vitamin b6', n)
    n = re.sub(r'^vitamin b ?12\b.*', 'vitamin b12', n); n = re.sub(r'^vitamin d ?[23]?\b.*', 'vitamin d', n)
    n = re.sub(r'^vitamin k ?[12]?\b.*', 'vitamin k', n)
    for k in DV:
        if n == k or n.startswith(k + ' (') : return k
    return None
def labels():
    files = sorted(glob.glob(f'{SRC}/**/*.json', recursive=True))
    for f in files:
        d = json.load(open(f))
        for x in (d if isinstance(d, list) else [d]):
            if isinstance(x, dict) and 'ingredientRows' in x: yield x
stats = Counter(); flags = []
for d in labels():
    stats['labels'] += 1
    def walk(rows):
        for r in rows:
            k = key(r.get('ingredientGroup')) or key(r.get('name'))
            if k:
                for q in (r.get('quantity') or [])[:1]:
                    tg = (q.get('dailyValueTargetGroup') or [{}])[0]
                    pct, amt = tg.get('percent'), q.get('quantity')
                    unit = re.sub(r'[^a-zµμα]', '', (q.get('unit') or '').lower())
                    if not pct or not amt or pct < 2 or tg.get('operator') not in (None, '='): continue
                    new, old, iu = DV[k]
                    if unit == 'iu': refs = iu if args.dv_set == 'both' else []; implied = amt / (pct / 100)
                    elif unit in TO_MCG: refs = (new + old) if args.dv_set == 'both' else new; implied = amt * TO_MCG[unit] / (pct / 100)
                    else: continue
                    if not refs: continue
                    stats['rows_checked'] += 1; stats['checked:' + k] += 1
                    ratio = min((implied / x for x in refs), key=lambda z: abs(math.log(z)))
                    if ratio >= 5 or ratio <= 0.2:
                        fits = lambda m: any(0.5 <= implied * m / x <= 2 for x in refs)
                        cls = 'unit_1000x' if fits(1e-3) or fits(1e3) else 'decimal_10x' if fits(0.1) or fits(10) else 'other'
                        flags.append(dict(id=d.get('id'), brand=d.get('brandName'), product=d.get('fullName'),
                                          entry=d.get('entryDate'), offMarket=d.get('offMarket'), nhanes=bool(d.get('nhanesId')),
                                          group=k, name=r.get('name'), amount=amt, unit=q.get('unit'), pct=pct,
                                          target=tg.get('name'), ratio=round(ratio, 4), cls=cls))
            walk(r.get('nestedRows') or [])
    walk(d.get('ingredientRows') or [])
with open(OUT, 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(flags[0].keys()) if flags else ['id']); w.writeheader(); w.writerows(flags)
json.dump(dict(stats), open(os.path.splitext(OUT)[0] + '_counts.json', 'w'), indent=1)
print({k: v for k, v in stats.items() if ':' not in k}, 'flagged rows', len(flags), 'labels flagged', len({f['id'] for f in flags}))
print(Counter(f['cls'] for f in flags)); print(Counter(f['group'] for f in flags if f['cls'] == 'unit_1000x').most_common(10))
