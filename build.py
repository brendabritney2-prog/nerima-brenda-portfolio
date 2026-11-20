#!/usr/bin/env python3
"""Static site generator for the interior portfolio."""
import os
from html import escape

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE = "https://brendabritney2-prog.github.io/nerima-brenda-portfolio"
SITE = "Nerima Brenda"
EMAIL = "brendanerima131@gmail.com"
PHONE = "0758596679"

PROJECTS = [
    {
        "slug": "oak-and-light",
        "title": "Oak &amp; Light",
        "plain": "Oak & Light",
        "category": "3D study · Living",
        "year": "2026",
        "typology": "Living room",
        "area": "21.8 m²",
        "scope": "3D visualisation, spatial planning, lighting",
        "palette": "Oak, linen, cream, sage",
        "img": "oak-and-light",
        "glb": "oak-and-light",
        "widths": [1280, 800],
        "w": 1280, "h": 720,
        "alt": "3D render of a warm living room with a linen sofa, oak coffee table, armchair and floor lamp",
        "intro": "A living room modelled around one clear metre of movement, a linen sofa, an oak table and a chair that can be pulled into the light.",
        "body": [
            "The room is 5.2 by 4.2 metres. The sofa is 2.1 metres long with a 450 mm seat height; the coffee table sits at 400 mm, 450 mm in front of it, so legs can pass without the room feeling like a corridor.",
            "Every clearance is drawn rather than guessed: a 900 mm route around the seating, artwork centred at 1.5 metres, and a window sized above one-eighth of the floor area. The render tests the proportions before materials are committed.",
        ],
        "captions": ["The seating group in warm afternoon light", "Linen, oak and a single brass note"],
        "card": "wide",
    },
    {
        "slug": "quiet-quarters",
        "title": "Quiet Quarters",
        "plain": "Quiet Quarters",
        "category": "3D study · Bedroom",
        "year": "2026",
        "typology": "Bedroom",
        "area": "18.5 m²",
        "scope": "3D visualisation, layout, joinery study",
        "palette": "Oat, linen, oak, brass",
        "img": "quiet-quarters",
        "glb": "quiet-quarters",
        "widths": [1280, 800],
        "w": 1280, "h": 720,
        "alt": "3D render of a calm bedroom with a low bed, slatted oak headboard, nightstands and sliding wardrobe",
        "intro": "A bedroom drawn to rest: a 1.6-metre bed with 600 mm either side, a slatted oak headboard and a wardrobe that disappears into the wall.",
        "body": [
            "At 4.4 by 4.2 metres the room can hold the bed, two 450 mm nightstands and a full-height wardrobe without crowding the route to the window. The mattress sits at 540 mm, low enough to read as calm, high enough to rise from easily.",
            "The headboard is a screen of oak slats; the wardrobe runs the left wall at 600 mm deep. Everything else is left quiet so the morning light has somewhere to land.",
        ],
        "captions": ["Washed linen and a low oak ledge", "Soft light at the edge of the room"],
        "card": "narrow",
    },
    {
        "slug": "warm-kitchen",
        "title": "The Warm Kitchen",
        "plain": "The Warm Kitchen",
        "category": "3D study · Kitchen",
        "year": "2026",
        "typology": "Kitchen",
        "area": "18.2 m²",
        "scope": "3D visualisation, joinery design, lighting",
        "palette": "Oak, cream, charcoal, brass",
        "img": "warm-kitchen",
        "glb": "warm-kitchen",
        "widths": [1280, 800],
        "w": 1280, "h": 720,
        "alt": "3D render of a warm oak kitchen with a stone worktop, island, stools and pendant lights",
        "intro": "A working kitchen modelled around the work triangle, fridge, range and sink within 1.5 to 2.7 metres of one another.",
        "body": [
            "The back run holds 900 mm worktops over 600 mm cabinets, with the fridge, range and sink spaced to keep the work triangle compact. A 2.2-metre island sits behind a 1.1-metre aisle, close enough to pass a plate across.",
            "Pendants hang 750 mm above the island, the height that lights the surface without blocking the view. Oak, cream and blackened steel keep the room warm rather than clinical.",
        ],
        "captions": ["Oak joinery and honed stone", "The working edge, in detail"],
        "card": "half",
    },
    {
        "slug": "reading-nook",
        "title": "Reading Nook",
        "plain": "Reading Nook",
        "category": "3D study · Study",
        "year": "2026",
        "typology": "Study corner",
        "area": "20 m²",
        "scope": "3D visualisation, spatial study",
        "palette": "Linen, sage, oak, brass",
        "img": "reading-nook",
        "glb": "reading-nook",
        "widths": [1280, 800],
        "w": 1280, "h": 720,
        "alt": "3D render of a reading nook with a linen armchair, brass side table and full bookshelf",
        "intro": "A quiet corner modelled at full scale: a 450 mm linen armchair, a brass side table at 545 mm and a wall of books.",
        "body": [
            "This study asks how little a room needs. A chair, a light, a surface for a cup, and enough books to make the walls feel inhabited. The answer is not much, but each object has to earn its place.",
            "The seat sits at 450 mm with a 545 mm table beside it, both within reach of the window light. The palette moves between linen, sage and oak, with brass only where the hand might rest.",
        ],
        "captions": ["The corner in warm evening light", "Books, brass and a place to sit"],
        "card": "half",
    },
    {
        "slug": "dining-corner",
        "title": "Dining Corner",
        "plain": "Dining Corner",
        "category": "3D study · Dining",
        "year": "2026",
        "typology": "Dining",
        "area": "21 m²",
        "scope": "3D visualisation, layout, lighting",
        "palette": "Oak, terracotta, sage, cream",
        "img": "dining-corner",
        "glb": "dining-corner",
        "widths": [1280, 800],
        "w": 1280, "h": 720,
        "alt": "3D render of a dining room with an oak table, four chairs, low pendant and sideboard",
        "intro": "A 1.8-metre oak table under a pendant hung 750 mm above the surface, a dining room drawn for slow evenings.",
        "body": [
            "Four chairs sit at 450 mm, leaving a 300 mm thigh clearance under the 750 mm tabletop and 900 mm behind each chair to pull out. The pendant pools light on the table rather than the room.",
            "A sideboard runs the back wall, holding bowls, a vase and the things a dining room gathers. Terracotta and sage keep the oak from feeling too polite.",
        ],
        "captions": ["Oak, terracotta and pooled light", "The sideboard, dressed simply"],
        "card": "full",
    },
]

ICON_ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M7 17L17 7M9 7h8v8"/></svg>'
ICON_DOWN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 4v16m0 0l-6-6m6 6l6-6"/></svg>'
ICON_LEFT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M19 12H5m0 0l6-6m-6 6l6 6"/></svg>'
ICON_UP = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M12 20V4m0 0l-6 6m6-6l6 6"/></svg>'


def head(title, desc, image, rel="", canonical=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{escape(desc)}">
<meta name="theme-color" content="#f7f2ea">
<link rel="canonical" href="{BASE}/{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:image" content="{BASE}/assets/img/{image}">
<meta property="og:url" content="{BASE}/{canonical}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{escape(desc)}">
<meta name="twitter:image" content="{BASE}/assets/img/{image}">
<link rel="icon" href="{rel}assets/favicon.svg" type="image/svg+xml">
<script>document.documentElement.classList.add("js");</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..600;1,9..144,300..600&family=Manrope:wght@300..700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel}assets/css/style.css">
<script type="importmap">{{"imports":{{"three":"{rel}assets/vendor/three.module.js","three/addons/":"{rel}assets/vendor/addons/"}}}}</script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(rel="", current=""):
    links = [
        ("#work", "Work", "work"),
        ("#studio", "About", "studio"),
        ("#practice", "Practice", "practice"),
        ("#process", "Process", "process"),
        ("#contact", "Contact", "contact"),
    ]
    parts = []
    for h, label, key in links:
        active = ' aria-current="page"' if current == key else ""
        parts.append(f'<a href="{rel}index.html{h}"{active}>{label}</a>')
    nav = "".join(parts)
    return f"""<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{rel}index.html">
      <span class="mark" aria-hidden="true">N</span>
      <span class="name">{SITE}</span>
    </a>
    <button class="menu-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="nav"><span></span></button>
    <nav class="nav" id="nav" aria-label="Main">
      {nav}
      <a class="cta" href="mailto:{EMAIL}">Start a project</a>
    </nav>
  </div>
</header>
"""


def footer(rel=""):
    return f"""<footer class="site-footer">
  <div class="wrap footer-inner">
    <span>© <span data-year>2026</span> {SITE} · Interior and landscape design</span>
    <a class="to-top" href="#top">Back to top {ICON_UP}</a>
  </div>
</footer>
<script src="{rel}assets/js/main.js" defer></script>
</body>
</html>
"""


def card(p, index):
    cls = {
        "wide": "card--wide",
        "narrow": "card--narrow",
        "half": "card--half",
        "full": "card--full",
    }[p["card"]]
    sizes = "(max-width:760px) 100vw, 60vw" if p["card"] in ("wide", "full") else "(max-width:760px) 100vw, 45vw"
    if p["card"] == "full":
        sizes = "(max-width:760px) 100vw, 100vw"
    widths = p.get("widths", [1800, 1200, 800])
    main = max(widths)
    srcset = ", ".join(f"assets/img/{p['img']}-{w}.webp {w}w" for w in widths)
    badge = '<span class="card-3d">3D view</span>' if p.get("glb") else ""
    return f"""<a class="card {cls} reveal" href="work/{p['slug']}.html" data-delay="{index % 3}">
  <div class="card-media">
    <span class="card-index">{index + 1:02d}</span>{badge}
    <img src="assets/img/{p['img']}-{main}.webp"
         srcset="{srcset}"
         sizes="{sizes}" width="{p['w']}" height="{p['h']}"
         alt="{escape(p['alt'])}" loading="lazy" decoding="async">
  </div>
  <div class="card-meta">
    <h3>{p['title']}</h3>
    <span>{p['category']} · {p['year']}</span>
  </div>
</a>"""


def index():
    cards = "\n".join(card(p, i) for i, p in enumerate(PROJECTS))
    ticker_items = [
        "Residential interiors", "Material palettes", "Spatial planning",
        "Styling", "3D visualisation", "Warm minimalism",
    ]
    ticker = "".join(f"<span>{t}</span>" for t in ticker_items)
    html = head(
        f"{SITE}, Interior and landscape design",
        "Nerima Brenda is an interior and landscape designer in Kampala working on residential interiors, custom furniture, floor plans, 3D design and landscaping.",
        "oak-and-light-og.webp",
    )
    html += header()
    html += f"""<main id="main">
<section class="hero" id="top">
  <div class="wrap hero-grid">
    <div>
        <span class="eyebrow reveal">Interior and landscape design · Kampala</span>
        <h1 class="reveal" data-delay="1">Spaces shaped around <em>the way you live.</em></h1>
        <p class="lede reveal" data-delay="2">I am {SITE}, an interior designer and landscape design graduate. I turn briefs into buildable drawings, custom furniture and rooms that feel considered from the first sketch to the final finish.</p>
      <div class="hero-actions reveal" data-delay="3">
        <a class="btn btn-dark" href="#work">View selected work {ICON_DOWN}</a>
        <a class="btn btn-ghost" href="#contact">Start a project {ICON_ARROW}</a>
      </div>
      <div class="hero-meta reveal" data-delay="3">
        <div><strong>05</strong>Room studies</div>
        <div><strong>05</strong>Orbitable models</div>
        <div><strong>KLA</strong>Kampala, Uganda</div>
      </div>
    </div>
    <div class="hero-visual reveal" data-delay="2">
      <div class="arch">
        <img src="assets/img/oak-and-light-1280.webp"
             srcset="assets/img/oak-and-light-800.webp 800w, assets/img/oak-and-light-1280.webp 1280w"
             sizes="(max-width:1000px) 90vw, 44vw" width="1280" height="720"
             alt="3D render of a warm living room with a linen sofa, oak coffee table and soft daylight" fetchpriority="high" decoding="async">
      </div>
      <div class="hero-note"><strong>Oak &amp; Light</strong>Living room · 3D study, 2026</div>
    </div>
  </div>
</section>

<div class="ticker" aria-hidden="true">
  <div class="ticker-track">{ticker}{ticker}</div>
</div>

<section class="section" id="work">
  <div class="wrap">
    <div class="section-head">
      <div>
        <span class="eyebrow reveal">Selected work</span>
        <h2 class="reveal" data-delay="1">A quiet collection of rooms</h2>
      </div>
      <p class="reveal" data-delay="2">Five rooms, modelled and measured in Blender, then published as orbitable 3D models. Open any room to move around it.</p>
    </div>
    <div class="work-grid">
      {cards}
    </div>
  </div>
</section>

<section class="section about" id="studio">
  <div class="wrap about-grid">
    <div class="about-figure reveal">
      <img src="assets/img/brenda-01-810.webp"
           srcset="assets/img/brenda-01-540.webp 540w, assets/img/brenda-01-810.webp 810w"
           sizes="(max-width:1000px) 80vw, 38vw" width="810" height="1080"
           alt="Nerima Brenda, interior and landscape designer" loading="lazy" decoding="async">
      <span class="tag">Nerima · Kampala</span>
    </div>
    <div class="about-copy">
      <span class="eyebrow reveal">About Nerima</span>
      <h2 class="reveal" data-delay="1">Design that starts at the drawing board.</h2>
      <p class="reveal" data-delay="2">I graduated from Kyambogo University with a Bachelor of Interior and Landscape Design, then completed two internships at Meek Construction Company Limited. There I worked directly with clients on furniture and interiors, from TV wall units and kitchen cabinets to floor plans, site plans and 3D designs.</p>
      <p class="reveal" data-delay="2">I like customising. That means starting with a blank sheet, developing a concept from scratch and making pieces that are not already on the market. I keep an eye on current trends, but the final decision always belongs to the person who will live with the space.</p>
      <blockquote class="big-quote reveal" data-delay="3">“A good design is one you can build, afford and still love a year later.”</blockquote>
      <div class="services reveal" data-delay="3">
        <div><span>Residential interiors</span><span>Whole-home concepts</span></div>
        <div><span>Custom furniture</span><span>Concept to drawing</span></div>
        <div><span>Space planning</span><span>Floor and site plans</span></div>
        <div><span>3D design</span><span>Visual studies</span></div>
        <div><span>Colour and styling</span><span>Finishes and objects</span></div>
        <div><span>Landscaping</span><span>Compounds and planting</span></div>
      </div>
      <p class="reveal" data-delay="3" style="margin-top:26px"><a class="link-arrow" href="assets/nerima-brenda-cv.pdf" target="_blank" rel="noopener">Download CV {ICON_ARROW}</a></p>
    </div>
  </div>
</section>

<section class="section practice" id="practice">
  <div class="wrap">
    <div class="section-head">
      <div>
        <span class="eyebrow reveal">In practice</span>
        <h2 class="reveal" data-delay="1">From brief to finished space</h2>
      </div>
      <p class="reveal" data-delay="2">A look at the work behind the drawings: client projects, material choices and the small details that make a room feel complete.</p>
    </div>
    <div class="practice-grid">
      <figure class="reveal">
        <img src="assets/img/brenda-02-960.webp" srcset="assets/img/brenda-02-640.webp 640w, assets/img/brenda-02-960.webp 960w" sizes="(max-width:1000px) 90vw, 50vw" width="960" height="1280" alt="Interior and furniture work by Nerima Brenda" loading="lazy" decoding="async">
        <figcaption>Furniture and interior detailing, from concept to drawing</figcaption>
      </figure>
      <figure class="reveal" data-delay="1">
        <img src="assets/img/brenda-03-498.webp" srcset="assets/img/brenda-03-360.webp 360w, assets/img/brenda-03-498.webp 498w" sizes="(max-width:1000px) 90vw, 40vw" width="498" height="1080" alt="A project from Nerima Brenda's design practice" loading="lazy" decoding="async">
        <figcaption>Residential planning, colour and styling</figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="section" id="process">
  <div class="wrap">
    <div class="section-head">
      <div>
        <span class="eyebrow reveal">How it works</span>
        <h2 class="reveal" data-delay="1">Four clear steps</h2>
      </div>
      <p class="reveal" data-delay="2">A simple, transparent process from first conversation to drawings you can build from.</p>
    </div>
    <div class="process-grid">
      <article class="step reveal"><span class="num">01</span><h3>Brief</h3><p>We talk about how the space is used, what you want to keep and what needs to change.</p></article>
      <article class="step reveal" data-delay="1"><span class="num">02</span><h3>Draw</h3><p>Floor plans, site plans and 3D views give you something concrete to respond to.</p></article>
      <article class="step reveal" data-delay="2"><span class="num">03</span><h3>Customise</h3><p>Furniture, joinery, colour and finishes are developed from the drawing board.</p></article>
      <article class="step reveal" data-delay="3"><span class="num">04</span><h3>Hand over</h3><p>You receive clear drawings and a palette you can take to a builder or installer.</p></article>
    </div>
  </div>
</section>

<section class="contact" id="contact">
  <div class="wrap contact-grid">
    <div>
      <span class="eyebrow reveal">Contact</span>
      <h2 class="reveal" data-delay="1">Let’s design a space that feels like <em>yours.</em></h2>
      <p class="reveal" data-delay="2">Available for residential interiors, custom furniture, floor plans and landscaping. Share a few lines about your space and timeline.</p>
      <a class="mail reveal" data-delay="3" href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
    <div class="contact-side reveal" data-delay="3">
      <div><span class="label">Based in</span>Kampala, Uganda, working across East Africa</div>
      <div><span class="label">Phone</span><a href="tel:+256758596679">{PHONE}</a></div>
      <div><span class="label">CV</span><a href="assets/nerima-brenda-cv.pdf" target="_blank" rel="noopener">Download PDF</a></div>
      <div><span class="label">Response</span>Within two working days</div>
    </div>
  </div>
</section>
</main>
"""
    html += footer()
    return html


def viewer_section(p):
    return f"""<section class="section viewer-section" id="3d">
  <div class="wrap">
    <div class="section-head">
      <div>
        <span class="eyebrow reveal">Interactive 3D</span>
        <h2 class="reveal" data-delay="1">Step inside {p['plain']}</h2>
      </div>
      <p class="reveal" data-delay="2">A real-time model built in Blender. Drag to orbit, scroll or pinch to zoom, and open it fullscreen to look closer. Use the arrow keys to move and press 0 to reset.</p>
    </div>
    <div class="viewer reveal" data-3d data-model="../assets/models/{p['glb']}.glb" data-poster="../assets/img/{p['img']}-1280.webp" data-name="{escape(p['plain'])}">
      <div class="viewer-stage" tabindex="0" role="application" aria-label="Interactive 3D model of {escape(p['plain'])}. Drag to orbit, scroll to zoom, or use the arrow keys. Press 0 to reset.">
        <img class="viewer-poster" src="../assets/img/{p['img']}-1280.webp" width="1280" height="720" alt="{escape(p['alt'])}" loading="lazy" decoding="async">
        <div class="viewer-loader" role="status" data-viewer-loader><span>Loading 3D model</span><span class="viewer-bar"><i></i></span></div>
        <div class="viewer-error" role="alert" data-viewer-error hidden><span>3D preview unavailable, the render above still shows the room.</span></div>
      </div>
      <div class="viewer-toolbar">
        <span class="viewer-hint">Drag to orbit · Scroll to zoom</span>
        <div class="viewer-actions">
          <button type="button" data-viewer-rotate aria-pressed="true" disabled>Auto-rotate: on</button>
          <button type="button" data-viewer-reset disabled>Reset view</button>
          <button type="button" data-viewer-fullscreen disabled>Fullscreen</button>
        </div>
      </div>
    </div>
  </div>
</section>
<script type="module" src="../assets/js/viewer3d.js"></script>"""


def project_page(p, nxt, prev, index):
    widths = p.get("widths", [1280, 800])
    main = max(widths)
    body = "".join(f"<p>{escape(par)}</p>" for par in p["body"])
    viewer = viewer_section(p) if p.get("glb") else ""
    chip = '<a class="project-chip" href="#3d">Explore in 3D</a>' if p.get("glb") else ""
    html = head(
        f"{p['plain']}, {SITE}",
        p["intro"],
        f"{p['img']}-og.webp",
        rel="../",
        canonical=f"work/{p['slug']}.html",
    )
    html += header(rel="../")
    html += f"""<main id="main">
<section class="project-hero">
  <div class="wrap">
    <a class="back" href="../index.html#work">{ICON_LEFT} All work</a>
    <div class="project-intro">
      <div>
        <span class="eyebrow" style="margin-top:26px;display:inline-flex">{p['category']} · {p['year']}</span>
        <h1 class="project-title">{p['title']}</h1>{chip}
      </div>
      <p>{p['intro']}</p>
    </div>
    <div class="project-main">
      <img src="../assets/img/{p['img']}-{main}.webp" width="{p['w']}" height="{p['h']}" alt="{escape(p['alt'])}" fetchpriority="high" decoding="async">
    </div>
    <div class="project-meta">
      <div><span class="label">Typology</span><span class="value">{p['typology']}</span></div>
      <div><span class="label">Year</span><span class="value">{p['year']}</span></div>
      <div><span class="label">Area</span><span class="value">{p['area']}</span></div>
      <div><span class="label">Palette</span><span class="value">{p['palette']}</span></div>
    </div>
  </div>
</section>

<section class="wrap project-body">
  <h2 class="reveal">Modelled at full scale, finished in light.</h2>
  <div class="prose reveal" data-delay="1">{body}</div>
</section>

{viewer}

<a class="next" href="{nxt['slug']}.html">
  <div class="wrap">
    <span class="eyebrow">Next project</span>
    <h2>{nxt['title']} {ICON_ARROW}</h2>
  </div>
</a>
</main>
"""
    html += footer(rel="../")
    return html


def main():
    os.makedirs(os.path.join(ROOT, "work"), exist_ok=True)
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(index())
    for i, p in enumerate(PROJECTS):
        nxt = PROJECTS[(i + 1) % len(PROJECTS)]
        prev = PROJECTS[(i - 1) % len(PROJECTS)]
        with open(os.path.join(ROOT, "work", p["slug"] + ".html"), "w", encoding="utf-8") as f:
            f.write(project_page(p, nxt, prev, i))
    urls = [""] + [f"work/{p['slug']}.html" for p in PROJECTS]
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        sitemap += f"  <url><loc>{BASE}/{u}</loc></url>\n"
    sitemap += "</urlset>\n"
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
    print("Built", len(urls), "pages")


if __name__ == "__main__":
    main()
