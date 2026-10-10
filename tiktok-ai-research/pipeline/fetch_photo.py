"""Photo-slideshow posts: fetch page HTML, parse rehydration JSON, download slides, build sheet."""
import sys, json, re, html, tempfile, shutil, pathlib, time, random
import requests
from PIL import Image
from common import *
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
S = requests.Session(); S.headers.update({"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
def item(url):
    r = S.get(url, timeout=30); r.raise_for_status()
    m = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">(.*?)</script>', r.text, re.S)
    if not m: raise RuntimeError("no rehydration json (status %s, len %d)" % (r.status_code, len(r.text)))
    j = json.loads(html.unescape(m.group(1)))
    scope = j.get("__DEFAULT_SCOPE__", {})
    det = scope.get("webapp.video-detail") or {}
    it = (det.get("itemInfo") or {}).get("itemStruct")
    if not it: raise RuntimeError("no itemStruct: " + json.dumps(det)[:200])
    return it
def one(row):
    rec = dict(id=row["id"], url=row["url"], creator=row["creator"], kind="photo", is_photo=True)
    try:
        it = item(row["url"])
        st = it.get("stats") or it.get("statsV2") or {}
        rec.update(uploader=(it.get("author") or {}).get("uniqueId"), channel=(it.get("author") or {}).get("nickname"),
                   description=it.get("desc"), hashtags=hashtags(it.get("desc")), timestamp=it.get("createTime"),
                   view_count=int(st.get("playCount") or 0), like_count=int(st.get("diggCount") or 0),
                   comment_count=int(st.get("commentCount") or 0), save_count=int(st.get("collectCount") or 0),
                   track=(it.get("music") or {}).get("title"), caption_langs=[], duration=0, ok=True)
        imgs = [(im.get("imageURL") or {}).get("urlList", [None])[0] for im in (it.get("imagePost") or {}).get("images", [])]
        tmp = pathlib.Path(tempfile.mkdtemp()); tiles = []
        for i, u in enumerate([u for u in imgs if u][:12]):
            try:
                p = tmp / f"f_{i:03d}.jpg"; open(p, "wb").write(S.get(u, timeout=30).content)
                im = Image.open(p).convert("RGB"); im = im.resize((360, int(360 * im.height / im.width))); tiles.append(im)
            except Exception: pass
        if tiles:
            h = max(t.height for t in tiles); cols = 3 if len(tiles) > 4 else len(tiles); rows = -(-len(tiles)//cols)
            grid = Image.new("RGB", (cols*360, rows*h), "black")
            for i, t in enumerate(tiles): grid.paste(t, ((i%cols)*360, (i//cols)*h))
            grid.save(FRAMES / f"{row['id']}.jpg", quality=80)
        shutil.rmtree(tmp, ignore_errors=True)
        ex = dict(id=row["id"], url=row["url"], is_photo=True, n_frames=len(tiles), transcript="", transcript_source="none(photo)", ok=True,
                  photo_title=(it.get("imagePost") or {}).get("title"))
        json.dump(ex, open(EXTRACT / f"{row['id']}.json", "w"), ensure_ascii=False, indent=1)
    except Exception as e:
        rec["ok"] = False; rec["error"] = "photo: " + str(e)[:200]
    json.dump(rec, open(META / f"{row['id']}.json", "w"), ensure_ascii=False, indent=1)
    time.sleep(random.uniform(1, 2))
    return rec["ok"]
if __name__ == "__main__":
    inv = [r for r in load_inventory() if r["kind"] == "photo"]
    res = [one(r) for r in inv]
    print(f"photos: {sum(res)} ok / {len(res)}")
