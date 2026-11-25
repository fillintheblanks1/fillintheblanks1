import html
USER = "fillintheblanks1"; LEETCODE = "fillintheblanks1"
RAMP = "@%#*+=-:. "
INV = {c: RAMP[len(RAMP)-1-i] for i, c in enumerate(RAMP)}

lines = [l.rstrip("\n") for l in open("art.txt")]
W = max(map(len, lines)); lines = [l.ljust(W, "@") for l in lines]
# crop columns that are pure background
cols = [i for i in range(W) if any(l[i] != "@" for l in lines)]
c0, c1 = min(cols), max(cols) + 1
art = ["".join(INV.get(ch, ch) for ch in l[c0:c1]).rstrip() for l in lines]
NC = c1 - c0

T = {
 "dark_mode":  dict(bg="#0d1117", border="#238636", key="#3fb950", val="#e6edf3", dim="#8b949e", head="#56d364", art="#3fb950", edge="#30363d"),
 "light_mode": dict(bg="#ffffff", border="#1a7f37", key="#1a7f37", val="#1f2328", dim="#59636e", head="#116329", art="#1a7f37", edge="#d0d7de"),
}
esc = lambda s: html.escape(s, quote=False)
ART_W = 400.0; cw = ART_W / NC; fs = cw / 0.6; lh = fs * 1.05
art_h = lh * len(art); X0 = 28; IX = int(X0 + ART_W + 32)

rows = [("OS","GitHub / Arch-ish"),("Host","Piyush"),("Kernel","learning"),("Shell","mysh (C++)"),("Uptime","Building & Learning")]
work = [("Project",f"github.com/{USER}/mysh"),("Learning","App Development"),("Stack","C, C++, Bash, Python, Swift, Figma"),("Trivia","I love the classics")]
contact = [("Email","piyush0x1904@gmail.com"),("LinkedIn","linkedin.com/in/peeyoushhhh"),("LeetCode",f"leetcode.com/u/fillintheblanks1"),("GitHub",f"github.com/fillintheblanks1")]

def build(t):
    info = []; y = 44
    info.append(f'<tspan x="{IX}" y="{y}" fill="{t["key"]}" font-weight="bold">piyush</tspan><tspan fill="{t["dim"]}">@</tspan><tspan fill="{t["key"]}" font-weight="bold">github</tspan>'); y += 20
    info.append(f'<tspan x="{IX}" y="{y}" fill="{t["border"]}">-------------</tspan>'); y += 24
    def sect(items):
        nonlocal y
        for k, v in items:
            info.append(f'<tspan x="{IX}" y="{y}" fill="{t["key"]}" font-weight="bold">{esc((k+":").ljust(10))}</tspan><tspan fill="{t["val"]}">{esc(v)}</tspan>'); y += 20
    sect(rows); y += 12
    info.append(f'<tspan x="{IX}" y="{y}" fill="{t["head"]}" font-weight="bold">- Workspace -</tspan>'); y += 22; sect(work); y += 12
    info.append(f'<tspan x="{IX}" y="{y}" fill="{t["head"]}" font-weight="bold">- Contact -</tspan>'); y += 22; sect(contact)
    pal_y = y + 6; H = pal_y + 10 + 24
    ay = (H - art_h) / 2 + fs
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="860" height="{H}" viewBox="0 0 860 {H}">',
         f'<rect x="1" y="1" width="858" height="{H-2}" rx="12" fill="{t["bg"]}" stroke="{t["border"]}" stroke-width="1.5"/>',
         f'<g font-family="monospace" font-size="{fs:.2f}" fill="{t["art"]}" xml:space="preserve">']
    for i, l in enumerate(art):
        if l.strip():
            o.append(f'<text x="{X0}" y="{ay+i*lh:.2f}" textLength="{len(l)*cw:.2f}" lengthAdjust="spacing">{esc(l)}</text>')
    o.append('</g>')
    o.append(f'<text font-family="monospace" font-size="14" xml:space="preserve">' + "".join(info) + '</text>')
    for i, c in enumerate(["#0d4429","#006d32","#26a641","#39d353","#56d364","#7ee787","#aff5b4","#e6edf3"]):
        o.append(f'<rect x="{IX+i*28}" y="{pal_y}" width="24" height="10" rx="2" fill="{c}" stroke="{t["edge"]}" stroke-width="0.5"/>')
    o.append('</svg>')
    return "\n".join(o)

for n, t in T.items():
    open(f"./{n}.svg", "w").write(build(t))
print("cols", NC, "rows", len(art))
