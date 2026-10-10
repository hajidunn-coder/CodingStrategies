import os, re, json, csv, pathlib
os.environ.setdefault("SSL_CERT_FILE", "/root/.ccr/ca-bundle.crt")
os.environ.setdefault("REQUESTS_CA_BUNDLE", "/root/.ccr/ca-bundle.crt")
ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
META = DATA / "meta"; EXTRACT = DATA / "extract"; FRAMES = DATA / "frames"
for d in (META, EXTRACT, FRAMES): d.mkdir(parents=True, exist_ok=True)
VID_RE = re.compile(r"tiktok\.com/@([\w.\-]+)/(video|photo)/(\d+)")
def parse_links(path):
    rows = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line: continue
        parts = line.split("|")
        if parts[0] == "liked": src, folder, url = "liked", "", parts[1]
        elif parts[0] == "saved": src, folder, url = "saved", parts[1], parts[2]
        else: continue
        m = VID_RE.search(url)
        if not m: continue
        rows.append(dict(id=m.group(3), creator=m.group(1), kind=m.group(2), source=src, folder=folder, url=url))
    return rows
def load_inventory():
    return list(csv.DictReader(open(DATA / "inventory.csv", encoding="utf-8")))
def hashtags(desc):
    return sorted(set(t.lower() for t in re.findall(r"#(\w+)", desc or "")))
