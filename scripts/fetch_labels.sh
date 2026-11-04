#!/bin/bash
# Download the label PDF of each sampled label from the database's public file service and render it at 300 dpi.
# Usage: bash scripts/fetch_labels.sh [out_dir]   (default: data/labels_png; needs curl and poppler's pdftoppm)
set -e
cd "$(dirname "$0")/.."
OUT="${1:-data/labels_png}"; mkdir -p "$OUT/pdf"
python3 -c "import json; [print(f['id']) for s in ['data/sample_round1.json','data/sample_round2.json'] for f in json.load(open(s))]" | sort -u |
while read -r i; do
  [ -s "$OUT/$i.png" ] && continue
  curl -s -o "$OUT/pdf/$i.pdf" "https://api.ods.od.nih.gov/dsld/s3/pdf/$i.pdf" && pdftoppm -png -r 300 -singlefile "$OUT/pdf/$i.pdf" "$OUT/$i"
done
