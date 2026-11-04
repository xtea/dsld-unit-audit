"""First and second readers: Claude Sonnet 5.5 and Claude Opus 5.5 read each sampled label image through the
Claude Code command-line client (`claude -p`, read-only file access), blind to the database value.
Outputs: data/readers/sonnet_round1/<k>_<id>.json, sonnet_round2/<k>_<id>.json, opus/<key>_<id>.json.
Existing outputs are kept, so a rerun only fills gaps.

Usage: python3 scripts/read_claude.py --model sonnet|opus [--images data/labels_png] [--workers 4]"""
import argparse, concurrent.futures as cf, json, os, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import DATA
PROMPT = ('Read the image file at {img} . It is a dietary supplement label. In the Supplement Facts panel, find the row for: {name}. '
          'Zoom in mentally and read exactly what is printed. Reply with ONLY one JSON object: '
          '{{"printed_amount": number, "printed_unit": string exactly as printed (e.g. mg, mcg, IU), '
          '"printed_percent_dv": number or null, "legible": true/false}}.')
ap = argparse.ArgumentParser(); ap.add_argument('--model', required=True, choices=['sonnet', 'opus'])
ap.add_argument('--images', default=os.path.join(DATA, 'labels_png')); ap.add_argument('--workers', type=int, default=4)
a = ap.parse_args(); images = os.path.abspath(a.images)
jobs = []
for sample, tag, sdir in [('sample_round1.json', 'a', 'sonnet_round1'), ('sample_round2.json', 'b', 'sonnet_round2')]:
    for k, f in enumerate(json.load(open(os.path.join(DATA, sample)))):
        out = (os.path.join(DATA, 'readers', sdir, f"{k}_{f['id']}.json") if a.model == 'sonnet'
               else os.path.join(DATA, 'readers', 'opus', f"{tag}{k}_{f['id']}.json"))
        jobs.append((os.path.join(images, f"{f['id']}.png"), out, f['name']))
def run(job):
    img, out, name = job
    if os.path.exists(out) and os.path.getsize(out): return 'cached'
    os.makedirs(os.path.dirname(out), exist_ok=True)
    r = subprocess.run(['claude', '-p', PROMPT.format(img=img, name=name), '--model', a.model, '--add-dir', images,
                        '--allowedTools', 'Read', '--output-format', 'text'], capture_output=True, text=True)
    if r.returncode == 0 and r.stdout.strip(): open(out, 'w').write(r.stdout); return 'ok'
    return 'error'
with cf.ThreadPoolExecutor(a.workers) as ex:
    from collections import Counter; print(Counter(ex.map(run, jobs)))
