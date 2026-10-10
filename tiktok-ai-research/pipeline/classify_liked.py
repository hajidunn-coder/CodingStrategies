"""Folder assignment for the 375 liked videos (indexes refer to data/liked_order.json, sorted by id). Human-reviewed by Claude on 2026-10-10."""
import json, csv
from common import *
order = json.load(open(DATA / "liked_order.json"))
S = {json.loads(l)["id"]: json.loads(l) for l in open(DATA / "summaries.jsonl")}
F = {
"AI – Coding & Agents": [15,25,63,80,83,88,94,96,134,135,136,143,144,162,168,170,173,175,177,178,181,182,185,188,197,198,199,201,208,212,216,223,227,228,236,237,241,242,243,244,245,250,251,255,262,263,271,273,274,281,290,294,296,300,301,302,306,307,316,319,323,325,328,331,337,338,359,364,372,373],
"AI – Tools & News": [10,26,30,35,37,68,101,123,125,154,186,218,233,235,258,264,266,267,268,269,275,280,284,286,293,297,305,309,314,332,336,339,348,349,351,353,357,367,368,371,374],
"Veterans & VA Benefits": [0,1,11,12,50,55,57,81,98,100,108,111,115,118,122,126,127,141,153,156,166,189,200,202,203,205,207,219,220,222,231,232,238,248,249,252,261,272,276,278,279,282,287,299,303,320,321,322,326,327,329,334,340,344,345,352,354,356,362,363,365,366,370],
"Gov Contracts & Grants": [99,106,117,121,151,161,163,172,174,176,190,192,206,210,211,213,259,289,304,311,330,333,342],
"Business ideas": [7,13,21,27,47,70,71,82,102,105,132,137,140,146,152,158,159,193,253,285,292,312,313,315,350],
"Relationships": [43,45,59,69,128,133,224,229,360],
"Faith & Mindset": [52,56,61,78,92,124,142,147,157,167,180,270,335],
"To-dos/Learning": [66,72,75,79,90,95,103,240,298,324],
"Money & Finance": [97,112,129,295],
"Health & Wellness": [3,19,58,60,62,76,113,119,194,217,341],
"Exercises": [5,18,41,49,53,64,65,67,104,109,120,169,195],
"Speed/Movement Drills": [2,22,29,39,85,107,114,116,149],
"Ball Mastery": [17,44],
"Tennis Drills": [358],
"Sports & Fun": [32,33,36,46,155],
"Parenting": [20,23,34,73,93,138,196,209,234,246,308,318],
"Homeschool": [89,191,226,260,343],
"Travel": [4,6,14,38,48,87,139,148,165,171,256,257,288,347,361],
"Food": [51,130,160,215,225,239,254,310,317,346],
"Wants/Buys": [8,16,31,40,42,54,77,84,86,91,110,150,187,204,221,230,247,265,283,291],
"Other": [24,131,164],
"NEEDS LOOK (photo/blocked)": [9,28,74,145,179,183,184,214,277,355,369],
}
EXISTING = {"Business ideas","Ball Mastery","Dribbling Drills","Speed/Movement Drills","Homeschool","To-dos/Learning","Wants/Buys","Exercises","Food","Parenting","Travel","Tennis Drills","Skills/Moved"}
AI_FLAG_EXTRA = {213, 312, 313, 315, 363, 89, 28, 369}   # AI-related but filed elsewhere; still deep-dived
seen = {}
for folder, idxs in F.items():
    for i in idxs:
        assert i not in seen, f"dup {i} in {folder} and {seen[i]}"
        seen[i] = folder
missing = [i for i in range(len(order)) if i not in seen]
assert not missing, f"unassigned: {missing}"
rows = []
for i, vid in enumerate(order):
    s = S[vid]; folder = seen[i]
    ai = folder.startswith("AI –") or i in AI_FLAG_EXTRA
    note = (s["desc"] or s["transcript"] or "").replace("\n"," ")[:110]
    rows.append(dict(idx=i, id=vid, url=s["url"], creator=s["creator"], folder=folder,
                     folder_status="existing" if folder in EXISTING else "NEW", ai_deep_dive="yes" if ai else "no",
                     also_saved_in=s["saved_folders"], note=note))
with open(DATA / "liked_classification.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
from collections import Counter
c = Counter(r["folder"] for r in rows)
print(f"{'FOLDER':34} {'STATUS':8} COUNT")
for folder, n in sorted(c.items(), key=lambda x: -x[1]):
    print(f"{folder:34} {'existing' if folder in EXISTING else 'NEW':8} {n}")
print("AI deep-dive set:", sum(r["ai_deep_dive"]=="yes" for r in rows))
print("already saved somewhere too:", sum(1 for r in rows if r["also_saved_in"]))
