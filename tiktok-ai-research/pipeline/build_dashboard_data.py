"""Aggregate everything into data/dashboard.json for the hosted dashboard."""
import json, glob, csv, collections
from common import *
S = {json.loads(l)['id']: json.loads(l) for l in open(DATA/'summaries.jsonl')}
cls = {r['id']: r for r in csv.DictReader(open(DATA/'liked_classification.csv', encoding='utf-8'))}
def load(d):
    out = []
    for f in sorted(glob.glob(str(d/'*.json'))):
        try: out.append(json.load(open(f)))
        except Exception as e: print("bad", f, e)
    return out
liked = load(DATA/'deep'); creators = load(DATA/'deep_creators')
videos = []
for r in liked:
    s = S.get(r['id'], {}); c = cls.get(r['id'], {})
    videos.append(dict(id=r['id'], url=r.get('url') or s.get('url'), creator=r.get('creator') or s.get('creator'), source='liked',
        folder=c.get('folder'), title=r.get('title'), category=r.get('category'), tools=[t.get('name') for t in r.get('tools',[]) if t.get('name')],
        claims=r.get('claims',[]), steps=r.get('how_to_steps',[]), on_screen=r.get('on_screen_only',[]), cta=r.get('cta'),
        relevance=(r.get('relevance') or {}).get('score'), implement=(r.get('implement_score') or {}).get('score'),
        implement_why=(r.get('implement_score') or {}).get('why'), verify=r.get('verify',[]),
        views=s.get('views'), likes=s.get('likes'), date=s.get('date'), duration=s.get('duration'), transcript=(s.get('transcript') or '')[:900],
        topic_match=None, gap=None))
sel = {it['id']: it for it in json.load(open(DATA/'creator_selected.json'))}
for r in creators:
    it = sel.get(r['id'], {})
    videos.append(dict(id=r['id'], url=r.get('url') or it.get('url'), creator=r.get('creator') or it.get('creator'), source='creator',
        folder=None, title=r.get('title'), category=r.get('category'), tools=[t.get('name') for t in r.get('tools',[]) if t.get('name')],
        claims=r.get('claims',[]), steps=r.get('how_to_steps',[]), on_screen=r.get('on_screen_only',[]), cta=r.get('cta'),
        relevance=(r.get('relevance') or {}).get('score'), implement=(r.get('implement_score') or {}).get('score'),
        implement_why=(r.get('implement_score') or {}).get('why'), verify=r.get('verify',[]),
        views=it.get('views'), likes=None, date=None, duration=None, transcript='',
        topic_match=r.get('topic_match'), gap=r.get('gap')))
research = []
for f in sorted(glob.glob(str(DATA/'research'/'*.json'))):
    if f.endswith('themes.json'): continue
    theme = pathlib.Path(f).stem
    for row in json.load(open(f)):
        row['theme'] = theme; research.append(row)
guides = {pathlib.Path(f).stem: open(f, encoding='utf-8').read() for f in glob.glob(str(DATA/'research'/'*.md')) if 'SCHEMA' not in f}
out = dict(generated='2026-10-10', videos=videos, research=research, guides=guides,
           stats=dict(liked_total=375, liked_ai=len(liked), creator_videos=len(creators), creators=len({v['creator'] for v in videos if v['source']=='creator'}),
                      verdicts=dict(collections.Counter(r.get('verdict') for r in research))))
json.dump(out, open(DATA/'dashboard.json','w'), ensure_ascii=False)
print(len(videos), "videos,", len(research), "research rows,", len(guides), "guides;", round((DATA/'dashboard.json').stat().st_size/1e6,2), "MB")
