import sys, re, csv, collections
src, out = sys.argv[1], sys.argv[2]
def rx(p): return re.compile(p, re.I | re.ASCII)
AWESOME = rx(r"\b(awesome|awesome-list|roadmap|interview|cheatsheet|handbook|curated)\b|面试|大全|汇总|知识库|图谱|指南")
AWESOME_WEAK = rx(r"\b(tutorials?|course|learn|learning|books?|notes)\b|教程|学习|资源|培训|笔记|中文版|源码")
AI = rx(r"\b(ai|llms?|gpt\w*|chatgpt|openai|claude\w*|anthropic|mcp|rag|langchain|ollama|gemini|diffusion|machine-learning|deep-learning|neural|tensorflow|pytorch|whisper|copilot|ai-agent|agentic|openclaw|\w*claw|skills?|llama|inference|tts|speech|bitnet|flux)\b|大模型|智能体|人工智能")
ANDROID_RE = rx(r"\b(android|androidx|apk|kotlin-android|android-library|aosp|jetpack|rxjava|rxandroid|retrofit|okhttp|recyclerview|viewpager|glide)\b|安卓")
ANDROID_SYS = rx(r"xposed|lsposed|magisk|shizuku|frida|apktool|jadx|smali|reverse.engineering|decompil|逆向|脱壳|提权|\broot\b")
ANDROID_UI = rx(r"\b(view|views|widget|animation|animations|recyclerview|viewpager|dialog|popup|popupwindow|toast|button|progress|layout|layoutmanager|banner|tablayout|indicator|ripple|loading|refresh|swipe|drawer|bottomsheet|snackbar|chart|picker|seekbar|textview|cardview|material-design|material|rating|badge|carousel|slider|wheel|calendar|toolbar|menu|fab|shimmer|skeleton|blur|zoom|gallery|scroll|spinner|tooltip|marquee|sticky|timeline|transition|flowlayout|sidebar|float|window|actionbar|emoji|selector|label|coupon|equalizer|showcase|onboarding|highlight)\b|控件|动画|自定义|弹窗|悬浮|布局|侧边|角标|下拉|刷新")
ANDROID_APP = rx(r"仿|高仿|客户端|模仿|\b(client|demo|sample|samples|example|examples|clone|news|app)\b|新闻|示例|源码|计步|壁纸|头条|音乐|选座|阅读")
DB = rx(r"\b(database|databases|sql|mysql|postgresql|postgres|redis|mongodb|sqlite|orm|etcd|kafka|elasticsearch|clickhouse|tidb|nosql|leveldb|rocksdb|minio|etl|flink|spark|duckdb|jdbc|mybatis|schema|migrations?|rocketmq|rabbitmq|activemq|nsq|zeromq|zookeeper|consul|nacos|shardingsphere|time-series|mongo|gorm|ormlite|message-queue|mq)\b|数据库")
IOT = rx(r"\b(iot|mqtt|esp32|esp8266|esp-idf|arduino|stm32|embedded|raspberry|raspberry-pi|modbus|firmware|rtos|zigbee|homeassistant|home-assistant|mcu|rs485|serial|opc|plc|lvgl|usb|spi|i2c|ch34\w*|armbian|rockchip|rk\d+|amlogic|radxa|phicomm|onvif|smart.home|sensor)\b|物联网|嵌入式|开发板")
DEVOPS = rx(r"\b(docker|docker-compose|kubernetes|k8s|helm|devops|ansible|terraform|prometheus|grafana|monitoring|observability|jenkins|gitops|argocd|containers?|portainer|serverless|cloud-native|opentelemetry|tracing|zabbix|oci|lxc|incus|vm|qemu|virtualization|synology|nas)\b")
NET = rx(r"\b(proxy|vpn|v2ray|xray|clash|shadowsocks|trojan|tunnel|frp|ngrok|wireguard|tailscale|sing-box|hysteria|dns|firewall|iptables|nginx|caddy|traefik|turn|coturn|stun|webrtc|rtmp|geoip|geosite|openwrt|openclash|mihomo|3x-ui|socks5?|vless|vmess)\b|穿透|代理|路由规则|翻墙")
CN = rx(r"wechat|weixin|微信|小程序|miniprogram|dingtalk|钉钉|alipay|支付宝|qq\b|taobao|淘宝|拼多多|bilibili|哔哩|douyin|抖音|wxjava|weibo|微博")
SEC = rx(r"\b(security|pentest|exploit|vulnerability|malware|hacking|hackers?|ctf|oauth2?|sso|keycloak|jwt|encryption|cryptography|privacy|ssl|tls|xss|waf|2fa|otp|auth|authentication|iam|identity)\b|渗透|安全|隐私|认证")
FRONT_LANG = {"TypeScript","JavaScript","Vue","HTML","CSS","Svelte","SCSS","Less","Astro"}
FRONT = rx(r"\b(react|vue|vue3|nextjs|nuxt|svelte|angular|typescript|javascript|nodejs|npm|webpack|vite|css|tailwind|tailwindcss|html|frontend|front-end|browser|chrome|extension|electron|pwa|editor|markdown|d3|three\.js|canvas|echarts|ant-design|element-ui|shadcn|dashboard|uniapp|uni-app|leaflet|zod|styled-components|ui|ui-kit|design-system)\b|前端|富文本")
JAVA_BACKEND = rx(r"\b(spring|springboot|spring-boot|springcloud|spring-cloud|maven|gradle|jvm|netty|dubbo|jpa|hibernate|quarkus|ktor|rpc|microservices?|swagger|openapi|admin|rbac|cms|erp|saas|workflow|bpm|activiti|crawler|mina|xmpp|backend|server|keycloak|logging|scaffold)\b|后台|管理系统|脚手架|微服务|爬虫")
SELFHOST = rx(r"\b(self-hosted|selfhosted|self-host|homelab|note-taking|notes|todo|rss|wiki|bookmark|password-manager|photos?|media|jellyfin|plex|download|downloader|aria2|music|video|player|reader|pdf|screenshot|screen|remote|rdp|ssh|terminal|clipboard|launcher|translate|translator|vscode|streaming|file-management|ffmpeg|obs|tv|live)\b|下载|播放器|远程|电视|直播|局域网")
DEVTOOL = rx(r"\b(cli|tools?|devtools|developer-tools|api|rest|http|json|yaml|git|github|lint|linter|formatter|debug|debugger|profiler|testing|test|mock|generator|codegen|compiler|parser|regex|logger|library|framework|template|boilerplate|starter|postman|diff|search|build|automation|script|scripts|bash|zsh|vim|neovim|command-line|utility|utilities|release|config|configuration|toolkit)\b|工具")
SYSTEM_LANG = {"C","C++","Rust","Zig","Shell","Makefile","PowerShell","Assembly","Batchfile","Dockerfile","Nix","Lua","CMake"}

LEARN = "学习资源 / Awesome 清单 / 教程"
OVERRIDE = {
 "xiaolai/the-craft-of-selfteaching": LEARN, "lingcoder/OnJava8": LEARN, "Kotlin/kotlin-examples": LEARN,
 "freeCodeCamp/freeCodeCamp": LEARN, "goinaction/code": LEARN, "guolindev/booksource": LEARN,
 "agegr/pi-web": "AI / LLM / Agent / MCP", "budtmo/docker-android": "Docker / K8s / 虚拟化 / DevOps",
 "facebook/infer": "开发者工具 / CLI / 库", "zealic/autorosvpn": "网络 / 代理 / 内网穿透",
 "ssllabs/research": "安全 / 认证 / 隐私", "996icu/996.ICU": "其他 / 待人工确认", "datacamp/RDocumentation": "其他 / 待人工确认",
 "mockito/mockito": "Java / Kotlin 后端 · Spring / 中间件", "alibaba/easyexcel": "Java / Kotlin 后端 · Spring / 中间件",
 "Javen205/IJPay": "Java / Kotlin 后端 · Spring / 中间件", "aosp-mirror/platform_frameworks_base": "Android · 库 / 架构 / 工具",
 "TecharoHQ/anubis": "安全 / 认证 / 隐私", "drone/drone-plugin-index": "Docker / K8s / 虚拟化 / DevOps",
 "drone-plugins/drone-webhook": "Docker / K8s / 虚拟化 / DevOps", "shubolab/drone-webhook": "Docker / K8s / 虚拟化 / DevOps",
 "17mon/china_ip_list": "网络 / 代理 / 内网穿透",
 "ventoy/Ventoy": "系统 / 内核 / C·C++·Rust 底层项目",
}
import importlib.util, os
_sp = importlib.util.spec_from_file_location('ov', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'overrides.py'))
_ov = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_ov)
OVERRIDE.update(_ov.M)
def classify(name, lang, topics, desc):
    repo = name.split("/")[1]
    text = " ".join([repo.replace("-", " ").replace("_", " "), topics.replace(",", " "), desc])
    tl = set(t for t in topics.split(",") if t)
    if name in OVERRIDE: return OVERRIDE[name]
    if AWESOME.search(text) or (lang in ("-","","Jupyter Notebook","Markdown") and AWESOME_WEAK.search(text)):
        return "学习资源 / Awesome 清单 / 教程"
    if AI.search(text): return "AI / LLM / Agent / MCP"
    if lang == "Dart" or "flutter" in repo.lower(): return "Flutter / Dart"
    is_android = bool(ANDROID_RE.search(text)) or "android" in tl
    if is_android or lang in ("Java","Kotlin") and not (JAVA_BACKEND.search(text) or DB.search(text)):
        if ANDROID_SYS.search(text) and is_android: return "Android · 逆向 / 系统 / Root"
        if ANDROID_APP.search(text) and not ANDROID_UI.search(text): return "Android · 开源应用 / 仿写 / Demo"
        if ANDROID_UI.search(text): return "Android · UI 控件 / 动画 / 自定义 View"
        if not is_android and re.search(r"\bjava\b", text, re.I): return "Java / Kotlin 后端 · Spring / 中间件"
        return "Android · 库 / 架构 / 工具" + ("" if is_android else "（按语言推断）")
    if lang in ("Swift","Objective-C") or tl & {"ios","macos","swift","swiftui"}: return "iOS / macOS / Swift"
    if DB.search(text): return "数据库 / 消息队列 / 中间件"
    if NET.search(text): return "网络 / 代理 / 内网穿透"
    if IOT.search(text): return "物联网 / 嵌入式 / 硬件"
    if DEVOPS.search(text): return "Docker / K8s / 虚拟化 / DevOps"
    if CN.search(text): return "微信 / 国内生态"
    if SEC.search(text): return "安全 / 认证 / 隐私"
    if lang in FRONT_LANG or FRONT.search(text): return "前端 · Web / React / Vue / Node"
    if lang == "Go": return "Go · 框架 / 库 / 工具"
    if lang in ("Java","Kotlin","Scala"): return "Java / Kotlin 后端 · Spring / 中间件"
    if SELFHOST.search(text): return "自托管应用 / 多媒体 / 效率工具"
    if DEVTOOL.search(text): return "开发者工具 / CLI / 库"
    if lang in SYSTEM_LANG: return "系统 / 内核 / C·C++·Rust 底层项目"
    if lang == "Python": return "Python 项目"
    if lang in ("-", ""): return LEARN
    return "其他 / 待人工确认"

rows = list(csv.reader(open(src, encoding="utf-8"), delimiter="\t"))
res = []
for r in rows:
    name, lang, stars, topics, desc, arch = (r + [""]*6)[:6]
    res.append((classify(name, lang, topics, desc), name, lang, stars, arch, desc))
w = csv.writer(open(out, "w", encoding="utf-8", newline=""), delimiter="\t")
for x in sorted(res, key=lambda x: (x[0], -int(x[3] or 0))): w.writerow(x)
for k, v in collections.Counter(x[0] for x in res).most_common(): print(v, k)
