"""Build data/summaries.jsonl: one compact record per video for classification."""
import json, glob
from common import *
inv = {r["id"]: r for r in load_inventory()}
out = []
for vid, r in inv.items():
    m = json.load(open(META / f"{vid}.json")) if (META / f"{vid}.json").exists() else {}
    e = json.load(open(EXTRACT / f"{vid}.json")) if (EXTRACT / f"{vid}.json").exists() else {}
    rec = dict(id=vid, url=r["url"], liked=r["liked"], saved_folders=r["saved_folders"], creator=m.get("uploader") or r["creator"],
               channel=m.get("channel"), desc=(m.get("description") or "")[:400], hashtags=m.get("hashtags", []),
               duration=round(m.get("duration") or e.get("duration") or 0), views=m.get("view_count"), likes=m.get("like_count"),
               saves=m.get("save_count"), date=m.get("upload_date"), photo=bool(m.get("is_photo") or e.get("is_photo")),
               transcript=(e.get("transcript") or "")[:900], tsrc=(e.get("transcript_source") or "").split(":")[0],
               has_sheet=(FRAMES / f"{vid}.jpg").exists(), meta_err=m.get("error") if not m.get("ok") else None,
               ext_err=e.get("error") if e and not e.get("ok") else None)
    out.append(rec)
with open(DATA / "summaries.jsonl", "w", encoding="utf-8") as f:
    for rec in out: f.write(json.dumps(rec, ensure_ascii=False) + "\n")
liked = [o for o in out if o["liked"] == "yes"]
print(len(out), "records;", len(liked), "liked;", sum(1 for o in liked if o["transcript"]), "with transcript;", sum(1 for o in liked if o["has_sheet"]), "with frame sheet;", sum(1 for o in liked if not o["transcript"] and not o["has_sheet"] and not o["desc"]), "with nothing")
