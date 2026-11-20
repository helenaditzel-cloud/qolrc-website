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
<link rel="icon" href="{up}assets/favicon.svg" type="image/svg+xml">
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
      <img src="{up}assets/logo-mark.svg" alt="" width="52" height="52">
      <span class="brand-text"><span class="brand-short">QoLRC</span><span class="brand-long">{esc(t(C.SITE['name'], lang))}</span></span>
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
        <img src="{up}assets/logo-mark.svg" alt="" width="44" height="44">
        <span class="brand-text"><span class="brand-short">QoLRC</span><span class="brand-long">{esc(t(C.SITE['name'], lang))}</span></span>
      </a>
      <p>{esc(t(C.SITE['footer_text'], lang))}</p>
    </div>
    <nav aria-label="{UI['pages'][lang]}">
      <p class="footer-heading">{UI['pages'][lang]}</p>
      <ul class="footer-links">{footer_links}</ul>
    </nav>
    <div>
      <p class="footer-heading">{UI['contact_us'][lang]}</p>
      <address>{"<br>".join(esc(t(line, lang)) for line in C.CONTACT['address'][:3])}</address>
      <p><a href="{url('contact', lang, d)}">{UI['all_contact'][lang]} &rarr;</a></p>
    </div>
  </div>
  <div class="footer-bottom"><div class="wrap">{esc(t(C.SITE['privacy'], lang))}</div></div>
</footer>
</body>
</html>
"""


def page_header(page, title, intro, lang):
    d = depth_of(page, lang)
    return f"""<section class="page-head">
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

def about(lang):
    a = C.ABOUT
    d = depth_of("about", lang)
    up = "../" * d
    paras = "\n".join(f"<p>{esc(p)}</p>" for p in a["intro"][lang])
    cards = "\n".join(
        f"""<li class="card theme">
  <div class="card-art" style="background-image:url('{up}assets/img/theme-{i}.svg')"></div>
  <div class="card-body">
    <h3>{esc(t(th['title'], lang))}</h3>
    <p>{esc(t(th['text'], lang))}</p>
  </div>
</li>"""
        for i, th in enumerate(a["themes"], 1)
    )
    figures = "\n".join(
        f'<li><span class="fig-value">{esc(f["value"])}</span><span class="fig-label">{esc(t(f["label"], lang))}</span></li>'
        for f in a["figures"]
    )
    body = f"""<section class="hero" style="background-image:url('{up}assets/img/hero-art.svg')">
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
<section class="band" style="background-image:url('{up}assets/img/band-art.svg')">
  <div class="wrap band-inner">
    <div>
      <h2>{esc(t(a['advice_heading'], lang))}</h2>
      <p>{esc(t(a['advice_text'], lang))}</p>
    </div>
    <p><a class="button button-accent" href="{url('contact', lang, d)}">{UI['contact_us'][lang]} &rarr;</a></p>
  </div>
</section>"""
    return layout("about", lang, nav_label("about", lang), body, t(a["hero_lead"], lang))


def studies(lang):
    items = []
    for s in C.STUDIES:
        reg = ""
        if s["nct"]:
            reg = (f'<a class="tag tag-link" href="https://clinicaltrials.gov/study/{s["nct"]}">'
                   f'{UI["registry"][lang]}: {s["nct"]}</a>')
        items.append(f"""<li class="card study">
  <p class="tags"><span class="tag">{esc(t(s['disease'], lang))}</span>{reg}</p>
  <h2>{esc(t(s['title'], lang))}</h2>
  <p>{esc(t(s['text'], lang))}</p>
  <p class="meta"><strong>{UI['our_role'][lang]}:</strong> {esc(t(s['role'], lang))}</p>
</li>""")
    body = page_header("studies", nav_label("studies", lang), C.STUDIES_INTRO, lang) + f"""
<section class="section">
  <div class="wrap"><ul class="stack">{''.join(items)}</ul></div>
</section>"""
    return layout("studies", lang, nav_label("studies", lang), body, t(C.STUDIES_INTRO, lang))


def initials(name):
    if name.startswith("TODO"):
        return "?"
    parts = [p for p in name.split() if p[0].isalpha()]
    return (parts[0][0] + parts[-1][0]).upper()


def members(lang):
    d = depth_of("members", lang)
    cards = []
    for m in C.MEMBERS:
        if m["photo"]:
            pic = f'<img class="avatar" src="{"../" * d}assets/img/{m["photo"]}" alt="" width="120" height="120">'
        else:
            pic = f'<span class="avatar avatar-initials" aria-hidden="true">{initials(m["name"])}</span>'
        mail = f'<p><a href="mailto:{m["email"]}">{esc(m["email"])}</a></p>' if m["email"] else ""
        if m.get("profile"):
            mail += f'<p><a href="{m["profile"]}">{UI["profile"][lang]}<span class="visually-hidden">: {esc(m["name"])}</span> &rarr;</a></p>'
        cards.append(f"""<li class="card member">
  {pic}
  <div>
    <h2>{esc(m['name'])}</h2>
    <p class="role">{esc(t(m['title'], lang))}</p>
    <p>{esc(t(m['bio'], lang))}</p>
    {mail}
  </div>
</li>""")
    body = page_header("members", nav_label("members", lang), C.MEMBERS_INTRO, lang) + f"""
<section class="section">
  <div class="wrap"><ul class="grid grid-2">{''.join(cards)}</ul></div>
</section>"""
    return layout("members", lang, nav_label("members", lang), body, t(C.MEMBERS_INTRO, lang))


def publications(lang):
    pubs = sorted(C.PUBLICATIONS, key=lambda p: (-p["year"], p["title"]))
    if not pubs:
        inner = f"<p>{esc(t(C.PUBLICATIONS_EMPTY, lang))}</p>"
    else:
        groups, year = [], None
        for p in pubs:
            if p["year"] != year:
                if year is not None:
                    groups.append("</ol>")
                year = p["year"]
                groups.append(f'<h2 class="year">{year}</h2><ol class="pubs">')
            doi = (f' <a href="https://doi.org/{html.escape(p["doi"])}">doi:{html.escape(p["doi"])}</a>'
                   if p.get("doi") else "")
            groups.append(f'<li><span class="pub-title">{esc(p["title"])}</span> '
                          f'<span class="pub-authors">{esc(p["authors"])}.</span> '
                          f'<em>{esc(p["journal"])}</em>. {p["year"]}.{doi}</li>')
        groups.append("</ol>")
        inner = "\n".join(groups)
    body = page_header("publications", nav_label("publications", lang), C.PUBLICATIONS_INTRO, lang) + f"""
<section class="section">
  <div class="wrap prose">{inner}</div>
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
      <p>{esc(c['phone'])}</p>
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
