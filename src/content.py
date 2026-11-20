# -*- coding: utf-8 -*-
"""
All website text lives here. Each text has an English ("en") and Danish ("da") version.
Edit the text, then run:  python3 src/build.py
Anything wrapped in TODO(...) is shown on the site as a yellow note so it is easy to spot.
"""

SITE = {
    "name": {"en": "Quality of Life Research Center", "da": "Quality of Life Research Center"},
    "short": "QoLRC",
    "affiliation": {
        "en": "Department of Hematology, Odense University Hospital",
        "da": "Hæmatologisk Afdeling, Odense Universitetshospital",
    },
    "footer_text": {
        "en": "QoLRC is part of the Department of Hematology at Odense University Hospital and is affiliated with the University of Southern Denmark.",
        "da": "QoLRC er en del af Hæmatologisk Afdeling på Odense Universitetshospital og er tilknyttet Syddansk Universitet.",
    },
    "privacy": {
        "en": "This website uses no cookies and no tracking.",
        "da": "Denne hjemmeside bruger ingen cookies og ingen sporing.",
    },
    "domain": "https://qolrc-odense.dk",
}

# Navigation: (page id, English label, Danish label)
NAV = [
    ("about", "About us", "Om os"),
    ("studies", "Ongoing studies", "Igangværende studier"),
    ("members", "Members", "Medarbejdere"),
    ("publications", "Publications", "Publikationer"),
    ("partners", "Partners", "Samarbejdspartnere"),
    ("contact", "Contact", "Kontakt"),
]

# ---------------------------------------------------------------- About us (home page)
ABOUT = {
    "hero_title": {
        "en": "Quality of Life Research Center",
        "da": "Quality of Life Research Center",
    },
    "hero_lead": {
        "en": "Bringing the patient perspective into hematologic research, clinical trials and care.",
        "da": "Vi bringer patientens perspektiv ind i hæmatologisk forskning, kliniske forsøg og behandling.",
    },
    "intro_heading": {"en": "About the center", "da": "Om centret"},
    "intro": {
        "en": [
            "The Quality of Life Research Center (QoLRC) studies how hematologic diseases and their treatment affect patients' everyday lives. We work with patient-reported outcomes (PROs) and health-related quality of life (HRQoL) in multiple myeloma, other hematologic cancers and benign hematologic conditions such as autoimmune cytopenias.",
            "The center is based in the Department of Hematology at Odense University Hospital and is affiliated with the University of Southern Denmark. We lead and contribute to national and multinational studies in close collaboration with clinicians, statisticians, patient organizations and research partners across the Nordic countries and Europe.",
        ],
        "da": [
            "Quality of Life Research Center (QoLRC) undersøger, hvordan hæmatologiske sygdomme og deres behandling påvirker patienternes hverdag. Vi arbejder med patientrapporterede oplysninger (PRO) og helbredsrelateret livskvalitet (HRQoL) ved myelomatose, andre hæmatologiske kræftsygdomme og godartede hæmatologiske sygdomme som autoimmune cytopenier.",
            "Centret har base i Hæmatologisk Afdeling på Odense Universitetshospital og er tilknyttet Syddansk Universitet. Vi leder og bidrager til nationale og internationale studier i tæt samarbejde med klinikere, statistikere, patientforeninger og forskningspartnere i Norden og Europa.",
        ],
    },
    "themes_heading": {"en": "Our research", "da": "Vores forskning"},
    "themes": [
        {
            "title": {"en": "PROs in clinical trials", "da": "PRO i kliniske forsøg"},
            "text": {
                "en": "Designing, collecting and analyzing patient-reported outcomes in randomized and single-arm trials, following international standards for PRO endpoints and estimands.",
                "da": "Planlægning, indsamling og analyse af patientrapporterede oplysninger i randomiserede og enkeltarmede forsøg efter internationale standarder for PRO-endepunkter og estimands.",
            },
        },
        {
            "title": {"en": "Instrument development and validation", "da": "Udvikling og validering af spørgeskemaer"},
            "text": {
                "en": "Developing and psychometrically validating questionnaires so that what matters to patients can be measured reliably, using COSMIN-aligned methodology.",
                "da": "Udvikling og psykometrisk validering af spørgeskemaer, så det, der betyder noget for patienterne, kan måles pålideligt, efter COSMIN-principper.",
            },
        },
        {
            "title": {"en": "Multiple myeloma", "da": "Myelomatose"},
            "text": {
                "en": "Quality of life during modern myeloma treatment, including measurable residual disease (MRD) guided strategies and long-term maintenance.",
                "da": "Livskvalitet under moderne myelomatosebehandling, herunder behandling styret af målbar restsygdom (MRD) og langvarig vedligeholdelsesbehandling.",
            },
        },
        {
            "title": {"en": "Autoimmune cytopenias", "da": "Autoimmune cytopenier"},
            "text": {
                "en": "Measuring the symptom burden of immune thrombocytopenia (ITP), autoimmune hemolytic anemia (AIHA) and their treatment, including corticosteroids.",
                "da": "Måling af symptombyrden ved immun trombocytopeni (ITP), autoimmun hæmolytisk anæmi (AIHA) og deres behandling, herunder binyrebarkhormon.",
            },
        },
        {
            "title": {"en": "Older patients and frailty", "da": "Ældre patienter og skrøbelighed"},
            "text": {
                "en": "Using geriatric screening tools such as the G8 to understand how frailty relates to treatment tolerance and outcomes in older patients with cancer.",
                "da": "Brug af geriatriske screeningsværktøjer som G8 til at forstå sammenhængen mellem skrøbelighed, behandlingstolerance og forløb hos ældre patienter med kræft.",
            },
        },
        {
            "title": {"en": "Patient involvement", "da": "Patientinddragelse"},
            "text": {
                "en": "Working with patients and patient organizations so that our questions, methods and results reflect what matters most to the people we study.",
                "da": "Samarbejde med patienter og patientforeninger, så vores spørgsmål, metoder og resultater afspejler det, der betyder mest for dem, vi forsker sammen med.",
            },
        },
    ],
    # Key figures shown in a band under the banner. Keep these accurate.
    "figures": [
        {"value": "3", "label": {"en": "Ongoing studies", "da": "Igangværende studier"}},
        {"value": "4", "label": {"en": "Countries in our collaborations", "da": "Lande i vores samarbejder"}},
        {"value": "6", "label": {"en": "Research areas", "da": "Forskningsområder"}},
    ],
    "advice_heading": {"en": "Advice and collaboration", "da": "Rådgivning og samarbejde"},
    "advice_text": {
        "en": "Planning a study with patient-reported outcomes? We advise on choice of instruments, PRO endpoints, statistical analysis plans and grant applications, and welcome new collaborations.",
        "da": "Planlægger du et studie med patientrapporterede oplysninger? Vi rådgiver om valg af spørgeskemaer, PRO-endepunkter, statistiske analyseplaner og fondsansøgninger og indgår gerne i nye samarbejder.",
    },
    "contact_box_heading": {"en": "Get in touch", "da": "Kontakt os"},
    "contact_box_text": {
        "en": "Interested in collaborating, or need advice on PROs for a study or grant application? We would like to hear from you.",
        "da": "Vil du samarbejde med os, eller har du brug for rådgivning om PRO i et studie eller en ansøgning? Vi hører gerne fra dig.",
    },
}

# ---------------------------------------------------------------- Ongoing studies
STUDIES_INTRO = {
    "en": "Selected ongoing studies led by or involving QoLRC.",
    "da": "Udvalgte igangværende studier, som QoLRC leder eller deltager i.",
}

STUDIES = [
    {
        "title": {
            "en": "REMNANT: quality of life in MRD-guided myeloma treatment",
            "da": "REMNANT: livskvalitet ved MRD-styret myelomatosebehandling",
        },
        "disease": {"en": "Multiple myeloma", "da": "Myelomatose"},
        "nct": "NCT04513639",
        "text": {
            "en": "A Nordic randomized trial in newly diagnosed multiple myeloma, led by Oslo University Hospital, in which treatment is guided by measurable residual disease. QoLRC leads the Danish health-related quality of life work, including the statistical analysis plans for the HRQoL sub-study.",
            "da": "Et nordisk randomiseret forsøg ved nydiagnosticeret myelomatose, ledet af Oslo universitetssykehus, hvor behandlingen styres af målbar restsygdom. QoLRC leder det danske arbejde med helbredsrelateret livskvalitet, herunder de statistiske analyseplaner for livskvalitetsdelen.",
        },
        "role": {"en": "Danish HRQoL lead", "da": "Dansk ansvarlig for livskvalitet"},
    },
    {
        "title": {
            "en": "Patient-reported outcomes in the Nordic IRd trial",
            "da": "Patientrapporterede oplysninger i det nordiske IRd-forsøg",
        },
        "disease": {"en": "Multiple myeloma", "da": "Myelomatose"},
        "nct": "NCT03376672",
        "text": {
            "en": "Analysis of quality of life, myeloma-specific symptoms and peripheral neuropathy in a Nordic Myeloma Study Group phase 2 trial in newly diagnosed, transplant-eligible patients, using the EORTC QLQ-C30, QLQ-MY20 and QLQ-CIPN20.",
            "da": "Analyse af livskvalitet, myelomatosespecifikke symptomer og perifer neuropati i et fase 2-forsøg fra Nordic Myeloma Study Group hos nydiagnosticerede patienter, der kan tåle højdosisbehandling, med EORTC QLQ-C30, QLQ-MY20 og QLQ-CIPN20.",
        },
        "role": {"en": "PRO analysis", "da": "PRO-analyse"},
    },
    {
        "title": {
            "en": "Validation of the Steroid Symptom Questionnaire in ITP and AIHA",
            "da": "Validering af Steroid Symptom Questionnaire ved ITP og AIHA",
        },
        "disease": {"en": "Autoimmune cytopenias", "da": "Autoimmune cytopenier"},
        "nct": "",
        "text": {
            "en": "A multinational psychometric validation study of a questionnaire measuring symptoms related to corticosteroid treatment in patients with immune thrombocytopenia and autoimmune hemolytic anemia, with sites in Denmark, Norway, Sweden and the United Kingdom. TODO(Confirm this study may be described publicly before launch.)",
            "da": "Et internationalt psykometrisk valideringsstudie af et spørgeskema, der måler symptomer relateret til behandling med binyrebarkhormon hos patienter med immun trombocytopeni og autoimmun hæmolytisk anæmi, med centre i Danmark, Norge, Sverige og Storbritannien. TODO(Bekræft, at studiet må omtales offentligt inden lancering.)",
        },
        "role": {"en": "Principal investigator", "da": "Forsøgsansvarlig"},
    },
]

# ---------------------------------------------------------------- Members
MEMBERS_INTRO = {
    "en": "The people behind QoLRC.",
    "da": "Menneskene bag QoLRC.",
}

# photo: file name in assets/img/people/ (portrait, ideally 800 x 1000 px). Leave "" to show a placeholder.
MEMBERS = [
    {
        "name": "Henrik Frederiksen",
        "title": {"en": "MD, PhD, Clinical Professor in Hematology", "da": "Læge, ph.d., klinisk professor i hæmatologi"},
        "bio": {
            "en": "Head of Research at the Hematology Research Unit, Odense University Hospital and University of Southern Denmark. His research covers non-malignant hematologic diseases and the complications and reduced quality of life that aging, frailty and other chronic conditions bring to patients with hematologic cancer. Former chair of the Danish Society of Hematology.",
            "da": "Forskningsleder for Hæmatologisk Forskningsenhed, Odense Universitetshospital og Syddansk Universitet. Hans forskning omfatter godartede hæmatologiske sygdomme samt de komplikationer og den nedsatte livskvalitet, som aldring, skrøbelighed og andre kroniske sygdomme medfører for patienter med hæmatologisk kræft. Tidligere formand for Dansk Hæmatologisk Selskab.",
        },
        "email": "",
        "photo": "henrik-frederiksen.jpg",
        "profile": "https://www.sdu.dk/en/forskning/haematologi",
    },
    {
        "name": "Niels Abildgaard",
        "title": {"en": "Clinical Professor in Hematology", "da": "Klinisk professor i hæmatologi"},
        "bio": {
            "en": "Clinical professor at the Department of Hematology, Odense University Hospital, and head of the Odense Amyloidosis Centre (AmyC OUH), a Center of Clinical Excellence. TODO(Niels to check and add his research focus, for example multiple myeloma.)",
            "da": "Klinisk professor på Hæmatologisk Afdeling, Odense Universitetshospital, og leder af Odense Amyloidosis Centre (AmyC OUH), et Center for Klinisk Excellence. TODO(Niels tjekker og tilføjer sit forskningsområde, fx myelomatose.)",
        },
        "email": "",
        "photo": "niels-abildgaard.jpg",
        "profile": "",
    },
    {
        "name": "Helena Møgelbjerg Ditzel",
        "title": {"en": "MD, PhD, Postdoctoral Researcher", "da": "Læge, ph.d., postdoc"},
        "bio": {
            "en": "Clinician-researcher working on patient-reported outcomes, health-related quality of life methodology and psychometric validation in hematologic oncology, with a focus on multiple myeloma and autoimmune cytopenias. Principal investigator and project manager in several multinational studies.",
            "da": "Klinisk forsker, der arbejder med patientrapporterede oplysninger, metoder til måling af helbredsrelateret livskvalitet og psykometrisk validering inden for hæmatologisk onkologi med fokus på myelomatose og autoimmune cytopenier. Forsøgsansvarlig og projektleder i flere internationale studier.",
        },
        "email": "",
        "photo": "helena-ditzel.jpg",
        "profile": "",
    },
    {
        "name": "Pia K. Pedersen",
        "title": {"en": "Daily Manager, Hematology Research Unit", "da": "Daglig leder, Hæmatologisk Forskningsenhed"},
        "bio": {
            "en": "TODO(Pia to confirm her title and add a short bio, 2 to 3 sentences.)",
            "da": "TODO(Pia bekræfter sin titel og tilføjer en kort biografi på 2 til 3 sætninger.)",
        },
        "email": "",
        "photo": "pia-pedersen.jpg",
        "profile": "",
    },
    {
        "name": "Tine Rosenberg",
        "title": {"en": "Research Coordinator and Fundraiser", "da": "Forskningskoordinator og fundraiser"},
        "bio": {
            "en": "TODO(Tine to confirm her title and add a short bio, 2 to 3 sentences.)",
            "da": "TODO(Tine bekræfter sin titel og tilføjer en kort biografi på 2 til 3 sætninger.)",
        },
        "email": "",
        "photo": "tine-rosenberg.jpg",
        "profile": "",
    },
]

# ---------------------------------------------------------------- Publications
PUBLICATIONS_INTRO = {
    "en": "Selected peer-reviewed publications from QoLRC members, newest first.",
    "da": "Udvalgte fagfællebedømte publikationer fra QoLRC's medarbejdere, nyeste først.",
}

# Each entry: year, authors, title, journal, doi (optional)
PUBLICATIONS = [
    # Example of the format:
    # {"year": 2026, "authors": "Ditzel HM, ...", "title": "...", "journal": "J Geriatr Oncol", "doi": "10.xxxx/xxxx"},
]

PUBLICATIONS_EMPTY = {
    "en": "TODO(The publication list will be filled in from PubMed. Send the author names and years to include.)",
    "da": "TODO(Publikationslisten udfyldes fra PubMed. Send de forfatternavne og år, der skal med.)",
}

# ---------------------------------------------------------------- Partners
PARTNERS_INTRO = {
    "en": "We work with clinical, academic and patient partners in Denmark and abroad.",
    "da": "Vi samarbejder med kliniske, akademiske og patientrelaterede partnere i Danmark og udlandet.",
}

PARTNERS = [
    {
        "name": {"en": "Department of Hematology, Odense University Hospital", "da": "Hæmatologisk Afdeling, Odense Universitetshospital"},
        "text": {"en": "Our home department.", "da": "Vores hjemafdeling."},
        "url": "https://ouh.dk",
        "country": {"en": "Denmark", "da": "Danmark"},
    },
    {
        "name": {"en": "University of Southern Denmark", "da": "Syddansk Universitet"},
        "text": {"en": "Academic affiliation.", "da": "Akademisk tilknytning."},
        "url": "https://www.sdu.dk",
        "country": {"en": "Denmark", "da": "Danmark"},
    },
    {
        "name": {"en": "Oslo University Hospital", "da": "Oslo universitetssykehus"},
        "text": {"en": "Sponsor of the REMNANT trial.", "da": "Sponsor for REMNANT-forsøget."},
        "url": "https://www.oslo-universitetssykehus.no",
        "country": {"en": "Norway", "da": "Norge"},
    },
    {
        "name": {"en": "Nordic Myeloma Study Group (NMSG)", "da": "Nordic Myeloma Study Group (NMSG)"},
        "text": {"en": "Nordic collaborative group for clinical myeloma research.", "da": "Nordisk samarbejdsgruppe for klinisk myelomatoseforskning."},
        "url": "",
        "country": {"en": "Nordic countries", "da": "Norden"},
    },
    {
        "name": {"en": "OPEN Statistics, Odense University Hospital", "da": "OPEN Statistik, Odense Universitetshospital"},
        "text": {"en": "Biostatistical collaboration.", "da": "Biostatistisk samarbejde."},
        "url": "",
        "country": {"en": "Denmark", "da": "Danmark"},
    },
]

PARTNERS_NOTE = {
    "en": "TODO(Confirm the partner list and add any missing partners, such as patient organizations and international collaborators.)",
    "da": "TODO(Bekræft listen og tilføj manglende partnere, fx patientforeninger og internationale samarbejdspartnere.)",
}

# ---------------------------------------------------------------- Contact
CONTACT = {
    "intro": {
        "en": "For questions about our research, collaboration or advice on patient-reported outcomes, please contact us.",
        "da": "Kontakt os gerne med spørgsmål om vores forskning, samarbejde eller rådgivning om patientrapporterede oplysninger.",
    },
    "address_heading": {"en": "Address", "da": "Adresse"},
    "address": [
        "Quality of Life Research Center",
        {"en": "Department of Hematology", "da": "Hæmatologisk Afdeling"},
        {"en": "Odense University Hospital", "da": "Odense Universitetshospital"},
        "TODO(Street address)",
        "TODO(Postal code) Odense",
        {"en": "Denmark", "da": "Danmark"},
    ],
    "email_heading": {"en": "Email", "da": "E-mail"},
    "email": "TODO(general email address)",
    "phone_heading": {"en": "Phone", "da": "Telefon"},
    "phone": "TODO(phone number)",
    "patients_heading": {"en": "For patients", "da": "Til patienter"},
    "patients": {
        "en": "We cannot answer questions about individual treatment. Please contact your own department or doctor.",
        "da": "Vi kan ikke besvare spørgsmål om individuel behandling. Kontakt venligst din egen afdeling eller læge.",
    },
}
