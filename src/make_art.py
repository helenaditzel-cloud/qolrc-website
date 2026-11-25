# Generates the abstract artwork used until real photos are added.
import os, random
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "img")
PAL = ["#0d4c7a", "#12629c", "#3d86bd", "#9cc3e0", "#889e29", "#c9d88f", "#eef4f9"]

def hero():
    random.seed(7)
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 640" preserveAspectRatio="xMidYMid slice">',
         '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0d4c7a"/><stop offset="1" stop-color="#12629c"/></linearGradient></defs>',
         '<rect width="1600" height="640" fill="url(#g)"/>']
    for i in range(14):
        cx, cy, r = random.randint(700, 1650), random.randint(-100, 740), random.randint(60, 300)
        col = random.choice(PAL[1:5])
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" opacity="{random.choice([.18,.25,.35,.5])}"/>')
    for k in range(9):
        y = 120 + k * 55
        s.append(f'<path d="M600 {y} C 900 {y-120}, 1200 {y+140}, 1650 {y-40}" fill="none" stroke="#c9d88f" stroke-opacity=".35" stroke-width="2"/>')
    s.append('</svg>')
    open(os.path.join(OUT, "hero-art.svg"), "w").write("\n".join(s))

def card(name, seed, base, accent):
    random.seed(seed)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 300" preserveAspectRatio="xMidYMid slice"><rect width="600" height="300" fill="{base}"/>']
    for i in range(7):
        cx, cy, r = random.randint(0, 600), random.randint(0, 300), random.randint(40, 170)
        s.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{random.choice([accent, "#ffffff", "#9cc3e0"])}" opacity="{random.choice([.15,.22,.3])}"/>')
    for k in range(5):
        y = 60 + k * 45
        s.append(f'<path d="M-20 {y} Q 150 {y-60} 300 {y} T 620 {y}" fill="none" stroke="#ffffff" stroke-opacity=".28" stroke-width="2"/>')
    s.append('</svg>')
    open(os.path.join(OUT, name), "w").write("\n".join(s))

def band():
    s = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 300" preserveAspectRatio="xMidYMid slice"><rect width="1600" height="300" fill="#0d4c7a"/>']
    random.seed(3)
    for i in range(10):
        s.append(f'<circle cx="{random.randint(800,1650)}" cy="{random.randint(-50,350)}" r="{random.randint(50,220)}" fill="{random.choice(PAL[1:4])}" opacity=".3"/>')
    s.append('</svg>')
    open(os.path.join(OUT, "band-art.svg"), "w").write("\n".join(s))

hero(); band()
specs = [("#1b6070", "#f2a541"), ("#0f3d4a", "#9cc3e0"), ("#2f8794", "#c9d88f"),
         ("#3b5f7a", "#f2a541"), ("#1f6b78", "#c9d88f"), ("#0f3d4a", "#f2a541")]
for i, (b, a) in enumerate(specs, 1):
    card(f"theme-{i}.svg", i * 11, b, a)
print("art done")
