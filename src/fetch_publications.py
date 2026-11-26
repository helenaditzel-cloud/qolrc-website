# -*- coding: utf-8 -*-
"""
Fetches publications for QoLRC members from PubMed (NCBI E-utilities)
and writes src/publications.json. Run by GitHub Actions every week,
or by hand:  python3 src/fetch_publications.py

Edit AUTHOR_QUERIES to add or change people. Full-name searches are used
because short author abbreviations match other researchers.
"""
import json
import os
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "src", "publications.json")
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
TOOL = "qolrc-website"

# name shown on the site -> PubMed query
AUTHOR_QUERIES = {
    "Helena Møgelbjerg Ditzel": '"Ditzel HM"[Author]',
    "Henrik Frederiksen": '"Frederiksen, Henrik"[Full Author Name] AND (Odense[Affiliation] OR "Southern Denmark"[Affiliation])',
    "Niels Abildgaard": '"Abildgaard, Niels"[Full Author Name]',
    "Tine Rosenberg": '"Rosenberg, Tine"[Full Author Name] AND (Hematology[Affiliation] OR Haematology[Affiliation] OR "Quality of Life Research"[Affiliation])',  # another Tine Rosenberg publishes in ENT surgery
    "Lene Kongsgaard Nielsen": '"Nielsen, Lene Kongsgaard"[Full Author Name]',
    "Anne Møller Clausen": '"Clausen AM"[Author] AND Odense[Affiliation]',
    "Nina Andersen": '"Andersen, Nina"[Full Author Name] AND Odense[Affiliation] AND (frailty OR geriatric) NOT Municipality[Affiliation]',  # another Nina Andersen publishes from Odense Municipality
    "Klara Rydahl": '"Rydahl KFK"[Author]',
    # Pia K. Pedersen and Tina Käehne: no PubMed publications found
    # Affiliated researchers (Madeleine King, Sören Möller) are left out on purpose
}

# How each member's name appears in PubMed author lists, used to highlight them
AUTHOR_MATCH = {
    "Helena Møgelbjerg Ditzel": [r"^Ditzel HM$"],
    "Henrik Frederiksen": [r"^Frederiksen H$"],
    "Niels Abildgaard": [r"^Abildgaard N$"],
    "Tine Rosenberg": [r"^Rosenberg T$"],
    "Lene Kongsgaard Nielsen": [r"^Nielsen LK$", r"^Kongsgaard Nielsen L$"],
    "Anne Møller Clausen": [r"^Clausen AM$"],
    "Nina Andersen": [r"^Andersen N$"],
    "Klara Rydahl": [r"^Rydahl K"],
}

# ---- PRO classification -------------------------------------------------
# A paper counts as a "PRO publication" if it is about quality of life,
# reports patient-reported outcomes in any form, or is a methodological
# study of PROs. Decided from title, abstract, keywords and MeSH terms.
PRO_STRONG = re.compile(
    r"quality[- ]of[- ]life|\bh?r?qol\b|\bhrql\b|patient[- ]reported|self[- ]reported|self[- ]report\b|"
    r"\bproms?\b|\bpros\b|\bpro\b(?![- ]?(?:tein|gnos|gress|lifer|phyla|duc|cedur|spect|mot|teas|thromb|bnp|inflam))|"
    r"questionnaire|psychometric|eortc|\bqlq|\bfact-|eq-5d|\bsf-?12\b|\bsf-?36\b|promis\b|"
    r"symptom burden|well-?being|cosmin|health utilit",
    re.I)
PRO_MESH = {"Quality of Life", "Patient Reported Outcome Measures", "Psychometrics",
            "Surveys and Questionnaires", "Self Report"}
# Manual corrections, by PubMed ID, if the automatic sorting gets a paper wrong
PRO_INCLUDE = set()
PRO_EXCLUDE = set()


def is_pro(pmid, title, abstract, keywords, mesh):
    if pmid in PRO_INCLUDE:
        return True
    if pmid in PRO_EXCLUDE:
        return False
    if PRO_STRONG.search(title) or PRO_STRONG.search(" ".join(keywords)):
        return True
    if PRO_MESH & set(mesh):
        return True
    return len(PRO_STRONG.findall(abstract)) >= 2


def efetch_details(ids):
    """Abstract, keywords and MeSH terms per PMID."""
    out = {}
    for i in range(0, len(ids), 200):
        batch = ids[i:i + 200]
        data = urllib.parse.urlencode({"db": "pubmed", "id": ",".join(batch),
                                       "retmode": "xml", "tool": TOOL}).encode()
        for attempt in range(4):
            try:
                req = urllib.request.Request(EUTILS + "efetch.fcgi", data=data, headers={"User-Agent": TOOL})
                with urllib.request.urlopen(req, timeout=120) as r:
                    root = ET.fromstring(r.read())
                break
            except Exception:
                if attempt == 3:
                    raise
                time.sleep(3 + attempt * 3)
        for art in root.iter("PubmedArticle"):
            pmid = art.findtext(".//MedlineCitation/PMID", "")
            abstract = " ".join("".join(t.itertext()) for t in art.iter("AbstractText"))
            keywords = ["".join(k.itertext()) for k in art.iter("Keyword")]
            mesh = [d.text or "" for d in art.iter("DescriptorName")]
            out[pmid] = (abstract, keywords, mesh)
        time.sleep(0.4)
    return out


MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}


def get(url, data=None, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, data=data, headers={"User-Agent": TOOL})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(2 + i * 3)


def esearch(term):
    q = urllib.parse.urlencode({"db": "pubmed", "term": term, "retmax": 2000,
                                "retmode": "json", "tool": TOOL})
    res = get(EUTILS + "esearch.fcgi?" + q)
    time.sleep(0.4)
    return res["esearchresult"]["idlist"]


def esummary(ids):
    out = {}
    for i in range(0, len(ids), 200):
        batch = ids[i:i + 200]
        data = urllib.parse.urlencode({"db": "pubmed", "id": ",".join(batch),
                                       "retmode": "json", "tool": TOOL}).encode()
        res = get(EUTILS + "esummary.fcgi", data=data)["result"]
        for uid in res.get("uids", []):
            out[uid] = res[uid]
        time.sleep(0.4)
    return out


def main():
    members_by_pmid = {}
    for name, term in AUTHOR_QUERIES.items():
        ids = esearch(term)
        print(f"{name}: {len(ids)} records")
        for pmid in ids:
            members_by_pmid.setdefault(pmid, set()).add(name)

    summaries = esummary(sorted(members_by_pmid))
    details = efetch_details(sorted(members_by_pmid))
    pubs = []
    for pmid, s in summaries.items():
        if s.get("error"):
            continue
        types = [t.lower() for t in s.get("pubtype", [])]
        if any(t in types for t in ("erratum", "published erratum", "retraction of publication")):
            continue
        sortdate = s.get("sortpubdate", "")[:10]  # "2024/09/01 00:00"
        year = int(sortdate[:4]) if sortdate[:4].isdigit() else 0
        doi = ""
        for a in s.get("articleids", []):
            if a.get("idtype") == "doi":
                doi = a.get("value", "")
        authors = [a.get("name", "") for a in s.get("authors", []) if a.get("authtype", "Author") == "Author"]
        title = re.sub(r"<[^>]+>", "", s.get("title", "")).strip()
        abstract, keywords, mesh = details.get(pmid, ("", [], []))
        pubs.append({
            "pmid": pmid,
            "year": year,
            "sortdate": sortdate,
            "title": title,
            "authors": authors,
            "journal": s.get("source", ""),
            "volume": s.get("volume", ""),
            "issue": s.get("issue", ""),
            "pages": s.get("pages", ""),
            "doi": doi,
            "members": sorted(members_by_pmid[pmid]),
            "pro": is_pro(pmid, title, abstract, keywords, mesh),
        })
    pubs.sort(key=lambda p: (p["sortdate"], p["pmid"]), reverse=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump({"updated": time.strftime("%Y-%m-%d"), "author_match": AUTHOR_MATCH,
                   "publications": pubs}, f, ensure_ascii=False, indent=1)
    print(f"wrote {len(pubs)} publications ({sum(p['pro'] for p in pubs)} PRO) to {os.path.relpath(OUT, ROOT)}")


if __name__ == "__main__":
    main()
