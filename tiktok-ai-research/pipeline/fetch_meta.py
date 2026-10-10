"""Metadata only (no download). Writes data/meta/<id>.json. Resumable."""
import sys, json, time, random, concurrent.futures as cf
from common import *
import yt_dlp
OPTS = dict(quiet=True, no_warnings=True, skip_download=True, noplaylist=True,
            extractor_args={"tiktok": {"app_info": []}}, socket_timeout=30)
FIELDS = ["id","uploader","uploader_id","channel","description","title","duration","upload_date","timestamp",
          "view_count","like_count","comment_count","repost_count","save_count","track","artists","webpage_url"]
def one(row):
    out = META / f"{row['id']}.json"
    if out.exists(): return "skip"
    rec = dict(id=row["id"], url=row["url"], creator=row["creator"], kind=row["kind"])
    try:
        with yt_dlp.YoutubeDL(OPTS) as y:
            info = y.extract_info(row["url"], download=False)
        for k in FIELDS:
            if k in info: rec[k] = info[k]
        rec["hashtags"] = hashtags(info.get("description"))
        ac = info.get("automatic_captions") or {}; sb = info.get("subtitles") or {}
        rec["caption_langs"] = sorted(set(list(ac.keys()) + list(sb.keys())))
        rec["is_photo"] = row["kind"] == "photo" or not info.get("formats")
        rec["ok"] = True
    except Exception as e:
        rec["ok"] = False; rec["error"] = str(e)[:300]
    json.dump(rec, open(out, "w"), ensure_ascii=False, indent=1)
    time.sleep(random.uniform(0.8, 2.0))
    return "ok" if rec["ok"] else "err"
if __name__ == "__main__":
    inv = load_inventory()
    only = sys.argv[1] if len(sys.argv) > 1 else "all"   # all | liked | <n>
    if only == "liked": inv = [r for r in inv if r["liked"] == "yes"]
    elif only.isdigit(): inv = inv[:int(only)]
    inv.sort(key=lambda r: (r["liked"] != "yes", r["id"]))
    c = {"ok":0,"err":0,"skip":0}
    with cf.ThreadPoolExecutor(2) as ex:
        for i, res in enumerate(ex.map(one, inv), 1):
            c[res] += 1
            if i % 25 == 0 or i == len(inv): print(f"{i}/{len(inv)} {c}", flush=True)
