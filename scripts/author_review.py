"""Read the author's filled-in review files and write the verdict tables used by stats.py.

  data/author_review30.md -> data/author_review.csv   (the 30 rows on which the three readers disagreed)
  data/author_spot30.md   -> data/author_spot30.csv   (random sample of 30 unanimous database-error rows)

Each row in a review file is a section headed '### <n>. <key> · <name> · ...' followed by a one-row table:
printed amount | printed unit | printed %DV | category | note. Categories are the eight codes in the
paper (Supplementary Appendix D); rows without a category are skipped."""
import csv, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import DATA
FINAL = {'DB_UNIT': 'DB_error', 'DB_AMOUNT': 'DB_error', 'DB_PCT': 'DB_error', 'LABEL_INCONSISTENT': 'label_misprint',
         'CANNOT_DETERMINE': 'unresolved', 'OTHER_DV_BASIS': 'not_error', 'COLUMN_OR_SERVING': 'column_or_serving',
         'IMAGE_MISMATCH': 'image_mismatch'}
COLS = ['key', 'category', 'final', 'printed_amount', 'printed_unit', 'printed_pct', 'note']

def parse(md):
    rows = []
    for sec in re.split(r'^### ', open(md).read(), flags=re.M)[1:]:
        key = sec.split('\n')[0].split(' · ')[0].split('. ', 1)[1].strip()
        table = [l for l in sec.split('\n') if l.startswith('|')]
        c = [x.strip() for x in table[2].strip().strip('|').split('|')]
        if c[3]:
            rows.append(dict(key=key, printed_amount=c[0], printed_unit=c[1], printed_pct=c[2], category=c[3],
                             final=FINAL[c[3]], note=c[4] if len(c) > 4 else ''))
    return rows

for src, out in [('author_review30.md', 'author_review.csv'), ('author_spot30.md', 'author_spot30.csv')]:
    rows = parse(os.path.join(DATA, src))
    w = csv.DictWriter(open(os.path.join(DATA, out), 'w', newline=''), fieldnames=COLS); w.writeheader(); w.writerows(rows)
    print(f'{src}: {len(rows)} reviewed rows -> {out}')
