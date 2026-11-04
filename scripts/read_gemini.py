"""Third, cross-vendor reader: Gemini reads the same 400 label images with the same instruction as the
Claude readers (Appendix A), blind to the database value. Outputs go to data/readers/gemini/<key>_<id>.json.

Usage: GEMINI_API_KEY=... python3 scripts/read_gemini.py [--limit N] [--cap-usd 30] [--model gemini-4-argon]
Spend is priced from usage metadata (input 2.0, output incl. thinking 10.0 USD per million tokens for
gemini-4-argon) and the run stops before any new call once the running total reaches the cap.
"""
import os, sys, json, time, argparse, threading, concurrent.futures as cf
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import DATA, LABELS

PRICES = {'gemini-4-argon': (2.0, 10.0), 'gemini-3.8-flash': (0.75, 3.75)}
PROMPT = ('It is a dietary supplement label. In the Supplement Facts panel, find the row for: {name}. '
          'Zoom in mentally and read exactly what is printed. Reply with ONLY one JSON object: '
          '{{"printed_amount": number, "printed_unit": string exactly as printed (e.g. mg, mcg, IU), '
          '"printed_percent_dv": number or null, "legible": true/false}}.')

ap = argparse.ArgumentParser()
ap.add_argument('--limit', type=int, default=0)
ap.add_argument('--cap-usd', type=float, default=30.0)
ap.add_argument('--model', default='gemini-4-argon')
ap.add_argument('--images', default=os.environ.get('DSLD_IMAGES', os.path.join(DATA, 'labels_png')), help='folder with <id>.png or <id>.jpg')
ap.add_argument('--workers', type=int, default=6)
args = ap.parse_args()

from google import genai
from google.genai import types
client = genai.Client(http_options=types.HttpOptions(retry_options=types.HttpRetryOptions(attempts=6)))
OUT = os.path.join(DATA, 'readers', 'gemini'); os.makedirs(OUT, exist_ok=True)
lock = threading.Lock(); spent = [0.0]
for f in os.listdir(OUT):
    if f.endswith('.json'): spent[0] += json.load(open(os.path.join(OUT, f))).get('cost', 0.0)

jobs = []
for sample, tag in [('sample_round1.json', 'a'), ('sample_round2.json', 'b')]:
    for k, f in enumerate(json.load(open(os.path.join(DATA, sample)))):
        jobs.append((f'{tag}{k}', f['id'], f['name']))
if args.limit: jobs = jobs[:args.limit]

def image_bytes(i):
    for ext, mime in (('.png', 'image/png'), ('.jpg', 'image/jpeg')):
        p = os.path.join(args.images, i + ext)
        if os.path.exists(p): return open(p, 'rb').read(), mime
    raise FileNotFoundError(i)

def run(job):
    key, i, name = job
    out = os.path.join(OUT, f'{key}_{i}.json')
    if os.path.exists(out): return 'cached'
    with lock:
        if spent[0] >= args.cap_usd: return 'cap'
    img, mime = image_bytes(i)
    cfg = types.GenerateContentConfig(thinking_config=types.ThinkingConfig(thinking_level='low'),
                                      max_output_tokens=16000, temperature=1.0)
    r = client.models.generate_content(model=args.model, config=cfg,
                                       contents=[types.Part(inline_data=types.Blob(data=img, mime_type=mime), media_resolution=types.PartMediaResolution(level=types.PartMediaResolutionLevel.MEDIA_RESOLUTION_ULTRA_HIGH)), types.Part.from_text(text=PROMPT.format(name=name))])
    u = r.usage_metadata; pin, pout = PRICES[args.model]
    cost = ((u.prompt_token_count or 0) * pin + ((u.candidates_token_count or 0) + (u.thoughts_token_count or 0)) * pout) / 1e6
    json.dump({'text': r.text or '', 'model': args.model, 'cost': cost, 'usage': {'in': u.prompt_token_count, 'out': u.candidates_token_count,
               'thought': u.thoughts_token_count}, 't': time.time()}, open(out, 'w'))
    with lock: spent[0] += cost
    return 'ok'

def safe(job):
    try: return run(job)
    except Exception as e: print('error', job[0], str(e)[:160], flush=True); return 'error'

t0 = time.time(); res = []
with cf.ThreadPoolExecutor(args.workers) as ex:
    for k, r in enumerate(ex.map(safe, jobs)):
        res.append(r)
        if (k + 1) % 50 == 0: print(f'{k+1}/{len(jobs)} spent ${spent[0]:.2f}', flush=True)
from collections import Counter
print(Counter(res), f'total spent ${spent[0]:.2f}', f'{time.time()-t0:.0f}s')
