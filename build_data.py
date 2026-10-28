"""把分类结果 + starred_at 合成页面用的 JSON，并按 7 个主题分组。

用法: python -I build_data.py <classified.tsv> <starred_at.tsv> <输出 stars-data.json>
"""
import csv, json, collections, sys

classified, starred_at, out = sys.argv[1:4]

# (主题名, 子类名前缀)；颜色顺序固定，与页面调色板的 7 个槽位一一对应
THEMES = [
    ("Android 开发", ["Android"]),
    ("AI · Agent", ["AI /"]),
    ("前端 · 跨平台", ["前端", "跨平台", "Flutter", "iOS", "微信"]),
    ("后端 · 语言 · 数据", ["Go ·", "Java /", "编程语言", "数据库", "Python"]),
    ("云原生 · 网络 · 安全", ["Docker", "网络", "安全"]),
    ("嵌入式 · 系统", ["物联网", "系统 /"]),
    ("工具 · 自托管 · 学习", ["终端", "开发者工具", "自托管", "学习资源", "其他"]),
]


def theme(cat):
    for i, (_, keys) in enumerate(THEMES):
        if any(cat.startswith(k) for k in keys):
            return i
    raise SystemExit("子类未映射到主题: " + cat)


st = dict(l.rstrip("\n").split("\t") for l in open(starred_at, encoding="utf-8"))
repos = []
for cat, name, lang, stars, arch, desc in csv.reader(open(classified, encoding="utf-8"), delimiter="\t"):
    repos.append({
        "n": name, "c": cat, "t": theme(cat), "l": lang if lang != "-" else "",
        "s": int(stars or 0), "a": 1 if arch == "true" else 0,
        "y": int(st[name][:4]), "m": st[name][:7], "d": desc[:110],
    })

cats = collections.OrderedDict()
for r in sorted(repos, key=lambda r: (r["t"], r["c"])):
    cats.setdefault(r["c"], r["t"])

data = {"themes": [t[0] for t in THEMES], "cats": [{"name": k, "t": v} for k, v in cats.items()], "repos": repos}
json.dump(data, open(out, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(f"{len(repos)} repos, {len(cats)} categories -> {out}")
