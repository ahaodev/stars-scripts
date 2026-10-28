import sys
tpl, data_path, out = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(tpl, encoding="utf-8").read()
dark = """  color-scheme:dark;
  --plane:#0d0d0d; --surface:#1a1a19; --ink:#f0efec; --ink2:#c3c2b7; --muted:#898781;
  --grid:#2c2c2a; --axis:#383835; --ring:rgba(255,255,255,.10); --wash:rgba(255,255,255,.07);
  --s1:#3987e5; --s2:#d95926; --s3:#199e70; --s4:#c98500; --s5:#d55181; --s6:#008300; --s7:#9085e9;"""
t = t.replace("/*DARK_MEDIA*/", '@media (prefers-color-scheme:dark){:root:where(:not([data-theme="light"])){\n' + dark + "\n}}")
t = t.replace("/*DARK_ATTR*/", ':root[data-theme="dark"]{\n' + dark + "\n}")
data = open(data_path, encoding="utf-8").read().replace("</", "<\\/")
t = t.replace("/*DATA*/", data)
open(out, "w", encoding="utf-8").write(t)
print(len(t) // 1024, "KB ->", out)
