import sys, csv
from common import *
rows = parse_links(sys.argv[1])
by_id = {}
for r in rows:
    e = by_id.setdefault(r["id"], dict(r, sources=set(), folders=set()))
    e["sources"].add(r["source"]);
    if r["folder"]: e["folders"].add(r["folder"])
out = []
for e in by_id.values():
    out.append(dict(id=e["id"], creator=e["creator"], kind=e["kind"], url=e["url"],
                    liked="yes" if "liked" in e["sources"] else "no",
                    saved_folders=";".join(sorted(e["folders"])) or ("(no folder)" if "saved" in e["sources"] else "")))
with open(DATA / "inventory.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=out[0].keys()); w.writeheader(); w.writerows(out)
print(len(rows), "lines ->", len(out), "unique videos;", sum(o["liked"]=="yes" for o in out), "liked")
