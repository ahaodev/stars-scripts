# stars-scripts

用 `gh` 拉取自己的 GitHub Star，按关键词 + 语言规则自动分类，并生成一个单页 HTML 来展示「关注点」（含每年各主题占比的变化）。

纯 Python 标准库 + `gh`，无需安装依赖。

## 流程

```bash
# 1. 拉取 star（需要已登录 gh）
./fetch_stars.sh out

# 2. 分类：stars.tsv -> classified.tsv（并在终端打印各类数量）
python -I classify_stars.py out/stars.tsv out/classified.tsv

# 3. 合成页面数据（按 7 个主题分组 + 收藏年份）
python -I build_data.py out/classified.tsv out/starred_at.tsv out/stars-data.json

# 4. 生成单页（数据内嵌，双击即可打开）
python -I build_page.py template.html out/stars-data.json out/stars-focus.html
```

## 文件

| 文件 | 作用 |
|---|---|
| `fetch_stars.sh` | 通过 `gh api user/starred` 拉取仓库信息与 `starred_at` |
| `classify_stars.py` | 分层规则分类器（先按语言/强信号，再按关键词；Android 另分 UI/库/应用/逆向） |
| `overrides.py` | **人工校正表**：规则分错的仓库（`owner/repo` → 子类），优先级最高 |
| `build_data.py` | 把子类合并成 7 个主题，并关联收藏时间 |
| `build_page.py` + `template.html` | 生成自包含的单页 HTML（浅色/深色、悬停提示、可筛选清单） |

## 说明

- `overrides.py` 里是我自己的 star 的校正结果，换成你的账号后请按需增删。
- 分类是启发式的，会有误判；发现分错就加一行到 `overrides.py`，重跑第 2–4 步。
- 子类名称与 `build_data.py` 中 `THEMES` 的前缀绑定，新增子类时需同步。
- 页面里的配色为 7 个固定槽位（已用色盲安全校验），主题顺序不要随意调换。
- 用 `python -I`（隔离模式）运行，避免当前目录里的同名模块被误导入。
