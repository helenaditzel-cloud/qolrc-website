# -*- coding: utf-8 -*-
"""
Builds the static QoLRC website from src/content.py.
Run from the repository root:  python3 src/build.py
English pages go in the repository root, Danish pages in /da/.
"""
import html
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
import content as C  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ["en", "da"]

UI = {
    "skip": {"en": "Skip to main content", "da": "Gå til hovedindhold"},
    "menu": {"en": "Menu", "da": "Menu"},
    "switch": {"en": "Dansk", "da": "English"},
    "switch_label": {"en": "Se siden på dansk", "da": "View this page in English"},
    "read_more_studies": {"en": "See our ongoing studies", "da": "Se vores igangværende studier"},
    "contact_us": {"en": "Contact us", "da": "Kontakt os"},
    "registry": {"en": "ClinicalTrials.gov", "da": "ClinicalTrials.gov"},
    "our_role": {"en": "Our role", "da": "Vores rolle"},
    "visit": {"en": "Visit website", "da": "Besøg hjemmeside"},
    "pages": {"en": "Pages", "da": "Sider"},
    "all_contact": {"en": "All contact details", "da": "Alle kontaktoplysninger"},
    "home": {"en": "Home", "da": "Forside"},
    "breadcrumb": {"en": "Breadcrumb", "da": "Brødkrumme"},
    "figures": {"en": "QoLRC in numbers", "da": "QoLRC i tal"},
    "profile": {"en": "Research profile", "da": "Forskerprofil"},
    "more_info": {"en": "More information", "da": "Mere information"},
    "danish_badge": {"en": "Danish validation", "da": "Dansk validering"},
    "our_paper": {"en": "Our paper", "da": "Vores artikel"},
    "useful_links": {"en": "Useful links", "da": "Nyttige links"},
    "photos": {"en": "Photos:", "da": "Fotos:"},
    "all": {"en": "All", "da": "Alle"},
    "filter_by": {"en": "Filter by person", "da": "Filtrér efter person"},
    "pub_source": {"en": "From PubMed, updated automatically every week. Last updated", "da": "Fra PubMed, opdateres automatisk hver uge. Senest opdateret"},
    "become_rep": {"en": "Become a patient representative", "da": "Bliv patientrepræsentant"},
    "how_we_help": {"en": "How we can help", "da": "Hvordan vi kan hjælpe"},
    "portrait_of": {"en": "Portrait of", "da": "Portræt af"},
    "photo_missing": {"en": "Photo coming soon", "da": "Foto følger"},
}


def t(value, lang):
    """Return the text for a language; plain strings are used as they are."""
    if isinstance(value, dict):
        return value[lang]
    return value


def esc(text):
    """Escape text and turn TODO(...) markers into visible notes."""
    out = html.escape(text)
    return re.sub(r"TODO\((.*?)\)", r'<mark class="todo">To do: \1</mark>', out)


def page_path(page, lang):
    base = "" if lang == "en" else "da/"
    return base + ("index.html" if page == "about" else page + "/index.html")


def url(page, lang, depth):
    prefix = "../" * depth
    base = "" if lang == "en" else "da/"
    return prefix + base + ("" if page == "about" else page + "/")


def depth_of(page, lang):
    return (0 if page == "about" else 1) + (1 if lang == "da" else 0)


def layout(page, lang, title, body, description):
    d = depth_of(page, lang)
    up = "../" * d
    other = "da" if lang == "en" else "en"
    labels = {p: (en if lang == "en" else da) for p, en, da in C.NAV}
    current = ' aria-current="page"'
    nav_items = "\n".join(
        f'<li><a href="{url(p, lang, d)}"{current if p == page else ""}>{esc(labels[p])}</a></li>'
        for p, _, _ in C.NAV
    )
    footer_links = "\n".join(
        f'<li><a href="{url(p, lang, d)}">{esc(labels[p])}</a></li>' for p, _, _ in C.NAV
    )
    canonical = C.SITE["domain"] + "/" + page_path(page, lang).replace("index.html", "")
    alt = C.SITE["domain"] + "/" + page_path(page, other).replace("index.html", "")
    full_title = (title + " | " if page != "about" else "") + "QoLRC, " + t(C.SITE["name"], lang)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="{lang}" href="{canonical}">
<link rel="alternate" hreflang="{other}" href="{alt}">
<link rel="icon" href="{up}assets/favicon.png" type="image/png">
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
<a class="skip" href="#main">{UI['skip'][lang]}</a>
<div class="topbar">
  <div class="wrap topbar-inner">
    <span>{esc(t(C.SITE['affiliation'], lang))}</span>
    <a class="lang-switch" href="{url(page, other, d)}" hreflang="{other}" lang="{other}" aria-label="{UI['switch_label'][lang]}">{UI['switch'][lang]}</a>
  </div>
</div>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{url('about', lang, d)}">
      <img class="brand-logo" src="{up}assets/img/logo.png" alt="Quality of Life Research Center OUH" width="828" height="394">
    </a>
    <a class="button header-cta" href="{url('contact', lang, d)}">{UI['contact_us'][lang]}</a>
  </div>
  <nav class="main-nav" aria-label="{UI['pages'][lang]}">
    <div class="wrap">
      <details class="nav-toggle">
        <summary>{UI['menu'][lang]}</summary>
        <ul>{nav_items}</ul>
      </details>
      <ul class="nav-desktop">{nav_items}</ul>
    </div>
  </nav>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap footer-grid">
    <div>
      <a class="brand brand-footer" href="{url('about', lang, d)}">
        <img class="brand-logo" src="{up}assets/img/logo-white.png" alt="Quality of Life Research Center OUH" width="828" height="394">
      </a>
      <p>{esc(t(C.SITE['footer_text'], lang))}</p>
    </div>
    <nav aria-label="{UI['pages'][lang]}">
      <p class="footer-heading">{UI['pages'][lang]}</p>
      <ul class="footer-links">{footer_links}</ul>
    </nav>
    <div>
      <p class="footer-heading">{UI['contact_us'][lang]}</p>
      <address>{"<br>".join(esc(t(line, lang)) for line in C.CONTACT['address'][1:5])}</address>
      <p><a href="mailto:{C.CONTACT['email']}">{C.CONTACT['email']}</a></p>
      <p><a href="{url('contact', lang, d)}">{UI['all_contact'][lang]} &rarr;</a></p>
    </div>
  </div>
  <div class="footer-bottom"><div class="wrap">{esc(t(C.SITE['privacy'], lang))} {UI['photos'][lang]} <a href="https://unsplash.com">Unsplash</a>.</div></div>
</footer>
</body>
</html>
"""


def page_header(page, title, intro, lang):
    d = depth_of(page, lang)
    src, has_photo = art(f"header-{page}", "", "../" * d)
    style = (f' style="background-image:linear-gradient(100deg, rgba(10,42,51,.94) 0%, rgba(15,61,74,.85) 45%, rgba(15,61,74,.45) 100%), url(\'{src}\')"'
             if has_photo else "")
    return f"""<section class="page-head{' page-head-photo' if has_photo else ''}"{style}>
  <div class="wrap">
    <nav class="crumbs" aria-label="{UI['breadcrumb'][lang]}">
      <a href="{url('about', lang, d)}">{UI['home'][lang]}</a> <span aria-hidden="true">/</span> <span aria-current="page">{esc(title)}</span>
    </nav>
    <h1>{esc(title)}</h1>
    <p class="lead">{esc(t(intro, lang))}</p>
  </div>
</section>"""


def nav_label(page, lang):
    for p, en, da in C.NAV:
        if p == page:
            return en if lang == "en" else da


# ------------------------------------------------------------------ pages

def art(photo_name, fallback, up):
    """Use a real photo from assets/img/photos/ if it exists, otherwise the generated artwork."""
    for ext in (".jpg", ".jpeg", ".png", ".webp"):
        if os.path.exists(os.path.join(ROOT, "assets", "img", "photos", photo_name + ext)):
            return f"{up}assets/img/photos/{photo_name}{ext}", True
    return f"{up}assets/img/{fallback}", False


def about(lang):
    a = C.ABOUT
    d = depth_of("about", lang)
    up = "../" * d
    hero_src, _ = art("hero", "hero-art.svg", up)
    band_src, band_photo = art("band", "band-art.svg", up)
    band_overlay = "linear-gradient(90deg, rgba(10,42,51,.92), rgba(10,42,51,.7)), " if band_photo else ""
    paras = "\n".join(f"<p>{md_links(p)}</p>" for p in a["intro"][lang])
    cards = "\n".join(
        f"""<li class="card theme">
  <div class="card-icon"><img src="{up}assets/img/icons/theme-{i}.svg" alt="" width="56" height="56"></div>
  <div class="card-body">
    <h3>{esc(t(th['title'], lang))}</h3>
    <p>{esc(t(th['text'], lang))}</p>
    {f'<p><a href="{url("patients", lang, d)}">{UI["become_rep"][lang]} &rarr;</a></p>' if i == 6 else ""}
  </div>
</li>"""
        for i, th in enumerate(a["themes"], 1)
    )
    figures = "\n".join(
        f'<li><span class="fig-value">{esc(f["value"])}</span><span class="fig-label">{esc(t(f["label"], lang))}</span></li>'
        for f in a["figures"]
    )
    body = f"""<section class="hero" style="background-image:url('{hero_src}')">
  <div class="wrap">
    <div class="hero-panel">
      <p class="eyebrow">{esc(t(C.SITE['affiliation'], lang))}</p>
      <h1>{esc(t(a['hero_title'], lang))}</h1>
      <p class="hero-lead">{esc(t(a['hero_lead'], lang))}</p>
      <p class="hero-actions"><a class="button" href="{url('studies', lang, d)}">{UI['read_more_studies'][lang]} &rarr;</a></p>
    </div>
  </div>
</section>
<section class="figures" aria-label="{UI['figures'][lang]}">
  <div class="wrap"><ul class="figures-list">{figures}</ul></div>
</section>
<section class="section">
  <div class="wrap split">
    <div class="prose">
      <p class="kicker">QoLRC</p>
      <h2>{esc(t(a['intro_heading'], lang))}</h2>
      {paras}
    </div>
    <aside class="contact-box" aria-labelledby="cb-h">
      <h2 id="cb-h">{esc(t(a['contact_box_heading'], lang))}</h2>
      <p>{esc(t(a['contact_box_text'], lang))}</p>
      <p><a class="button button-accent" href="{url('contact', lang, d)}">{UI['contact_us'][lang]} &rarr;</a></p>
    </aside>
  </div>
</section>
<section class="section section-tint">
  <div class="wrap">
    <h2 class="section-title">{esc(t(a['themes_heading'], lang))}</h2>
    <ul class="grid grid-3">{cards}</ul>
  </div>
</section>
<section class="band" style="background-image:{band_overlay}url('{band_src}')">
  <div class="wrap band-inner">
    <div>
      <h2>{esc(t(a['advice_heading'], lang))}</h2>
      <p>{esc(t(a['advice_text'], lang))}</p>
    </div>
    <p><a class="button button-accent" href="{url('pro', lang, d)}">{UI['how_we_help'][lang]} &rarr;</a></p>
  </div>
</section>"""
    return layout("about", lang, nav_label("about", lang), body, t(a["hero_lead"], lang))


def studies(lang):
    sections = []
    for gid, gtitle in C.STUDY_GROUPS:
        items = []
        for s in [x for x in C.STUDIES if x.get("group") == gid]:
            reg = ""
            if s["nct"]:
                reg = (f'<a class="tag tag-link" href="https://clinicaltrials.gov/study/{s["nct"]}">'
                       f'{UI["registry"][lang]}: {s["nct"]}</a>')
            status = f'<span class="tag tag-status">{esc(t(s["status"], lang))}</span>' if s.get("status") else ""
            role = t(s.get("role", ""), lang) if s.get("role") else ""
            role_html = f'<p class="meta"><strong>{UI["our_role"][lang]}:</strong> {esc(role)}</p>' if role else ""
            items.append(f"""<li class="card study">
  <p class="tags">{status}<span class="tag">{esc(t(s['disease'], lang))}</span>{reg}</p>
  <h3>{esc(t(s['title'], lang))}</h3>
  <p>{esc(t(s['text'], lang))}</p>
  {role_html}
</li>""")
        sections.append(f"""<h2 class="section-title study-group">{esc(t(gtitle, lang))}</h2>
<ul class="grid grid-2 study-grid">{''.join(items)}</ul>""")
    body = page_header("studies", nav_label("studies", lang), C.STUDIES_INTRO, lang) + f"""
<section class="section">
  <div class="wrap">{''.join(sections)}</div>
</section>"""
    return layout("studies", lang, nav_label("studies", lang), body, t(C.STUDIES_INTRO, lang))


def md_links(text):
    """Escape text, then turn [label](https://...) into links."""
    out = esc(text)
    return re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', out)


def pro(lang):
    P = C.PRO
    d = depth_of("pro", lang)
    groups = []
    for g in P["instrument_groups"]:
        rows = []
        for i in g["items"]:
            name = (f'<a href="{i["url"]}">{esc(i["name"])}</a>' if i.get("url") else esc(i["name"]))
            badge = f' <span class="tag tag-dk">{UI["danish_badge"][lang]}</span>' if i.get("danish") else ""
            paper = (f' <a class="paper-link" href="https://doi.org/{html.escape(i["doi"])}">{UI["our_paper"][lang]}</a>'
                     if i.get("doi") else "")
            rows.append(f'<li><span class="inst-name">{name}</span>{badge}<span class="inst-what">{esc(t(i["what"], lang))}{paper}</span></li>')
        groups.append(f'''<div class="card inst-group"><h3>{esc(t(g["title"], lang))}</h3><ul class="inst-list">{"".join(rows)}</ul></div>''')
    adv = "\n".join(
        f"""<li class="card theme-plain"><h3>{esc(t(a['title'], lang))}</h3><p>{esc(t(a['text'], lang))}</p></li>"""
        for a in P["advice"]
    )
    links = "\n".join(f'<li><a href="{l["url"]}">{esc(l["name"])}</a></li>' for l in P["links"])
    body = page_header("pro", nav_label("pro", lang), P["intro"], lang) + f"""
<section class="section">
  <div class="wrap">
    <h2 class="section-title">{esc(t(P['instruments_heading'], lang))}</h2>
    <p class="lead-dark">{esc(t(P['instruments_note'], lang))}</p>
    <div class="grid grid-2 inst-grid">{''.join(groups)}</div>
  </div>
</section>
<section class="section section-tint">
  <div class="wrap">
    <h2 class="section-title">{esc(t(P['advice_heading'], lang))}</h2>
    <ul class="grid grid-3">{adv}</ul>
    <p class="center-cta"><a class="button" href="{url('contact', lang, d)}">{UI['contact_us'][lang]} &rarr;</a></p>
  </div>
</section>
<section class="section">
  <div class="wrap split">
    <div class="prose">
      <h2>{esc(t(P['resources_heading'], lang))}</h2>
      <p class="resource-callout">{md_links(t(P['proteus'], lang))}</p>
    </div>
    <aside class="card">
      <h3>{UI['useful_links'][lang]}</h3>
      <ul class="link-list">{links}</ul>
    </aside>
  </div>
</section>"""
    return layout("pro", lang, nav_label("pro", lang), body, t(P["intro"], lang))


def patients(lang):
    P = C.PATIENTS
    d = depth_of("patients", lang)
    why = "\n".join(f"<p>{esc(x)}</p>" for x in P["why"][lang])
    tasks = "\n".join(
        f"""<li class="card theme-plain"><h3>{esc(t(x['title'], lang))}</h3><p>{esc(t(x['text'], lang))}</p></li>"""
        for x in P["tasks"])
    who = "\n".join(f"<li>{esc(x)}</li>" for x in P["who"][lang])
    practical = "\n".join(f"<li>{esc(x)}</li>" for x in P["practical"][lang])
    email = P["join_email"]
    email_html = (f'<a class="button button-accent" href="mailto:{email}">{esc(email)}</a>'
                  if "@" in email and "TODO" not in email else esc(email))
    title = t(P["title"], lang)
    body = page_header("patients", title, P["intro"], lang) + f"""
<section class="section">
  <div class="wrap split">
    <div class="prose">
      <h2>{esc(t(P['why_heading'], lang))}</h2>
      {why}
    </div>
    <aside class="contact-box">
      <h2>{esc(t(P['join_heading'], lang))}</h2>
      <p>{esc(t(P['join_text'], lang))}</p>
      <p>{email_html}</p>
      <p class="small-note">{esc(t(P['join_privacy'], lang))}</p>
    </aside>
  </div>
</section>
<section class="section section-tint">
  <div class="wrap">
    <h2 class="section-title">{esc(t(P['tasks_heading'], lang))}</h2>
    <ul class="grid grid-2">{tasks}</ul>
  </div>
</section>
<section class="section">
  <div class="wrap grid grid-2">
    <div class="card"><h2>{esc(t(P['who_heading'], lang))}</h2><ul class="checklist">{who}</ul></div>
    <div class="card"><h2>{esc(t(P['practical_heading'], lang))}</h2><ul class="checklist">{practical}</ul></div>
  </div>
</section>"""
    return layout("patients", lang, title, body, t(P["intro"], lang))


def initials(name):
    if name.startswith("TODO"):
        return "?"
    parts = [p for p in name.split() if p[0].isalpha()]
    return (parts[0][0] + parts[-1][0]).upper()


def members(lang):
    d = depth_of("members", lang)
    up = "../" * d
    cards = []
    for m in C.MEMBERS:
        photo_file = os.path.join(ROOT, "assets", "img", "people", m["photo"]) if m["photo"] else ""
        if photo_file and os.path.exists(photo_file):
            pic = f'<img class="portrait" src="{up}assets/img/people/{m["photo"]}" alt="{esc(UI["portrait_of"][lang])} {esc(m["name"])}" width="400" height="500">'
        else:
            pic = (f'<div class="portrait portrait-placeholder" role="img" aria-label="{esc(UI["photo_missing"][lang])}">'
                   f'<img src="{up}assets/img/portrait-placeholder.svg" alt="" width="400" height="500">'
                   f'<span>{esc(UI["photo_missing"][lang])}</span></div>')
        links = ""
        if m["email"]:
            links += f'<p><a href="mailto:{m["email"]}">{esc(m["email"])}</a></p>'
        if m.get("profile"):
            links += f'<p><a href="{m["profile"]}">{UI["profile"][lang]}<span class="visually-hidden">: {esc(m["name"])}</span> &rarr;</a></p>'
        if m.get("orcid"):
            links += f'<p class="orcid"><a href="https://orcid.org/{m["orcid"]}">ORCID {m["orcid"]}</a></p>'
        cards.append(f"""<li class="card member">
  {pic}
  <div class="member-body">
    <h2>{esc(m['name'])}</h2>
    <p class="role">{esc(t(m['title'], lang))}</p>
    <p>{esc(t(m['bio'], lang))}</p>
    {links}
  </div>
</li>""")
    body = page_header("members", nav_label("members", lang), C.MEMBERS_INTRO, lang) + f"""
<section class="section">
  <div class="wrap"><ul class="grid grid-3 members-grid">{''.join(cards)}</ul></div>
</section>"""
    return layout("members", lang, nav_label("members", lang), body, t(C.MEMBERS_INTRO, lang))


def load_pubmed():
    path = os.path.join(ROOT, "src", "publications.json")
    if not os.path.exists(path):
        return None
    import json
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def publications(lang):
    data = load_pubmed()
    if not data or not data.get("publications"):
        inner = f"<p>{esc(t(C.PUBLICATIONS_EMPTY, lang))}</p>"
    else:
        pubs = data["publications"]
        match = {m: [re.compile(rx) for rx in rxs] for m, rxs in data.get("author_match", {}).items()}
        members = sorted({m for p in pubs for m in p["members"]})
        chips = [f'<button type="button" class="chip" aria-pressed="true" data-filter="all">{UI["all"][lang]} ({len(pubs)})</button>']
        for m in members:
            n = sum(1 for p in pubs if m in p["members"])
            chips.append(f'<button type="button" class="chip" aria-pressed="false" data-filter="{esc(m)}">{esc(m)} ({n})</button>')
        out, year = [], None
        for p in pubs:
            if p["year"] != year:
                if year is not None:
                    out.append("</ol></section>")
                year = p["year"]
                out.append(f'<section class="pub-year" data-year="{year}"><h2 class="year">{year or ""}</h2><ol class="pubs">')
            flags = [any(rx.search(a) for rxs in match.values() for rx in rxs) for a in p["authors"]]
            names, gap = [], False
            n = len(p["authors"])
            for k, (a, is_member) in enumerate(zip(p["authors"], flags)):
                keep = n <= 12 or k < 10 or k == n - 1 or is_member
                if keep:
                    if gap:
                        names.append("…")
                        gap = False
                    names.append(f"<strong>{esc(a)}</strong>" if is_member else esc(a))
                else:
                    gap = True
            cite = esc(p["journal"])
            if p.get("volume"):
                cite += f" {esc(p['volume'])}"
                if p.get("issue"):
                    cite += f"({esc(p['issue'])})"
            if p.get("pages"):
                cite += f":{esc(p['pages'])}"
            links = f'<a href="https://pubmed.ncbi.nlm.nih.gov/{p["pmid"]}/">PubMed</a>'
            if p.get("doi"):
                links += f' · <a href="https://doi.org/{html.escape(p["doi"])}">DOI</a>'
            out.append(f'''<li data-members="{esc("|".join(p["members"]))}"><span class="pub-title">{esc(p["title"])}</span> <span class="pub-authors">{", ".join(names)}.</span> <em>{cite}</em>. {p["year"]}. <span class="pub-links">{links}</span></li>''')
        out.append("</ol></section>")
        inner = f"""<div class="pub-tools">
  <p class="pub-updated">{UI['pub_source'][lang]} {esc(data.get('updated', ''))}.</p>
  <div class="chips" role="group" aria-label="{UI['filter_by'][lang]}">{''.join(chips)}</div>
</div>
{''.join(out)}
<script>
(function () {{
  var chips = document.querySelectorAll('.chip');
  chips.forEach(function (c) {{
    c.addEventListener('click', function () {{
      var f = c.getAttribute('data-filter');
      chips.forEach(function (o) {{ o.setAttribute('aria-pressed', o === c ? 'true' : 'false'); }});
      document.querySelectorAll('.pubs li').forEach(function (li) {{
        li.hidden = !(f === 'all' || li.getAttribute('data-members').split('|').indexOf(f) > -1);
      }});
      document.querySelectorAll('.pub-year').forEach(function (sec) {{
        sec.hidden = !sec.querySelector('li:not([hidden])');
      }});
    }});
  }});
}})();
</script>"""
    body = page_header("publications", nav_label("publications", lang), C.PUBLICATIONS_INTRO, lang) + f"""
<section class="section">
  <div class="wrap prose-wide">{inner}</div>
</section>"""
    return layout("publications", lang, nav_label("publications", lang), body, t(C.PUBLICATIONS_INTRO, lang))


def partners(lang):
    cards = []
    for p in C.PARTNERS:
        link = (f'<p><a href="{p["url"]}">{UI["visit"][lang]}<span class="visually-hidden">: '
                f'{esc(t(p["name"], lang))}</span></a></p>') if p["url"] else ""
        cards.append(f"""<li class="card partner">
  <p class="tags"><span class="tag">{esc(t(p['country'], lang))}</span></p>
  <h2>{esc(t(p['name'], lang))}</h2>
  <p>{esc(t(p['text'], lang))}</p>
  {link}
</li>""")
    body = page_header("partners", nav_label("partners", lang), C.PARTNERS_INTRO, lang) + f"""
<section class="section">
  <div class="wrap">
    <ul class="grid grid-3">{''.join(cards)}</ul>
    <p>{esc(t(C.PARTNERS_NOTE, lang))}</p>
  </div>
</section>"""
    return layout("partners", lang, nav_label("partners", lang), body, t(C.PARTNERS_INTRO, lang))


def contact(lang):
    c = C.CONTACT
    addr = "<br>".join(esc(t(line, lang)) for line in c["address"])
    email = c["email"]
    email_html = (f'<a href="mailto:{email}">{esc(email)}</a>' if "@" in email and "TODO" not in email
                  else esc(email))
    body = page_header("contact", nav_label("contact", lang), c["intro"], lang) + f"""
<section class="section">
  <div class="wrap grid grid-3 contact-grid">
    <div class="card">
      <h2>{esc(t(c['address_heading'], lang))}</h2>
      <address>{addr}</address>
    </div>
    <div class="card">
      <h2>{esc(t(c['email_heading'], lang))}</h2>
      <p>{email_html}</p>
      <h2>{esc(t(c['phone_heading'], lang))}</h2>
      <p>{esc(t(c['phone'], lang))}</p>
    </div>
    <div class="card card-note">
      <h2>{esc(t(c['patients_heading'], lang))}</h2>
      <p>{esc(t(c['patients'], lang))}</p>
    </div>
  </div>
</section>"""
    return layout("contact", lang, nav_label("contact", lang), body, t(c["intro"], lang))


PAGES = {
    "about": about,
    "studies": studies,
    "pro": pro,
    "patients": patients,
    "members": members,
    "publications": publications,
    "partners": partners,
    "contact": contact,
}


def main():
    for lang in LANGS:
        for page, fn in PAGES.items():
            path = os.path.join(ROOT, page_path(page, lang))
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(fn(lang))
            print("wrote", os.path.relpath(path, ROOT))


if __name__ == "__main__":
    main()
