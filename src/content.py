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
    ("team", "Our team", "Vores team"),
    ("publications", "Publications", "Publikationer"),
    ("news", "News & events", "Nyheder"),
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
            "The Quality of Life Research Center (QoLRC) studies how hematologic diseases and their treatment affect patients' everyday lives. We work with patient-reported outcomes (PROs) and health-related quality of life (HRQoL) across hematologic cancers and benign hematologic diseases.",
            "The center was established in 2017 as a strategic investment by the Department of Hematology and the Hematology Research Unit at Odense University Hospital, and is affiliated with the University of Southern Denmark. QoLRC is the core facility for quality of life research in the [Nordic Myeloma Study Group (NMSG)](https://www.nordicmyeloma.org/), building on 35 years of experience with quality of life data from Nordic myeloma trials. We also work closely with the [Nordic ITP Group](https://nordicitp.com/) on patient-reported outcomes in benign hematology.",
            "Our work covers the whole path of patient-reported outcome research: planning and analyzing quality of life endpoints in clinical trials, following patients in routine care and population-based data, developing and validating questionnaires, and evaluating new models of care, such as home-based treatment and care adapted to older patients with frailty.",
            "Our vision is to establish an interdisciplinary center for research in health-related quality of life at an international level, working closely with clinicians, statisticians, patient representatives, patient organizations and research partners across the Nordic countries and Europe.",
        ],
        "da": [
            "Quality of Life Research Center (QoLRC) undersøger, hvordan hæmatologiske sygdomme og deres behandling påvirker patienternes hverdag. Vi arbejder med patientrapporterede oplysninger (PRO) og helbredsrelateret livskvalitet (HRQoL) ved hæmatologiske kræftsygdomme og godartede hæmatologiske sygdomme.",
            "Centret blev etableret i 2017 som en strategisk investering i Hæmatologisk Afdeling og Hæmatologisk Forskningsenhed på Odense Universitetshospital og er tilknyttet Syddansk Universitet. QoLRC er core facility for forskning i livskvalitet i [Nordic Myeloma Study Group (NMSG)](https://www.nordicmyeloma.org/) og bygger på 35 års erfaring med livskvalitetsdata fra nordiske myelomatoseforsøg. Vi samarbejder også tæt med [Nordic ITP Group](https://nordicitp.com/) om patientrapporterede oplysninger inden for benign hæmatologi.",
            "Vores arbejde dækker hele vejen gennem forskning i patientrapporterede oplysninger: planlægning og analyse af livskvalitetsendepunkter i kliniske forsøg, opfølgning af patienter i den daglige klinik og i populationsbaserede data, udvikling og validering af spørgeskemaer samt evaluering af nye behandlingsformer, fx hjemmebehandling og behandling tilpasset ældre, skrøbelige patienter.",
            "Vores vision er at etablere et tværfagligt center for forskning i helbredsrelateret livskvalitet på internationalt niveau i tæt samarbejde med klinikere, statistikere, patientrepræsentanter, patientforeninger og forskningspartnere i Norden og Europa.",
        ],
    },
    "themes_heading": {"en": "Our research", "da": "Vores forskning"},
    "themes": [
        {
            "title": {"en": "PROs in clinical trials", "da": "PRO i kliniske forsøg"},
            "text": {
                "en": "Study design, data collection and analysis of patient-reported outcomes in randomized and single-arm trials, following international standards for PRO endpoints and estimands.",
                "da": "Studiedesign, dataindsamling og analyse af patientrapporterede oplysninger i randomiserede og enkeltarmede forsøg efter internationale standarder for PRO-endepunkter og estimands.",
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
        {"value": "2017", "label": {"en": "Year established", "da": "Etableret"}},
        {"value": "12", "label": {"en": "Ongoing and early-phase studies", "da": "Igangværende studier og studier i tidlig fase"}},
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
    "en": "Selected ongoing and early-phase studies led by or involving QoLRC.",
    "da": "Udvalgte igangværende studier og studier i tidlig fase, som QoLRC leder eller deltager i.",
}

STUDY_GROUPS = [
    ("nmsg", {"en": "Nordic Myeloma Study Group (NMSG) studies", "da": "Studier i Nordic Myeloma Study Group (NMSG)"}),
    ("other", {"en": "Other ongoing studies", "da": "Andre igangværende studier"}),
    ("early", {"en": "Studies in an early phase", "da": "Studier i tidlig fase"}),
]

STUDIES = [{'group': 'nmsg',
  'title': {'en': 'REST: isatuximab with minimal dexamethasone', 'da': 'REST: isatuximab med minimal dexamethason'},
  'disease': {'en': 'Multiple myeloma', 'da': 'Myelomatose'},
  'nct': 'NCT04939844',
  'text': {'en': 'A phase 2 study of isatuximab combined with bortezomib and lenalidomide with minimal dexamethasone in patients with multiple myeloma who are '
                 'not eligible for stem cell transplantation.',
           'da': 'Et fase 2-studie af isatuximab kombineret med bortezomib og lenalidomid med minimal dexamethason hos patienter med myelomatose, der ikke kan '
                 'tåle stamcellebehandling.'},
  'role': {'en': 'Quality of life data, design, management and analysis (NMSG core facility)', 'da': 'Livskvalitetsdata: design, datahåndtering og analyse (NMSG core facility)'}},
 {'group': 'nmsg',
  'title': {'en': 'SABLe: selinexor in newly diagnosed myeloma', 'da': 'SABLe: selinexor ved nydiagnosticeret myelomatose'},
  'disease': {'en': 'Multiple myeloma', 'da': 'Myelomatose'},
  'nct': 'NCT04717700',
  'text': {'en': 'A phase 2 study of selinexor with alternating bortezomib or lenalidomide plus dexamethasone in newly diagnosed patients who are not eligible '
                 'for stem cell transplantation.',
           'da': 'Et fase 2-studie af selinexor med skiftevis bortezomib eller lenalidomid plus dexamethason hos nydiagnosticerede patienter, der ikke kan '
                 'tåle stamcellebehandling.'},
  'role': {'en': 'Quality of life data, design, management and analysis (NMSG core facility)', 'da': 'Livskvalitetsdata: design, datahåndtering og analyse (NMSG core facility)'}},
 {'title': {'en': 'REMNANT: quality of life in MRD-guided myeloma treatment', 'da': 'REMNANT: livskvalitet ved MRD-styret myelomatosebehandling'},
  'disease': {'en': 'Multiple myeloma', 'da': 'Myelomatose'},
  'nct': 'NCT04513639',
  'text': {'en': 'A Nordic randomized trial in newly diagnosed multiple myeloma, led by Oslo University Hospital, in which treatment is guided by measurable '
                 'residual disease. QoLRC leads the Danish health-related quality of life work, including the statistical analysis plans for the HRQoL '
                 'sub-study.',
           'da': 'Et nordisk randomiseret forsøg ved nydiagnosticeret myelomatose, ledet af Oslo universitetssykehus, hvor behandlingen styres af målbar '
                 'restsygdom. QoLRC leder det danske arbejde med helbredsrelateret livskvalitet, herunder de statistiske analyseplaner for '
                 'livskvalitetsdelen.'},
  'role': {'en': 'Quality of life data, design, management and analysis (NMSG core facility)', 'da': 'Livskvalitetsdata: design, datahåndtering og analyse (NMSG core facility)'},
  'group': 'nmsg'},
 {'group': 'nmsg',
  'title': {'en': 'SHIELD: subcutaneous immunoglobulin against early infections in multiple myeloma',
            'da': 'SHIELD: subkutant immunglobulin mod tidlige infektioner ved myelomatose'},
  'disease': {'en': 'Multiple myeloma', 'da': 'Myelomatose'},
  'nct': '',
  'text': {'en': 'A randomized phase 2 trial (NMSG 32/23) testing whether preventive subcutaneous immunoglobulin reduces infections and early mortality '
                 'compared with standard infection prophylaxis in patients with newly diagnosed multiple myeloma who are not eligible for stem cell '
                 'transplantation. Quality of life is measured repeatedly during the first year of treatment.',
           'da': 'Et randomiseret fase 2-forsøg (NMSG 32/23), der undersøger, om forebyggende subkutant immunglobulin mindsker infektioner og tidlig '
                 'dødelighed sammenlignet med standard infektionsprofylakse hos patienter med nydiagnosticeret myelomatose, som ikke kan tilbydes '
                 'stamcelletransplantation. Livskvaliteten måles gentagne gange gennem det første behandlingsår.'},
  'role': {'en': 'Quality of life data, design, management and analysis (NMSG core facility)', 'da': 'Livskvalitetsdata: design, datahåndtering og analyse (NMSG core facility)'}},
 {'title': {'en': 'Patient-reported outcomes in the Nordic IRd trial', 'da': 'Patientrapporterede oplysninger i det nordiske IRd-forsøg'},
  'disease': {'en': 'Multiple myeloma', 'da': 'Myelomatose'},
  'nct': 'NCT03376672',
  'text': {'en': 'Analysis of quality of life, myeloma-specific symptoms and peripheral neuropathy in a Nordic Myeloma Study Group phase 2 trial in newly '
                 'diagnosed, transplant-eligible patients, using the EORTC QLQ-C30, QLQ-MY20 and QLQ-CIPN20.',
           'da': 'Analyse af livskvalitet, myelomatosespecifikke symptomer og perifer neuropati i et fase 2-forsøg fra Nordic Myeloma Study Group hos '
                 'nydiagnosticerede patienter, der kan tåle højdosisbehandling, med EORTC QLQ-C30, QLQ-MY20 og QLQ-CIPN20.'},
  'role': {'en': 'Quality of life data, design, management and analysis (NMSG core facility)', 'da': 'Livskvalitetsdata: design, datahåndtering og analyse (NMSG core facility)'},
  'group': 'nmsg'},
 {'group': 'nmsg',
  'title': {'en': 'TALTEC: talquetamab and teclistamab consolidation', 'da': 'TALTEC: konsolidering med talquetamab og teclistamab'},
  'disease': {'en': 'Multiple myeloma', 'da': 'Myelomatose'},
  'nct': 'NCT06505369',
  'text': {'en': 'A phase 2 study of consolidation with the bispecific antibodies talquetamab and teclistamab as part of first-line treatment in '
                 'transplant-eligible patients, measuring measurable residual disease (MRD) negativity.',
           'da': 'Et fase 2-studie af konsolidering med de bispecifikke antistoffer talquetamab og teclistamab som del af førstelinjebehandlingen hos '
                 'patienter, der kan tåle højdosisbehandling, med måling af MRD-negativitet.'},
  'role': {'en': 'Quality of life data, design, management and analysis (NMSG core facility)', 'da': 'Livskvalitetsdata: design, datahåndtering og analyse (NMSG core facility)'}},
 {'group': 'other',
  'title': {'en': 'QoL-MM: quality of life in Danish patients with multiple myeloma', 'da': 'QoL-MM: livskvalitet hos danske patienter med myelomatose'},
  'disease': {'en': 'Multiple myeloma', 'da': 'Myelomatose'},
  'nct': 'NCT02892383',
  'text': {'en': 'A nationwide observational study of quality of life in 681 Danish patients with newly diagnosed or relapsed multiple myeloma, followed with '
                 'patient-reported outcomes for two years outside clinical trials.',
           'da': 'Et landsdækkende observationelt studie af livskvalitet hos 681 danske patienter med nydiagnosticeret eller recidiverende myelomatose, fulgt '
                 'med patientrapporterede oplysninger i to år uden for kliniske forsøg.'},
  'role': {'en': 'Sponsor and study lead', 'da': 'Sponsor og studieledelse'}},
 {'group': 'other',
  'title': {'en': 'DARA-PRO', 'da': 'DARA-PRO'},
  'disease': {'en': 'Multiple myeloma', 'da': 'Myelomatose'},
  'nct': '',
  'text': {'en': 'TODO(Add a one-sentence description of DARA-PRO.)', 'da': 'TODO(Tilføj en kort beskrivelse af DARA-PRO.)'},
  'role': {'en': '', 'da': ''}},
 {'group': 'other',
  'title': {'en': 'IMPROVE: geriatric assessment in older patients with frailty and hematologic cancer',
            'da': 'IMPROVE: geriatrisk vurdering hos ældre, skrøbelige patienter med hæmatologisk kræft'},
  'disease': {'en': 'Hematologic cancer', 'da': 'Hæmatologisk kræft'},
  'nct': 'NCT06373471',
  'text': {'en': 'A randomized controlled trial of whether adding comprehensive geriatric assessment and treatment to standard care improves quality '
                 'of life and physical functioning in patients aged 70 or older with frailty and hematologic cancer. The trial aims to include 152 patients. '
                 'It builds on the completed IMPROVE pilot study (NCT06689332).',
           'da': 'Et randomiseret kontrolleret forsøg, der undersøger, om geriatrisk helbredsvurdering og behandling som tillæg til standardbehandling '
                 'forbedrer livskvalitet og fysisk funktion hos patienter på 70 år eller derover med skrøbelighed og hæmatologisk kræft. Forsøget skal '
                 'inkludere 152 patienter. Det bygger videre på det afsluttede IMPROVE-pilotstudie (NCT06689332).'},
  'role': {'en': 'Sponsor and study lead (PI Henrik Frederiksen, PhD student Nina Andersen)',
           'da': 'Sponsor og studieledelse (forsøgsansvarlig Henrik Frederiksen, ph.d.-studerende Nina Andersen)'}},
 {'group': 'other',
  'title': {'en': 'Revision of the EORTC QLQ-MY20', 'da': 'Revision af EORTC QLQ-MY20'},
  'disease': {'en': 'Multiple myeloma', 'da': 'Myelomatose'},
  'nct': '',
  'text': {'en': 'Revision of the EORTC questionnaire module for patients with multiple myeloma, so that it reflects the symptoms and side effects of modern '
                 'myeloma treatment. TODO(Check this description.)',
           'da': "Revision af EORTC's spørgeskemamodul til patienter med myelomatose, så det afspejler symptomer og bivirkninger ved moderne "
                 'myelomatosebehandling. TODO(Tjek beskrivelsen.)'},
  'role': {'en': '', 'da': ''}},
 {'group': 'early',
  'title': {'en': 'ISOLDE', 'da': 'ISOLDE'},
  'disease': {'en': 'Multiple myeloma', 'da': 'Myelomatose'},
  'nct': '',
  'status': {'en': 'Early phase', 'da': 'Tidlig fase'},
  'text': {'en': 'An investigator-initiated, single-arm, open-label, multicenter phase 2 study of isatuximab, iberdomide and limited bortezomib '
                 'in patients with newly diagnosed multiple myeloma who are not eligible for high-dose melphalan with autologous stem cell transplantation.',
           'da': 'Et investigatorinitieret, enkeltarmet, åbent multicenter fase 2-studie af isatuximab, iberdomid og begrænset bortezomib hos patienter '
                 'med nydiagnosticeret myelomatose, som ikke kan tilbydes højdosis melphalan med autolog stamcelletransplantation.'},
  'role': {'en': 'Quality of life data, design, management and analysis (NMSG core facility)', 'da': 'Livskvalitetsdata: design, datahåndtering og analyse (NMSG core facility)'}},
 {'title': {'en': 'Validation of the Steroid Symptom Questionnaire in ITP and AIHA', 'da': 'Validering af Steroid Symptom Questionnaire ved ITP og AIHA'},
  'disease': {'en': 'Autoimmune cytopenias', 'da': 'Autoimmune cytopenier'},
  'nct': '',
  'text': {'en': 'A multinational psychometric validation study of a questionnaire measuring symptoms related to corticosteroid treatment in patients with '
                 'immune thrombocytopenia and autoimmune hemolytic anemia, with planned sites in Denmark, Norway, Sweden and the United Kingdom.',
           'da': 'Et internationalt psykometrisk valideringsstudie af et spørgeskema, der måler symptomer relateret til behandling med binyrebarkhormon hos '
                 'patienter med immun trombocytopeni og autoimmun hæmolytisk anæmi, med planlagte centre i Danmark, Norge, Sverige og Storbritannien.'},
  'status': {'en': 'Early phase', 'da': 'Tidlig fase'},
  'role': {'en': 'Principal investigator', 'da': 'Forsøgsansvarlig'},
  'group': 'early'}]

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
            {"name": "SSQ (ITP and AIHA)", "what": {"en": "Steroid Symptom Questionnaire, to be validated in immune thrombocytopenia and autoimmune hemolytic anemia in a study in its early phase.", "da": "Steroid Symptom Questionnaire, som skal valideres ved immun trombocytopeni og autoimmun hæmolytisk anæmi i et studie i tidlig fase."},
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
    "collab_heading": {"en": "Research collaboration", "da": "Forskningssamarbejde"},
    "collab_intro": {"en": "We also take part in studies as research partners, contributing to the parts of a project where PRO expertise is needed.",
                     "da": "Vi indgår også i studier som forskningspartnere og bidrager til de dele af et projekt, hvor der er brug for PRO-ekspertise."},
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
            "The expected time commitment is about 8 to 10 hours every six months.",
            "Travel expenses are reimbursed. The role is voluntary and unpaid.",
        ],
        "da": [
            "Du bestemmer selv, hvor meget tid du vil bruge, og du kan stoppe når som helst.",
            "Du skal forvente at bruge omkring 8 til 10 timer hvert halve år.",
            "Udgifter til transport dækkes. Det er en frivillig og ulønnet rolle.",
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
MEMBER_GROUPS = [
    ("leadership", {"en": "Leadership", "da": "Ledelse"}),
    ("researchers", {"en": "Researchers", "da": "Forskere"}),
    ("phd", {"en": "PhD students", "da": "Ph.d.-studerende"}),
    ("adjunct", {"en": "Adjunct and affiliated", "da": "Tilknyttede forskere"}),
    ("admin", {"en": "Administration", "da": "Administration"}),
]

MEMBER_GROUP_OF = {
    "Henrik Frederiksen": "leadership",
    "Lene Kongsgaard Nielsen": "leadership",
    "Pia K. Pedersen": "leadership",
    "Niels Abildgaard": "researchers",
    "Helena Møgelbjerg Ditzel": "researchers",
    "Tine Rosenberg": "researchers",
    "Anne Møller Clausen": "phd",
    "Nina Andersen": "phd",
    "Klara Rydahl": "phd",
    "Madeleine King": "adjunct",
    "Sören Möller": "adjunct",
    "Tina Käehne": "admin",
}

MEMBERS = [{'name': 'Henrik Frederiksen',
  'title': {'en': 'MD, PhD, Head of Research and Professor', 'da': 'Læge, ph.d., forskningsleder og professor'},
  'bio': {'en': 'Consultant and Head of Research at the Department and Research Unit of Hematology, Odense University Hospital and University of Southern '
                'Denmark. His research focuses on frailty and supportive care in hematologic cancer, including how frailty assessment can be used in routine '
                'care to tailor treatment, as well as non-malignant hematologic diseases. Former chair of the Danish Society of Hematology.',
          'da': 'Overlæge og forskningsleder ved Hæmatologisk Afdeling og Forskningsenhed, Odense Universitetshospital og Syddansk Universitet. Hans forskning '
                'fokuserer på skrøbelighed og understøttende behandling ved hæmatologisk kræft, herunder hvordan vurdering af skrøbelighed kan bruges i den '
                'daglige klinik til at tilpasse behandlingen, samt godartede hæmatologiske sygdomme. Tidligere formand for Dansk Hæmatologisk Selskab.'},
  'email': '',
  'photo': 'henrik-frederiksen.jpg',
  'profile': 'https://www.sdu.dk/en/forskning/haematologi',
  'orcid': '0000-0001-8905-0220'},
 {'name': 'Niels Abildgaard',
  'title': {'en': 'Senior Professor', 'da': 'Seniorprofessor'},
  'bio': {'en': 'Senior professor at the Department of Hematology, Odense University Hospital, and the University of Southern Denmark, and head of the Odense '
                'Amyloidosis Centre (AmyC OUH), a Center of Clinical Excellence. His research covers multiple myeloma from disease biology to treatment, with '
                'particular emphasis on myeloma bone disease.',
          'da': 'Seniorprofessor på Hæmatologisk Afdeling, Odense Universitetshospital, og Syddansk Universitet samt leder af Odense Amyloidosis Centre (AmyC '
                'OUH), et Center for Klinisk Excellence. Hans forskning dækker myelomatose fra sygdomsbiologi til behandling med særligt fokus på knoglesygdom '
                'ved myelomatose.'},
  'email': '',
  'photo': 'niels-abildgaard.jpg',
  'profile': 'https://portal.findresearcher.sdu.dk/en/persons/nabildgaard/',
  'orcid': '0000-0001-6852-2014'},
 {'name': 'Lene Kongsgaard Nielsen',
  'title': {'en': 'MD, PhD, Scientific Leader and Associate Professor', 'da': 'Læge, ph.d., videnskabelig leder og lektor'},
  'bio': {'en': 'Consultant in hematology, associate professor at the University of Southern Denmark and scientific leader of the Quality of Life Research '
                "Center. She leads the center's research on quality of life in multiple myeloma, including the design, collection and analysis of quality of "
                'life data in Nordic Myeloma Study Group trials and in real-world Danish cohorts.',
          'da': 'Overlæge i hæmatologi, lektor ved Syddansk Universitet og videnskabelig leder af Quality of Life Research Center. Hun leder centrets '
                'forskning i livskvalitet ved myelomatose, herunder planlægning, indsamling og analyse af livskvalitetsdata i studier fra Nordic Myeloma Study '
                'Group og i danske kohorter uden for kliniske forsøg.'},
  'email': '',
  'photo': 'lene-kongsgaard-nielsen.jpg',
  'profile': 'https://portal.findresearcher.sdu.dk/da/persons/lenekn',
  'orcid': '0000-0003-2083-3870'},
 {'name': 'Helena Møgelbjerg Ditzel',
  'title': {'en': 'MD, PhD, Postdoctoral Researcher', 'da': 'Læge, ph.d., postdoc'},
  'bio': {'en': 'Clinician-researcher working on health-related quality of life, patient-reported outcomes and psychometric validation in hematology and '
                'oncology, with a focus on multiple myeloma, autoimmune cytopenias and frailty in older adults. Project manager of the REMNANT-PRO study and '
                'principal investigator of the PROGNOSIS-G8 cohort study. PhD in geriatric oncology from the University of Southern Denmark (2025) and board '
                'member of the Danish Society of Geriatric Oncology.',
          'da': 'Klinisk forsker, der arbejder med helbredsrelateret livskvalitet, patientrapporterede oplysninger og psykometrisk validering inden for '
                'hæmatologi og onkologi med fokus på myelomatose, autoimmune cytopenier og skrøbelighed hos ældre. Projektleder for REMNANT-PRO-studiet og '
                'forsøgsansvarlig for kohortestudiet PROGNOSIS-G8. Ph.d. i geriatrisk onkologi fra Syddansk Universitet (2025) og bestyrelsesmedlem i Dansk '
                'Selskab for Geriatrisk Onkologi.'},
  'email': '',
  'photo': 'helena-ditzel.jpg',
  'profile': 'https://portal.findresearcher.sdu.dk/en/persons/hmditzel/',
  'orcid': '0000-0002-9435-0524'},
 {'name': 'Tine Rosenberg',
  'title': {'en': 'Project Coordinator', 'da': 'Projektkoordinator'},
  'bio': {'en': 'Research coordinator and project manager (MSc in Health Science) at the Hematology Research Unit and QoLRC, Odense University Hospital. Her '
                'research focuses on home-based treatment and digital patient-reported outcomes in multiple myeloma, including home-administered daratumumab '
                'and digital symptom reporting before treatment, and she has contributed to the Danish translation and validation of several questionnaires, '
                'including the SSQ-MM. From 2026 she is a PhD fellow in the national Treat@Home program, studying home-based daratumumab treatment across '
                'Danish hematology departments.',
          'da': 'Forskningskoordinator og projektleder (cand.scient.san.) ved Hæmatologisk Forskningsenhed og QoLRC, Odense Universitetshospital. Hendes '
                'forskning fokuserer på hjemmebehandling og digitale patientrapporterede oplysninger ved myelomatose, herunder daratumumab givet i eget hjem '
                'og digital symptomrapportering før behandling, og hun har bidraget til dansk oversættelse og validering af flere spørgeskemaer, herunder '
                'SSQ-MM. Fra 2026 er hun ph.d.-studerende i det nationale Treat@Home-program, hvor hun undersøger hjemmebehandling med daratumumab på tværs af '
                'danske hæmatologiske afdelinger.'},
  'email': '',
  'photo': 'tine-rosenberg.jpg',
  'profile': 'https://portal.findresearcher.sdu.dk/en/persons/tinerosenberg/',
  'orcid': '0000-0002-7874-5526'},
 {'name': 'Pia K. Pedersen',
  'title': {'en': 'Daily Manager and Chief Nurse', 'da': 'Daglig leder og oversygeplejerske'},
  'bio': {'en': 'Daily manager of the Hematology Research Unit at Odense University Hospital and the University of Southern Denmark. She is responsible for '
                "the unit's day-to-day management and administration and supports researchers and research projects across the unit, including QoLRC.",
          'da': 'Daglig leder af Hæmatologisk Forskningsenhed på Odense Universitetshospital og Syddansk Universitet. Hun har ansvaret for enhedens daglige '
                'drift og administration og understøtter forskere og forskningsprojekter på tværs af enheden, herunder QoLRC.'},
  'email': '',
  'photo': 'pia-pedersen.jpg',
  'profile': ''},
 {'name': 'Madeleine King',
  'title': {'en': 'PhD, Adjunct Professor', 'da': 'Ph.d., adjungeret professor'},
  'bio': {'en': 'Professor at the University of Sydney and adjunct professor at the University of Southern Denmark and the Hematology Research Unit. An '
                'internationally leading researcher in health-related quality of life and patient-reported outcome measures, she has helped set standards for '
                "using PRO measures in clinical trials, and received the ISOQOL President's Award in 2022.",
          'da': 'Professor ved University of Sydney og adjungeret professor ved Syddansk Universitet og Hæmatologisk Forskningsenhed. Hun er en internationalt '
                'førende forsker i helbredsrelateret livskvalitet og patientrapporterede måleinstrumenter, har bidraget til standarder for brug af PRO i '
                "kliniske forsøg og modtog ISOQOL's President's Award i 2022."},
  'email': '',
  'photo': 'madeleine-king.jpg',
  'profile': ''},
 {'name': 'Sören Möller',
  'title': {'en': 'PhD, Professor of Translational Biostatistics', 'da': 'Ph.d., professor i translationel biostatistik'},
  'bio': {'en': 'Professor of translational biostatistics at Epidemiology, Biostatistics and Biodemography, Department of Public Health, University of '
                'Southern Denmark, and previously biostatistician at OPEN, Odense University Hospital. His work focuses on applying and developing advanced '
                'statistical methods in health research and clinical epidemiology, and he collaborates with QoLRC on the statistical analysis of quality of '
                'life data.',
          'da': 'Professor i translationel biostatistik ved Epidemiologi, Biostatistik og Biodemografi, Institut for Sundhedstjenesteforskning, Syddansk Universitet, '
                'og tidligere biostatistiker ved OPEN, Odense Universitetshospital. Hans arbejde handler om at anvende og udvikle avancerede statistiske '
                'metoder i sundhedsforskning og klinisk epidemiologi, og han samarbejder med QoLRC om statistisk analyse af livskvalitetsdata.'},
  'email': '',
  'photo': 'soren-moller.jpg',
  'profile': '',
  'orcid': '0000-0003-0858-4269'},
 {'name': 'Anne Møller Clausen',
  'title': {'en': 'RN, MSc in Clinical Nursing, PhD Student', 'da': 'Sygeplejerske, cand.cur., ph.d.-studerende'},
  'bio': {'en': 'Registered nurse with an MSc in Clinical Nursing and PhD student at the Department of Hematology, Odense University Hospital. Her PhD '
                'project, AmyCare, focuses on supportive care for patients with AL amyloidosis.',
          'da': 'Sygeplejerske, cand.cur. og ph.d.-studerende på Hæmatologisk Afdeling, Odense Universitetshospital. Hendes ph.d.-projekt, AmyCare, handler om '
                'understøttende behandling til patienter med AL-amyloidose.'},
  'email': '',
  'photo': 'anne-moller-clausen.jpg',
  'profile': ''},
 {'name': 'Nina Andersen',
  'title': {'en': 'MD, PhD Student', 'da': 'Læge, ph.d.-studerende'},
  'bio': {'en': 'Medical doctor and PhD student at the Hematology Research Unit. Her research investigates adding comprehensive geriatric assessment to '
                'standard care for older patients with frailty and hematologic cancer.',
          'da': 'Læge og ph.d.-studerende ved Hæmatologisk Forskningsenhed. Hendes forskning undersøger, om en geriatrisk helbredsvurdering som supplement til '
                'standardbehandling gavner ældre, skrøbelige patienter med hæmatologisk kræft.'},
  'email': '',
  'photo': 'nina-andersen.jpg',
  'profile': ''},
 {'name': 'Klara Rydahl',
  'title': {'en': 'MD, PhD Student', 'da': 'Læge, ph.d.-studerende'},
  'bio': {'en': 'Medical doctor and PhD student at the Hematology Research Unit. Her research focuses on frailty and quality of life in patients with '
                'multiple myeloma, using real-world data from the QoL-MM study. Her first study, published in the British Journal of Haematology, '
                'showed that frail patients have clinically relevant lower quality of life and physical functioning than fit patients.',
          'da': 'Læge og ph.d.-studerende ved Hæmatologisk Forskningsenhed. Hun forsker i skrøbelighed og livskvalitet hos patienter med myelomatose '
                'med udgangspunkt i real-world-data fra QoL-MM-studiet. Hendes første studie, publiceret i British Journal of Haematology, viste, at '
                'skrøbelige patienter har klinisk relevant lavere livskvalitet og fysisk funktion end fitte patienter.'},
  'email': '',
  'photo': 'klara-rydahl.jpg',
  'profile': ''},
 {'name': 'Tina Käehne',
  'title': {'en': 'Finance', 'da': 'Økonomi'},
  'bio': {'en': 'Responsible for finances at QoLRC and the Hematology Research Unit. TODO(Tina to check and add a sentence.)',
          'da': 'Ansvarlig for økonomi i QoLRC og Hæmatologisk Forskningsenhed. TODO(Tina tjekker og tilføjer en sætning.)'},
  'email': '',
  'photo': 'tina-kaehne.jpg',
  'profile': ''}]

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
        "name": {"en": "Nordic Myeloma Study Group (NMSG)", "da": "Nordic Myeloma Study Group (NMSG)"},
        "text": {"en": "Collaborative group for clinical myeloma research in Norway, Sweden, Finland, Estonia, Iceland and Denmark. QoLRC is the group's core facility for quality of life research in clinical protocols.", "da": "Samarbejdsgruppe for klinisk myelomatoseforskning i Norge, Sverige, Finland, Estland, Island og Danmark. QoLRC er gruppens core facility for forskning i livskvalitet i kliniske protokoller."},
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
        "name": {"en": "OPEN, Open Patient data Explorative Network", "da": "OPEN, Open Patient data Explorative Network"},
        "text": {"en": "Data management and biostatistics, including our collaboration with Professor Sören Möller, Department of Public Health, University of Southern Denmark.", "da": "Datahåndtering og biostatistik, herunder vores samarbejde med professor Sören Möller, Institut for Sundhedstjenesteforskning, Syddansk Universitet."},
        "url": "",
        "country": {"en": "Denmark", "da": "Danmark"},
    },
]

SPONSORS_HEADING = {"en": "Our funders", "da": "Vores bevillingsgivere"}
SPONSORS_INTRO = {"en": "Our research is made possible by grants from these foundations and organizations.",
                  "da": "Vores forskning er muliggjort af bevillinger fra disse fonde og organisationer."}
# logo: file name in assets/img/sponsors/ (PNG or SVG). Without a logo file the name is shown instead.
SPONSORS = [
    {"name": "Kræftens Bekæmpelse", "url": "https://www.cancer.dk/", "logo": "kraeftens-bekaempelse.png"},
    {"name": "Stiftelsen Dam", "url": "https://dam.no/", "logo": "stiftelsen-dam.png"},
    {"name": "Sygeforsikring danmark", "url": "https://www.sygeforsikring.dk/", "logo": "sygeforsikring-danmark.png"},
]

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


# ---------------------------------------------------------------- News & events
# Newest posts are shown first, and the three newest also appear on the homepage.
# To add a post: put a photo in assets/img/news/ and add an entry at the top of this list.
# date: YYYY-MM-DD. photo: file name in assets/img/news/ (or ""). link: optional web address.
NEWS_INTRO = {
    "en": "Meetings, conferences and presentations from QoLRC.",
    "da": "Møder, konferencer og præsentationer fra QoLRC.",
}

NEWS = [
    {"date": "2026-10-19",
     "title": {"en": "SSQ-MM validation study presented at ISOQOL 2026 in Prague",
               "da": "SSQ-MM-valideringsstudiet præsenteret på ISOQOL 2026 i Prag"},
     "text": {"en": "Helena Møgelbjerg Ditzel presented a poster on the multinational psychometric validation of the Steroid Symptom Questionnaire – Multiple Myeloma (SSQ-MM) in patients with immune thrombocytopenia (ITP) and autoimmune hemolytic anemia (AIHA) at the 33rd Annual Conference of the International Society for Quality of Life Research (ISOQOL) in Prague. The study will include 180 patients in Denmark, Norway, Sweden and the United Kingdom, and will also develop a Swedish version of the questionnaire.",
              "da": "Helena Møgelbjerg Ditzel præsenterede en poster om den multinationale psykometriske validering af Steroid Symptom Questionnaire – Multiple Myeloma (SSQ-MM) hos patienter med immun trombocytopeni (ITP) og autoimmun hæmolytisk anæmi (AIHA) på den 33. årlige konference i International Society for Quality of Life Research (ISOQOL) i Prag. Studiet skal inkludere 180 patienter i Danmark, Norge, Sverige og Storbritannien og udvikler desuden en svensk version af spørgeskemaet."},
     "photo": "helena-isoqol-2026.jpg", "link": "https://www.isoqol.org/events/33rd-annual-conference/"},
    {"date": "2026-09-10",
     "title": {"en": "Quality of life results from the SABLe study presented at the NMSG meeting in Reykjavik",
               "da": "Livskvalitetsresultater fra SABLe-studiet præsenteret på NMSG-mødet i Reykjavik"},
     "text": {"en": "Tine Rosenberg presented the patient-reported outcome results from the phase II SABLe study (NMSG 29/21) at the Nordic Myeloma Study Group meeting in Reykjavik. The study tested an alternating selinexor-based regimen in patients with newly diagnosed multiple myeloma who are not eligible for stem cell transplantation, and patients reported improved quality of life.",
              "da": "Tine Rosenberg præsenterede resultaterne for patientrapporterede oplysninger fra fase II-studiet SABLe (NMSG 29/21) på Nordic Myeloma Study Groups møde i Reykjavik. Studiet afprøvede et alternerende selinexor-baseret behandlingsregime hos patienter med nydiagnosticeret myelomatose, som ikke kan tilbydes stamcelletransplantation, og patienterne rapporterede forbedret livskvalitet."},
     "photo": "tine-nmsg-2026.jpg", "link": "https://www.nordicmyeloma.org/",
     "gallery": [
         {"file": "helena-lene-reykjavik.jpg", "full": "helena-lene-reykjavik-full.jpg",
          "alt": {"en": "Helena Møgelbjerg Ditzel and Lene Kongsgaard Nielsen in front of Hallgrímskirkja in Reykjavik",
                  "da": "Helena Møgelbjerg Ditzel og Lene Kongsgaard Nielsen foran Hallgrímskirkja i Reykjavik"}},
         {"file": "helena-tine-reykjavik.jpg", "full": "helena-tine-reykjavik-full.jpg",
          "alt": {"en": "Helena Møgelbjerg Ditzel and Tine Rosenberg at the Gullfoss waterfall",
                  "da": "Helena Møgelbjerg Ditzel og Tine Rosenberg ved vandfaldet Gullfoss"}},
     ]},
    {"date": "2026-04-17",
     "title": {"en": "QoLRC at the Nordic ITP meeting in Oslo",
               "da": "QoLRC til det nordiske ITP-møde i Oslo"},
     "text": {"en": "At the Nordic ITP meeting in Oslo on 17–18 April 2026, Henrik Frederiksen presented a case of acquired amegakaryocytic thrombocytopenia after treatment with an immune checkpoint inhibitor as part of neoadjuvant treatment for bilateral breast cancer (BMJ Case Reports, 2025). Helena Møgelbjerg Ditzel presented the SSQ-MM validation study in patients with ITP and AIHA.",
              "da": "På det nordiske ITP-møde i Oslo den 17.–18. april 2026 præsenterede Henrik Frederiksen et tilfælde af erhvervet amegakaryocytær trombocytopeni efter behandling med en immun checkpoint-hæmmer som led i neoadjuverende behandling for bilateral brystkræft (BMJ Case Reports, 2025). Helena Møgelbjerg Ditzel præsenterede SSQ-MM-valideringsstudiet hos patienter med ITP og AIHA."},
     "photo": "henrik-nordic-itp-2026.jpg", "link": "https://nordicitp.com/"},
    {"date": "2026-10-28",
     "title": {"en": "Research in Focus at the Department of Hematology",
               "da": "Forskning i fokus på Hæmatologisk Afdeling"},
     "text": {"en": "Colleagues from across the Department of Hematology at Odense University Hospital gathered for the annual Research in Focus (Forskning i fokus) afternoon, organized by Henrik Frederiksen. The program covered acute leukemia and hematopathology, lymphoma and cellular therapies, multiple myeloma and amyloidosis, home-based treatment and supportive care, quality of life and population-based research, and benign hematology and frailty. Hans Henrik Knudsen, who is a patient representative in Lene Kongsgaard Nielsen's quality of life research at QoLRC, spoke about the role of patient involvement in research. From QoLRC, Henrik Frederiksen, Pia Pedersen, Tine Rosenberg, Anne Møller Clausen and Klara Rydahl presented their work.",
              "da": "Kolleger fra hele Hæmatologisk Afdeling på Odense Universitetshospital samledes til den årlige eftermiddag Forskning i fokus, som Henrik Frederiksen stod for. Programmet omfattede akut leukæmi og hæmatopatologi, lymfom og cellulære terapier, myelomatose og amyloidose, hjemmebehandling og understøttende behandling, livskvalitet og populationsbaseret forskning samt benign hæmatologi og skrøbelighed. Hans Henrik Knudsen, som er patientrepræsentant i Lene Kongsgaard Nielsens livskvalitetsforskning i QoLRC, fortalte om betydningen af patientinddragelse i forskningen. Fra QoLRC præsenterede Henrik Frederiksen, Pia Pedersen, Tine Rosenberg, Anne Møller Clausen og Klara Rydahl deres arbejde."},
     "photo": "forskning-i-fokus-2026.jpg", "link": ""},
    {"date": "2026-10-01",
     "title": {"en": "Funding from Stiftelsen Dam for the REMNANT quality of life sub-study",
               "da": "Bevilling fra Stiftelsen Dam til REMNANT-studiets livskvalitetsdel"},
     "text": {"en": "The patient-reported outcome sub-study of REMNANT has received funding from the Norwegian foundation Stiftelsen Dam, through the Norwegian Blood Cancer Society (Blodkreftforeningen). REMNANT is a Nordic randomized trial led by Oslo University Hospital, in which treatment of newly diagnosed multiple myeloma is guided by measurable residual disease. The grant supports the quality of life analyses in part 2 of the study, which are carried out at QoLRC and led by Helena Møgelbjerg Ditzel.",
              "da": "REMNANT-studiets delstudie om patientrapporterede oplysninger har fået støtte fra den norske fond Stiftelsen Dam gennem den norske blodkræftforening (Blodkreftforeningen). REMNANT er et nordisk randomiseret forsøg ledet af Oslo universitetssykehus, hvor behandlingen af nydiagnosticeret myelomatose styres af målbar restsygdom. Bevillingen støtter livskvalitetsanalyserne i studiets del 2, som udføres i QoLRC og ledes af Helena Møgelbjerg Ditzel."},
     "photo": "", "link": "https://dam.no/"},
]
