"""Per video: download -> captions or whisper transcript -> contact sheet of frames -> delete media.
Writes data/extract/<id>.json and data/frames/<id>.jpg. Resumable."""
import sys, json, subprocess, tempfile, shutil, re, glob, time, random
import numpy as np
from PIL import Image
from common import *
WHISPER = None
def whisper():
    global WHISPER
    if WHISPER is None:
        from faster_whisper import WhisperModel
        WHISPER = WhisperModel("small", device="cpu", compute_type="int8", cpu_threads=2)
    return WHISPER
def vtt_text(path):
    out, seen = [], set()
    for line in open(path, encoding="utf-8", errors="ignore"):
        line = line.strip()
        if not line or "-->" in line or line.startswith(("WEBVTT","Kind:","Language:")) or line.isdigit(): continue
        line = re.sub(r"<[^>]+>", "", line)
        if line not in seen: seen.add(line); out.append(line)
    return " ".join(out)
def sheet(frames_dir, out_path, max_tiles=12):
    files = sorted(glob.glob(str(frames_dir / "f_*.jpg")))
    if not files: return 0
    if len(files) > max_tiles:
        idx = np.linspace(0, len(files)-1, max_tiles).round().astype(int); files = [files[i] for i in idx]
    ims = [Image.open(f) for f in files]
    w, h = ims[0].size; cols = 3 if len(ims) > 4 else len(ims); rows = -(-len(ims)//cols)
    grid = Image.new("RGB", (cols*w, rows*h), "black")
    for i, im in enumerate(ims): grid.paste(im, ((i%cols)*w, (i//cols)*h))
    grid.save(out_path, quality=80); return len(ims)
def one(row):
    out = EXTRACT / f"{row['id']}.json"
    if out.exists(): return "skip"
    rec = dict(id=row["id"], url=row["url"])
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="tt_"))
    try:
        cmd = ["yt-dlp","-q","--no-warnings","-f","mp4/best","-o",str(tmp/"v.%(ext)s"),
               "--write-auto-subs","--write-subs","--sub-langs","en.*,eng.*,all","--sub-format","vtt",row["url"]]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        vids = [p for p in tmp.iterdir() if p.suffix in (".mp4",".webm",".mov")]
        imgs = [p for p in tmp.iterdir() if p.suffix.lower() in (".jpg",".jpeg",".png",".webp")]
        subs = sorted(tmp.glob("*.vtt"))
        en = [s for s in subs if ".en" in s.name] or subs
        if en:
            rec["transcript"] = vtt_text(en[0]); rec["transcript_source"] = "tiktok_captions:" + en[0].name.split(".")[-2]
        fdir = tmp / "frames"; fdir.mkdir()
        if vids:
            v = vids[0]
            dur = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",str(v)],capture_output=True,text=True).stdout.strip() or 0)
            rec["duration"] = dur
            step = max(1.0, dur/12)   # ~12 frames, min 1s apart
            subprocess.run(["ffmpeg","-v","error","-y","-i",str(v),"-vf",f"fps=1/{step:.2f},scale=360:-1",str(fdir/"f_%03d.jpg")],timeout=300)
            if "transcript" not in rec:
                subprocess.run(["ffmpeg","-v","error","-y","-i",str(v),"-vn","-ac","1","-ar","16000","-f","s16le",str(tmp/"a.pcm")],timeout=300)
                audio = np.frombuffer(open(tmp/"a.pcm","rb").read(), dtype=np.int16).astype(np.float32)/32768.0
                segs, info = whisper().transcribe(audio, vad_filter=True)
                rec["transcript"] = " ".join(s.text.strip() for s in segs); rec["transcript_source"] = f"whisper_small:{info.language}"
        elif imgs:
            rec["is_photo"] = True
            for i, p in enumerate(sorted(imgs)[:12]):
                Image.open(p).convert("RGB").resize((360, int(360*Image.open(p).height/Image.open(p).width))).save(fdir/f"f_{i:03d}.jpg")
            rec["transcript"] = rec.get("transcript",""); rec["transcript_source"] = rec.get("transcript_source","none(photo)")
        else:
            rec["ok"] = False; rec["error"] = (r.stderr or r.stdout)[-300:]
            json.dump(rec, open(out,"w"), ensure_ascii=False, indent=1); return "err"
        rec["n_frames"] = sheet(fdir, FRAMES / f"{row['id']}.jpg")
        rec["ok"] = True
    except Exception as e:
        rec["ok"] = False; rec["error"] = str(e)[:300]
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    json.dump(rec, open(out,"w"), ensure_ascii=False, indent=1)
    time.sleep(random.uniform(0.5, 1.5))
    return "ok" if rec.get("ok") else "err"
if __name__ == "__main__":
    inv = load_inventory()
    only = sys.argv[1] if len(sys.argv) > 1 else "liked"
    if only == "liked": inv = [r for r in inv if r["liked"] == "yes"]
    elif only.isdigit(): inv = [r for r in inv if r["liked"] == "yes"][:int(only)]
    c = {"ok":0,"err":0,"skip":0}
    for i, row in enumerate(inv, 1):
        c[one(row)] += 1
        if i % 10 == 0 or i == len(inv): print(f"{i}/{len(inv)} {c}", flush=True)
