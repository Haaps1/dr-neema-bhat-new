"""Builds the static pages from shared parts.

Run:  python3 build.py
Edit shared pieces (header, menu, footer, services list) here, then rebuild.
The generated .html files are what gets published.
"""
from pathlib import Path

ROOT = Path(__file__).parent
PHONE_DISPLAY = "+91 78997 56677"
PHONE_TEL = "+917899756677"
WA = "https://wa.me/917899756677"

# name, slug, category, short description
SERVICES = [
    ("Anaemia Treatment", "anaemia", "Hematology", "Iron-deficiency, nutritional and inherited anaemias — finding the cause, not just treating the count."),
    ("Thalassemia Treatment", "thalassemia", "Hematology", "Transfusion programmes, iron chelation and evaluation for curative transplant."),
    ("Hemophilia & Bleeding Disorders", "hemophilia", "Hematology", "Diagnosis and long-term management of hemophilia, von Willebrand disease and low platelets."),
    ("Leukaemia (Blood Cancer)", "leukaemia", "Hematology", "Acute and chronic leukaemias, with chemotherapy, targeted therapy and transplant planning."),
    ("Lymphoma & Myeloma", "lymphoma-myeloma", "Hematology", "Accurate subtyping and tailored treatment for Hodgkin, non-Hodgkin lymphoma and myeloma."),
    ("Childhood Leukaemia & Lymphoma", "childhood-leukaemia", "Pediatric", "Child-centred treatment with close attention to comfort, growth and schooling."),
    ("Pediatric Solid Tumours", "pediatric-tumours", "Pediatric", "Neuroblastoma, Wilms tumour, sarcomas and more, with a multidisciplinary team."),
    ("Pediatric Blood Disorders", "pediatric-blood", "Pediatric", "Sickle cell disease, aplastic anaemia, ITP and immune disorders in children."),
    ("Bone Marrow Transplant", "bone-marrow-transplant", "Pediatric & Adult", "Autologous and allogeneic transplants for children and adults, from donor matching to follow-up."),
]
BMT_PAGE = "bone-marrow-transplant.html"


def svc_href(slug):
    return BMT_PAGE if slug == "bone-marrow-transplant" else f"index.html#svc-{slug}"


ICONS = """
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <symbol id="i-phone" viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></symbol>
  <symbol id="i-wa" viewBox="0 0 24 24"><path d="M4 20l1.3-4A8 8 0 1 1 8 18.7L4 20z"/><path d="M9 9.5c.3 2 2.3 4.3 5 5l1.2-1.3-1.8-1-1 .8c-1-.4-1.8-1.2-2.2-2.2l.8-1-1-1.8L9 9.5z"/></symbol>
  <symbol id="i-pin" viewBox="0 0 24 24"><path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></symbol>
  <symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></symbol>
  <symbol id="i-cal" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/></symbol>
  <symbol id="i-go" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
  <symbol id="i-chev" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></symbol>
  <symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 8h16M4 16h10"/></symbol>
  <symbol id="i-check" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></symbol>
  <symbol id="i-drop" viewBox="0 0 24 24"><path d="M12 3c3 4.2 6 7.4 6 11a6 6 0 0 1-12 0c0-3.6 3-6.8 6-11z"/></symbol>
  <symbol id="i-child" viewBox="0 0 24 24"><circle cx="12" cy="7" r="3.5"/><path d="M5 21c0-4 3-7 7-7s7 3 7 7"/></symbol>
  <symbol id="i-adult" viewBox="0 0 24 24"><circle cx="12" cy="6.5" r="3"/><path d="M6 21v-5a6 6 0 0 1 12 0v5"/></symbol>
  <symbol id="i-award" viewBox="0 0 24 24"><circle cx="12" cy="9" r="6"/><path d="M8.5 14l-1.5 7 5-3 5 3-1.5-7"/></symbol>
  <symbol id="i-marrow" viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><circle cx="12" cy="12" r="8"/><path d="M12 1v3M12 20v3M1 12h3M20 12h3"/></symbol>
  <symbol id="i-hosp" viewBox="0 0 24 24"><path d="M4 21V7l8-4 8 4v14"/><path d="M9 21v-5h6v5M12 8v5M9.5 10.5h5"/></symbol>
  <symbol id="i-cells" viewBox="0 0 24 24"><circle cx="8" cy="9" r="4"/><circle cx="16" cy="15" r="4"/><circle cx="17" cy="6" r="2"/></symbol>
  <symbol id="i-shield" viewBox="0 0 24 24"><path d="M12 3l7 3v6c0 4.5-3 7.8-7 9-4-1.2-7-4.5-7-9V6l7-3z"/><path d="M9 12l2 2 4-4"/></symbol>
  <symbol id="i-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></symbol>
  <symbol id="i-moon" viewBox="0 0 24 24"><path d="M20 14.5A8 8 0 0 1 9.5 4 8 8 0 1 0 20 14.5z"/></symbol>
  <symbol id="i-car" viewBox="0 0 24 24"><path d="M5 16l1.5-5h11L19 16"/><rect x="3" y="16" width="18" height="4" rx="1.5"/><path d="M6 11l1.5-4h9L18 11"/></symbol>
  <symbol id="i-doc" viewBox="0 0 24 24"><rect x="5" y="3" width="14" height="18" rx="3"/><path d="M9 8h6M9 12h6M9 16h3"/></symbol>
</defs></svg>"""


def head(title, desc, canonical, extra=""):
    return f"""<!doctype html>
<html lang="en-IN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#081536">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <link rel="canonical" href="https://drneemabhat.com/{canonical}">
  <link rel="manifest" href="manifest.webmanifest">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="https://drneemabhat.com/assets/images/portrait-scrubs-720.webp">
  <script>document.documentElement.classList.add('js');</script>
  <link rel="icon" type="image/png" href="assets/images/logo-mark.png">
  <link rel="apple-touch-icon" href="assets/images/logo-mark.png">
  <link rel="preload" href="assets/fonts/poppins-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="assets/fonts/roboto-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="assets/css/styles.css">
{extra}</head>"""


def appbar(active, dark=True):
    def cur(p):
        return ' aria-current="page"' if p == active else ""
    hema = "".join(f'<a href="{svc_href(s)}" data-svc="{s}"><b>{n}</b><svg class="ic"><use href="#i-go"/></svg></a>' for n, s, c, _ in SERVICES if c == "Hematology")
    ped = "".join(f'<a href="{svc_href(s)}" data-svc="{s}"><b>{n}</b><svg class="ic"><use href="#i-go"/></svg></a>' for n, s, c, _ in SERVICES if c == "Pediatric")
    sheet_h = "".join(f'<a href="{svc_href(s)}">{n}</a>' for n, s, c, _ in SERVICES if c == "Hematology")
    sheet_p = "".join(f'<a href="{svc_href(s)}">{n}</a>' for n, s, c, _ in SERVICES if c == "Pediatric")
    sheet_p += f'<a href="{BMT_PAGE}"><b>Bone Marrow Transplant</b></a>'
    return f"""
  <a class="skip" href="#main">Skip to main content</a>
  <div class="curtain" aria-hidden="true"><img src="assets/images/logo-mark.png" alt=""></div>
  <div class="cursor" aria-hidden="true"></div><div class="cursor-dot" aria-hidden="true"></div>

  <header class="appbar{' on-dark' if dark else ''}">
    <div class="wrap appbar__in">
      <a class="brand" href="index.html" aria-label="Dr. Neema Bhat — home"><img src="assets/images/logo.png" alt="Dr. Neema Bhat, Hematologist and Pediatric Oncologist" width="928" height="275"></a>
      <nav aria-label="Primary">
        <ul class="menu">
          <li><a href="index.html"{cur('home')}>Home</a></li>
          <li><a href="about.html"{cur('about')}>About</a></li>
          <li class="has-drop">
            <button type="button" aria-expanded="false" aria-controls="drop-services"{' aria-current="page"' if active == 'service' else ''}>Services<svg class="ic chev"><use href="#i-chev"/></svg></button>
            <div class="drop" id="drop-services">
              <div class="drop__col"><h3>Hematology</h3>{hema}</div>
              <div class="drop__col"><h3>Pediatric</h3>{ped}</div>
              <a class="drop__feat" href="{BMT_PAGE}"><svg class="ic" style="font-size:1.6rem;color:var(--teal)"><use href="#i-marrow"/></svg><span><small>Specialty</small>Bone Marrow Transplant</span><svg class="ic" style="margin-left:auto"><use href="#i-go"/></svg></a>
            </div>
          </li>
          <li><a href="contact.html"{cur('contact')}>Contact</a></li>
        </ul>
      </nav>
      <a class="btn btn--teal appbar__cta" href="contact.html">Book Appointment<svg class="ic ic--go"><use href="#i-go"/></svg></a>
      <div class="appbar__icons">
        <a class="appbar__icon" href="tel:{PHONE_TEL}" aria-label="Call {PHONE_DISPLAY}"><svg class="ic"><use href="#i-phone"/></svg></a>
        <button class="appbar__icon" type="button" data-sheet-open aria-label="Open menu" aria-controls="sheet" aria-expanded="false"><svg class="ic"><use href="#i-menu"/></svg></button>
      </div>
    </div>
  </header>

  <div class="sheet" id="sheet" aria-hidden="true">
    <div class="sheet__scrim" data-sheet-close></div>
    <div class="sheet__panel" role="dialog" aria-modal="true" aria-label="Menu">
      <div class="sheet__grab"></div>
      <ul class="sheet__nav">
        <li><a href="index.html"{cur('home')}>Home<svg class="ic"><use href="#i-go"/></svg></a></li>
        <li><a href="about.html"{cur('about')}>About<svg class="ic"><use href="#i-go"/></svg></a></li>
        <li><button type="button" data-acc aria-expanded="false">Services<svg class="ic chev"><use href="#i-chev"/></svg></button>
          <div class="sheet__sub"><div><small>Hematology</small>{sheet_h}<small>Pediatric</small>{sheet_p}</div></div></li>
        <li><a href="contact.html"{cur('contact')}>Contact<svg class="ic"><use href="#i-go"/></svg></a></li>
      </ul>
      <div class="sheet__actions">
        <a class="btn btn--line" href="tel:{PHONE_TEL}"><svg class="ic"><use href="#i-phone"/></svg>Call</a>
        <a class="btn btn--navy" href="contact.html"><svg class="ic"><use href="#i-cal"/></svg>Book</a>
      </div>
    </div>
  </div>
"""


def footer(fab=True):
    links = "".join(f'<li><a href="{svc_href(s)}">{n}</a></li>' for n, s, c, _ in SERVICES[:5])
    links2 = "".join(f'<li><a href="{svc_href(s)}">{n}</a></li>' for n, s, c, _ in SERVICES[5:])
    return f"""
  <footer class="foot">
    <div class="wrap">
      <p class="foot__big" data-fx="wipe">Let’s talk about<br>your care. <a href="contact.html">Book<svg class="ic"><use href="#i-go"/></svg></a></p>
      <div class="foot__grid">
        <div>
          <img class="foot__logo" src="assets/images/logo.png" alt="Dr. Neema Bhat" width="928" height="275" loading="lazy">
          <p>Hematologist, Pediatric Oncologist and Bone Marrow Transplant specialist in Bangalore.</p>
          <ul style="margin-top:18px">
            <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
            <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></li>
            <li>Apollo Hospitals, Bannerghatta Road</li>
          </ul>
        </div>
        <div><h2>Pages</h2><ul><li><a href="index.html">Home</a></li><li><a href="about.html">About</a></li><li><a href="{BMT_PAGE}">Bone Marrow Transplant</a></li><li><a href="contact.html">Contact</a></li></ul></div>
        <div><h2>Hematology</h2><ul>{links}</ul></div>
        <div><h2>Pediatric</h2><ul>{links2}</ul></div>
      </div>
      <div class="foot__base"><p>© <span data-year>2026</span> Dr. Neema Bhat. All rights reserved.</p><p>Information on this website is for general awareness and is not a substitute for medical advice.</p></div>
    </div>
  </footer>

  {'<a class="fab" href="contact.html">' if fab else '<a class="fab" href="#wizard">'}<svg class="ic"><use href="#i-cal"/></svg>Book</a>
  <dialog class="lb" id="lb" aria-label="Photo viewer"><button class="lb__x" type="button" aria-label="Close">×</button><button class="lb__nav lb__nav--p" type="button" aria-label="Previous">‹</button><figure><img src="" alt=""><figcaption></figcaption></figure><button class="lb__nav lb__nav--n" type="button" aria-label="Next">›</button></dialog>
  <script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def lit_words(text):
    """Wrap each word in a span so it can light up on scroll; *word* is highlighted in teal."""
    out = []
    for w in text.split():
        teal = w.startswith("*") and w.rstrip(".,—").endswith("*")
        clean = w.replace("*", "")
        out.append(f'<span class="w{" w--teal" if teal else ""}">{clean}</span>')
    return " ".join(out)


def ticker(items):
    row = "".join(f"<span>{t}</span>" for t in items)
    return f'<div class="ticker" aria-hidden="true"><div class="ticker__track">{row}{row}</div></div>'


LD_PHYSICIAN = """  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"Physician","name":"Dr. Neema Bhat","description":"Hematologist, Pediatric Oncologist and Bone Marrow Transplant specialist in Bangalore.","url":"https://drneemabhat.com/","image":"https://drneemabhat.com/assets/images/portrait-scrubs.webp","telephone":"+91-78997-56677","medicalSpecialty":["Hematologic","Oncologic","Pediatric"],"alumniOf":{"@type":"Hospital","name":"Penn State Health"},
   "hospitalAffiliation":[{"@type":"Hospital","name":"Apollo Hospitals, Bannerghatta Road"},{"@type":"Hospital","name":"Apollo One & Apollo Cradle, Electronic City"},{"@type":"Hospital","name":"Bhagawan Mahaveer Jain Hospital"}],
   "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"11:00","closes":"16:00","description":"OPD — Apollo Hospitals, Bannerghatta Road"},{"@type":"OpeningHoursSpecification","dayOfWeek":"Friday","opens":"14:00","closes":"16:00","description":"Apollo One & Apollo Cradle, Hosa Road, Electronic City"},{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"17:00","closes":"19:00","description":"Therapy Clinic"}],
   "address":{"@type":"PostalAddress","addressLocality":"Bengaluru","addressRegion":"Karnataka","addressCountry":"IN"},"areaServed":"Bangalore"}
  </script>
"""

# ------------------------------------------------------------------ HOME
def home():
    cards = []
    for i, (n, s, c, d) in enumerate(SERVICES):
        feat = s == "bone-marrow-transplant"
        cards.append(f"""
          <a class="scard{' scard--feat' if feat else ''}" id="svc-{s}" href="{BMT_PAGE if feat else 'contact.html?topic=' + s}" style="--i:{i}">
            <span class="scard__n">{i + 1:02d}</span>
            <div><span class="scard__cat">{c}</span><h3>{n}{'<span class="scard__pill">Specialty</span>' if feat else ''}</h3></div>
            <p>{d}</p>
            <span class="scard__go" aria-hidden="true"><svg class="ic"><use href="#i-go"/></svg></span>
          </a>""")
    shots = [
        ("young-patient-care-team", "With a young patient and the care team", False),
        ("with-patients", "With patients after a follow-up visit", True),
        ("pediatric-tumour-care-ethiopia", "Pediatric tumour care programme, Ethiopia · 2025", False),
        ("conference-mumbai-hematology-group", "Mumbai Hematology Group mid-term conference · 2025", False),
        ("conference-bengaluru-physicians-update", "Bengaluru Physicians Update-4 · August 2025", False),
    ]
    alts = {
        "young-patient-care-team": "Dr. Neema Bhat with the nursing and care team beside a young patient in a hospital room",
        "with-patients": "Dr. Neema Bhat standing with two smiling patients at the hospital",
        "pediatric-tumour-care-ethiopia": "Dr. Neema Bhat with doctors at a programme to improve pediatric tumour care in Ethiopia",
        "conference-mumbai-hematology-group": "Dr. Neema Bhat with fellow delegates at the Mumbai Hematology Group mid-term conference",
        "conference-bengaluru-physicians-update": "Dr. Neema Bhat with speakers at Bengaluru Physicians Update-4",
    }
    rail = "".join(f"""
          <figure class="shot{' shot--tall' if tall else ''}" data-fx="iris" style="--d:{k * 0.08:.2f}s">
            <button class="shot__img" type="button" data-full="assets/images/gallery/{f}.webp" data-cap="{cap}"><img src="assets/images/gallery/{f}-760.webp" alt="{alts[f]}" loading="lazy" decoding="async" draggable="false"></button>
            <p><b>{k + 1:02d}</b>{cap}</p>
          </figure>""" for k, (f, cap, tall) in enumerate(shots))
    statement = ("A decade of *dedicated* *hematology-oncology* care — clear conversations, careful diagnosis and "
                 "treatment plans built around each *child* and *adult*, not a one-size-fits-all protocol.")
    return head("Dr. Neema Bhat | Hematologist & Pediatric Oncologist in Bangalore",
                "Dr. Neema Bhat is a Hematologist and Pediatric Oncologist in Bangalore offering specialist care for blood disorders, childhood cancers and bone marrow transplantation.",
                "", LD_PHYSICIAN) + f"""
<body data-page="home">{ICONS}{appbar('home')}
  <main id="main">
    <section class="hero" data-glow aria-labelledby="hero-title">
      <div class="hero__grid" aria-hidden="true"></div>
      <div class="hero__glow" aria-hidden="true"></div>
      <div class="wrap hero__in">
        <div class="hero__copy">
          <p class="tag tag--light" data-fx="wipe-x">Hematology · Pediatric Oncology · BMT</p>
          <h1 id="hero-title" class="hero__title">
            <span class="sr-only">Best Hematologist, Pediatrician and Bone Marrow Transplant Specialist in Bangalore</span>
            <span aria-hidden="true"><span class="l" data-fx="wipe" style="--d:.1s">Best</span><span class="l" data-fx="wipe" style="--d:.2s"><span class="scramble" data-scramble="Hematologist|Pediatrician|BMT Specialist">Hematologist</span></span><span class="l" data-fx="wipe" style="--d:.3s">in Bangalore</span></span>
          </h1>
          <p class="hero__sub" data-fx="fade" style="--d:.5s">Dr. Neema Bhat is a US-trained Haemato-Oncologist caring for children and adults with blood disorders and blood cancers — and Head of the Bone Marrow Transplant Unit at Bhagawan Mahaveer Jain Hospital.</p>
          <div class="hero__acts" data-fx="fade" style="--d:.65s">
            <a class="btn btn--teal magnet" href="contact.html">Book an Appointment<span class="btn__dot"><svg class="ic ic--go"><use href="#i-go"/></svg></span></a>
            <a class="btn btn--ghost magnet" href="tel:{PHONE_TEL}"><svg class="ic"><use href="#i-phone"/></svg>{PHONE_DISPLAY}</a>
          </div>
        </div>
        <div class="hero__art" data-fx="iris" style="--d:.2s" data-tilt-scene>
          <div class="arch"><img src="assets/images/portrait-scrubs.webp" srcset="assets/images/portrait-scrubs-720.webp 720w, assets/images/portrait-scrubs.webp 1200w" sizes="(max-width: 900px) 80vw, 470px" alt="Dr. Neema Bhat in a white coat over blue scrubs, arms folded" width="1200" height="1873" fetchpriority="high"></div>
          <div class="badge" aria-hidden="true">
            <svg viewBox="0 0 132 132"><defs><path id="circ" d="M66,66 m-50,0 a50,50 0 1,1 100,0 a50,50 0 1,1 -100,0"/></defs><text><textPath href="#circ">MD USA · FAAP · Penn State Health ·</textPath></text></svg>
            <b>10+<small>YEARS</small></b>
          </div>
          <div class="hero__meta"><strong>Dr. Neema Bhat</strong><span>Haemato-Oncologist &amp; BMT Physician</span></div>
        </div>
      </div>
      {ticker(["Anaemia", "Thalassemia", "Hemophilia", "Leukaemia", "Lymphoma &amp; Myeloma", "Childhood Cancers", "Pediatric Solid Tumours", "Bone Marrow Transplant"])}
    </section>

    <section class="block" aria-labelledby="st-title">
      <div class="wrap statement">
        <p class="tag" id="st-title">Approach</p>
        <div>
          <p class="statement__text" data-lit>{lit_words(statement)}</p>
          <div class="statement__foot" data-fx="fade">
            <div class="sig"><img src="assets/images/portrait-coat-720.webp" alt="" width="56" height="56" loading="lazy"><div><strong>Dr. Neema Bhat</strong><span>MD (USA) · FAAP · HOD, BMT Unit</span></div></div>
            <a class="btn btn--line magnet" href="about.html">Her story<svg class="ic ic--go"><use href="#i-go"/></svg></a>
          </div>
        </div>
      </div>
    </section>

    <section class="block block--soft" id="services" aria-labelledby="svc-title">
      <div class="wrap">
        <div class="svc-head">
          <div><p class="tag" data-fx="wipe-x">Services</p><h2 class="title" id="svc-title" data-fx="wipe">Best <em>Hematologist</em> in Bangalore</h2></div>
          <p class="lead" data-fx="fade" style="max-width:420px">Nine specialist services across adult hematology and pediatric hemato-oncology.</p>
        </div>
        <div class="stack" data-stack>{''.join(cards)}
        </div>
        <div class="rail-dots" data-dots-for="stack" aria-hidden="true"></div>
      </div>
    </section>

    <section class="block block--navy" aria-label="Experience in numbers">
      <div class="wrap">
        <div class="nums">
          <div class="num" data-fx="diag" data-num style="--off:18"><svg class="num__ring" viewBox="0 0 120 120"><circle cx="60" cy="60" r="50"/><circle class="arc" cx="60" cy="60" r="50" pathLength="100"/></svg><b><span data-count="10">10</span>+</b><span>Years of specialist experience</span></div>
          <div class="num" data-fx="diag" data-num style="--off:8;--d:.1s"><svg class="num__ring" viewBox="0 0 120 120"><circle cx="60" cy="60" r="50"/><circle class="arc" cx="60" cy="60" r="50" pathLength="100"/></svg><b><span data-count="100">100</span>+</b><span>Bone marrow transplants</span></div>
          <div class="num" data-fx="diag" data-num style="--off:30;--d:.2s"><svg class="num__ring" viewBox="0 0 120 120"><circle cx="60" cy="60" r="50"/><circle class="arc" cx="60" cy="60" r="50" pathLength="100"/></svg><b><span data-count="9">9</span></b><span>Specialist services for children &amp; adults</span></div>
        </div>
      </div>
    </section>

    <section class="block" aria-labelledby="gal-title">
      <div class="wrap svc-head" style="margin-bottom:0">
        <div><p class="tag" data-fx="wipe-x">In practice</p><h2 class="title" id="gal-title" data-fx="wipe">With patients, teams <em>&amp; peers</em></h2></div>
        <p class="lead" data-fx="fade" style="max-width:380px">Drag or swipe through moments from the ward, the clinic and conferences.</p>
      </div>
      <div class="rail" data-rail><div class="rail__track">{rail}
      </div></div>
      <div class="rail__bar" aria-hidden="true"><div><i></i></div></div>
    </section>

    <section class="block block--soft" id="timings" aria-labelledby="t-title">
      <div class="wrap clinic">
        <div>
          <p class="tag" data-fx="wipe-x">OPD Timings</p>
          <h2 class="title" id="t-title" data-fx="wipe">Find Dr. Neema Bhat <em>this week</em></h2>
          <p class="lead" data-fx="fade">Pick a day to see where she consults. Please call or WhatsApp to book before visiting.</p>
          <div class="notes">
            <div class="note" data-fx="wipe-x"><h4>Second Wednesday of every month</h4><p><strong>10 AM – 1 PM:</strong> Janappana and Ramnagara OPD. Then Apollo Bannerghatta Road and the Therapy Clinic as usual.</p></div>
            <div class="note" data-fx="wipe-x" style="--d:.1s"><h4>SOS availability</h4><p>Digvish Hospital · AV Hospital (Outer Ring Road) · Promed Hospital (Banashankari 2nd Stage)</p></div>
          </div>
        </div>
        <div data-days>
          <div class="seg" role="tablist" aria-label="Day of the week"><span class="seg__thumb" aria-hidden="true"></span></div>
          <div class="slots" role="tabpanel" aria-live="polite"></div>
        </div>
      </div>
    </section>

    <section class="block">
      <div class="wrap">
        <div class="cta" data-fx="diag">
          <h2>Questions about a diagnosis? Talk to a specialist.</h2>
          <a class="btn btn--navy magnet" href="contact.html">Book an Appointment<span class="btn__dot"><svg class="ic ic--go"><use href="#i-go"/></svg></span></a>
        </div>
      </div>
    </section>
  </main>
""" + footer()


# ------------------------------------------------------------------ ABOUT
def about():
    return head("About Dr. Neema Bhat | Hematologist & Pediatric Oncologist, Bangalore",
                "About Dr. Neema Bhat: US-trained Haemato-Oncologist, FAAP fellowship at Penn State Health, Program Director & HOD of the Bone Marrow Transplant Unit at Bhagawan Mahaveer Jain Hospital, Bangalore.",
                "about.html", LD_PHYSICIAN) + f"""
<body data-page="about">{ICONS}{appbar('about')}
  <main id="main">
    <section class="phero" aria-labelledby="ab-title">
      <div class="hero__grid" aria-hidden="true"></div>
      <div class="wrap phero__in">
        <div>
          <ol class="crumbs" data-fx="fade"><li><a href="index.html">Home</a></li><li>About</li></ol>
          <h1 id="ab-title" data-fx="wipe">Meet <em>Dr. Neema Bhat</em></h1>
          <p class="phero__sub" data-fx="fade" style="--d:.2s">Haemato-Oncologist, Pediatric Oncologist and Bone Marrow Transplant physician in Bangalore — caring for children and adults for more than ten years.</p>
        </div>
        <div class="phero__card" data-fx="diag" style="--d:.2s">
          <dl>
            <div><dt>Currently</dt><dd>Program Director &amp; HOD, Bone Marrow Transplant Unit</dd></div>
            <div><dt>Hospital</dt><dd>Bhagawan Mahaveer Jain Hospital, with Sankalp India Foundation</dd></div>
            <div><dt>Training</dt><dd>MD (USA) · Fellowship (FAAP), Penn State Health</dd></div>
          </dl>
        </div>
      </div>
    </section>

    <section class="block">
      <div class="wrap story">
        <figure class="portrait" data-fx="iris" style="margin:0">
          <img src="assets/images/portrait-coat.webp" srcset="assets/images/portrait-coat-720.webp 720w, assets/images/portrait-coat.webp 1200w" sizes="(max-width: 900px) 90vw, 480px" alt="Dr. Neema Bhat in a white coat, arms folded, smiling" width="1200" height="1911">
          <figcaption class="portrait__cap"><strong>Dr. Neema Bhat</strong><span>MD (USA) · FAAP · Hemato-Oncologist</span></figcaption>
        </figure>
        <div>
          <p class="tag" data-fx="wipe-x">Her story</p>
          <h2 class="title" data-fx="wipe">A decade of dedicated <em>hematology-oncology</em> care</h2>
          <div class="prose" style="margin-top:26px">
            <p class="big" data-fx="fade">She completed her MD in the United States, followed by a fellowship (FAAP) in Pediatric Hematology, Oncology &amp; Bone Marrow Transplantation at Penn State Health.</p>
            <p data-fx="fade">Dr. Neema Bhat is a Haemato-Oncologist based in Bangalore, with more than ten years of specialised experience treating blood disorders and blood cancers in both children and adults. Her training shapes how she diagnoses, stages and treats every patient who comes to her.</p>
            <p data-fx="fade">She is known for a patient-centric approach that prioritises clear communication and treatment plans built around each individual’s needs, rather than a one-size-fits-all protocol.</p>
          </div>
          <div class="path" data-path>
            <div class="path__line"><i></i></div>
            <div class="step"><time>2020 – Present</time><h3>Program Director &amp; HOD, Bone Marrow Transplant Unit</h3><p>Bhagawan Mahaveer Jain Hospital, in partnership with Sankalp India Foundation</p></div>
            <div class="step"><time>2020 – 2023</time><h3>Consultant Hematologist, BMT Physician &amp; Pediatric Oncology</h3><p>Fortis Hospitals, Bangalore</p></div>
            <div class="step"><time>2018 – 2020</time><h3>Consultant Hematologist, BMT Physician &amp; Pediatric Oncology</h3><p>BGS Gleneagles Global Hospitals, Bangalore</p></div>
            <div class="step"><time>2018</time><h3>Clinical Hematologist &amp; BMT Physician</h3><p>Sankalp India Foundation — BMT Unit at Peopletree Hospitals, Yeshwanthpur</p></div>
            <div class="step"><time>Training</time><h3>Fellowship (FAAP), Pediatric Hematology, Oncology &amp; BMT</h3><p>Penn State Health, USA · MD, United States</p></div>
          </div>
        </div>
      </div>
    </section>

    <section class="block block--soft">
      <div class="wrap">
        <p class="tag" data-fx="wipe-x">What sets her care apart</p>
        <h2 class="title" data-fx="wipe" style="margin-bottom:44px">Expertise, <em>explained clearly</em></h2>
        <div class="creds">
          <div class="cred" data-tilt data-fx="diag"><span class="cred__ic"><svg class="ic"><use href="#i-award"/></svg></span><h3>US-trained specialist</h3><p>MD in the United States and a fellowship (FAAP) in Pediatric Hematology, Oncology &amp; BMT at Penn State Health.</p></div>
          <div class="cred" data-tilt data-fx="diag" style="--d:.1s"><span class="cred__ic"><svg class="ic"><use href="#i-marrow"/></svg></span><h3>Transplant leadership</h3><p>Program Director and Head of the Bone Marrow Transplant Unit at Bhagawan Mahaveer Jain Hospital.</p></div>
          <div class="cred" data-tilt data-fx="diag" style="--d:.2s"><span class="cred__ic"><svg class="ic"><use href="#i-shield"/></svg></span><h3>Children &amp; adults</h3><p>Blood disorders and blood cancers across all ages, with plans built around each patient.</p></div>
        </div>
      </div>
    </section>

    <section class="block">
      <div class="wrap">
        <p class="tag" data-fx="wipe-x">Gallery</p>
        <h2 class="title" data-fx="wipe" style="margin-bottom:44px">In the ward <em>&amp; beyond</em></h2>
        <div class="mosaic" data-gallery>
          <figure class="m1" data-fx="iris" tabindex="0" data-full="assets/images/gallery/young-patient-care-team.webp"><img src="assets/images/gallery/young-patient-care-team-760.webp" alt="Dr. Neema Bhat with the care team beside a young patient" loading="lazy"><figcaption>With a young patient and the care team</figcaption></figure>
          <figure class="m2 m-portrait" data-fx="iris" style="--d:.1s" tabindex="0" data-full="assets/images/portrait-classic.webp"><img src="assets/images/portrait-classic-720.webp" alt="Dr. Neema Bhat in a white coat" loading="lazy"><figcaption>Dr. Neema Bhat</figcaption></figure>
          <figure class="m3" data-fx="iris" tabindex="0" data-full="assets/images/gallery/with-patients.webp"><img src="assets/images/gallery/with-patients-760.webp" alt="Dr. Neema Bhat with two patients" loading="lazy" style="object-position:50% 25%"><figcaption>With patients after a follow-up visit</figcaption></figure>
          <figure class="m4" data-fx="iris" style="--d:.1s" tabindex="0" data-full="assets/images/gallery/pediatric-tumour-care-ethiopia.webp"><img src="assets/images/gallery/pediatric-tumour-care-ethiopia-760.webp" alt="Dr. Neema Bhat at a pediatric tumour care programme in Ethiopia" loading="lazy"><figcaption>Pediatric tumour care programme, Ethiopia · 2025</figcaption></figure>
          <figure class="m5" data-fx="iris" style="--d:.2s" tabindex="0" data-full="assets/images/gallery/conference-mumbai-hematology-group.webp"><img src="assets/images/gallery/conference-mumbai-hematology-group-760.webp" alt="Dr. Neema Bhat at the Mumbai Hematology Group conference" loading="lazy"><figcaption>Mumbai Hematology Group conference · 2025</figcaption></figure>
        </div>
      </div>
    </section>

    <section class="block" style="padding-top:0">
      <div class="wrap"><div class="cta" data-fx="diag"><h2>Book a consultation with Dr. Neema Bhat.</h2><a class="btn btn--navy magnet" href="contact.html">Book an Appointment<span class="btn__dot"><svg class="ic ic--go"><use href="#i-go"/></svg></span></a></div></div>
    </section>
  </main>
""" + footer()


# ------------------------------------------------------------------ CONTACT
def contact():
    topics = "".join(f'<label class="choice"><input type="radio" name="topic" value="{n}" data-slug="{s}"{" checked" if i == 0 else ""}><span><svg class="ic"><use href="#i-{"child" if c == "Pediatric" else "marrow" if s == "bone-marrow-transplant" else "drop"}"/></svg>{n}</span></label>' for i, (n, s, c, _) in enumerate(SERVICES))
    topics += '<label class="choice"><input type="radio" name="topic" value="Second opinion" data-slug="second-opinion"><span><svg class="ic"><use href="#i-doc"/></svg>Second opinion</span></label>'
    return head("Contact Dr. Neema Bhat | Book an Appointment in Bangalore",
                "Book an appointment with Dr. Neema Bhat, Hematologist and Pediatric Oncologist. OPD at Apollo Hospitals, Bannerghatta Road. Call or WhatsApp +91 78997 56677.",
                "contact.html", LD_PHYSICIAN) + f"""
<body data-page="contact">{ICONS}{appbar('contact')}
  <main id="main">
    <section class="phero" aria-labelledby="c-title">
      <div class="hero__grid" aria-hidden="true"></div>
      <div class="wrap phero__in">
        <div>
          <ol class="crumbs" data-fx="fade"><li><a href="index.html">Home</a></li><li>Contact</li></ol>
          <h1 id="c-title" data-fx="wipe">Book a <em>consultation</em></h1>
          <p class="phero__sub" data-fx="fade" style="--d:.2s">Three quick steps — your request opens in WhatsApp so you can review it before sending.</p>
        </div>
        <div class="phero__card" data-fx="diag" style="--d:.2s">
          <dl>
            <div><dt>Call / WhatsApp</dt><dd><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></dd></div>
            <div><dt>OPD</dt><dd>Apollo Hospitals, Bannerghatta Road · Mon – Sat, 11 AM – 4 PM</dd></div>
            <div><dt>Evenings</dt><dd>Therapy Clinic · Mon – Sat, 5 – 7 PM</dd></div>
          </dl>
        </div>
      </div>
    </section>

    <section class="block">
      <div class="wrap contact">
        <form class="wizard" id="wizard" novalidate data-fx="diag">
          <div class="wizard__top"><h2>Request an appointment</h2><div class="dots" aria-hidden="true"><i class="is-on"></i><i></i><i></i></div></div>
          <p class="sr-only" aria-live="polite" data-wz-status>Step 1 of 3</p>
          <div class="wz-step is-active" data-step="1">
            <h3>Who is the consultation for?</h3>
            <div class="choices">
              <label class="choice"><input type="radio" name="who" value="Child" checked><span><svg class="ic"><use href="#i-child"/></svg>A child</span></label>
              <label class="choice"><input type="radio" name="who" value="Adult"><span><svg class="ic"><use href="#i-adult"/></svg>An adult</span></label>
            </div>
          </div>
          <div class="wz-step" data-step="2">
            <h3>What is it about?</h3>
            <div class="choices choices--list">{topics}</div>
          </div>
          <div class="wz-step" data-step="3">
            <h3>Your details</h3>
            <div class="field"><label for="w-name">Patient’s name</label><input id="w-name" name="name" type="text" autocomplete="name" required><span class="field__err">Please enter the patient’s name</span></div>
            <div class="field"><label for="w-phone">Phone number</label><input id="w-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" required pattern="[0-9+\\s\\-]{{8,}}"><span class="field__err">Please enter a valid phone number</span></div>
            <div class="field"><label for="w-msg">Anything else? (optional)</label><textarea id="w-msg" name="message" rows="3"></textarea></div>
          </div>
          <div class="wz-nav">
            <button class="btn btn--line" type="button" data-wz-back hidden>Back</button>
            <button class="btn btn--navy" type="button" data-wz-next style="margin-left:auto">Continue<svg class="ic ic--go"><use href="#i-go"/></svg></button>
            <button class="btn btn--teal" type="submit" data-wz-send hidden style="margin-left:auto">Send on WhatsApp<svg class="ic"><use href="#i-wa"/></svg></button>
          </div>
          <p class="wz-note">For medical emergencies, please visit the nearest emergency department.</p>
        </form>

        <div>
          <div class="cards">
            <a class="ccard" href="tel:{PHONE_TEL}" data-fx="wipe-x"><span class="ccard__ic"><svg class="ic"><use href="#i-phone"/></svg></span><span><small>Call</small><b>{PHONE_DISPLAY}</b></span><svg class="ic ic--go"><use href="#i-go"/></svg></a>
            <a class="ccard" href="{WA}" target="_blank" rel="noopener" data-fx="wipe-x" style="--d:.08s"><span class="ccard__ic"><svg class="ic"><use href="#i-wa"/></svg></span><span><small>WhatsApp</small><b>{PHONE_DISPLAY}</b></span><svg class="ic ic--go"><use href="#i-go"/></svg></a>
            <a class="ccard" href="https://www.google.com/maps/search/?api=1&amp;query=Apollo+Hospitals+Bannerghatta+Road+Bengaluru" target="_blank" rel="noopener" data-fx="wipe-x" style="--d:.16s"><span class="ccard__ic"><svg class="ic"><use href="#i-pin"/></svg></span><span><small>OPD · Directions</small><b>Apollo Hospitals, Bannerghatta Road</b></span><svg class="ic ic--go"><use href="#i-go"/></svg></a>
          </div>
          <div class="map" data-fx="iris"><iframe title="Map showing Apollo Hospitals, Bannerghatta Road, Bengaluru" src="https://maps.google.com/maps?q=Apollo%20Hospitals%2C%20Bannerghatta%20Road%2C%20Bengaluru&amp;z=15&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
        </div>
      </div>
    </section>

    <section class="block block--soft" id="timings" aria-labelledby="t-title">
      <div class="wrap clinic">
        <div>
          <p class="tag" data-fx="wipe-x">OPD Timings</p>
          <h2 class="title" id="t-title" data-fx="wipe">Where to find her, <em>day by day</em></h2>
          <div class="notes">
            <div class="note" data-fx="wipe-x"><h4>Second Wednesday of every month</h4><p><strong>10 AM – 1 PM:</strong> Janappana and Ramnagara OPD. Then Apollo Bannerghatta Road and the Therapy Clinic as usual.</p></div>
            <div class="note" data-fx="wipe-x" style="--d:.1s"><h4>SOS availability</h4><p>Digvish Hospital · AV Hospital (Outer Ring Road) · Promed Hospital (Banashankari 2nd Stage)</p></div>
          </div>
        </div>
        <div data-days>
          <div class="seg" role="tablist" aria-label="Day of the week"><span class="seg__thumb" aria-hidden="true"></span></div>
          <div class="slots" role="tabpanel" aria-live="polite"></div>
        </div>
      </div>
    </section>
  </main>
""" + footer(fab=False)


# ------------------------------------------------------------------ BMT SERVICE
def bmt():
    faqs = [
        ("What is a bone marrow transplant?", "It replaces damaged or diseased bone marrow with healthy blood-forming stem cells. The new cells settle in the marrow and begin producing healthy red cells, white cells and platelets."),
        ("Is it only for cancer?", "No. Besides leukaemia, lymphoma and myeloma, transplants are used for non-cancerous conditions such as thalassemia major, aplastic anaemia, sickle cell disease and some inherited immune disorders."),
        ("Who can be a donor?", "For an allogeneic transplant, a brother or sister is often checked first — each full sibling has roughly a one-in-four chance of being a full match. Unrelated volunteer donors and half-matched family donors may also be options."),
        ("Is the stem cell infusion painful?", "The infusion itself is given through a drip, much like a blood transfusion, and is usually not painful. The preparation (conditioning) and recovery phases need close care, which the team plans in detail with you."),
        ("How long does recovery take?", "It varies with the type of transplant and the condition being treated. Hospital stays are commonly several weeks, followed by months of regular follow-up while the immune system recovers."),
    ]
    faq_html = "".join(f'<details data-fx="fade"><summary>{q}<span class="faq__pm" aria-hidden="true"></span></summary><p class="faq__a">{a}</p></details>' for q, a in faqs)
    ld_faq = '  <script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ",".join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q, a.replace('"', '\\"')) for q, a in faqs) + "]}</script>\n"
    ld_proc = '  <script type="application/ld+json">{"@context":"https://schema.org","@type":"MedicalProcedure","name":"Bone Marrow Transplantation","alternateName":"Stem cell transplant","procedureType":"https://schema.org/TherapeuticProcedure","performer":{"@type":"Physician","name":"Dr. Neema Bhat"}}</script>\n'
    steps = [
        ("Evaluation", "Tests, donor matching and counselling so the family understands each step."),
        ("Collection", "Stem cells are collected — from the patient (autologous) or a donor (allogeneic)."),
        ("Conditioning", "Chemotherapy, sometimes with radiation, prepares the marrow for new cells."),
        ("Infusion", "Healthy stem cells are given through a drip, much like a transfusion."),
        ("Engraftment", "New cells settle in and start making blood, with close monitoring."),
        ("Recovery", "A gradual return to daily life with long-term follow-up."),
    ]
    step_html = "".join(f'<div class="jstep"><span class="jstep__n">{i + 1:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))
    who = [("i-cells", "Leukaemia"), ("i-cells", "Lymphoma &amp; Myeloma"), ("i-drop", "Thalassemia major"), ("i-drop", "Aplastic anaemia"),
           ("i-drop", "Sickle cell disease"), ("i-shield", "Immune disorders"), ("i-child", "Childhood cancers"), ("i-marrow", "Marrow failure")]
    who_html = "".join(f'<li data-fx="diag" style="--d:{k * 0.05:.2f}s"><svg class="ic"><use href="#{ic}"/></svg>{t}</li>' for k, (ic, t) in enumerate(who))
    return head("Bone Marrow Transplant in Bangalore | Dr. Neema Bhat",
                "Bone marrow (stem cell) transplant in Bangalore with Dr. Neema Bhat, Program Director & HOD of the BMT Unit at Bhagawan Mahaveer Jain Hospital. Autologous and allogeneic transplants for children and adults.",
                BMT_PAGE, LD_PHYSICIAN + ld_proc + ld_faq) + f"""
<body data-page="service">{ICONS}{appbar('service')}
  <main id="main">
    <section class="phero" aria-labelledby="b-title">
      <div class="hero__grid" aria-hidden="true"></div>
      <div class="wrap phero__in">
        <div>
          <ol class="crumbs" data-fx="fade"><li><a href="index.html">Home</a></li><li><a href="index.html#services">Services</a></li><li>Bone Marrow Transplant</li></ol>
          <h1 id="b-title" data-fx="wipe">Bone Marrow <em>Transplant</em> in Bangalore</h1>
          <p class="phero__sub" data-fx="fade" style="--d:.2s">Autologous and allogeneic stem cell transplants for children and adults — led by Dr. Neema Bhat, Program Director and Head of the Bone Marrow Transplant Unit at Bhagawan Mahaveer Jain Hospital.</p>
          <div class="hero__acts" data-fx="fade" style="--d:.35s"><a class="btn btn--teal magnet" href="contact.html?topic=bone-marrow-transplant">Discuss a transplant<span class="btn__dot"><svg class="ic ic--go"><use href="#i-go"/></svg></span></a></div>
        </div>
        <div class="phero__card" data-fx="diag" style="--d:.2s">
          <dl>
            <div><dt>Transplants</dt><dd>Autologous &amp; allogeneic</dd></div>
            <div><dt>For</dt><dd>Children and adults · cancers and non-cancerous blood disorders</dd></div>
            <div><dt>Experience</dt><dd>100+ bone marrow transplants</dd></div>
          </dl>
        </div>
      </div>
    </section>

    <section class="block">
      <div class="wrap intro2">
        <div>
          <p class="tag" data-fx="wipe-x">Overview</p>
          <h2 class="title" data-fx="wipe">A new source of <em>healthy blood cells</em></h2>
          <p class="lead" data-fx="fade">A bone marrow (stem cell) transplant replaces damaged or diseased marrow with healthy blood-forming stem cells. For many blood cancers and serious blood disorders, it offers the best chance of long-term control — and for some, a cure.</p>
          <p class="lead" data-fx="fade">Every transplant is planned in detail, from choosing the right type and donor to the months of follow-up afterwards, with the family involved at each step.</p>
        </div>
        <div class="cellviz" data-cellviz aria-hidden="true">
          <svg viewBox="0 0 460 460">
            <circle class="orb" cx="230" cy="230" r="210"/><circle class="orb" cx="230" cy="230" r="160" style="transition-delay:.3s"/><circle class="orb" cx="230" cy="230" r="110" style="transition-delay:.6s"/>
            <circle class="core" cx="230" cy="230" r="72"/>
            <text x="230" y="224" text-anchor="middle">Stem</text><text x="230" y="246" text-anchor="middle">cells</text>
            <g class="sat"><circle cx="230" cy="20" r="11"/><circle cx="440" cy="230" r="7"/></g>
            <g class="sat sat2"><circle cx="230" cy="390" r="9"/><circle cx="70" cy="230" r="6"/></g>
          </svg>
        </div>
      </div>
    </section>

    <section class="block block--soft">
      <div class="wrap">
        <p class="tag" data-fx="wipe-x">Who may need it</p>
        <h2 class="title" data-fx="wipe" style="margin-bottom:40px">Conditions treated with <em>transplant</em></h2>
        <ul class="who">{who_html}</ul>
      </div>
    </section>

    <section class="block block--navy">
      <div class="wrap types">
        <div>
          <p class="tag tag--light" data-fx="wipe-x">Types of transplant</p>
          <h2 class="title title--light" data-fx="wipe">Two ways to <em>rebuild the marrow</em></h2>
          <div class="switch" role="tablist" aria-label="Transplant type" data-switch>
            <button type="button" role="tab" aria-selected="true" aria-controls="t-auto" id="tab-auto">Autologous</button>
            <button type="button" role="tab" aria-selected="false" aria-controls="t-allo" id="tab-allo" tabindex="-1">Allogeneic</button>
            <span class="switch__thumb" aria-hidden="true"></span>
          </div>
        </div>
        <div>
          <div class="type-panel" id="t-auto" role="tabpanel" aria-labelledby="tab-auto">
            <h3>Autologous — your own cells</h3>
            <p>The patient’s own stem cells are collected and stored, then returned after high-dose treatment.</p>
            <ul><li><svg class="ic"><use href="#i-check"/></svg>No donor needed</li><li><svg class="ic"><use href="#i-check"/></svg>Often used for lymphoma, myeloma and some solid tumours</li><li><svg class="ic"><use href="#i-check"/></svg>No risk of graft-versus-host disease</li></ul>
          </div>
          <div class="type-panel" id="t-allo" role="tabpanel" aria-labelledby="tab-allo" hidden>
            <h3>Allogeneic — cells from a donor</h3>
            <p>Healthy stem cells come from a matched donor — a sibling, a relative or an unrelated volunteer.</p>
            <ul><li><svg class="ic"><use href="#i-check"/></svg>Used for leukaemia, thalassemia, aplastic anaemia and immune disorders</li><li><svg class="ic"><use href="#i-check"/></svg>Donor’s immune cells can help fight remaining disease</li><li><svg class="ic"><use href="#i-check"/></svg>Careful donor matching and follow-up are essential</li></ul>
          </div>
        </div>
      </div>
    </section>

    <section class="block">
      <div class="wrap">
        <p class="tag" data-fx="wipe-x">The journey</p>
        <h2 class="title" data-fx="wipe" style="margin-bottom:56px">Six stages, <em>one team</em></h2>
        <div class="journey" data-journey><div class="journey__rail"><div class="journey__line"><i></i></div>{step_html}</div></div>
      </div>
    </section>

    <section class="block block--soft">
      <div class="wrap">
        <p class="tag" data-fx="wipe-x">Questions</p>
        <h2 class="title" data-fx="wipe" style="margin-bottom:30px">Common <em>questions</em></h2>
        <div class="faq">{faq_html}</div>
        <p class="disclaimer">General information only — every patient is different. Your consultation is the place for advice specific to you or your child.</p>
      </div>
    </section>

    <section class="block">
      <div class="wrap"><div class="cta" data-fx="diag"><h2>Considering a transplant? Talk it through.</h2><a class="btn btn--navy magnet" href="contact.html?topic=bone-marrow-transplant">Book an Appointment<span class="btn__dot"><svg class="ic ic--go"><use href="#i-go"/></svg></span></a></div></div>
    </section>
  </main>
""" + footer()


if __name__ == "__main__":
    for name, fn in [("index.html", home), ("about.html", about), ("contact.html", contact), (BMT_PAGE, bmt)]:
        (ROOT / name).write_text(fn(), encoding="utf-8")
        print("built", name)
