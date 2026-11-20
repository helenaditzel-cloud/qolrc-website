# QoLRC website

Informational website for the Quality of Life Research Center (QoLRC), Department of Hematology, Odense University Hospital.

- English pages are in the repository root, Danish pages in `/da/`.
- All text lives in `src/content.py`. Edit it, then rebuild:

```
python3 src/build.py
```

- Styles are in `assets/style.css`. Photos go in `assets/img/`.
- Text marked `TODO(...)` shows on the site as a yellow "To do" note until it is filled in.
- Publications are fetched from PubMed every Monday by `.github/workflows/update-publications.yml` (edit the people in `src/fetch_publications.py`).
- Hosted with GitHub Pages (Settings, Pages, deploy from branch `main`, folder `/ (root)`).
- The site uses no cookies, no tracking and no external fonts or scripts.
