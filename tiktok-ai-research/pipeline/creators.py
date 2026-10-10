"""List last N posts of every creator in the AI deep-dive set. Writes data/creators/<creator>.jsonl"""
import csv, json, subprocess, time, random, sys
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 50
CRE = DATA / "creators"; CRE.mkdir(exist_ok=True)
rows = list(csv.DictReader(open(DATA / "liked_classification.csv", encoding="utf-8")))
creators = sorted({r["creator"] for r in rows if r["ai_deep_dive"] == "yes" and r["creator"]})
print(len(creators), "creators")
for c in creators:
    out = CRE / f"{c}.jsonl"
    if out.exists(): continue
    r = subprocess.run(["yt-dlp","--flat-playlist","--playlist-end",str(N),"--impersonate","","--print","%(id)s\t%(title)s\t%(duration)s\t%(view_count)s",
                        f"https://www.tiktok.com/@{c}"], capture_output=True, text=True, timeout=300)
    items = []
    for line in r.stdout.splitlines():
        p = line.split("\t")
        if len(p) >= 2 and p[0].isdigit(): items.append(dict(id=p[0], title=p[1], duration=p[2] if len(p)>2 else "", views=p[3] if len(p)>3 else ""))
    with open(out, "w", encoding="utf-8") as f:
        for it in items: f.write(json.dumps(it, ensure_ascii=False) + "\n")
    print(f"@{c}: {len(items)} posts" + ("" if items else f"  ERR {r.stderr.strip().splitlines()[-1][:120] if r.stderr.strip() else ''}"), flush=True)
    time.sleep(random.uniform(1.5, 3))
