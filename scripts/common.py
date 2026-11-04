"""Shared paths and helpers. Set DSLD_SNAPSHOT to the unzipped export folder
(default: data/snapshot/DSLD-full-database-JSON) and DSLD_LABELS to the folder of
rendered label images (default: data/labels)."""
import os, math, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAPSHOT = os.environ.get('DSLD_SNAPSHOT', os.path.join(ROOT, 'data', 'snapshot', 'DSLD-full-database-JSON'))
LABELS = os.environ.get('DSLD_LABELS', os.path.join(ROOT, 'data', 'labels'))
DATA = os.path.join(ROOT, 'data'); RESULTS = os.path.join(ROOT, 'results')

def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n; c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return c - h, c + h

def norm_unit(u):
    return re.sub(r'[^a-z]', '', (u or '').lower().replace('µ', 'mc').replace('μ', 'mc')).replace('ug', 'mcg')
