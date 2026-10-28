LANGRT = "编程语言 / 运行时 / 编译器"
TERM = "终端 / Shell / 命令行工具"
XPLAT = "跨平台 / 桌面应用框架"
SELF = "自托管应用 / 多媒体 / 效率工具"
AI = "AI / LLM / Agent / MCP"
FRONT = "前端 · Web / React / Vue / Node"
DEVOPS = "Docker / K8s / 虚拟化 / DevOps"
DB = "数据库 / 消息队列 / 中间件"
NET = "网络 / 代理 / 内网穿透"
DEVT = "开发者工具 / CLI / 库"
JAVA = "Java / Kotlin 后端 · Spring / 中间件"
CN = "微信 / 国内生态"
SYS = "系统 / 内核 / C·C++·Rust 底层项目"
PY = "Python 项目"
A_LIB = "Android · 库 / 架构 / 工具"
A_APP = "Android · 开源应用 / 仿写 / Demo"
A_SYS = "Android · 逆向 / 系统 / Root"
M = {}
def put(cat, names):
    for n in names.split(): M[n] = cat
put(LANGRT, "golang/go rust-lang/rust ziglang/zig JetBrains/kotlin nodejs/node")
put(TERM, "ohmyzsh/ohmyzsh tmux/tmux junegunn/fzf jesseduffield/lazygit charmbracelet/bubbletea spf13/cobra Eugeny/tabby microsoft/terminal nvm-sh/nvm nvm-windows/nvm termux/termux-app tw93/Mole kingToolbox/WindTerm mbadolato/iTerm2-Color-Schemes")
put(XPLAT, "electron/electron tauri-apps/tauri wailsapp/wails react/react-native expo/expo ionic-team/ionic-framework dcloudio/uni-app NervJS/taro")
put(SELF, "immich-app/immich rustdesk/rustdesk photoprism/photoprism AppFlowy-IO/AppFlowy twentyhq/twenty blakeblackshear/frigate makeplane/plane maybe-finance/maybe appsmithorg/appsmith directus/directus HeyPuter/puter glanceapp/glance gethomepage/homepage IceWhaleTech/CasaOS mattermost/mattermost TryGhost/Ghost filebrowser/filebrowser agalwood/Motrix qier222/YesPlayMusic FFmpeg/FFmpeg OpenCut-app/OpenCut rclone/rclone FreeCAD/FreeCAD")
put(AI, "anomalyco/opencode openai/codex ai-job-search-dev/ai-job-search")
put(FRONT, "shadcn-ui/ui colinhacks/zod FortAwesome/Font-Awesome sampotts/plyr")
put(DB, "supabase/supabase drawdb-io/drawdb ClickHouse/ClickHouse duckdb/duckdb rustfs/rustfs seaweedfs/seaweedfs minio/minio")
put(DEVOPS, "netdata/netdata grafana/grafana apple/container getsentry/sentry")
put(DEVT, "anuraghazra/github-readme-stats grpc/grpc curl/curl")
put(NET, "Kong/kong traefik/traefik")
put(SYS, "ocornut/imgui pbatard/rufus Raphire/Win11Debloat")
put(CN, "LC044/WeChatMsg binarywang/WxJava")
put(JAVA, "macrozheng/mall")
put(PY, "fastapi/fastapi MetaCubeX/mihomo")
put(A_LIB, "lysine-dev/okhttp lysine-dev/retrofit bumptech/glide Blankj/AndroidUtilCode Genymobile/scrcpy")
put(A_APP, "android/architecture-samples")
put(A_SYS, "Genymobile/scrcpy")
put("其他 / 待人工确认", "996icu/996.ICU chinese-poetry/chinese-poetry")
put(A_SYS, "RikkaApps/Shizuku")
put(DEVT, "DevToys-app/DevToys")
put("安全 / 认证 / 隐私", "fail2ban/fail2ban casdoor/casdoor ory/kratos authelia/authelia open-policy-agent/opa")
put(SYS, "glfw/glfw")
put(NET, "netbirdio/netbird")
put("Go · 框架 / 库 / 工具", "flipped-aurora/gin-vue-admin qax-os/excelize")
put(SELF, "Budibase/budibase nocobase/nocobase")
put(DEVOPS, "openobserve/openobserve nezhahq/nezha")
put("物联网 / 嵌入式 / 硬件", "emqx/emqx")
put("学习资源 / Awesome 清单 / 教程", "norvig/pytudes")
put(TERM, "electerm/electerm")
put(JAVA, "alibaba/Sentinel")
