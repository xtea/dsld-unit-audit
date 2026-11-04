"""Write the list of verified rows shared with the database maintainers: results/dsld_verified_rows.csv.
One row per sampled flagged row: database values, the printed values (author's reading where the author reviewed
the row, otherwise the reading of a model reader whose verdict matches the final verdict), the verdict and its basis."""
import csv, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import DATA, RESULTS
from adjudicate import read
def rg(p):
    try: return json.loads(re.findall(r'\{[^{}]*\}', json.load(open(p))['text'], re.S)[-1])
    except Exception: return None
V = list(csv.DictReader(open(os.path.join(DATA, 'final_verdicts.csv'))))
AR = {r['key']: r for r in csv.DictReader(open(os.path.join(DATA, 'author_review.csv')))}
SP = {r['key']: r for r in csv.DictReader(open(os.path.join(DATA, 'author_spot30.csv')))}
TEXT = {'DB_error': 'database differs from label', 'label_misprint': 'label printed as stored (label inconsistency)',
        'unresolved': 'unresolved', 'not_error': "not an error (%DV based on a children's Daily Value)",
        'column_or_serving': 'database took %DV from another column', 'image_mismatch': 'image and record differ'}
out = []
for r in V:
    k, i = r['key'], r['id']; n = int(k[1:]); sdir = 'sonnet_round1' if k[0] == 'a' else 'sonnet_round2'
    reads = {'opus': read(os.path.join(DATA, 'readers', 'opus', f'{k}_{i}.json')),
             'gemini': rg(os.path.join(DATA, 'readers', 'gemini', f'{k}_{i}.json')),
             'sonnet': read(os.path.join(DATA, 'readers', sdir, f'{n}_{i}.json'))}
    rev = AR.get(k) or SP.get(k)
    if rev: pa, pu, pp = rev['printed_amount'], rev['printed_unit'], rev['printed_pct']
    else:
        m = next((m for m in ['opus', 'gemini', 'sonnet'] if r[m] == r['final'] and reads[m]), None)
        o = reads[m] if m else {}
        pa, pu, pp = o.get('printed_amount', ''), o.get('printed_unit', ''), o.get('printed_percent_dv', '')
    basis = ('author review of reader disagreement' if k in AR else 'three readers agree; author spot check' if k in SP
             else 'three readers agree' if r['unanimous'] == 'True' else 'two of three readers')
    out.append(dict(dsld_id=i, ingredient=r['name'], flag_class=r['cls'], db_amount=r['amount'], db_unit=r['unit'], db_percent_dv=r['pct'],
                    label_amount=pa, label_unit=pu, label_percent_dv=pp if pp is not None else '', verdict=TEXT[r['final']], basis=basis))
w = csv.DictWriter(open(os.path.join(RESULTS, 'dsld_verified_rows.csv'), 'w', newline=''), fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
from collections import Counter
print(len(out), Counter((o['flag_class'], o['verdict']) for o in out))
