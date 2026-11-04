# dsld-unit-audit

Code, model outputs and verification data for:

> Xiaomeng Li. *A thousand times off: unit errors in a national dietary supplement label database, separated from label misprints by image verification.* Manuscript, 2026.

The study audits a complete snapshot of the NIH Dietary Supplement Label Database (DSLD; 214,780 labels, 3 November 2026). A consistency check between each row's amount and its percent Daily Value flags rows about 1,000-fold (milligram–microgram) or 10-fold off; a random sample of flagged rows is verified against the label images by three multimodal models (Claude Sonnet 5.5, Claude Opus 5.5, Gemini 4 Argon), with the author's review of the rows on which they disagree and a spot check of rows on which they agree.

## What is here

| Path | Content |
|---|---|
| `scripts/dv_check.py` | Full-database consistency check → `data/flags.csv`, `data/flags_counts.json`. `--dv-set 2016` runs the 2016-Daily-Values-only sensitivity analysis. |
| `scripts/fetch_labels.sh` | Downloads the PDF of each sampled label from the database's public file service and renders it at 300 dpi. |
| `scripts/read_claude.py` | First and second readers (Claude Sonnet 5.5, Claude Opus 5.5) through the Claude Code CLI. |
| `scripts/read_gemini.py` | Third reader (Gemini 4 Argon) through the Gemini API, with a USD spend cap. |
| `scripts/adjudicate.py` | Rule that turns a reader's printed reading into a verdict (database error, label misprint, unresolved). |
| `scripts/three_readers.py` | Majority of the three readers, pairwise and Fleiss' κ → `data/three_reader.csv`, `results/three_readers.json`. |
| `scripts/author_review.py` | Parses the author's filled-in review files → `data/author_review.csv`, `data/author_spot30.csv`. |
| `scripts/stats.py` | Every number in the paper, including significance tests → `results/stats.json`, `data/final_verdicts.csv`. |
| `scripts/ul_analysis.py` | Upper-limit analysis with the applicability rules (nutrient form, adult products) → `results/ul_assessment.csv`. |
| `scripts/figures.py` | Figures 1 and 2 → `results/`. |
| `data/sample_round1.json`, `data/sample_round2.json` | The 400 sampled flagged rows (300 unit, 100 10-fold). |
| `data/readers/` | Raw output of each reader for each sampled row (`sonnet_round1/`, `sonnet_round2/`, `opus/`, `gemini/`). |
| `data/author_review30.md` | The author's review of the 30 rows without full agreement: printed values, category and note, as filled in. The readers' readings were shown; the review was not blind. |
| `data/author_spot30.md`, `data/spot30_keys.txt` | Spot check of 30 random rows (seed 20261104) on which all three readers found a database error; readers' outputs hidden. |
| `data/snapshot.sha256` | SHA-256 of the database export used. |
| `pilot/` | Pilot: one model's full transcription of 200 labels (Supplementary Appendix B); not used in any estimate. |

## Data (not redistributed)

- **DSLD full JSON export**: https://dsld.od.nih.gov/ (Download → full database, JSON). The analysis used the export of 3 November 2026; its SHA-256 is in `data/snapshot.sha256`. Unzip it and set `DSLD_SNAPSHOT` to the folder of per-label JSON files (default `data/snapshot/DSLD-full-database-JSON`).
- **Label images**: public at the NIH Office of Dietary Supplements; `scripts/fetch_labels.sh` downloads those of the sampled labels. Images are not included here.

The database is updated over time, so a newer export will give somewhat different flags.

## Reproduce

Python 3.12; `pip install numpy==2.5.4 scipy==1.16.1 matplotlib==3.11.2` (and `google-genai pillow` for the Gemini reader). Rendering label PDFs needs poppler (`pdftoppm`).

```bash
export DSLD_SNAPSHOT=/path/to/DSLD-full-database-JSON
python3 scripts/dv_check.py          # flags (about 70 s); identical to data/flags.csv for the 3 Nov 2026 export
python3 scripts/three_readers.py     # verdicts from the stored reader outputs
python3 scripts/author_review.py     # author's review files -> verdict tables
python3 scripts/stats.py             # all numbers -> results/stats.json
python3 scripts/ul_analysis.py       # upper-limit analysis
python3 scripts/figures.py           # figures
```

These steps use only the stored outputs and make **no model calls**. To read the images again:

```bash
bash scripts/fetch_labels.sh                               # -> data/labels_png/
python3 scripts/read_claude.py --model sonnet              # needs the Claude Code CLI
python3 scripts/read_claude.py --model opus
GEMINI_API_KEY=... python3 scripts/read_gemini.py --cap-usd 10
```

Hosted models change over time; the stored outputs (Claude readers on 3 November 2026, Gemini on 4 November 2026) are the reference for the reported numbers. Existing outputs are never overwritten, so delete a reader's folder to rerun it.

## License

Code: MIT (see `LICENSE`). Model outputs and review files are provided for research reproducibility. The database and label images belong to their providers and are not included.
