"""Extract (transcript + frames) for a JSON list of {id,url,...}. Resumable."""
import sys, json
from extract import one
items = json.load(open(sys.argv[1]))
c = {"ok":0,"err":0,"skip":0}
for i, it in enumerate(items, 1):
    c[one(dict(id=it["id"], url=it["url"]))] += 1
    if i % 20 == 0 or i == len(items): print(f"{i}/{len(items)} {c}", flush=True)
