#!/usr/bin/env bash
# 用法: ./fetch_stars.sh <输出目录>
# 需要已登录的 gh（gh auth status）。产出：
#   stars.tsv      full_name  language  stars  topics  description  archived
#   starred_at.tsv full_name  starred_at
set -euo pipefail
out="${1:?usage: fetch_stars.sh <output-dir>}"
mkdir -p "$out"

gh api --paginate "user/starred?per_page=100" --jq '.[] | [
  .full_name, (.language // "-"), .stargazers_count,
  ((.topics // []) | join(",")),
  ((.description // "") | gsub("[\t\n\r]"; " ")),
  .archived
] | @tsv' > "$out/stars.tsv"

gh api --paginate -H "Accept: application/vnd.github.star+json" "user/starred?per_page=100" \
  --jq '.[] | [.repo.full_name, .starred_at] | @tsv' > "$out/starred_at.tsv"

wc -l "$out/stars.tsv" "$out/starred_at.tsv"
