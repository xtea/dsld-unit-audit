"""Turn a reader's printed reading into a verdict for a flagged row (rules in the paper, Methods)."""
import json, re, csv, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import DATA, norm_unit, wilson

def close(a, b):
    try: return abs(float(a) - float(b)) <= 0.011 * max(abs(float(b)), 1e-9) + 1e-9
    except Exception: return False

def read(path):
    try: return json.loads(re.findall(r'\{[^{}]*\}', open(path).read(), re.S)[-1])
    except Exception: return None

def verdict(f, o):
    if not o or o.get('legible') is False or o.get('printed_amount') is None: return 'unresolved'
    same_u = norm_unit(o.get('printed_unit'))[:3] == norm_unit(f['unit'])[:3]
    same_a = close(o.get('printed_amount'), f['amount'])
    same_p = o.get('printed_percent_dv') is None or close(o.get('printed_percent_dv'), f['pct'])
    if f['cls'] == 'unit_1000x':
        return 'label_misprint' if same_u and same_a else 'DB_error' if not same_u else 'unresolved'
    return 'label_misprint' if same_u and same_a and same_p else 'DB_error' if same_u else 'unresolved'
