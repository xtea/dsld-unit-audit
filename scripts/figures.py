import json, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import RESULTS
S = json.load(open(os.path.join(RESULTS, 'stats.json'))); OUT = RESULTS + '/'
plt.rcParams.update({'font.family': 'serif', 'font.size': 9})
nut = sorted(S['by_nutrient'], key=lambda x: x[3])
fig, ax = plt.subplots(figsize=(5.2, 5.0))
ax.barh([n[0].replace('vitamin', 'vit.') for n in nut], [n[3] for n in nut], color='#4a6fa5')
for i, n in enumerate(nut): ax.text(n[3] + 0.1, i, f'{n[2]}', va='center', fontsize=7, color='#444')
ax.set_xlabel('Unit-flagged rows per 1,000 checkable rows'); ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout(); plt.savefig(OUT + 'fig1_by_nutrient.pdf'); plt.close()
yrs = sorted(S['by_year']); fig, ax = plt.subplots(figsize=(5.2, 2.6))
ax.plot([int(y) for y in yrs], [S['by_year'][y][2] for y in yrs], marker='o', color='#4a6fa5')
ax.set_ylabel('Labels with ≥1 flag\nper 1,000 labels entered'); ax.set_xlabel('Year entered into the database')
ax.set_ylim(0, None); ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout(); plt.savefig(OUT + 'fig2_by_year.pdf'); plt.close(); print('ok')
