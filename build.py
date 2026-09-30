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

# Patient rating shown in the home hero and reviews section.
# Currently: Apollo Hospitals' published patient rating for Dr. Neema Bhat.
# To show her Google rating instead, set source="Google", fill in score/count
# from her Google Business Profile and point url at that profile.
RATING = {
    "source": "Apollo Hospitals",
    "score": "4.56",
    "count": "97% of 32 patients recommend",
    "url": "https://www.apollohospitals.com/doctors/medical-oncology-and-clinical-haematology/bangalore/dr-neema-bhat",
}
GOOGLE_REVIEWS_URL = "https://www.google.com/search?q=Dr.+Neema+Bhat+Hematologist+Bangalore+reviews"

# Review cards on the home page. These are SAMPLES (layout only) — replace each
# with a real patient review and set sample=False before going live.
REVIEWS = [
    ("Parent of a patient", "Thalassemia care", "Sample review — replace with a real patient review. Share what the family valued: clear explanations, careful review of reports, time taken to answer questions.", True),
    ("Patient", "Hematology consultation", "Sample review — replace with a real patient review from Google or the hospital’s feedback page.", True),
    ("Family member", "Bone marrow transplant", "Sample review — replace with a real patient review describing their experience of the transplant journey.", True),
    ("Parent of a patient", "Childhood leukaemia", "Sample review — replace with a real review from a family whose child was treated for leukaemia.", True),
    ("Patient", "Anaemia treatment", "Sample review — replace with a real review about diagnosis and follow-up for anaemia.", True),
    ("Patient", "Second opinion", "Sample review — replace with a real review from a patient who came for a second opinion.", True),
]


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
  <symbol id="i-thermo" viewBox="0 0 24 24"><path d="M10 14V5a2 2 0 0 1 4 0v9a4 4 0 1 1-4 0z"/><path d="M12 10v7"/></symbol>
  <symbol id="i-bone" viewBox="0 0 24 24"><path d="M7 17l10-10M5.5 14.5a2.5 2.5 0 1 0 4 4M14.5 5.5a2.5 2.5 0 1 1 4 4M9.5 18.5a2.5 2.5 0 0 1-4 0M18.5 9.5a2.5 2.5 0 0 1 0-4"/></symbol>
  <symbol id="i-scale" viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="4"/><path d="M9 10a3 3 0 0 1 6 0M12 10l1.5-2"/></symbol>
  <symbol id="i-heart" viewBox="0 0 24 24"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z"/></symbol>
  <symbol id="i-users" viewBox="0 0 24 24"><circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><path d="M16 5a3 3 0 0 1 0 6M18 14c2 .6 3 2.8 3 6"/></symbol>
  <symbol id="i-flask" viewBox="0 0 24 24"><path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 1.7 3h10.6a2 2 0 0 0 1.7-3l-5-9V3"/><path d="M7.5 15h9"/></symbol>
  <symbol id="i-chat" viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4z"/><path d="M8 9.5h8M8 12.5h5"/></symbol>
  <symbol id="i-star" viewBox="0 0 24 24"><path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/></symbol>
  <symbol id="i-lungs" viewBox="0 0 24 24"><path d="M12 4v8M12 12c-1 0-2 1-2 2v5c0 1-1 2-3 2s-3-1-3-3v-4c0-3 2-7 4-7s2 2 2 3M12 12c1 0 2 1 2 2v5c0 1 1 2 3 2s3-1 3-3v-4c0-3-2-7-4-7s-2 2-2 3"/></symbol>
  <symbol id="i-link" viewBox="0 0 24 24"><circle cx="7" cy="12" r="3.5"/><circle cx="17" cy="12" r="3.5"/><path d="M10.5 12h3"/></symbol>
</defs></svg>"""


LD_PHYSICIAN = """  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"Physician","name":"Dr. Neema Bhat","description":"Hematologist, Pediatric Oncologist and Bone Marrow Transplant specialist in Bangalore.","url":"https://drneemabhat.com/","image":"https://drneemabhat.com/assets/images/portrait-scrubs.webp","telephone":"+91-78997-56677","medicalSpecialty":["Hematologic","Oncologic","Pediatric"],"alumniOf":{"@type":"Hospital","name":"Penn State Health"},
   "hospitalAffiliation":[{"@type":"Hospital","name":"Apollo Hospitals, Bannerghatta Road"},{"@type":"Hospital","name":"Apollo One & Apollo Cradle, Electronic City"},{"@type":"Hospital","name":"Bhagawan Mahaveer Jain Hospital"}],
   "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"11:00","closes":"16:00","description":"OPD — Apollo Hospitals, Bannerghatta Road"},{"@type":"OpeningHoursSpecification","dayOfWeek":"Friday","opens":"14:00","closes":"16:00","description":"Apollo One & Apollo Cradle, Hosa Road, Electronic City"},{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"17:00","closes":"19:00","description":"Therapy Clinic"}],
   "address":{"@type":"PostalAddress","addressLocality":"Bengaluru","addressRegion":"Karnataka","addressCountry":"IN"},"areaServed":"Bangalore"}
  </script>
"""

SVC_ICON = {"Hematology": "i-drop", "Pediatric": "i-child", "Pediatric & Adult": "i-marrow"}
SVC_ICON_BY_SLUG = {"leukaemia": "i-cells", "lymphoma-myeloma": "i-cells", "hemophilia": "i-shield", "pediatric-tumours": "i-heart"}


def ic(name, cls="ic"):
    return f'<svg class="{cls}"><use href="#{name}"/></svg>'


def head(title, desc, canonical, extra=""):
    return f"""<!doctype html>
<html lang="en-IN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="theme-color" content="#ffffff">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
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


def header(active):
    def cur(p):
        return ' aria-current="page"' if p == active else ""
    hema = "".join(f'<a href="{svc_href(s)}">{n}</a>' for n, s, c, _ in SERVICES if c == "Hematology")
    ped = "".join(f'<a href="{svc_href(s)}">{n}</a>' for n, s, c, _ in SERVICES if c == "Pediatric")
    return f"""
  <a class="skip" href="#main">Skip to main content</a>
  <div class="curtain" aria-hidden="true"><img src="assets/images/logo-mark.png" alt=""></div>

  <header class="bar">
    <div class="wrap bar__in">
      <a class="brand" href="index.html" aria-label="Dr. Neema Bhat — home"><img src="assets/images/logo.png" alt="Dr. Neema Bhat, Hematologist and Pediatric Oncologist" width="928" height="275"></a>
      <nav class="primary" aria-label="Primary">
        <ul class="menu">
          <li><a href="index.html"{cur('home')}>Home</a></li>
          <li><a href="about.html"{cur('about')}>About</a></li>
          <li class="has-drop">
            <button type="button" aria-expanded="false" aria-controls="drop-services"{' aria-current="page"' if active == 'service' else ''}>Services{ic('i-chev', 'ic chev')}</button>
            <div class="drop" id="drop-services">
              <div class="drop__col"><h3>Hematology</h3>{hema}</div>
              <div class="drop__col"><h3>Pediatric</h3>{ped}</div>
              <a class="drop__feat" href="{BMT_PAGE}">Bone Marrow Transplant{ic('i-go')}</a>
            </div>
          </li>
          <li><a href="contact.html"{cur('contact')}>Contact</a></li>
        </ul>
      </nav>
      <div class="bar__end">
        <a class="bar__call" href="tel:{PHONE_TEL}">{ic('i-phone')}{PHONE_DISPLAY}</a>
        <a class="btn btn--grad btn--sm" href="contact.html">Book Appointment{ic('i-go', 'ic ic--go')}</a>
        <div class="bar__icons">
          <a class="bar__icon" href="tel:{PHONE_TEL}" aria-label="Call {PHONE_DISPLAY}">{ic('i-phone')}</a>
          <button class="bar__icon" type="button" data-sheet-open aria-label="Open menu" aria-controls="sheet" aria-expanded="false">{ic('i-menu')}</button>
        </div>
      </div>
    </div>
  </header>

  <div class="sheet" id="sheet" aria-hidden="true">
    <div class="sheet__scrim" data-sheet-close></div>
    <div class="sheet__panel" role="dialog" aria-modal="true" aria-label="Menu">
      <div class="sheet__grab"></div>
      <ul class="sheet__nav">
        <li><a href="index.html"{cur('home')}>Home{ic('i-go')}</a></li>
        <li><a href="about.html"{cur('about')}>About{ic('i-go')}</a></li>
        <li><button type="button" data-acc aria-expanded="false">Services{ic('i-chev', 'ic chev')}</button>
          <div class="sheet__sub"><div><small>Hematology</small>{hema}<small>Pediatric</small>{ped}<small>Specialty</small><a href="{BMT_PAGE}">Bone Marrow Transplant</a></div></div></li>
        <li><a href="contact.html"{cur('contact')}>Contact{ic('i-go')}</a></li>
      </ul>
      <div class="sheet__actions">
        <a class="btn btn--line" href="tel:{PHONE_TEL}">{ic('i-phone')}Call</a>
        <a class="btn btn--grad" href="contact.html">{ic('i-cal')}Book</a>
      </div>
    </div>
  </div>
"""


def footer(fab=True):
    links = "".join(f'<li><a href="{svc_href(s)}">{n}</a></li>' for n, s, c, _ in SERVICES if c == "Hematology")
    links2 = "".join(f'<li><a href="{svc_href(s)}">{n}</a></li>' for n, s, c, _ in SERVICES if c != "Hematology")
    return f"""
  <footer class="foot">
    <div class="wrap">
      <div class="foot__grid">
        <div>
          <img class="foot__logo" src="assets/images/logo.png" alt="Dr. Neema Bhat" width="928" height="275" loading="lazy">
          <p>Hematologist, Pediatric Oncologist and Bone Marrow Transplant specialist in Bangalore.</p>
          <ul style="margin-top:18px">
            <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
            <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></li>
            <li>Apollo Hospitals, Bannerghatta Road, Bengaluru</li>
          </ul>
        </div>
        <div><h2>Pages</h2><ul><li><a href="index.html">Home</a></li><li><a href="about.html">About</a></li><li><a href="{BMT_PAGE}">Bone Marrow Transplant</a></li><li><a href="contact.html">Contact</a></li></ul></div>
        <div><h2>Hematology</h2><ul>{links}</ul></div>
        <div><h2>Pediatric</h2><ul>{links2}</ul></div>
      </div>
      <div class="foot__base"><p>© <span data-year>2026</span> Dr. Neema Bhat. All rights reserved.</p><p>Information on this website is for general awareness and is not a substitute for medical advice.</p></div>
    </div>
  </footer>

  <nav class="dock" aria-label="Quick actions">
    <a href="{WA}" target="_blank" rel="noopener">{ic('i-wa')}<span>WhatsApp</span></a>
    <a href="tel:{PHONE_TEL}">{ic('i-phone')}<span>Call</span></a>
    <a class="dock__book" href="{'contact.html' if fab else '#wizard'}">{ic('i-cal')}<span>Book</span></a>
  </nav>
  <dialog class="lb" id="lb" aria-label="Photo viewer"><button class="lb__x" type="button" aria-label="Close">×</button><button class="lb__nav lb__nav--p" type="button" aria-label="Previous">‹</button><figure><img src="" alt=""><figcaption></figcaption></figure><button class="lb__nav lb__nav--n" type="button" aria-label="Next">›</button></dialog>
  <script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def stepper(kind, items, label):
    """Clickable step row. kind: 'steps' (home) or 'journey' (service page). items: (title, short, more)."""
    n = len(items)
    lis = "".join(
        f'<li><button type="button" class="stp" data-step="{k}" aria-pressed="false">'
        f'<span class="stp__n">{k + 1:02d}</span><span class="stp__t"><b>{t}</b><span>{d}</span></span>'
        f'<span class="stp__more">{more}</span></button></li>'
        for k, (t, d, more) in enumerate(items))
    return f"""<ol class="{kind}" data-stepper aria-label="{label}" style="--n:{n}">{lis}</ol>
        <div class="stp-panel" aria-live="polite">
          <span class="stp-panel__n"></span>
          <div><h3></h3><p></p></div>
          <div class="stp-panel__nav"><button type="button" data-prev aria-label="Previous step">{ic('i-go')}</button><button type="button" data-next aria-label="Next step">{ic('i-go')}</button></div>
        </div>"""


def stars():
    return '<span class="stars" aria-hidden="true">' + ic('i-star') * 5 + '</span>'


def rating_badge():
    r = RATING
    return (f'<a class="rating chip chip--b" href="{r["url"]}" target="_blank" rel="noopener">'
            f'<b>{r["score"]}</b>{stars()}<span><strong>{r["source"]} patient rating</strong>{r["count"]}</span></a>')


def reviews_section():
    r = RATING
    SAMPLE_TAG = '<span class="review__sample">Sample</span>'
    cards = "".join(
        f'<figure class="review">{stars()}'
        f'{SAMPLE_TAG if sample else ""}'
        f'<blockquote>{text}</blockquote><figcaption><b>{who}</b><span>{topic}</span></figcaption></figure>'
        for k, (who, topic, text, sample) in enumerate(REVIEWS))
    return f"""
    <section class="sec" aria-labelledby="rv-title">
      <div class="wrap">
        {sec_head('Patient reviews', 'What patients <span class="grad-text">say</span>', 'Families trust Dr. Neema Bhat with some of the hardest diagnoses. Read reviews, or share your own experience.', hid='rv-title')}
        <div class="reviews">
          <div class="rsum" data-fx="iris">
            <b class="rsum__score">{r["score"]}<small>/5</small></b>
            {stars()}
            <p><strong>{r["source"]} patient rating</strong><br>{r["count"]}</p>
            <div class="rsum__acts">
              <a class="btn btn--white btn--sm" href="{GOOGLE_REVIEWS_URL}" target="_blank" rel="noopener">Reviews on Google{ic('i-go', 'ic ic--go')}</a>
              <a class="btn btn--line btn--sm" href="{r["url"]}" target="_blank" rel="noopener">View source{ic('i-go', 'ic ic--go')}</a>
            </div>
          </div>
          <div class="reviews__list" data-fx="fade"><div class="reviews__track">{cards}<div class="reviews__dup" aria-hidden="true" style="display:contents">{cards.replace(' data-fx="fade"', '')}</div></div></div>
        </div>
      </div>
    </section>"""


def sec_head(tag, title, lead="", center=False, hid=""):
    idattr = f' id="{hid}"' if hid else ""
    lead_html = f'<p class="lead" data-fx="fade">{lead}</p>' if lead else ""
    return f"""<div class="head{' head--center' if center else ''}">
          <div><p class="tag" data-fx="wipe-x">{tag}</p><h2 class="title"{idattr} data-fx="wipe">{title}</h2></div>
          {lead_html}
        </div>"""


def faq_block(faqs):
    html = "".join(f'<details><summary>{q}<span class="faq__pm" aria-hidden="true"></span></summary><p class="faq__a">{a}</p></details>' for q, a in faqs)
    ld = '  <script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ",".join(
        '{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q, a.replace('"', '\\"')) for q, a in faqs) + "]}</script>\n"
    return html, ld


def cta(title, text, topic=""):
    href = "contact.html" + (f"?topic={topic}" if topic else "")
    return f"""
    <section class="sec sec--tight">
      <div class="wrap">
        <div class="cta" data-fx="iris">
          <div><h2>{title}</h2><p>{text}</p></div>
          <div class="cta__acts">
            <a class="btn btn--white" href="{href}">Book an Appointment{ic('i-go', 'ic ic--go')}</a>
            <a class="btn btn--line" href="{WA}" target="_blank" rel="noopener">{ic('i-wa')}WhatsApp</a>
          </div>
        </div>
      </div>
    </section>"""


WHERE_NOTES = """<div class="notes">
            <div class="note"><b>Second Wednesday of every month · 10 AM – 1 PM:</b> Janappana and Ramnagara OPD, then Apollo Bannerghatta Road and the Therapy Clinic as usual.</div>
            <div class="note"><b>SOS availability:</b> Digvish Hospital · AV Hospital (Outer Ring Road) · Promed Hospital (Banashankari 2nd Stage)</div>
          </div>"""

DAY_PICKER = """<div data-days>
          <div class="seg" role="tablist" aria-label="Day of the week"><span class="seg__thumb" aria-hidden="true"></span></div>
          <div class="slots" role="tabpanel" aria-live="polite"></div>
        </div>"""


def where_section(title="Where Dr. Neema Bhat <span class=\"grad-text\">consults</span>"):
    hosp = [
        ("Apollo Hospitals, Bannerghatta Road", "OPD · Mon – Sat, 11 AM – 4 PM"),
        ("Therapy Clinic", "Evenings · Mon – Sat, 5 – 7 PM"),
        ("Apollo One &amp; Apollo Cradle, Electronic City", "Hosa Road · Fridays, 2 – 4 PM"),
        ("Bhagawan Mahaveer Jain Hospital", "Bone Marrow Transplant Unit · Program Director &amp; HOD"),
    ]
    items = "".join(f'<li>{ic("i-pin")}<div><b>{h}</b><span>{t}</span></div></li>' for h, t in hosp)
    return f"""
    <section class="sec" id="timings" aria-labelledby="t-title">
      <div class="wrap where">
        <div>
          <p class="tag" data-fx="wipe-x">OPD timings</p>
          <h2 class="title" id="t-title" data-fx="wipe">{title}</h2>
          <p class="lead" data-fx="fade">Please call or WhatsApp {PHONE_DISPLAY} to confirm before visiting.</p>
          <ul class="hosp">{items}</ul>
        </div>
        <div>
          <p class="lead" style="margin:0 0 12px;color:var(--navy);font-weight:500">Pick a day to see her schedule</p>
          {DAY_PICKER}
          {WHERE_NOTES}
        </div>
      </div>
    </section>"""


GALLERY = [
    ("gallery/young-patient-care-team", "With a young patient and the care team", "Dr. Neema Bhat with the nursing and care team beside a young patient in a hospital room", False),
    ("portrait-classic", "Dr. Neema Bhat", "Dr. Neema Bhat in a white coat", True),
    ("gallery/with-patients", "With patients after a follow-up visit", "Dr. Neema Bhat standing with two smiling patients at the hospital", True),
    ("gallery/pediatric-tumour-care-ethiopia", "Pediatric tumour care programme, Ethiopia · 2025", "Dr. Neema Bhat with doctors at a programme to improve pediatric tumour care in Ethiopia", False),
    ("portrait-coat", "Dr. Neema Bhat", "Dr. Neema Bhat in a white coat, arms folded, smiling", True),
    ("gallery/conference-mumbai-hematology-group", "Mumbai Hematology Group mid-term conference · 2025", "Dr. Neema Bhat with fellow delegates at the Mumbai Hematology Group mid-term conference", False),
    ("gallery/conference-bengaluru-physicians-update", "Bengaluru Physicians Update-4 · August 2025", "Dr. Neema Bhat with speakers at Bengaluru Physicians Update-4", False),
    ("portrait-scrubs", "Dr. Neema Bhat", "Dr. Neema Bhat in a white coat over blue scrubs", True),
]


def img_small(f):
    return f"assets/images/{f}-{'720' if f.startswith('portrait') else '760'}.webp"


# ------------------------------------------------------------------ HOME
def home():
    cards = "".join(f"""
          <a class="svc{' svc--feat' if s == 'bone-marrow-transplant' else ''}" id="svc-{s}" href="{BMT_PAGE if s == 'bone-marrow-transplant' else 'contact.html?topic=' + s}" data-fx="fade" style="--d:{(i % 3) * 0.08:.2f}s">
            <div class="svc__top">{ic(SVC_ICON_BY_SLUG.get(s, SVC_ICON[c]), 'ic svc__ic')}<span class="svc__cat">{c}</span></div>
            <h3>{n}</h3>
            <p>{d}</p>
            <span class="svc__go">{'Explore the transplant page' if s == 'bone-marrow-transplant' else 'Book a consultation'}{ic('i-go')}</span>
          </a>""" for i, (n, s, c, d) in enumerate(SERVICES))

    symptoms = [
        ("i-sun", "Constant tiredness", "Fatigue, breathlessness or looking pale for weeks."),
        ("i-drop", "Easy bruising or bleeding", "Nosebleeds, gum bleeding or bruises without injury."),
        ("i-thermo", "Recurring fevers", "Fevers or infections that keep coming back."),
        ("i-cells", "Swollen lymph nodes", "Painless lumps in the neck, armpit or groin."),
        ("i-bone", "Bone or joint pain", "Persistent aches, especially in children."),
        ("i-scale", "Unexplained weight loss", "With night sweats or loss of appetite."),
        ("i-flask", "Abnormal blood report", "Low or high Hb, WBC or platelet counts."),
        ("i-users", "Family history", "Thalassemia, hemophilia or sickle cell in the family."),
    ]
    sym = "".join(f'<li data-fx="fade" style="--d:{(k % 4) * 0.06:.2f}s">{ic(i)}<b>{t}</b><span>{d}</span></li>' for k, (i, t, d) in enumerate(symptoms))

    why = [
        ("i-award", "US-trained specialist", "MD in the USA and a fellowship (FAAP) in Pediatric Hematology, Oncology &amp; BMT at Penn State Health."),
        ("i-marrow", "Transplant leadership", "Program Director &amp; HOD of the Bone Marrow Transplant Unit at Bhagawan Mahaveer Jain Hospital."),
        ("i-users", "Children and adults", "One specialist for blood disorders and blood cancers across all ages."),
        ("i-chat", "Clear conversations", "Diagnosis, options and next steps explained in plain language for the whole family."),
    ]
    why_html = "".join(f'<li data-fx="fade" style="--d:{k * 0.08:.2f}s">{ic(i)}<div><b>{t}</b><span>{d}</span></div></li>' for k, (i, t, d) in enumerate(why))

    visit = [
        ("Book", "Call, WhatsApp or send a request online — we confirm a slot.",
         f"Call or WhatsApp {PHONE_DISPLAY}, or use the form on the Contact page. Share the patient’s age and main concern so the right slot can be arranged."),
        ("Bring reports", "Carry previous blood tests, scans and prescriptions.",
         "Bring recent blood counts, smear, bone marrow or biopsy reports, scans, discharge summaries and a list of current medicines — they save time and repeat tests."),
        ("Consultation", "A detailed history, examination and discussion of options.",
         "Dr. Neema Bhat takes a detailed history, examines the patient and reviews every report, then explains what the findings mean in plain language."),
        ("Your plan", "Tests, treatment and follow-up — explained step by step.",
         "You leave with a clear plan — further tests if needed, treatment options and when to follow up — with the whole family’s questions answered."),
    ]

    def fig(f, cap, alt, tall, hidden=False):
        extra = ' tabindex="-1"' if hidden else ""
        return f'<figure class="{"tall" if tall else ""}"><button type="button" data-full="assets/images/{f}.webp" data-cap="{cap}"{extra}><img src="{img_small(f)}" alt="{"" if hidden else alt}" loading="lazy" decoding="async"></button><figcaption>{cap}</figcaption></figure>'
    reel = "".join(fig(*g) for g in GALLERY)
    reel_dup = "".join(fig(*g, hidden=True) for g in GALLERY)

    faqs = [
        ("What does a hematologist treat?", "A hematologist diagnoses and treats disorders of the blood, bone marrow and lymph nodes — such as anaemia, bleeding and clotting problems, thalassemia, and blood cancers like leukaemia, lymphoma and myeloma."),
        ("Does Dr. Neema Bhat treat children as well as adults?", "Yes. Dr. Neema Bhat is trained in pediatric hematology and oncology and also treats adults, so she cares for blood disorders and blood cancers across all ages."),
        ("When should my child see a pediatric hemato-oncologist?", "If your child has unexplained paleness, frequent bruising or bleeding, persistent fevers, swollen glands, bone pain or an abnormal blood test, a specialist opinion helps find the cause early."),
        ("Where does Dr. Neema Bhat consult?", "OPD is at Apollo Hospitals, Bannerghatta Road (Mon – Sat, 11 AM – 4 PM), the Therapy Clinic (Mon – Sat, 5 – 7 PM) and Apollo One &amp; Apollo Cradle, Electronic City (Fridays, 2 – 4 PM)."),
        ("Can I get a second opinion?", "Yes. Bring your reports, biopsy results and current treatment details, and Dr. Neema Bhat will review the diagnosis and options with you."),
        ("How do I book an appointment?", f"Call or WhatsApp {PHONE_DISPLAY}, or use the booking form on the Contact page — your request opens in WhatsApp so you can review it before sending."),
    ]
    faq_html, ld_faq = faq_block(faqs)

    return head("Dr. Neema Bhat | Best Hematologist &amp; Pediatric Oncologist in Bangalore",
                "Dr. Neema Bhat is a Hematologist, Pediatric Oncologist and Bone Marrow Transplant specialist in Bangalore, caring for children and adults with blood disorders and blood cancers.",
                "", LD_PHYSICIAN + ld_faq) + f"""
<body data-page="home">{ICONS}{header('home')}
  <main id="main">
    <section class="hero" aria-labelledby="hero-title">
      <div class="wrap hero__in">
        <div class="hero__copy">
          <p class="tag" data-fx="wipe-x">{ic('i-award')}MD (USA) · FAAP · Penn State Health</p>
          <h1 id="hero-title" class="hero__title">
            <span class="sr-only">Best Hematologist, Pediatrician and Bone Marrow Transplant Specialist in Bangalore</span>
            <span aria-hidden="true">
              <span class="l" data-fx="wipe">Best</span>
              <span class="l fader" data-fader><span class="grad-text is-on">Hematologist</span><span class="grad-text">Pediatrician</span><span class="grad-text">BMT Specialist</span></span>
              <span class="l" data-fx="wipe" style="--d:.15s">in Bangalore</span>
            </span>
          </h1>
          <p class="hero__sub" data-fx="fade" style="--d:.3s">Dr. Neema Bhat is a US-trained Haemato-Oncologist for children and adults, and Head of the Bone Marrow Transplant Unit at Bhagawan Mahaveer Jain Hospital.</p>
          <div class="hero__acts" data-fx="fade" style="--d:.4s">
            <a class="btn btn--grad" href="contact.html">Book an Appointment{ic('i-go', 'ic ic--go')}</a>
            <a class="btn btn--line" href="tel:{PHONE_TEL}">{ic('i-phone')}{PHONE_DISPLAY}</a>
          </div>
          <div class="facts facts--hero" data-fx="fade" style="--d:.5s">
            <div class="fact">{ic('i-marrow')}<b>100+ transplants</b><span>Performed and supervised</span></div>
            <div class="fact">{ic('i-users')}<b>Children &amp; adults</b><span>Pediatric and adult BMT</span></div>
            <div class="fact">{ic('i-hosp')}<b>Dedicated unit</b><span>Bhagawan Mahaveer Jain Hospital</span></div>
          </div>
        </div>
        <div class="hero__art" data-fx="iris" style="--d:.1s">
          <div class="frame"><img src="assets/images/portrait-scrubs.webp" srcset="assets/images/portrait-scrubs-720.webp 720w, assets/images/portrait-scrubs.webp 1200w" sizes="(max-width: 900px) 80vw, 460px" alt="Dr. Neema Bhat in a white coat over blue scrubs, arms folded" width="1200" height="1873" fetchpriority="high"></div>
          <div class="chip chip--a">{ic('i-award')}<div><b>10+ Years</b><span>Specialist experience</span></div></div>
          {rating_badge()}
        </div>
      </div>
    </section>

    <section class="sec sec--tint" id="services" aria-labelledby="svc-title">
      <div class="wrap">
        {sec_head('Services', 'Best <span class="grad-text">Hematologist</span> in Bangalore', 'Nine specialist services across adult hematology and pediatric hemato-oncology — tap a service to book or learn more.', hid='svc-title')}
        <div class="svc-grid" data-svc>{cards}
        </div>
        <div class="dots" data-dots-for="svc" aria-hidden="true"></div>
      </div>
    </section>

    <section class="sec" aria-labelledby="sym-title">
      <div class="wrap">
        {sec_head('Know the signs', 'When should you see a <span class="grad-text">hematologist?</span>', 'Many blood disorders begin with everyday symptoms. See a specialist if any of these last for more than a few weeks.', center=True, hid='sym-title')}
        <ul class="sym">{sym}</ul>
        <p class="note-inline" style="text-align:center">These signs have many causes — a consultation and simple blood tests help find the right one.</p>
      </div>
    </section>

    <section class="sec sec--tint" aria-labelledby="why-title">
      <div class="wrap why">
        <div>
          <p class="tag" data-fx="wipe-x">Why patients choose her</p>
          <h2 class="title" id="why-title" data-fx="wipe">Specialist care, <span class="grad-text">explained clearly</span></h2>
          <ul class="why__list">{why_html}</ul>
        </div>
        <div class="nums">
          <div class="num" data-num><svg class="num__ring" viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="50"/><circle class="arc" cx="60" cy="60" r="50" pathLength="100"/></svg><b><span data-count="10">10</span>+</b><span>Years of specialist experience in hematology &amp; oncology</span></div>
          <div class="num" data-num><b class="grad-text"><span data-count="100">100</span>+</b><span>Bone marrow transplants</span></div>
          <div class="num" data-num><b class="grad-text"><span data-count="9">9</span></b><span>Specialist services</span></div>
          <div class="num" data-num><b class="grad-text"><span data-count="4">4</span></b><span>Hospitals &amp; clinics</span></div>
          <div class="num" data-num><b class="grad-text"><span data-count="6">6</span></b><span>Days a week OPD</span></div>
        </div>
      </div>
    </section>

    <section class="sec" aria-labelledby="v-title">
      <div class="wrap">
        {sec_head('Your first visit', 'What to expect, <span class="grad-text">step by step</span>', center=True, hid='v-title')}
        {stepper('steps', visit, 'First visit steps')}
      </div>
    </section>

    <section class="sec sec--tint" aria-labelledby="gal-title">
      <div class="wrap">
        {sec_head('Gallery', 'With patients, teams <span class="grad-text">&amp; peers</span>', 'Moments from the ward, the clinic and conferences. Tap a photo to view it larger.', hid='gal-title')}
      </div>
      <div class="reel" data-reel><div class="reel__track">{reel}<div class="reel__dup" aria-hidden="true" style="display:contents">{reel_dup}</div></div></div>
    </section>
{reviews_section()}
{where_section()}

    <section class="sec sec--tint" aria-labelledby="faq-title">
      <div class="wrap">
        {sec_head('FAQs', 'Common <span class="grad-text">questions</span>', center=True, hid='faq-title')}
        <div class="faq">{faq_html}</div>
      </div>
    </section>
{cta('Questions about a diagnosis? Talk to a specialist.', 'Consultations for children and adults at Apollo Hospitals, Bannerghatta Road.')}
  </main>
""" + footer()


# ------------------------------------------------------------------ ABOUT
def about():
    cards = [
        ("i-award", "US training", "MD in the United States, followed by a fellowship (FAAP) in Pediatric Hematology, Oncology &amp; BMT at Penn State Health."),
        ("i-marrow", "Transplant leadership", "Program Director and Head of the Bone Marrow Transplant Unit at Bhagawan Mahaveer Jain Hospital."),
        ("i-users", "Children &amp; adults", "Blood disorders and blood cancers across all ages, with plans built around each patient."),
        ("i-drop", "Benign hematology", "Anaemia, thalassemia, hemophilia, low platelets and other non-cancerous blood conditions."),
        ("i-cells", "Blood cancers", "Leukaemia, lymphoma and myeloma — diagnosis, chemotherapy, targeted therapy and transplant planning."),
        ("i-heart", "Community care", "Works with Sankalp India Foundation to make curative transplant accessible to children with thalassemia."),
    ]
    cards_html = "".join(f'<div class="card" data-fx="fade" style="--d:{(k % 3) * 0.08:.2f}s">{ic(i)}<h3>{t}</h3><p>{d}</p></div>' for k, (i, t, d) in enumerate(cards))
    POS = ' style="object-position:50% 25%"'
    tiles = [GALLERY[0], GALLERY[2], GALLERY[3], GALLERY[5], GALLERY[6], GALLERY[1]]
    collage = "".join(
        f'<button type="button" class="{"portrait-tile" if f.startswith("portrait") else ""}" data-full="assets/images/{f}.webp" data-cap="{cap}" data-fx="iris" style="--d:{k * 0.06:.2f}s"><img src="{img_small(f)}" alt="{alt}" loading="lazy"{POS if "with-patients" in f else ""}></button>'
        for k, (f, cap, alt, _) in enumerate(tiles))
    return head("About Dr. Neema Bhat | Hematologist &amp; Pediatric Oncologist, Bangalore",
                "About Dr. Neema Bhat: US-trained Haemato-Oncologist, FAAP fellowship at Penn State Health, Program Director &amp; HOD of the Bone Marrow Transplant Unit at Bhagawan Mahaveer Jain Hospital, Bangalore.",
                "about.html", LD_PHYSICIAN) + f"""
<body data-page="about">{ICONS}{header('about')}
  <main id="main">
    <section class="phero" aria-labelledby="ab-title">
      <div class="wrap phero__in">
        <div>
          <ol class="crumbs"><li><a href="index.html">Home</a></li><li>About</li></ol>
          <h1 id="ab-title" data-fx="wipe">Meet <span class="grad-text">Dr. Neema Bhat</span></h1>
          <p class="phero__sub" data-fx="fade" style="--d:.15s">Haemato-Oncologist, Pediatric Oncologist and Bone Marrow Transplant physician in Bangalore — caring for children and adults for more than ten years.</p>
        </div>
        <div class="phero__card" data-fx="fade" style="--d:.2s">
          <dl>
            <div><dt>Currently</dt><dd>Program Director &amp; HOD, Bone Marrow Transplant Unit</dd></div>
            <div><dt>Hospital</dt><dd>Bhagawan Mahaveer Jain Hospital, with Sankalp India Foundation</dd></div>
            <div><dt>Training</dt><dd>MD (USA) · Fellowship (FAAP), Penn State Health</dd></div>
          </dl>
        </div>
      </div>
    </section>

    <section class="sec">
      <div class="wrap story">
        <div class="pic" data-fx="iris">
          <img src="assets/images/portrait-coat.webp" srcset="assets/images/portrait-coat-720.webp 720w, assets/images/portrait-coat.webp 1200w" sizes="(max-width: 900px) 90vw, 440px" alt="Dr. Neema Bhat in a white coat, arms folded, smiling" width="1200" height="1911">
          <div class="pic__badge">{ic('i-award')}<div><b>Dr. Neema Bhat</b><span>MD (USA) · FAAP · Haemato-Oncologist</span></div></div>
        </div>
        <div>
          <p class="tag" data-fx="wipe-x">Her story</p>
          <h2 class="title" data-fx="wipe">A decade of dedicated <span class="grad-text">hematology-oncology</span> care</h2>
          <div class="prose" style="margin-top:20px">
            <p class="big" data-fx="fade">She completed her MD in the United States, followed by a fellowship (FAAP) in Pediatric Hematology, Oncology &amp; Bone Marrow Transplantation at Penn State Health.</p>
            <p data-fx="fade">Dr. Neema Bhat is a Haemato-Oncologist based in Bangalore, with more than ten years of specialised experience treating blood disorders and blood cancers in both children and adults. Her training shapes how she diagnoses, stages and treats every patient who comes to her.</p>
            <p data-fx="fade">She is currently Program Director and HOD of the Bone Marrow Transplant Unit at Bhagawan Mahaveer Jain Hospital, in association with Sankalp India Foundation, and has previously worked at BGS Gleneagles Global Hospitals and Fortis Hospitals.</p>
          </div>
          <p class="quote" data-fx="fade">A patient-centric approach — clear communication and treatment plans built around each individual, rather than a one-size-fits-all protocol.</p>
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

    <section class="sec sec--tint">
      <div class="wrap">
        {sec_head('Expertise', 'What sets her care <span class="grad-text">apart</span>', center=True)}
        <div class="cards3">{cards_html}</div>
      </div>
    </section>

    <section class="sec">
      <div class="wrap">
        {sec_head('Gallery', 'In the ward <span class="grad-text">&amp; beyond</span>', 'Tap any photo to view it larger.')}
        <div class="collage">{collage}</div>
      </div>
    </section>
{cta('Book a consultation with Dr. Neema Bhat.', 'For children and adults — OPD at Apollo Hospitals, Bannerghatta Road.')}
  </main>
""" + footer()


# ------------------------------------------------------------------ CONTACT
def contact():
    topics = "".join(f'<label class="choice"><input type="radio" name="topic" value="{n}" data-slug="{s}"{" checked" if i == 0 else ""}><span>{ic(SVC_ICON_BY_SLUG.get(s, SVC_ICON[c]))}{n}</span></label>' for i, (n, s, c, _) in enumerate(SERVICES))
    topics += f'<label class="choice"><input type="radio" name="topic" value="Second opinion" data-slug="second-opinion"><span>{ic("i-doc")}Second opinion</span></label>'
    return head("Contact Dr. Neema Bhat | Book an Appointment in Bangalore",
                "Book an appointment with Dr. Neema Bhat, Hematologist and Pediatric Oncologist. OPD at Apollo Hospitals, Bannerghatta Road. Call or WhatsApp +91 78997 56677.",
                "contact.html", LD_PHYSICIAN) + f"""
<body data-page="contact">{ICONS}{header('contact')}
  <main id="main">
    <section class="phero" aria-labelledby="c-title">
      <div class="wrap phero__in">
        <div>
          <ol class="crumbs"><li><a href="index.html">Home</a></li><li>Contact</li></ol>
          <h1 id="c-title" data-fx="wipe">Book a <span class="grad-text">consultation</span></h1>
          <p class="phero__sub" data-fx="fade" style="--d:.15s">Three quick steps — your request opens in WhatsApp so you can review it before sending.</p>
        </div>
        <div class="phero__card" data-fx="fade" style="--d:.2s">
          <dl>
            <div><dt>Call / WhatsApp</dt><dd><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></dd></div>
            <div><dt>OPD</dt><dd>Apollo Hospitals, Bannerghatta Road · Mon – Sat, 11 AM – 4 PM</dd></div>
            <div><dt>Evenings</dt><dd>Therapy Clinic · Mon – Sat, 5 – 7 PM</dd></div>
          </dl>
        </div>
      </div>
    </section>

    <section class="sec">
      <div class="wrap contact">
        <form class="wizard" id="wizard" novalidate>
          <div class="wizard__top"><h2>Request an appointment</h2><div class="progress" aria-hidden="true"><i class="is-on"></i><i></i><i></i></div></div>
          <p class="sr-only" aria-live="polite" data-wz-status>Step 1 of 3</p>
          <div class="wz-step is-active">
            <h3>Who is the consultation for?</h3>
            <div class="choices">
              <label class="choice"><input type="radio" name="who" value="Child" checked><span>{ic('i-child')}A child</span></label>
              <label class="choice"><input type="radio" name="who" value="Adult"><span>{ic('i-adult')}An adult</span></label>
            </div>
          </div>
          <div class="wz-step">
            <h3>What is it about?</h3>
            <div class="choices">{topics}</div>
          </div>
          <div class="wz-step">
            <h3>Your details</h3>
            <div class="field"><label for="w-name">Patient’s name</label><input id="w-name" name="name" type="text" autocomplete="name" required><span class="field__err">Please enter the patient’s name</span></div>
            <div class="field"><label for="w-phone">Phone number</label><input id="w-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" required pattern="[0-9+\\s\\-]{{8,}}"><span class="field__err">Please enter a valid phone number</span></div>
            <div class="field"><label for="w-msg">Anything else? (optional)</label><textarea id="w-msg" name="message" rows="3"></textarea></div>
          </div>
          <div class="wz-nav">
            <button class="btn btn--line" type="button" data-wz-back hidden>Back</button>
            <button class="btn btn--grad" type="button" data-wz-next style="margin-left:auto">Continue{ic('i-go', 'ic ic--go')}</button>
            <button class="btn btn--grad" type="submit" data-wz-send hidden style="margin-left:auto">Send on WhatsApp{ic('i-wa')}</button>
          </div>
          <p class="wz-note">For medical emergencies, please visit the nearest emergency department.</p>
        </form>

        <div>
          <div class="ccards">
            <a class="ccard" href="tel:{PHONE_TEL}">{ic('i-phone')}<span><small>Call</small><b>{PHONE_DISPLAY}</b></span>{ic('i-go', 'ic ic--go')}</a>
            <a class="ccard" href="{WA}" target="_blank" rel="noopener">{ic('i-wa')}<span><small>WhatsApp</small><b>{PHONE_DISPLAY}</b></span>{ic('i-go', 'ic ic--go')}</a>
            <a class="ccard" href="https://www.google.com/maps/search/?api=1&amp;query=Apollo+Hospitals+Bannerghatta+Road+Bengaluru" target="_blank" rel="noopener">{ic('i-pin')}<span><small>OPD · Directions</small><b>Apollo Hospitals, Bannerghatta Road</b></span>{ic('i-go', 'ic ic--go')}</a>
          </div>
          <div class="map"><iframe title="Map showing Apollo Hospitals, Bannerghatta Road, Bengaluru" src="https://maps.google.com/maps?q=Apollo%20Hospitals%2C%20Bannerghatta%20Road%2C%20Bengaluru&amp;z=15&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
        </div>
      </div>
    </section>
{where_section('Where to find her, <span class="grad-text">day by day</span>').replace('class="sec"', 'class="sec sec--tint"', 1)}
  </main>
""" + footer(fab=False)


# ------------------------------------------------------------------ BMT SERVICE
def bmt():
    faqs = [
        ("What is a bone marrow transplant?", "It replaces damaged or diseased bone marrow with healthy blood-forming stem cells. The new cells settle in the marrow and begin producing healthy red cells, white cells and platelets."),
        ("Is a bone marrow transplant only for cancer?", "No. Besides leukaemia, lymphoma and myeloma, transplants are used for non-cancerous conditions such as thalassemia major, aplastic anaemia, sickle cell disease and some inherited immune disorders."),
        ("Who can be a donor?", "For an allogeneic transplant, brothers and sisters are usually tested first — each full sibling has roughly a one-in-four chance of being a full match. Unrelated volunteer donors and half-matched (haploidentical) family donors may also be options."),
        ("How is a donor matched?", "Donors are matched by HLA typing, a blood or cheek-swab test that compares immune markers between the patient and the potential donor."),
        ("Is donating stem cells safe for the donor?", "For most healthy donors it is. Stem cells are commonly collected from the blood after a few days of growth-factor injections, and donors usually return to normal activities within days."),
        ("Is the stem cell infusion painful?", "The infusion itself is given through a drip, much like a blood transfusion, and is usually not painful. The preparation (conditioning) and recovery phases need close care, which the team plans in detail with you."),
        ("How long is the hospital stay?", "It varies with the type of transplant and the condition being treated. Hospital stays are commonly several weeks, until blood counts recover and the patient is well enough to go home."),
        ("What happens after discharge?", "Regular follow-up visits, blood tests and medicines continue for months while the immune system recovers. The team guides the family on infection precautions, diet, vaccinations and returning to school or work."),
    ]
    faq_html, ld_faq = faq_block(faqs)
    ld_proc = '  <script type="application/ld+json">{"@context":"https://schema.org","@type":"MedicalProcedure","name":"Bone Marrow Transplantation","alternateName":"Stem cell transplant","procedureType":"https://schema.org/TherapeuticProcedure","performer":{"@type":"Physician","name":"Dr. Neema Bhat"}}</script>\n'

    facts = [("i-marrow", "100+ transplants", "Performed and supervised"), ("i-users", "Children &amp; adults", "Pediatric and adult BMT"),
             ("i-link", "Two types", "Autologous &amp; allogeneic"), ("i-hosp", "Dedicated unit", "Bhagawan Mahaveer Jain Hospital")]
    facts_html = "".join(f'<div class="fact" data-fx="fade" style="--d:{k * 0.06:.2f}s">{ic(i)}<b>{t}</b><span>{d}</span></div>' for k, (i, t, d) in enumerate(facts))

    conds = [
        ("i-cells", "Leukaemia", "Acute and chronic leukaemias, especially when high-risk or relapsed."),
        ("i-cells", "Lymphoma", "Hodgkin and non-Hodgkin lymphoma that returns after treatment."),
        ("i-cells", "Multiple myeloma", "Autologous transplant is a standard part of treatment for many patients."),
        ("i-drop", "Thalassemia major", "A matched transplant can free a child from lifelong transfusions."),
        ("i-drop", "Aplastic anaemia", "When the marrow stops making enough blood cells."),
        ("i-drop", "Sickle cell disease", "For severe disease with repeated complications."),
        ("i-shield", "Immune disorders", "Inherited immune deficiencies such as SCID."),
        ("i-child", "Childhood cancers", "Selected solid tumours such as neuroblastoma."),
        ("i-marrow", "Marrow failure syndromes", "Inherited conditions such as Fanconi anaemia."),
    ]
    conds_html = "".join(f'<li data-fx="fade" style="--d:{(k % 3) * 0.06:.2f}s"><b>{ic(i)}{t}</b><p>{d}</p></li>' for k, (i, t, d) in enumerate(conds))

    donors = [
        ("i-users", "Matched sibling donor", "A brother or sister with a full HLA match — often the first choice."),
        ("i-link", "Matched unrelated donor", "A volunteer found through stem cell donor registries."),
        ("i-heart", "Half-matched family donor", "A parent, child or sibling who is a half match (haploidentical) — widening access when no full match is found."),
    ]
    donors_html = "".join(f'<div class="card" data-fx="fade" style="--d:{k * 0.08:.2f}s">{ic(i)}<h3>{t}</h3><p>{d}</p></div>' for k, (i, t, d) in enumerate(donors))

    steps = [
        ("Evaluation", "Tests, donor matching and counselling so the family understands each step.",
         "The team reviews the diagnosis and overall health — blood tests, heart, lung and kidney checks and infection screening — and HLA-tests family members for a match. The family meets the team to understand the plan, the risks and the timeline."),
        ("Collection", "Stem cells are collected from the patient (autologous) or a donor (allogeneic).",
         "For an autologous transplant, the patient’s own stem cells are collected from the blood after growth-factor injections and frozen. For an allogeneic transplant, cells are collected from the donor’s blood or bone marrow."),
        ("Conditioning", "Chemotherapy, sometimes with radiation, prepares the marrow for new cells.",
         "Over several days, chemotherapy — sometimes with radiation — clears the diseased marrow and makes room for the new cells. In allogeneic transplants it also lowers immunity so donor cells are not rejected."),
        ("Infusion", "Healthy stem cells are given through a drip, much like a transfusion.",
         "On “Day 0” the stem cells are given through the central line, much like a blood transfusion. It is usually not painful, and the family can stay close by."),
        ("Engraftment", "New cells settle in and start making blood, with close monitoring.",
         "Over the following weeks the new cells settle in the marrow and begin making blood. Until counts recover, the patient stays in a protected room with transfusions, antibiotics and daily monitoring."),
        ("Recovery", "A gradual return to daily life with long-term follow-up.",
         "After discharge, regular visits continue for months — checking counts, adjusting medicines, watching for graft-versus-host disease and planning re-vaccination and the return to school or work."),
    ]

    before = ["Detailed review of diagnosis and disease status", "Blood tests, imaging and heart, lung and kidney checks", "HLA typing of the patient and family members",
              "Dental and infection screening", "Central line placement for medicines and blood draws", "Counselling for the patient and caregivers"]
    before_html = "".join(f'<li>{ic("i-check")}{t}</li>' for t in before)

    why = [
        ("i-award", "US fellowship training", "Fellowship (FAAP) in Pediatric Hematology, Oncology &amp; BMT at Penn State Health."),
        ("i-marrow", "Leads a transplant unit", "Program Director &amp; HOD, Bone Marrow Transplant Unit, Bhagawan Mahaveer Jain Hospital."),
        ("i-heart", "Access for families", "Works with Sankalp India Foundation to make curative transplant reachable for children with thalassemia."),
        ("i-chat", "One doctor, start to finish", "From the first evaluation to long-term follow-up, families know who is guiding their care."),
    ]
    why_html = "".join(f'<li data-fx="fade" style="--d:{k * 0.08:.2f}s">{ic(i)}<div><b>{t}</b><span>{d}</span></div></li>' for k, (i, t, d) in enumerate(why))

    return head("Bone Marrow Transplant in Bangalore | Dr. Neema Bhat",
                "Bone marrow (stem cell) transplant in Bangalore with Dr. Neema Bhat, Program Director &amp; HOD of the BMT Unit at Bhagawan Mahaveer Jain Hospital. Autologous and allogeneic transplants for children and adults.",
                BMT_PAGE, LD_PHYSICIAN + ld_proc + ld_faq) + f"""
<body data-page="service">{ICONS}{header('service')}
  <main id="main">
    <section class="phero" aria-labelledby="b-title" style="padding-bottom:clamp(56px,6vw,84px)">
      <div class="wrap phero__in">
        <div>
          <ol class="crumbs"><li><a href="index.html">Home</a></li><li><a href="index.html#services">Services</a></li><li>Bone Marrow Transplant</li></ol>
          <h1 id="b-title" data-fx="wipe">Bone Marrow <span class="grad-text">Transplant</span> in Bangalore</h1>
          <p class="phero__sub" data-fx="fade" style="--d:.15s">Autologous and allogeneic stem cell transplants for children and adults — led by Dr. Neema Bhat, Program Director and Head of the Bone Marrow Transplant Unit at Bhagawan Mahaveer Jain Hospital.</p>
          <div class="hero__acts" data-fx="fade" style="--d:.25s">
            <a class="btn btn--grad" href="contact.html?topic=bone-marrow-transplant">Discuss a transplant{ic('i-go', 'ic ic--go')}</a>
            <a class="btn btn--line" href="tel:{PHONE_TEL}">{ic('i-phone')}{PHONE_DISPLAY}</a>
          </div>
        </div>
        <div class="phero__card" data-fx="fade" style="--d:.2s">
          <dl>
            <div><dt>Transplants</dt><dd>Autologous &amp; allogeneic</dd></div>
            <div><dt>For</dt><dd>Children and adults · cancers and non-cancerous blood disorders</dd></div>
            <div><dt>Unit</dt><dd>Bhagawan Mahaveer Jain Hospital, with Sankalp India Foundation</dd></div>
          </dl>
        </div>
      </div>
    </section>

    <div class="wrap"><div class="facts">{facts_html}</div></div>

    <section class="sec" aria-labelledby="ov-title">
      <div class="wrap split">
        <div>
          <p class="tag" data-fx="wipe-x">Overview</p>
          <h2 class="title" id="ov-title" data-fx="wipe">A new source of <span class="grad-text">healthy blood cells</span></h2>
          <p class="lead" data-fx="fade">A bone marrow (stem cell) transplant replaces damaged or diseased marrow with healthy blood-forming stem cells. For many blood cancers and serious blood disorders, it offers the best chance of long-term control — and for some, a cure.</p>
          <p class="lead" data-fx="fade">Stem cells can come from the bone marrow, from the bloodstream (peripheral blood stem cells) or, in some cases, from umbilical cord blood. Every transplant is planned in detail, from choosing the right type and donor to the months of follow-up afterwards, with the family involved at each step.</p>
        </div>
        <div class="cellviz" data-cellviz aria-hidden="true">
          <svg viewBox="0 0 460 460">
            <defs><linearGradient id="cg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4fb6bb"/><stop offset=".5" stop-color="#2f84a0"/><stop offset="1" stop-color="#0f265d"/></linearGradient></defs>
            <circle class="orb" cx="230" cy="230" r="210"/><circle class="orb" cx="230" cy="230" r="160" style="transition-delay:.3s"/><circle class="orb" cx="230" cy="230" r="110" style="transition-delay:.6s"/>
            <circle class="core" cx="230" cy="230" r="72" fill="url(#cg)"/>
            <text x="230" y="224" text-anchor="middle">Stem</text><text x="230" y="246" text-anchor="middle">cells</text>
            <g class="sat"><circle cx="230" cy="20" r="11"/><circle cx="440" cy="230" r="7"/></g>
            <g class="sat sat2"><circle cx="230" cy="390" r="9"/><circle cx="70" cy="230" r="6"/></g>
          </svg>
        </div>
      </div>
    </section>

    <section class="sec sec--tint" aria-labelledby="w-title">
      <div class="wrap">
        {sec_head('Who may need it', 'Conditions treated with <span class="grad-text">transplant</span>', 'A transplant is considered when it offers a better chance of cure or long-term control than other treatments.', hid='w-title')}
        <ul class="conds">{conds_html}</ul>
      </div>
    </section>

    <section class="sec" aria-labelledby="ty-title">
      <div class="wrap split">
        <div>
          <p class="tag" data-fx="wipe-x">Types of transplant</p>
          <h2 class="title" id="ty-title" data-fx="wipe">Two ways to <span class="grad-text">rebuild the marrow</span></h2>
          <p class="lead" data-fx="fade">The right type depends on the diagnosis, the stage of disease and whether a suitable donor is available.</p>
          <div class="switch" role="tablist" aria-label="Transplant type" data-switch>
            <button type="button" role="tab" aria-selected="true" aria-controls="t-auto" id="tab-auto">Autologous</button>
            <button type="button" role="tab" aria-selected="false" aria-controls="t-allo" id="tab-allo" tabindex="-1">Allogeneic</button>
            <span class="switch__thumb" aria-hidden="true"></span>
          </div>
        </div>
        <div>
          <div class="panel" id="t-auto" role="tabpanel" aria-labelledby="tab-auto">
            <h3>Autologous — your own cells</h3>
            <p>The patient’s own stem cells are collected and frozen, then returned after high-dose treatment to rebuild the marrow.</p>
            <ul class="list"><li>{ic('i-check')}No donor needed</li><li>{ic('i-check')}Often used for lymphoma, myeloma and some solid tumours</li><li>{ic('i-check')}No risk of graft-versus-host disease</li><li>{ic('i-check')}Usually a shorter recovery</li></ul>
          </div>
          <div class="panel" id="t-allo" role="tabpanel" aria-labelledby="tab-allo" hidden>
            <h3>Allogeneic — cells from a donor</h3>
            <p>Healthy stem cells come from a donor — a matched sibling, an unrelated volunteer or a half-matched family member.</p>
            <ul class="list"><li>{ic('i-check')}Used for leukaemia, thalassemia, aplastic anaemia and immune disorders</li><li>{ic('i-check')}The donor’s immune cells can help fight remaining disease</li><li>{ic('i-check')}Careful donor matching and close follow-up are essential</li><li>{ic('i-check')}Monitoring for graft-versus-host disease</li></ul>
          </div>
        </div>
      </div>
    </section>

    <section class="sec sec--tint" aria-labelledby="d-title">
      <div class="wrap">
        {sec_head('Donor matching', 'Finding the <span class="grad-text">right donor</span>', 'Matching is done by HLA typing — a simple blood or cheek-swab test for the patient and potential donors.', hid='d-title')}
        <div class="cards3">{donors_html}</div>
      </div>
    </section>

    <section class="sec" aria-labelledby="j-title">
      <div class="wrap">
        {sec_head('The journey', 'Six stages, <span class="grad-text">one team</span>', center=True, hid='j-title')}
        {stepper('journey', steps, 'Transplant journey')}
      </div>
    </section>

    <section class="sec sec--tint" aria-labelledby="ba-title">
      <div class="wrap cols2">
        <div class="box" data-fx="fade">
          <h3 id="ba-title">{ic('i-doc')}Before the transplant</h3>
          <ul class="list">{before_html}</ul>
        </div>
        <div class="box" data-fx="fade" style="--d:.1s">
          <h3>{ic('i-shield')}After the transplant</h3>
          <ul class="list">
            <li>{ic('i-check')}Protective isolation while counts recover</li>
            <li>{ic('i-check')}Daily blood tests, transfusions and infection control</li>
            <li>{ic('i-check')}Monitoring for graft-versus-host disease</li>
            <li>{ic('i-check')}Diet, hygiene and medicine plan for home</li>
            <li>{ic('i-check')}Re-vaccination as the immune system rebuilds</li>
            <li>{ic('i-check')}Guidance on returning to school or work</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="sec" aria-labelledby="wy-title">
      <div class="wrap why">
        <div class="pic" data-fx="iris">
          <img src="assets/images/portrait-scrubs.webp" srcset="assets/images/portrait-scrubs-720.webp 720w, assets/images/portrait-scrubs.webp 1200w" sizes="(max-width: 900px) 90vw, 440px" alt="Dr. Neema Bhat in a white coat over blue scrubs" width="1200" height="1873" loading="lazy">
          <div class="pic__badge">{ic('i-marrow')}<div><b>Dr. Neema Bhat</b><span>Program Director &amp; HOD, BMT Unit</span></div></div>
        </div>
        <div>
          <p class="tag" data-fx="wipe-x">Why Dr. Neema Bhat</p>
          <h2 class="title" id="wy-title" data-fx="wipe">Transplant care led by a <span class="grad-text">specialist</span></h2>
          <ul class="why__list">{why_html}</ul>
        </div>
      </div>
    </section>

    <section class="sec sec--tint" aria-labelledby="fq-title">
      <div class="wrap">
        {sec_head('Questions', 'Bone marrow transplant <span class="grad-text">FAQs</span>', center=True, hid='fq-title')}
        <div class="faq">{faq_html}</div>
        <p class="small">General information only — every patient is different. Your consultation is the place for advice specific to you or your child.</p>
      </div>
    </section>
{cta('Considering a transplant? Talk it through.', 'Bring your reports — Dr. Neema Bhat will explain the options for you or your child.', 'bone-marrow-transplant')}
  </main>
""" + footer()


if __name__ == "__main__":
    for name, fn in [("index.html", home), ("about.html", about), ("contact.html", contact), (BMT_PAGE, bmt)]:
        (ROOT / name).write_text(fn(), encoding="utf-8")
        print("built", name)
