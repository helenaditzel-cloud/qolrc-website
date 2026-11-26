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
    ("pro", "PRO expertise", "PRO-ekspertise"),
    ("patients", "Patient involvement", "Patientinddragelse"),
    ("members", "Members", "Medarbejdere"),
    ("publications", "Publications", "Publikationer"),
    ("partners", "Partners", "Partnere"),
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
            "The center is based in the Department of Hematology at Odense University Hospital and is affiliated with the University of Southern Denmark. For 35 years we have been part of the [Nordic Myeloma Study Group (NMSG)](https://www.nordicmyeloma.org/), where our focus has been designing, collecting and analyzing quality of life data in clinical trials. We have also collected long-term quality of life data from Danish patients outside clinical trials. Within the [Nordic ITP Group](https://nordicitp.com/), we work on patient-reported outcomes in immune thrombocytopenia, including the translation and psychometric evaluation of questionnaires.",
            "Our vision is to develop an interdisciplinary center for research in quality of life, working closely with clinicians, statisticians, patient organizations and research partners across the Nordic countries and Europe.",
        ],
        "da": [
            "Quality of Life Research Center (QoLRC) undersøger, hvordan hæmatologiske sygdomme og deres behandling påvirker patienternes hverdag. Vi arbejder med patientrapporterede oplysninger (PRO) og helbredsrelateret livskvalitet (HRQoL) ved myelomatose, andre hæmatologiske kræftsygdomme og godartede hæmatologiske sygdomme som autoimmune cytopenier.",
            "Centret har base i Hæmatologisk Afdeling på Odense Universitetshospital og er tilknyttet Syddansk Universitet. I 35 år har vi været en del af [Nordic Myeloma Study Group (NMSG)](https://www.nordicmyeloma.org/), hvor vores fokus har været at planlægge, indsamle og analysere livskvalitetsdata i kliniske forsøg. Vi har også indsamlet langsigtede livskvalitetsdata fra danske patienter uden for kliniske forsøg. I [Nordic ITP Group](https://nordicitp.com/) arbejder vi med patientrapporterede oplysninger ved immun trombocytopeni, herunder oversættelse og psykometrisk evaluering af spørgeskemaer.",
            "Vores vision er at udvikle et tværfagligt center for forskning i livskvalitet i tæt samarbejde med klinikere, statistikere, patientforeninger og forskningspartnere i Norden og Europa.",
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

# ---------------------------------------------------------------- PRO expertise
PRO = {
    "intro": {
        "en": "The patient-reported outcome measures we work with, and how we can help you use them in your study.",
        "da": "De patientrapporterede måleinstrumenter, vi arbejder med, og hvordan vi kan hjælpe dig med at bruge dem i dit studie.",
    },
    "instruments_heading": {"en": "Questionnaires we work with", "da": "Spørgeskemaer, vi arbejder med"},
    "instruments_note": {
        "en": "Based on published work by QoLRC members. The badge marks questionnaires our team has translated or validated in Danish.",
        "da": "Baseret på publiceret arbejde fra QoLRC's medarbejdere. Mærket viser spørgeskemaer, som vores team har oversat eller valideret på dansk.",
    },
    # Each instrument: name, what it measures, official link (optional),
    # doi of a QoLRC paper that used it, and danish=True if the team translated or validated it into Danish.
    "instrument_groups": [
        {"title": {"en": "Cancer-specific quality of life", "da": "Kræftspecifik livskvalitet"},
         "items": [
            {"name": "EORTC QLQ-C30", "what": {"en": "Core questionnaire for health-related quality of life in cancer, including the summary score.", "da": "Kernespørgeskema om helbredsrelateret livskvalitet ved kræft, inkl. summary score."},
             "url": "https://qol.eortc.org/questionnaire/eortc-qlq-c30/", "doi": "10.1186/s41687-024-00691-2"},
            {"name": "EORTC QLQ-MY20", "what": {"en": "Module for multiple myeloma.", "da": "Modul til myelomatose."},
             "url": "https://qol.eortc.org/questionnaires/", "doi": "10.3324/haematol.2019.222299"},
            {"name": "EORTC QLQ-CIPN20", "what": {"en": "Module for chemotherapy-induced peripheral neuropathy.", "da": "Modul om kemoterapiinduceret perifer neuropati."},
             "url": "https://qol.eortc.org/questionnaires/", "doi": "10.1111/bjh.70870"},
            {"name": "EORTC QLU-C10D", "what": {"en": "Utility measure derived from the QLQ-C30, used for quality-adjusted survival.", "da": "Nyttemål afledt af QLQ-C30, brugt til kvalitetsjusteret overlevelse."},
             "url": "https://qol.eortc.org/", "doi": "10.1186/s41687-024-00691-2"},
         ]},
        {"title": {"en": "Hematology-specific", "da": "Hæmatologispecifikke"},
         "items": [
            {"name": "SSQ-MM", "what": {"en": "Steroid Symptom Questionnaire for multiple myeloma: side effects of corticosteroid treatment. Translated into Danish and Norwegian by our team.", "da": "Steroid Symptom Questionnaire til myelomatose: bivirkninger af binyrebarkhormon. Oversat til dansk og norsk af vores team."},
             "url": "", "doi": "10.1007/s11136-026-04415-5", "danish": True},
            {"name": "SSQ (ITP and AIHA)", "what": {"en": "Steroid Symptom Questionnaire, currently being validated in immune thrombocytopenia and autoimmune hemolytic anemia.", "da": "Steroid Symptom Questionnaire, som vi validerer ved immun trombocytopeni og autoimmun hæmolytisk anæmi."},
             "url": "", "doi": ""},
            {"name": "HM-PRO", "what": {"en": "Generic patient-reported outcome measure for hematologic malignancies.", "da": "Generisk PRO-mål for hæmatologiske kræftsygdomme."},
             "url": "", "doi": "10.1186/s41687-025-00869-2", "danish": True},
            {"name": "Lee cGVHD Symptom Scale", "what": {"en": "Symptoms of chronic graft-versus-host disease after allogeneic stem cell transplantation.", "da": "Symptomer på kronisk graft-versus-host-sygdom efter allogen stamcelletransplantation."},
             "url": "", "doi": "10.61409/A09250759", "danish": True},
         ]},
        {"title": {"en": "Symptoms and side effects", "da": "Symptomer og bivirkninger"},
         "items": [
            {"name": "FACIT-Fatigue", "what": {"en": "Cancer-related fatigue.", "da": "Kræftrelateret træthed."},
             "url": "https://www.facit.org/measures/facit-f", "doi": "10.1200/JCO-26-00578"},
            {"name": "FACT-PSI", "what": {"en": "Pulmonary symptoms such as shortness of breath.", "da": "Lungesymptomer som åndenød."},
             "url": "https://www.facit.org/", "doi": "10.1111/ejh.14358"},
            {"name": "FACT/GOG-Ntx", "what": {"en": "Treatment-related neurotoxicity.", "da": "Behandlingsrelateret neurotoksicitet."},
             "url": "https://www.facit.org/", "doi": "10.1186/s41687-024-00691-2"},
            {"name": "PRO-CTCAE", "what": {"en": "Patient-reported adverse events in cancer treatment.", "da": "Patientrapporterede bivirkninger ved kræftbehandling."},
             "url": "https://healthcaredelivery.cancer.gov/pro-ctcae/", "doi": "10.61409/A09250759"},
         ]},
        {"title": {"en": "Generic health and well-being", "da": "Generelt helbred og trivsel"},
         "items": [
            {"name": "PROMIS-29", "what": {"en": "Profile of physical function, anxiety, depression, fatigue, sleep, social participation and pain.", "da": "Profil af fysisk funktion, angst, depression, træthed, søvn, social deltagelse og smerte."},
             "url": "https://www.healthmeasures.net/explore-measurement-systems/promis", "doi": ""},
            {"name": "SF-12", "what": {"en": "Short generic health survey.", "da": "Kort generisk helbredsskema."},
             "url": "", "doi": "10.1111/bjh.70870"},
            {"name": "HADS", "what": {"en": "Hospital Anxiety and Depression Scale.", "da": "Hospital Anxiety and Depression Scale."},
             "url": "", "doi": "10.1186/s12955-021-01887-6"},
            {"name": "GAD-7", "what": {"en": "Anxiety, used in an adapted version during COVID-19.", "da": "Angst, brugt i en tilpasset version under COVID-19."},
             "url": "", "doi": "10.1080/0284186X.2021.1902565"},
         ]},
        {"title": {"en": "Care experience and caregivers", "da": "Oplevet kvalitet og pårørende"},
         "items": [
            {"name": "CTM-15 and PACT-M", "what": {"en": "Patient-reported experience of care transitions.", "da": "Patienters oplevelse af overgange i forløbet."},
             "url": "", "doi": "10.1186/s41687-024-00739-3", "danish": True},
            {"name": "Caregiver Roles and Responsibilities Scale", "what": {"en": "The tasks and roles of family caregivers of people with cancer.", "da": "Pårørendes opgaver og roller ved kræftsygdom."},
             "url": "", "doi": "10.1007/s11136-026-04234-8", "danish": True},
         ]},
        {"title": {"en": "Older patients and frailty", "da": "Ældre patienter og skrøbelighed"},
         "items": [
            {"name": "G8 and modified G8", "what": {"en": "Geriatric screening tools to identify frailty in older patients with cancer.", "da": "Geriatriske screeningsværktøjer til at finde skrøbelighed hos ældre patienter med kræft."},
             "url": "", "doi": "10.1016/j.jgo.2022.07.004", "danish": True},
            {"name": "EORTC QLQ-ELD14", "what": {"en": "Module for older patients with cancer.", "da": "Modul til ældre patienter med kræft."},
             "url": "https://qol.eortc.org/questionnaires/", "doi": "10.1016/S2666-7568(24)00118-1"},
            {"name": "Tilburg Frailty Indicator", "what": {"en": "Self-reported frailty.", "da": "Selvrapporteret skrøbelighed."},
             "url": "", "doi": "10.1177/26335565251415477"},
         ]},
    ],
    "advice_heading": {"en": "How we can help", "da": "Hvordan vi kan hjælpe"},
    "advice": [
        {"title": {"en": "Choosing instruments", "da": "Valg af spørgeskemaer"},
         "text": {"en": "Selecting PRO measures that fit your research question, population and setting.",
                  "da": "Valg af PRO-mål, der passer til dit forskningsspørgsmål, din population og dit setting."}},
        {"title": {"en": "PRO endpoints and protocols", "da": "PRO-endepunkter og protokoller"},
         "text": {"en": "Defining PRO objectives, endpoints, estimands and assessment schedules, following SPIRIT-PRO.",
                  "da": "Fastlæggelse af PRO-formål, endepunkter, estimands og måletidspunkter efter SPIRIT-PRO."}},
        {"title": {"en": "Statistical analysis plans", "da": "Statistiske analyseplaner"},
         "text": {"en": "Analysis of longitudinal PRO data, including mixed models for repeated measures and handling of missing data.",
                  "da": "Analyse af longitudinelle PRO-data, herunder mixed models for gentagne målinger og håndtering af manglende data."}},
        {"title": {"en": "Psychometric validation", "da": "Psykometrisk validering"},
         "text": {"en": "Developing and validating questionnaires and translations, following COSMIN methodology.",
                  "da": "Udvikling og validering af spørgeskemaer og oversættelser efter COSMIN-metoden."}},
        {"title": {"en": "Data collection in practice", "da": "Dataindsamling i praksis"},
         "text": {"en": "Setting up electronic and paper-based PRO collection and monitoring missing responses in real time.",
                  "da": "Opsætning af elektronisk og papirbaseret PRO-indsamling og løbende opfølgning på manglende besvarelser."}},
        {"title": {"en": "Grant applications", "da": "Fondsansøgninger"},
         "text": {"en": "Writing the PRO sections of grant applications and study protocols.",
                  "da": "Udarbejdelse af PRO-afsnit i fondsansøgninger og protokoller."}},
    ],
    "resources_heading": {"en": "Resources", "da": "Ressourcer"},
    "proteus": {
        "en": "Please also see resources for the use of PROs in trials and routine care on the [Proteus Consortium](https://theproteusconsortium.org/) website.",
        "da": "Se også ressourcer om brug af PRO i kliniske forsøg og i den daglige klinik på [Proteus Consortium](https://theproteusconsortium.org/)s hjemmeside.",
    },
    "links": [
        {"name": "EORTC Quality of Life Group", "url": "https://qol.eortc.org/"},
        {"name": "PROMIS / HealthMeasures", "url": "https://www.healthmeasures.net/"},
        {"name": "COSMIN", "url": "https://www.cosmin.nl/"},
    ],
}

# ---------------------------------------------------------------- Become a patient representative
PATIENTS = {
    "title": {"en": "Become a patient representative", "da": "Bliv patientrepræsentant"},
    "intro": {
        "en": "Your experience can help make our research more relevant for patients and their families.",
        "da": "Dine erfaringer kan gøre vores forskning mere relevant for patienter og pårørende.",
    },
    "why_heading": {"en": "Why we involve patients", "da": "Hvorfor vi inddrager patienter"},
    "why": {
        "en": [
            "Our research is about how disease and treatment affect everyday life. Only patients and their relatives know what that is really like, so we want people with that experience to help shape our studies from the start.",
            "Patient representatives help us ask the right questions, choose questionnaires that cover what matters, and explain our results in a way that makes sense to the people they concern.",
        ],
        "da": [
            "Vores forskning handler om, hvordan sygdom og behandling påvirker hverdagen. Det er kun patienter og pårørende, der ved, hvordan det virkelig er, og derfor vil vi gerne have mennesker med de erfaringer med til at forme vores studier fra starten.",
            "Patientrepræsentanter hjælper os med at stille de rigtige spørgsmål, vælge spørgeskemaer, der dækker det, der betyder noget, og formidle vores resultater, så de giver mening for dem, de handler om.",
        ],
    },
    "tasks_heading": {"en": "What a patient representative does", "da": "Hvad en patientrepræsentant laver"},
    "tasks": [
        {"title": {"en": "Comment on questionnaires", "da": "Kommenterer spørgeskemaer"},
         "text": {"en": "Read questionnaires and tell us whether the questions are relevant, clear and not too burdensome.",
                  "da": "Læser spørgeskemaer og fortæller os, om spørgsmålene er relevante, forståelige og ikke for belastende."}},
        {"title": {"en": "Review study materials", "da": "Gennemlæser studiemateriale"},
         "text": {"en": "Give feedback on patient information, consent forms and plans for new studies.",
                  "da": "Giver feedback på patientinformation, samtykkeerklæringer og planer for nye studier."}},
        {"title": {"en": "Join meetings", "da": "Deltager i møder"},
         "text": {"en": "Take part in occasional meetings, in person or online, with researchers and other representatives.",
                  "da": "Deltager i møder en gang imellem, fysisk eller online, med forskere og andre repræsentanter."}},
        {"title": {"en": "Help share results", "da": "Hjælper med at formidle resultater"},
         "text": {"en": "Help us write plain-language summaries so our findings reach patients and the public.",
                  "da": "Hjælper os med at skrive letforståelige resuméer, så vores resultater når ud til patienter og offentligheden."}},
    ],
    "who_heading": {"en": "Who can take part", "da": "Hvem kan være med"},
    "who": {
        "en": [
            "People who have, or have had, a hematologic disease such as multiple myeloma, lymphoma, leukemia, ITP or AIHA.",
            "Relatives and caregivers of people with a hematologic disease.",
            "No research experience is needed. We explain everything along the way.",
        ],
        "da": [
            "Personer, der har eller har haft en hæmatologisk sygdom, fx myelomatose, lymfom, leukæmi, ITP eller AIHA.",
            "Pårørende til personer med en hæmatologisk sygdom.",
            "Du behøver ingen erfaring med forskning. Vi forklarer det hele undervejs.",
        ],
    },
    "practical_heading": {"en": "Practical information", "da": "Praktisk information"},
    "practical": {
        "en": [
            "You decide how much time you want to spend, and you can stop at any time.",
            "TODO(Describe the expected time commitment, for example a few hours per study.)",
            "TODO(State whether transport and other expenses are reimbursed, or any fee.)",
        ],
        "da": [
            "Du bestemmer selv, hvor meget tid du vil bruge, og du kan stoppe når som helst.",
            "TODO(Beskriv den forventede tidsforbrug, fx nogle timer pr. studie.)",
            "TODO(Angiv, om transport og andre udgifter dækkes, eller om der gives honorar.)",
        ],
    },
    "join_heading": {"en": "Interested?", "da": "Interesseret?"},
    "join_text": {
        "en": "Send us a short email with your name and phone number, and tell us whether you are a patient or a relative. We will contact you for an informal talk.",
        "da": "Send os en kort e-mail med dit navn og telefonnummer, og fortæl, om du er patient eller pårørende. Så kontakter vi dig for en uforpligtende snak.",
    },
    "join_privacy": {
        "en": "Please do not include details about your health or treatment in your email.",
        "da": "Skriv venligst ikke oplysninger om dit helbred eller din behandling i e-mailen.",
    },
    "join_email": "OUH.QoLReC@rsyd.dk",
}

# ---------------------------------------------------------------- Members
MEMBERS_INTRO = {
    "en": "The people behind QoLRC.",
    "da": "Menneskene bag QoLRC.",
}

# photo: file name in assets/img/people/ (portrait, ideally 800 x 1000 px). Leave "" to show a placeholder.
MEMBERS = [
    {
        "name": "Lene Kongsgaard Nielsen",
        "title": {"en": "MD, PhD, Associate Professor, Head of QoLRC", "da": "Læge, ph.d., lektor, leder af QoLRC"},
        "bio": {
            "en": "Consultant in hematology, associate professor at the University of Southern Denmark and head of the Quality of Life Research Center. She leads the center's research on quality of life in multiple myeloma, including the design, collection and analysis of quality of life data in Nordic Myeloma Study Group trials and in real-world Danish cohorts.",
            "da": "Overlæge i hæmatologi, lektor ved Syddansk Universitet og leder af Quality of Life Research Center. Hun leder centrets forskning i livskvalitet ved myelomatose, herunder planlægning, indsamling og analyse af livskvalitetsdata i studier fra Nordic Myeloma Study Group og i danske kohorter uden for kliniske forsøg.",
        },
        "email": "",
        "photo": "lene-kongsgaard-nielsen.jpg",
        "profile": "https://portal.findresearcher.sdu.dk/da/persons/lenekn",
        "orcid": "0000-0003-2083-3870",
    },
    {
        "name": "Henrik Frederiksen",
        "title": {"en": "MD, PhD, Professor, Head of Research", "da": "Læge, ph.d., professor, forskningsleder"},
        "bio": {
            "en": "Consultant and Head of Research at the Department and Research Unit of Hematology, Odense University Hospital and University of Southern Denmark. His research focuses on frailty and supportive care in hematologic cancer, including how frailty assessment can be used in routine care to tailor treatment, as well as non-malignant hematologic diseases. Former chair of the Danish Society of Hematology.",
            "da": "Overlæge og forskningsleder ved Hæmatologisk Afdeling og Forskningsenhed, Odense Universitetshospital og Syddansk Universitet. Hans forskning fokuserer på skrøbelighed og understøttende behandling ved hæmatologisk kræft, herunder hvordan vurdering af skrøbelighed kan bruges i den daglige klinik til at tilpasse behandlingen, samt godartede hæmatologiske sygdomme. Tidligere formand for Dansk Hæmatologisk Selskab.",
        },
        "email": "",
        "photo": "henrik-frederiksen.jpg",
        "profile": "https://www.sdu.dk/en/forskning/haematologi",
        "orcid": "0000-0001-8905-0220",
    },
    {
        "name": "Niels Abildgaard",
        "title": {"en": "Clinical Professor in Hematology", "da": "Klinisk professor i hæmatologi"},
        "bio": {
            "en": "Clinical professor at the Department of Hematology, Odense University Hospital, and the University of Southern Denmark, and head of the Odense Amyloidosis Centre (AmyC OUH), a Center of Clinical Excellence. His research covers multiple myeloma from disease biology to treatment, with particular emphasis on myeloma bone disease.",
            "da": "Klinisk professor på Hæmatologisk Afdeling, Odense Universitetshospital, og Syddansk Universitet samt leder af Odense Amyloidosis Centre (AmyC OUH), et Center for Klinisk Excellence. Hans forskning dækker myelomatose fra sygdomsbiologi til behandling med særligt fokus på knoglesygdom ved myelomatose.",
        },
        "email": "",
        "photo": "niels-abildgaard.jpg",
        "profile": "https://portal.findresearcher.sdu.dk/en/persons/nabildgaard/",
        "orcid": "0000-0001-6852-2014",
    },
    {
        "name": "Helena Møgelbjerg Ditzel",
        "title": {"en": "MD, PhD, Postdoctoral Researcher", "da": "Læge, ph.d., postdoc"},
        "bio": {
            "en": "Clinician-researcher working on health-related quality of life, patient-reported outcomes and psychometric validation in hematology and oncology, with a focus on multiple myeloma, autoimmune cytopenias and frailty in older adults. Project manager of the REMNANT-PRO study and principal investigator of the PROGNOSIS-G8 cohort study. PhD in geriatric oncology from the University of Southern Denmark (2025) and board member of the Danish Society of Geriatric Oncology.",
            "da": "Klinisk forsker, der arbejder med helbredsrelateret livskvalitet, patientrapporterede oplysninger og psykometrisk validering inden for hæmatologi og onkologi med fokus på myelomatose, autoimmune cytopenier og skrøbelighed hos ældre. Projektleder for REMNANT-PRO-studiet og forsøgsansvarlig for kohortestudiet PROGNOSIS-G8. Ph.d. i geriatrisk onkologi fra Syddansk Universitet (2025) og bestyrelsesmedlem i Dansk Selskab for Geriatrisk Onkologi.",
        },
        "email": "",
        "photo": "helena-ditzel.jpg",
        "profile": "https://portal.findresearcher.sdu.dk/en/persons/hmditzel/",
        "orcid": "0000-0002-9435-0524",
    },
    {
        "name": "Pia K. Pedersen",
        "title": {"en": "Daily Manager, Hematology Research Unit", "da": "Daglig leder, Hæmatologisk Forskningsenhed"},
        "bio": {
            "en": "Daily manager of the Hematology Research Unit at Odense University Hospital and the University of Southern Denmark. She is responsible for the unit's day-to-day management and administration and supports researchers and research projects across the unit, including QoLRC.",
            "da": "Daglig leder af Hæmatologisk Forskningsenhed på Odense Universitetshospital og Syddansk Universitet. Hun har ansvaret for enhedens daglige drift og administration og understøtter forskere og forskningsprojekter på tværs af enheden, herunder QoLRC.",
        },
        "email": "",
        "photo": "pia-pedersen.jpg",
        "profile": "",
    },
    {
        "name": "Tine Rosenberg",
        "title": {"en": "Research Coordinator and Fundraiser", "da": "Forskningskoordinator og fundraiser"},
        "bio": {
            "en": "Research coordinator and project manager (MSc in Health Science) at the Hematology Research Unit and QoLRC, Odense University Hospital. Her research focuses on home-based treatment and digital patient-reported outcomes in multiple myeloma, including home-administered daratumumab and digital symptom reporting before treatment, and she has contributed to the Danish translation and validation of several questionnaires, including the SSQ-MM. From 2026 she is a PhD fellow in the national Treat@Home program, studying home-based daratumumab treatment across Danish hematology departments.",
            "da": "Forskningskoordinator og projektleder (cand.scient.san.) ved Hæmatologisk Forskningsenhed og QoLRC, Odense Universitetshospital. Hendes forskning fokuserer på hjemmebehandling og digitale patientrapporterede oplysninger ved myelomatose, herunder daratumumab givet i eget hjem og digital symptomrapportering før behandling, og hun har bidraget til dansk oversættelse og validering af flere spørgeskemaer, herunder SSQ-MM. Fra 2026 er hun ph.d.-studerende i det nationale Treat@Home-program, hvor hun undersøger hjemmebehandling med daratumumab på tværs af danske hæmatologiske afdelinger.",
        },
        "email": "",
        "photo": "tine-rosenberg.jpg",
        "profile": "https://portal.findresearcher.sdu.dk/en/persons/tinerosenberg/",
        "orcid": "0000-0002-7874-5526",
    },
]

# ---------------------------------------------------------------- Publications
PUBLICATIONS_INTRO = {
    "en": "Publications by QoLRC members, newest first.",
    "da": "Publikationer fra QoLRC's medarbejdere, nyeste først.",
}

# Each entry: year, authors, title, journal, doi (optional)
PUBLICATIONS = [
    # Example of the format:
    # {"year": 2026, "authors": "Ditzel HM, ...", "title": "...", "journal": "J Geriatr Oncol", "doi": "10.xxxx/xxxx"},
]

PUBLICATIONS_EMPTY = {
    "en": "The publication list is being fetched from PubMed and will appear here shortly.",
    "da": "Publikationslisten hentes fra PubMed og vises her om lidt.",
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
        "text": {"en": "Collaborative group for clinical myeloma research in Norway, Sweden, Finland, Estonia, Iceland and Denmark. QoLRC has been part of the group for 35 years.", "da": "Samarbejdsgruppe for klinisk myelomatoseforskning i Norge, Sverige, Finland, Estland, Island og Danmark. QoLRC har været en del af gruppen i 35 år."},
        "url": "https://www.nordicmyeloma.org/",
        "country": {"en": "Nordic countries", "da": "Norden"},
    },
    {
        "name": {"en": "Nordic ITP Group", "da": "Nordic ITP Group"},
        "text": {"en": "Nordic network for research and education in immune thrombocytopenia, with members from Denmark, Finland, Iceland, Norway and Sweden. Henrik Frederiksen is a member of the steering committee.", "da": "Nordisk netværk for forskning og uddannelse inden for immun trombocytopeni med medlemmer fra Danmark, Finland, Island, Norge og Sverige. Henrik Frederiksen er medlem af styregruppen."},
        "url": "https://nordicitp.com/",
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
        {"en": "Hematology Research Unit, Dept. X", "da": "Hæmatologisk Forskningsenhed, Afd. X"},
        "Quality of Life Research Center (QoLRC)",
        {"en": "Odense University Hospital", "da": "Odense Universitetshospital"},
        {"en": "Kløvervænget 10, Entrance 112, 12th floor", "da": "Kløvervænget 10, Indgang 112, 12. sal"},
        "5000 Odense C",
        {"en": "Denmark", "da": "Danmark"},
    ],
    "email_heading": {"en": "Email", "da": "E-mail"},
    "email": "OUH.QoLReC@rsyd.dk",
    "phone_heading": {"en": "Phone", "da": "Telefon"},
    "phone": {"en": "+45 66 11 33 33 (OUH switchboard)", "da": "66 11 33 33 (OUH's hovednummer)"},
    "patients_heading": {"en": "For patients", "da": "Til patienter"},
    "patients": {
        "en": "We cannot answer questions about individual treatment. Please contact your own department or doctor.",
        "da": "Vi kan ikke besvare spørgsmål om individuel behandling. Kontakt venligst din egen afdeling eller læge.",
    },
}
