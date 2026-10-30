"""Builds the static pages from shared parts.

Run:  python3 build.py
Edit shared pieces (header, menu, footer, services list) here, then rebuild.
The generated .html files are what gets published.
"""
from hashlib import md5
from pathlib import Path

ROOT = Path(__file__).parent


def asset_v(rel):
    """Short content hash so browsers fetch the new file after every change."""
    return md5((ROOT / rel).read_bytes()).hexdigest()[:8]
PHONE_DISPLAY = "+91 78997 56677"
PHONE_TEL = "+917899756677"
WA = "https://wa.me/917899756677"
# Live site address (no "www"): used for canonical links, sitemap and llms.txt.
SITE_URL = "https://drneemabhat.com"

# Footer social links. Replace each "#" with the profile address; delete a line to hide that icon.
SOCIAL = [
    ("Facebook", "i-fb", "#"),
    ("Instagram", "i-ig", "#"),
    ("LinkedIn", "i-in", "#"),
    ("YouTube", "i-yt", "#"),
]

# name, slug, category, short description
SERVICES = [
    ("Hematology Treatment", "hematology", "Hematology", "Anemia, bleeding and clotting problems, abnormal blood counts and blood cancers, finding the exact cause."),
    ("Anemia Treatment", "anaemia", "Hematology", "Iron-deficiency, nutritional and inherited anemias, finding the cause, not just treating the count."),
    ("Thalassemia Treatment", "thalassemia", "Hematology", "Transfusion and chelation care, carrier testing and curative bone marrow transplant."),
    ("Leukemia Treatment", "leukaemia", "Hematology", "Acute and chronic leukemias, with chemotherapy, targeted therapy and transplant planning."),
    ("Lymphoma Treatment", "lymphoma", "Hematology", "Hodgkin and non-Hodgkin lymphoma, accurate subtyping and treatment matched to each type."),
    ("Multiple Myeloma Treatment", "multiple-myeloma", "Hematology", "Plasma cell cancer care: staging, drug therapy, transplant and protection for bones and kidneys."),
    ("Pediatric Oncology", "pediatric-oncology", "Pediatric", "Childhood leukemia, lymphoma, solid tumours and blood disorders, with child-friendly care."),
    ("Brain Tumor Treatment", "brain-tumor", "Pediatric & Adult", "Brain and spinal tumours, with surgery, radiation and chemotherapy planned together."),
    ("Bone Marrow Transplant", "bone-marrow-transplant", "Pediatric & Adult", "Autologous and allogeneic transplants for children and adults, from donor matching to follow-up."),
]
BMT_PAGE = "bone-marrow-transplant.html"

# Mobile treatments layout: "icons" (app icon grid) or "tiles" (bento tiles).
# The visitor can switch with the Option 1 / Option 2 control; set SHOW_SVC_SWITCH = False
# once a final layout is chosen to hide the control.
SVC_MOBILE_DEFAULT = "icons"
SHOW_SVC_SWITCH = True
SHORT_NAMES = {
    "hematology": "Hematology", "pediatric-oncology": "Pediatric Oncology", "brain-tumor": "Brain Tumor",
    "anaemia": "Anemia", "thalassemia": "Thalassemia", "leukaemia": "Leukemia", "lymphoma": "Lymphoma",
    "multiple-myeloma": "Multiple Myeloma", "bone-marrow-transplant": "Bone Marrow Transplant",
}

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

# Review cards on the home page. These are SAMPLES (layout only), replace each
# with a real patient review and set sample=False before going live.
REVIEWS = [
    ("Parent of a patient", "Thalassemia care", "Sample review: replace with a real patient review. Share what the family valued: clear explanations, careful review of reports, time taken to answer questions.", True),
    ("Patient", "Hematology consultation", "Sample review: replace with a real patient review from Google or the hospital’s feedback page.", True),
    ("Family member", "Bone marrow transplant", "Sample review: replace with a real patient review describing their experience of the transplant journey.", True),
    ("Parent of a patient", "Childhood leukaemia", "Sample review: replace with a real review from a family whose child was treated for leukaemia.", True),
    ("Patient", "Anaemia treatment", "Sample review: replace with a real review about diagnosis and follow-up for anaemia.", True),
    ("Patient", "Second opinion", "Sample review: replace with a real review from a patient who came for a second opinion.", True),
]


ANEMIA_PAGE = "anemia-treatment.html"
HEMA_PAGE = "hematology-treatment.html"
THAL_PAGE = "thalassemia-treatment.html"
LEUK_PAGE = "leukemia-treatment.html"
MYEL_PAGE = "multiple-myeloma-treatment.html"
LYMPH_PAGE = "lymphoma-treatment.html"
PEDONC_PAGE = "pediatric-oncology-treatment.html"
BRAIN_PAGE = "brain-tumor-treatment.html"
# treatments that have their own page
SERVICE_PAGES = {"bone-marrow-transplant": BMT_PAGE, "anaemia": ANEMIA_PAGE, "thalassemia": THAL_PAGE,
                 "leukaemia": LEUK_PAGE, "lymphoma": LYMPH_PAGE, "multiple-myeloma": MYEL_PAGE,
                 "hematology": HEMA_PAGE, "pediatric-oncology": PEDONC_PAGE, "brain-tumor": BRAIN_PAGE}


def svc_href(slug):
    return SERVICE_PAGES.get(slug, f"index.html#svc-{slug}")


def svc_link(slug):
    """Where a treatment card/icon goes: its own page, else the booking form."""
    return SERVICE_PAGES.get(slug, "contact.html?topic=" + slug)


ICONS = """
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
  <symbol id="i-phone" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></symbol>
  <symbol id="i-wa" viewBox="0 0 24 24"><path d="M4 20l1.3-4A8 8 0 1 1 8 18.7L4 20z"/><path d="M9 9.5c.3 2 2.3 4.3 5 5l1.2-1.3-1.8-1-1 .8c-1-.4-1.8-1.2-2.2-2.2l.8-1-1-1.8L9 9.5z"/></symbol>
  <symbol id="i-pin" viewBox="0 0 24 24"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></symbol>
  <symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></symbol>
  <symbol id="i-cal" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18M12 14v4M10 16h4"/></symbol>
  <symbol id="i-go" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
  <symbol id="i-chev" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6"/></symbol>
  <symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 8h16M4 16h10"/></symbol>
  <symbol id="i-check" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></symbol>
  <symbol id="i-star" viewBox="0 0 24 24"><path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/></symbol>
  <symbol id="i-chat" viewBox="0 0 24 24"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 9h8M8 13h5"/></symbol>
  <symbol id="i-sun" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></symbol>
  <symbol id="i-moon" viewBox="0 0 24 24"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></symbol>
  <symbol id="i-users" viewBox="0 0 24 24"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></symbol>
  <symbol id="i-adult" viewBox="0 0 24 24"><path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></symbol>
  <symbol id="i-drop" viewBox="0 0 24 24"><path d="M12 22a7 7 0 0 0 7-7c0-2-1-3.9-3-5.5s-3.5-4-4-6.5c-.5 2.5-2 4.9-4 6.5C6 11.1 5 13 5 15a7 7 0 0 0 7 7z"/><path d="M9 15a3 3 0 0 0 3 3"/></symbol>
  <symbol id="i-child" viewBox="0 0 24 24"><path d="M9 12h.01M15 12h.01"/><path d="M10 16c.5.3 1.2.5 2 .5s1.5-.2 2-.5"/><path d="M19 6.3a9 9 0 0 1 1.8 3.9 2 2 0 0 1 0 3.6 9 9 0 0 1-17.6 0 2 2 0 0 1 0-3.6A9 9 0 0 1 12 3c2 0 3.5 1.1 3.5 2.5s-.9 2.5-2 2.5c-.8 0-1.5-.4-1.5-1"/></symbol>
  <symbol id="i-award" viewBox="0 0 24 24"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></symbol>
  <symbol id="i-stetho" viewBox="0 0 24 24"><path d="M11 2v2M5 2v2"/><path d="M5 3H4a2 2 0 0 0-2 2v4a6 6 0 0 0 12 0V5a2 2 0 0 0-2-2h-1"/><path d="M8 15a6 6 0 0 0 12 0v-3"/><circle cx="20" cy="10" r="2"/></symbol>
  <symbol id="i-micro" viewBox="0 0 24 24"><path d="M6 18h8M3 22h18"/><path d="M14 22a7 7 0 1 0 0-14h-1"/><path d="M9 14h2"/><path d="M9 12a2 2 0 0 1-2-2V6h6v4a2 2 0 0 1-2 2Z"/><path d="M12 6V3a1 1 0 0 0-1-1H9a1 1 0 0 0-1 1v3"/></symbol>
  <symbol id="i-syringe" viewBox="0 0 24 24"><path d="m18 2 4 4M17 7l3-3"/><path d="M19 9 8.7 19.3c-1 1-2.5 1-3.4 0l-.6-.6c-1-1-1-2.5 0-3.4L15 5"/><path d="m9 11 4 4M5 19l-3 3M14 4l6 6"/></symbol>
  <symbol id="i-pill" viewBox="0 0 24 24"><path d="m10.5 20.5 10-10a4.95 4.95 0 1 0-7-7l-10 10a4.95 4.95 0 1 0 7 7Z"/><path d="m8.5 8.5 7 7"/></symbol>
  <symbol id="i-flask" viewBox="0 0 24 24"><path d="M14.5 2v17.5a2.5 2.5 0 0 1-5 0V2"/><path d="M8.5 2h7M14.5 16h-5"/></symbol>
  <symbol id="i-link" viewBox="0 0 24 24"><path d="M2 15c6.67-6 13.33 0 20-6"/><path d="M9 22c1.8-2 2.52-4 2.8-6M15 2c-1.8 2-2.52 4-2.8 6"/><path d="m17 6-2.9-2.9M7 18l2.9 2.9M16.5 10.5l1 1M6.5 12.5l1 1M10 16l1.5 1.5M14 8l-1.5-1.5M20 9l.9.9M3.1 14.1 4 15"/></symbol>
  <symbol id="i-brain" viewBox="0 0 24 24"><path d="M12 5a3 3 0 1 0-6 .13 4 4 0 0 0-2.52 5.77 4 4 0 0 0 .55 6.59A4 4 0 1 0 12 18Z"/><path d="M12 5a3 3 0 1 1 6 .13 4 4 0 0 1 2.52 5.77 4 4 0 0 1-.55 6.59A4 4 0 1 1 12 18Z"/><path d="M15 13a4.5 4.5 0 0 1-3-4 4.5 4.5 0 0 1-3 4"/></symbol>
  <symbol id="i-bone" viewBox="0 0 24 24"><path d="M17 10c.7-.7 1.69 0 2.5 0a2.5 2.5 0 1 0 0-5 .5.5 0 0 1-.5-.5 2.5 2.5 0 1 0-5 0c0 .81.7 1.8 0 2.5l-7 7c-.7.7-1.69 0-2.5 0a2.5 2.5 0 0 0 0 5c.28 0 .5.22.5.5a2.5 2.5 0 1 0 5 0c0-.81-.7-1.8 0-2.5Z"/></symbol>
  <symbol id="i-heart" viewBox="0 0 24 24"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/><path d="M3.22 12H9.5l.5-1 2 4.5 2-7 1.5 3.5h5.27"/></symbol>
  <symbol id="i-thermo" viewBox="0 0 24 24"><path d="M14 4v10.54a4 4 0 1 1-4 0V4a2 2 0 0 1 4 0Z"/><path d="M12 9v8"/></symbol>
  <symbol id="i-shield" viewBox="0 0 24 24"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="M9 12h6M12 9v6"/></symbol>
  <symbol id="i-doc" viewBox="0 0 24 24"><rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M9 14h6M12 11v6"/></symbol>
  <symbol id="i-hosp" viewBox="0 0 24 24"><path d="M12 6v4M14 8h-4M14 14h-4M14 18h-4"/><path d="M18 12h2a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-9a2 2 0 0 1 2-2h2"/><path d="M18 22V4a2 2 0 0 0-2-2H8a2 2 0 0 0-2 2v18"/></symbol>
  <symbol id="i-scale" viewBox="0 0 24 24"><circle cx="12" cy="5" r="3"/><path d="M6.5 8a2 2 0 0 0-1.9 1.46L2.1 18.5A2 2 0 0 0 4 21h16a2 2 0 0 0 1.93-2.54L19.4 9.5A2 2 0 0 0 17.48 8Z"/></symbol>
  <symbol id="i-cells" viewBox="0 0 24 24"><ellipse cx="8" cy="9" rx="5.5" ry="4.5"/><ellipse cx="8" cy="9" rx="2" ry="1.5"/><ellipse cx="16" cy="15.5" rx="5.5" ry="4.5"/><ellipse cx="16" cy="15.5" rx="2" ry="1.5"/></symbol>
  <symbol id="i-marrow" viewBox="0 0 24 24"><path d="M7 2h10v9a5 5 0 0 1-10 0z"/><path d="M7 7h10M12 16v3"/><path d="M12 19a3 3 0 0 1-3 3"/><path d="M10.5 10.5h3M12 9v3"/></symbol>
  <symbol id="i-lungs" viewBox="0 0 24 24"><path d="M12 4v8"/><path d="M12 12c-1 0-2 1-2 2v5c0 1-1 2-3 2s-3-1-3-3v-4c0-3 2-7 4-7s2 2 2 3"/><path d="M12 12c1 0 2 1 2 2v5c0 1 1 2 3 2s3-1 3-3v-4c0-3-2-7-4-7s-2 2-2 3"/></symbol>
  <symbol id="i-ribbon" viewBox="0 0 24 24"><path d="M12 2.5c-2.2 0-4 1.8-4 4 0 2.4 1.9 4.6 4 7.3 2.1-2.7 4-4.9 4-7.3 0-2.2-1.8-4-4-4Z"/><path d="M10 11.6 5 20.5l3.2.4 1.6 2.6L14 14.6"/><path d="M14 11.6l5 8.9-3.2.4-1.6 2.6-2.4-4.3"/></symbol>
  <symbol id="i-radiation" viewBox="0 0 24 24"><circle cx="12" cy="12" r="1.5"/><path d="M7.5 4.2C5 5.6 3.3 8.2 3 11h5a4 4 0 0 1 2-3.4z"/><path d="M16.5 4.2C19 5.6 20.7 8.2 21 11h-5a4 4 0 0 0-2-3.4z"/><path d="M7.5 19.8c2.8 1.6 6.2 1.6 9 0L14 15.5a4 4 0 0 1-4 0z"/></symbol>
  <symbol id="i-apple" viewBox="0 0 24 24"><path d="M12 20.94c1.5 0 2.75 1.06 4 1.06 3 0 6-8 6-12.22A4.91 4.91 0 0 0 17 5c-2.22 0-4 1.44-5 2-1-.56-2.78-2-5-2a4.9 4.9 0 0 0-5 4.78C2 14 5 22 8 22c1.25 0 2.5-1.06 4-1.06Z"/><path d="M10 2c1 .5 2 2 2 5"/></symbol>
  <symbol id="i-eye" viewBox="0 0 24 24"><path d="M2.06 12.35a1 1 0 0 1 0-.7 10.75 10.75 0 0 1 19.88 0 1 1 0 0 1 0 .7 10.75 10.75 0 0 1-19.88 0"/><circle cx="12" cy="12" r="3"/></symbol>
  <symbol id="i-bed" viewBox="0 0 24 24"><path d="M2 4v16M2 8h18a2 2 0 0 1 2 2v10M2 17h20M6 8v9"/></symbol>
  <symbol id="i-activity" viewBox="0 0 24 24"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></symbol>
  <symbol id="i-fb" viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></symbol>
  <symbol id="i-ig" viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/></symbol>
  <symbol id="i-in" viewBox="0 0 24 24"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></symbol>
  <symbol id="i-yt" viewBox="0 0 24 24"><path d="M2.5 17a24.12 24.12 0 0 1 0-10 2 2 0 0 1 1.4-1.4 49.56 49.56 0 0 1 16.2 0A2 2 0 0 1 21.5 7a24.12 24.12 0 0 1 0 10 2 2 0 0 1-1.4 1.4 49.55 49.55 0 0 1-16.2 0A2 2 0 0 1 2.5 17"/><path d="m10 15 5-3-5-3z"/></symbol>
</defs></svg>"""


LD_PHYSICIAN = """  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"Physician","name":"Dr. Neema Bhat","description":"Hematologist, Pediatric Oncologist and Bone Marrow Transplant specialist in Bangalore.","url":"https://drneemabhat.com/","image":"https://drneemabhat.com/assets/images/portrait-scrubs.webp","telephone":"+91-78997-56677","medicalSpecialty":["Hematologic","Oncologic","Pediatric"],"alumniOf":{"@type":"Hospital","name":"Penn State Health"},
   "hospitalAffiliation":[{"@type":"Hospital","name":"Apollo Hospitals, Bannerghatta Road"},{"@type":"Hospital","name":"Apollo One & Apollo Cradle, Electronic City"},{"@type":"Hospital","name":"Bhagawan Mahaveer Jain Hospital"}],
   "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"11:00","closes":"16:00","description":"OPD, Apollo Hospitals, Bannerghatta Road"},{"@type":"OpeningHoursSpecification","dayOfWeek":"Friday","opens":"14:00","closes":"16:00","description":"Apollo One & Apollo Cradle, Hosa Road, Electronic City"},{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"17:00","closes":"19:00","description":"Therapy Clinic"}],
   "address":{"@type":"PostalAddress","addressLocality":"Bengaluru","addressRegion":"Karnataka","addressCountry":"IN"},"areaServed":"Bangalore"}
  </script>
"""

SVC_ICON = {"Hematology": "i-micro", "Pediatric": "i-child", "Pediatric & Adult": "i-marrow"}
SVC_ICON_BY_SLUG = {"hematology": "i-micro", "anaemia": "i-drop", "thalassemia": "i-link", "leukaemia": "i-cells", "lymphoma": "i-ribbon", "multiple-myeloma": "i-bone", "pediatric-oncology": "i-child", "brain-tumor": "i-brain", "bone-marrow-transplant": "i-marrow"}


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
  <link rel="canonical" href="{SITE_URL}/{canonical}">
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
  <link rel="stylesheet" href="assets/css/styles.css?v={asset_v('assets/css/styles.css')}">
{extra}</head>"""


def header(active, current=""):
    if PHP_MODE:  # Hostinger copy: the header lives in includes/header.php
        return f"<?php $nb_active = '{active}'; $nb_current = '{current}'; include __DIR__ . '/includes/header.php'; ?>\n"
    return _header_html(active, current)


def _header_html(active, current="", php=False):
    def cur(p):
        if php:
            return f"@@CUR:{p}@@"
        return ' aria-current="page"' if p == active else ""
    items = "".join(f'<a href="{svc_href(s)}">{n}</a>' for n, s, c, _ in SERVICES)
    html = f"""
  <a class="skip" href="#main">Skip to main content</a>
  <div class="curtain" aria-hidden="true"><img src="assets/images/logo-mark.png" alt=""></div>

  <header class="bar">
    <div class="wrap bar__in">
      <a class="brand" href="index.html" aria-label="Dr. Neema Bhat, home"><img src="assets/images/logo.png" alt="Dr. Neema Bhat, Hematologist and Pediatric Oncologist" width="928" height="275"></a>
      <nav class="primary" aria-label="Primary">
        <ul class="menu">
          <li><a href="index.html"{cur('home')}>Home</a></li>
          <li><a href="about.html"{cur('about')}>About</a></li>
          <li class="has-drop">
            <button type="button" aria-expanded="false" aria-controls="drop-services"{cur('service')}>Services{ic('i-chev', 'ic chev')}</button>
            <div class="drop" id="drop-services">
              <div class="drop__list">{items}</div>
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
          <div class="sheet__sub"><div>{items}</div></div></li>
        <li><a href="contact.html"{cur('contact')}>Contact{ic('i-go')}</a></li>
      </ul>
      <div class="sheet__actions">
        <a class="btn btn--line" href="tel:{PHONE_TEL}">{ic('i-phone')}Call</a>
        <a class="btn btn--grad" href="contact.html">{ic('i-cal')}Book</a>
      </div>
    </div>
  </div>
"""
    if current and not php:  # highlight the page you are on inside Services
        html = html.replace(f'href="{current}">', f'href="{current}" aria-current="page">')
    return html

def footer(fab=True):
    if PHP_MODE:  # Hostinger copy: the footer lives in includes/footer.php
        return f"<?php $nb_fab = {'true' if fab else 'false'}; include __DIR__ . '/includes/footer.php'; ?>\n"
    return _footer_html(fab)


def _footer_html(fab=True):
    links = "".join(f'<li><a href="{svc_href(s)}">{n}</a></li>' for n, s, c, _ in SERVICES)
    social = "".join(f'<li><a href="{url}" target="_blank" rel="noopener" aria-label="Dr. Neema Bhat on {name}">{ic(icon)}</a></li>' for name, icon, url in SOCIAL)
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
          <ul class="social" aria-label="Social media">{social}</ul>
        </div>
        <div><h2>Pages</h2><ul><li><a href="index.html">Home</a></li><li><a href="about.html">About</a></li><li><a href="contact.html">Contact</a></li><li><a href="privacy-policy.html">Privacy Policy</a></li></ul></div>
        <div class="foot__wide"><h2>Treatments</h2><ul class="foot__cols">{links}</ul></div>
      </div>
      <div class="foot__base"><p>© <span data-year>2026</span> Dr. Neema Bhat. All rights reserved.</p><p>Information on this website is for general awareness and is not a substitute for medical advice.</p></div>
    </div>
  </footer>

  <nav class="dock" aria-label="Quick actions">
    <a href="{WA}" target="_blank" rel="noopener">{ic('i-wa')}<span>WhatsApp</span></a>
    <a href="tel:{PHONE_TEL}">{ic('i-phone')}<span>Call</span></a>
    <a class="dock__book" href="{fab if fab == '@@FAB@@' else 'contact.html' if fab else '#wizard'}">{ic('i-cal')}<span>Book</span></a>
  </nav>
  <dialog class="lb" id="lb" aria-label="Photo viewer"><button class="lb__x" type="button" aria-label="Close">×</button><button class="lb__nav lb__nav--p" type="button" aria-label="Previous">‹</button><figure><img src="" alt=""><figcaption></figcaption></figure><button class="lb__nav lb__nav--n" type="button" aria-label="Next">›</button></dialog>
  <script src="assets/js/main.js?v={asset_v('assets/js/main.js')}" defer></script>
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
          <div class="reviews__list" data-marquee="42" tabindex="0" aria-label="Patient reviews, scrolls automatically, swipe or drag to browse"><div class="reviews__track">{cards}<div class="reviews__dup" aria-hidden="true" style="display:contents">{cards.replace(' data-fx="fade"', '')}</div></div></div>
        </div>
      </div>
    </section>"""


def svc_mobile():
    """Phone-only treatments block: app icon grid and bento tiles, switchable."""
    href = svc_link
    def icon(s, c):
        return SVC_ICON_BY_SLUG.get(s, SVC_ICON[c])
    apps = "".join(
        f'<li><a class="app" href="{href(s)}" data-m-svc="{s}">'
        f'<span class="app__ic">{ic(icon(s, c))}</span><b>{SHORT_NAMES[s]}</b></a></li>' for n, s, c, _ in SERVICES)
    tiles = "".join(
        f'<a class="tile" href="{href(s)}" data-m-svc="{s}">{ic(icon(s, c))}'
        f'<span class="tile__txt"><b>{n}</b></span><span class="tile__go">{ic("i-go")}</span></a>' for n, s, c, _ in SERVICES)
    switch = "" if not SHOW_SVC_SWITCH else f"""
          <div class="vswitch" role="group" aria-label="Choose layout">
            <button type="button" data-view="icons" aria-pressed="false">Option 1</button>
            <button type="button" data-view="tiles" aria-pressed="false">Option 2</button>
          </div>"""
    return f"""
        <div class="svc-m" data-svc-m data-view="{SVC_MOBILE_DEFAULT}">{switch}
          <div class="svc-m__icons">
            <ul class="apps">{apps}</ul>
          </div>
          <div class="svc-m__tiles"><div class="bento">{tiles}</div></div>
        </div>"""


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


def faq_section(faqs, intro, note=""):
    """Two-column FAQ: sticky intro + help box on the left, numbered question cards on the right."""
    cards = "".join(
        f'<details class="qa"{" open" if k == 0 else ""}><summary><span class="qa__n">{k + 1:02d}</span><span class="qa__q">{q}</span><span class="qa__pm" aria-hidden="true"></span></summary><p class="qa__a">{a}</p></details>'
        for k, (q, a) in enumerate(faqs))
    note_html = f'<p class="faq2__note">{note}</p>' if note else ""
    return f"""
    <section class="sec sec--tint" aria-labelledby="fq-title">
      <div class="wrap faq2">
        <div class="faq2__intro" data-fx="fade">
          <h2 class="title" id="fq-title">FAQs</h2>
          <p class="lead">{intro}</p>
          <div class="faq2__help">
            <b>Still have a question?</b>
            <span>Talk to the clinic directly.</span>
            <div class="faq2__acts">
              <a class="btn btn--grad btn--sm" href="{WA}" target="_blank" rel="noopener">{ic('i-wa')}WhatsApp</a>
              <a class="btn btn--line btn--sm" href="tel:{PHONE_TEL}">{ic('i-phone')}Call</a>
            </div>
          </div>
          {note_html}
        </div>
        <div class="faq2__list">{cards}</div>
      </div>
    </section>"""


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
        ("Bhagawan Mahaveer Jain Hospital", "Bone Marrow Transplant Unit"),
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
          <a class="svc" id="svc-{s}" href="{svc_link(s)}" data-fx="fade" style="--d:{(i % 3) * 0.08:.2f}s">
            <div class="svc__top">{ic(SVC_ICON_BY_SLUG.get(s, SVC_ICON[c]), 'ic svc__ic')}</div>
            <h3>{n}</h3>
            <p>{d}</p>
            <span class="svc__go">{'Learn more' if s in SERVICE_PAGES else 'Book a consultation'}{ic('i-go')}</span>
          </a>""" for i, (n, s, c, d) in enumerate(SERVICES))

    symptoms = [
        ("i-activity", "Constant tiredness", "Fatigue, breathlessness or looking pale for weeks."),
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
        ("i-marrow", "Transplant expertise", "Autologous and donor bone marrow transplants for children and adults, from donor matching to follow-up."),
        ("i-users", "Children and adults", "One specialist for blood disorders and blood cancers across all ages."),
        ("i-chat", "Clear conversations", "Diagnosis, options and next steps explained in plain language for the whole family."),
    ]
    why_html = "".join(f'<li data-fx="fade" style="--d:{k * 0.08:.2f}s">{ic(i)}<div><b>{t}</b><span>{d}</span></div></li>' for k, (i, t, d) in enumerate(why))

    visit = [
        ("Book", "Call, WhatsApp or send a request online and we confirm a slot.",
         f"Call or WhatsApp {PHONE_DISPLAY}, or use the form on the Contact page. Share the patient’s age and main concern so the right slot can be arranged."),
        ("Bring reports", "Carry previous blood tests, scans and prescriptions.",
         "Bring recent blood counts, smear, bone marrow or biopsy reports, scans, discharge summaries and a list of current medicines, they save time and repeat tests."),
        ("Consultation", "A detailed history, examination and discussion of options.",
         "Dr. Neema Bhat takes a detailed history, examines the patient and reviews every report, then explains what the findings mean in plain language."),
        ("Your plan", "Tests, treatment and follow-up, explained step by step.",
         "You leave with a clear plan (further tests if needed, treatment options and when to follow up), with the whole family’s questions answered."),
    ]

    def fig(f, cap, alt, tall, hidden=False):
        extra = ' tabindex="-1"' if hidden else ""
        return f'<figure class="{"tall" if tall else ""}"><button type="button" data-full="assets/images/{f}.webp" data-cap="{cap}"{extra}><img src="{img_small(f)}" alt="{"" if hidden else alt}" loading="lazy" decoding="async"></button><figcaption>{cap}</figcaption></figure>'
    reel = "".join(fig(*g) for g in GALLERY)
    reel_dup = "".join(fig(*g, hidden=True) for g in GALLERY)

    faqs = [
        ("What does a hematologist treat?", "A hematologist diagnoses and treats disorders of the blood, bone marrow and lymph nodes: such as anaemia, bleeding and clotting problems, thalassemia, and blood cancers like leukaemia, lymphoma and myeloma."),
        ("Does Dr. Neema Bhat treat children as well as adults?", "Yes. Dr. Neema Bhat is trained in pediatric hematology and oncology and also treats adults, so she cares for blood disorders and blood cancers across all ages."),
        ("When should my child see a pediatric hemato-oncologist?", "If your child has unexplained paleness, frequent bruising or bleeding, persistent fevers, swollen glands, bone pain or an abnormal blood test, a specialist opinion helps find the cause early."),
        ("Where does Dr. Neema Bhat consult?", "OPD is at Apollo Hospitals, Bannerghatta Road (Mon – Sat, 11 AM – 4 PM), the Therapy Clinic (Mon – Sat, 5 – 7 PM) and Apollo One &amp; Apollo Cradle, Electronic City (Fridays, 2 – 4 PM)."),
        ("Can I get a second opinion?", "Yes. Bring your reports, biopsy results and current treatment details, and Dr. Neema Bhat will review the diagnosis and options with you."),
        ("How do I book an appointment?", f"Call or WhatsApp {PHONE_DISPLAY}, or use the booking form on the Contact page. Your request opens in WhatsApp so you can review it before sending."),
    ]
    _, ld_faq = faq_block(faqs)

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
          <p class="hero__sub" data-fx="fade" style="--d:.3s">Dr. Neema Bhat is a US-trained Haemato-Oncologist and Bone Marrow Transplant specialist, caring for children and adults with blood disorders and blood cancers.</p>
          <div class="hero__acts" data-fx="fade" style="--d:.4s">
            <a class="btn btn--grad" href="contact.html">Book an Appointment{ic('i-go', 'ic ic--go')}</a>
            <a class="btn btn--line" href="tel:{PHONE_TEL}">{ic('i-phone')}{PHONE_DISPLAY}</a>
          </div>
          <div class="facts facts--hero" data-fx="fade" style="--d:.5s">
            <div class="fact">{ic('i-marrow')}<b>100+ transplants</b><span>Performed and supervised</span></div>
            <div class="fact">{ic('i-users')}<b>Children &amp; adults</b><span>Pediatric and adult BMT</span></div>
            <div class="fact">{ic('i-hosp')}<b>Apollo Hospitals</b><span>Bannerghatta Road, Bangalore</span></div>
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
        {sec_head('Services', 'Best <span class="grad-text">Hematologist</span> in Bangalore', 'Nine specialist services across adult hematology and pediatric hemato-oncology, tap a service to book or learn more.', hid='svc-title')}
        <div class="svc-grid" data-svc>{cards}
        </div>
        <div class="dots" data-dots-for="svc" aria-hidden="true"></div>{svc_mobile()}
      </div>
    </section>

    <section class="sec" aria-labelledby="sym-title">
      <div class="wrap">
        {sec_head('Know the signs', 'When should you see a <span class="grad-text">hematologist?</span>', 'Many blood disorders begin with everyday symptoms. See a specialist if any of these last for more than a few weeks.', center=True, hid='sym-title')}
        <ul class="sym">{sym}</ul>
        <p class="note-inline" style="text-align:center">These signs have many causes, a consultation and simple blood tests help find the right one.</p>
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
      <div class="reel" data-marquee="36" tabindex="0" aria-label="Photo gallery, scrolls automatically, swipe to browse"><div class="reel__track">{reel}<div class="reel__dup" aria-hidden="true" style="display:contents">{reel_dup}</div></div></div>
    </section>
{reviews_section()}
{where_section()}
{faq_section(faqs, 'Quick answers to the questions patients ask most about seeing a hematologist.')}
{cta('Questions about a diagnosis? Talk to a specialist.', 'Consultations for children and adults at Apollo Hospitals, Bannerghatta Road.')}
  </main>
""" + footer()


# ------------------------------------------------------------------ ABOUT
def about():
    cards = [
        ("i-award", "US training", "MD in the United States, followed by a fellowship (FAAP) in Pediatric Hematology, Oncology &amp; BMT at Penn State Health."),
        ("i-marrow", "Transplant expertise", "Autologous and donor bone marrow transplants for children and adults, from donor matching to follow-up."),
        ("i-users", "Children &amp; adults", "Blood disorders and blood cancers across all ages, with plans built around each patient."),
        ("i-drop", "Benign hematology", "Anaemia, thalassemia, hemophilia, low platelets and other non-cancerous blood conditions."),
        ("i-cells", "Blood cancers", "Leukaemia, lymphoma and myeloma: diagnosis, chemotherapy, targeted therapy and transplant planning."),
        ("i-heart", "Community care", "Works with Sankalp India Foundation to make curative transplant accessible to children with thalassemia."),
    ]
    cards_html = "".join(f'<div class="card" data-fx="fade" style="--d:{(k % 3) * 0.08:.2f}s">{ic(i)}<h3>{t}</h3><p>{d}</p></div>' for k, (i, t, d) in enumerate(cards))
    tiles = [("a", GALLERY[0]), ("b", GALLERY[2]), ("c", GALLERY[3]), ("p", GALLERY[1]), ("d", GALLERY[5]), ("e", GALLERY[6])]
    collage = "".join(
        f'<button type="button" class="ct ct--{area}{" ct--portrait" if f.startswith("portrait") else ""}" data-full="assets/images/{f}.webp" data-cap="{cap}" data-fx="fade" style="--d:{k * 0.06:.2f}s">'
        f'<img src="{img_small(f)}" alt="{alt}" loading="lazy"><span class="ct__cap">{cap}</span></button>'
        for k, (area, (f, cap, alt, _)) in enumerate(tiles))
    return head("About Dr. Neema Bhat | Hematologist &amp; Pediatric Oncologist, Bangalore",
                "About Dr. Neema Bhat: US-trained Haemato-Oncologist, FAAP fellowship at Penn State Health, Hematologist, Pediatric Oncologist and Bone Marrow Transplant specialist in Bangalore.",
                "about.html", LD_PHYSICIAN) + f"""
<body data-page="about">{ICONS}{header('about')}
  <main id="main">
    <section class="phero" aria-labelledby="ab-title">
      <div class="wrap phero__in">
        <div>
          <ol class="crumbs"><li><a href="index.html">Home</a></li><li>About</li></ol>
          <h1 id="ab-title" data-fx="wipe">Meet <span class="grad-text">Dr. Neema Bhat</span></h1>
          <p class="phero__sub" data-fx="fade" style="--d:.15s">Haemato-Oncologist, Pediatric Oncologist and Bone Marrow Transplant physician in Bangalore, caring for children and adults for more than ten years.</p>
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
            <p data-fx="fade">Over her career she has worked with the Bone Marrow Transplant Unit at Bhagawan Mahaveer Jain Hospital and Sankalp India Foundation, BGS Gleneagles Global Hospitals and Fortis Hospitals.</p>
          </div>
          <p class="quote" data-fx="fade">A patient-centric approach: clear communication and treatment plans built around each individual, rather than a one-size-fits-all protocol.</p>
          <div class="path" data-path>
            <div class="path__line"><i></i></div>
            <div class="step"><time>2020 – Present</time><h3>Bone Marrow Transplant Unit</h3><p>Bhagawan Mahaveer Jain Hospital, in partnership with Sankalp India Foundation</p></div>
            <div class="step"><time>2020 – 2023</time><h3>Consultant Hematologist, BMT Physician &amp; Pediatric Oncology</h3><p>Fortis Hospitals, Bangalore</p></div>
            <div class="step"><time>2018 – 2020</time><h3>Consultant Hematologist, BMT Physician &amp; Pediatric Oncology</h3><p>BGS Gleneagles Global Hospitals, Bangalore</p></div>
            <div class="step"><time>2018</time><h3>Clinical Hematologist &amp; BMT Physician</h3><p>Sankalp India Foundation, BMT Unit at Peopletree Hospitals, Yeshwanthpur</p></div>
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
{cta('Book a consultation with Dr. Neema Bhat.', 'For children and adults, OPD at Apollo Hospitals, Bannerghatta Road.')}
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
          <p class="phero__sub" data-fx="fade" style="--d:.15s">Three quick steps. Your request opens in WhatsApp so you can review it before sending.</p>
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
    T = "bone marrow transplant in Bangalore"
    hero = cond_hero("b-title", "Bone Marrow Transplant", 'Bone Marrow Transplant in <span class="grad-text">Bangalore</span>',
                     "A bone marrow transplant (BMT), also called a stem cell transplant, replaces diseased or damaged bone marrow with healthy blood-forming stem cells. It can cure conditions like thalassemia, aplastic anemia and some leukemias, and helps control others like myeloma and lymphoma.",
                     "bmt-cells.svg", "Illustration of a stem cell inside bone marrow giving rise to new blood cells, representing a bone marrow transplant", "bone-marrow-transplant")
    intro = _sec(f"""
        <div class="split split--top">
          <div>
            <p class="tag" data-fx="wipe-x">Overview</p>
            <h2 class="title" id="bt-what" data-fx="wipe">What is a <span class="grad-text">bone marrow transplant?</span></h2>
            <p class="lead" data-fx="fade">Bone marrow is the soft, spongy tissue inside your bones. It contains stem cells that make all your blood cells. When the bone marrow is damaged by disease, or when high-dose treatment is needed to destroy a cancer, healthy stem cells can be given to rebuild it.</p>
            <p class="lead" data-fx="fade">In a bone marrow transplant, healthy stem cells are given into a vein, much like a blood transfusion. <b>It is not surgery.</b> The stem cells travel to the bone marrow on their own and start making new red cells, white cells and platelets. This is called engraftment.</p>
            <p class="lead" data-fx="fade">Dr. Neema Bhat, a US-trained hematologist and bone marrow transplant specialist with 10+ years of experience and 100+ transplants, offers {T} for adults and children.</p>
          </div>
          {_box('i-marrow', 'Where the stem cells come from', _ul(['<b>Your own body</b> (autologous transplant)', '<b>A donor</b>, such as a brother, sister, parent or an unrelated volunteer (allogeneic transplant)']) + _p('Today, most stem cells are collected from the blood, not directly from the bone marrow. The term “bone marrow transplant” is still used for all types.') + _p(f'The need is large: India has about 1 to 1.5 lakh children with thalassemia major, and 10,000 to 15,000 more are born every year (Ministry of Health). For many of these children, a transplant is the only cure. Timely {T}, done at the right stage of disease, gives the best chance of success.'))}
        </div>""", label="bt-what")
    who = _sec(sec_head('Who needs it', 'Who needs a <span class="grad-text">bone marrow transplant?</span>', 'A bone marrow transplant may be advised for these conditions:', hid='bt-who') + f"""<div class="cols2">
          {_box('i-cells', 'Blood cancers', _ul([f'Acute myeloid leukemia (AML) and acute lymphoblastic leukemia (ALL), <a href="{LEUK_PAGE}">leukemia</a>', 'Chronic myeloid leukemia (CML) not controlled by other treatment', f'Hodgkin and non-Hodgkin <a href="{LYMPH_PAGE}">lymphoma</a> that has relapsed or is high-risk', f'<a href="{MYEL_PAGE}">Multiple myeloma</a>', 'Myelodysplastic syndromes (MDS) and myelofibrosis']))}
          {_box('i-drop', 'Non-cancerous blood disorders', _ul([f'<a href="{THAL_PAGE}">Thalassemia major</a>', 'Sickle cell disease', 'Severe aplastic anemia', 'Other bone marrow failure syndromes, such as Fanconi anemia']), 0.08)}
        </div>
        <div class="cols2 mt">
          {_box('i-child', 'Immune and inherited disorders, mostly in children', _ul(['Severe combined immunodeficiency (SCID) and other primary immunodeficiencies', 'Chronic granulomatous disease (CGD)', 'HLH (hemophagocytic lymphohistiocytosis)', 'Some inherited metabolic disorders']))}
          {_box('i-heart', 'Solid tumours (selected cases)', _ul(['Neuroblastoma in children', 'Relapsed germ cell tumours']), 0.08)}
        </div>""" + _p('Not every patient with these conditions needs a transplant. The decision depends on the disease, its stage, how it responded to earlier treatment, your age and overall health, and whether a suitable donor is available. A transplant evaluation with a BMT specialist answers these questions.'), tint=True, label="bt-who")
    types = _sec(sec_head('Types', 'Types of bone marrow <span class="grad-text">transplant</span>', center=True, hid='bt-types') + _table(
        ["Type", "Where the stem cells come from", "Mainly used for"], [
            ("Autologous transplant", "Your own stem cells, collected and stored before high-dose treatment", "Multiple myeloma, relapsed lymphoma, some solid tumours"),
            ("Matched sibling donor (allogeneic)", "A brother or sister with a full tissue (HLA) match", "Thalassemia, aplastic anemia, leukemia, sickle cell disease"),
            ("Matched unrelated donor (allogeneic)", "An unrelated volunteer found through a stem cell donor registry", "Leukemia, MDS, aplastic anemia, when no family match is available"),
            ("Haploidentical (half-matched)", "A parent, child, brother or sister who is a half match", "Leukemia, aplastic anemia, thalassemia and others, when no full match is available"),
            ("Cord blood transplant", "Stem cells from a newborn’s umbilical cord, stored in a cord blood bank", "Mainly children, in selected cases"),
        ]) + f"""<div class="cols2 mt">
          {_box('i-flask', 'Myeloablative conditioning', _p('Before a transplant, you receive conditioning treatment with chemotherapy, and sometimes radiation. Myeloablative (full-intensity) conditioning uses high doses to fully clear the bone marrow. It is mostly used for younger, fitter patients.'))}
          {_box('i-shield', 'Reduced-intensity conditioning', _p('Uses lower doses and relies more on the donor’s immune cells to fight the disease. It allows older patients or those with other health problems to have a transplant.'), 0.08)}
        </div>""", label="bt-types")
    donor = _sec(f"""<div class="cols2">
          {_box('i-users', 'Finding a donor: HLA matching', _p('For a donor transplant, the donor’s tissue type must match the patient’s. This is checked with a simple blood test or cheek swab called HLA typing (human leukocyte antigen typing).') + _ul(['<b>Brothers and sisters:</b> each full sibling has a 1 in 4 chance of being a full match.', '<b>Parents and children:</b> are usually a half match, so they can be donors for a haploidentical transplant.', '<b>Unrelated donors:</b> can be searched in Indian and international stem cell donor registries.']) + _p('A close match lowers the risk of rejection and graft-versus-host disease (GVHD). Thanks to newer methods, a half-matched family member is now a safe option for many patients who do not have a full match.'), hid='bt-donor')}
          {_box('i-heart', 'Is donating stem cells safe?', _p('Yes. Most donors give stem cells from the blood, through a process called apheresis. The donor first gets a few days of injections to move stem cells into the blood. Blood is then drawn from one arm, the stem cells are separated by a machine, and the rest of the blood is returned through the other arm.') + _p('It takes about 4 to 6 hours and needs no surgery. The donor’s body replaces the stem cells within a few weeks.'), 0.08)}
        </div>""", tint=True, label="bt-donor")
    process = _sec(sec_head('The process', 'The transplant process, <span class="grad-text">step by step</span>', hid='bt-proc') + _olist([
        ("Transplant evaluation", "Blood tests, heart, lung, kidney and liver tests, imaging, infection screening and a dental check-up to make sure you are fit for transplant."),
        ("Donor search and HLA typing", "For donor transplants, family members are tested first, then registries if needed."),
        ("Central line placement", "A thin tube (catheter) is placed in a large vein in the chest to give medicines, blood and stem cells, and to take blood samples."),
        ("Stem cell collection", "Stem cells are collected from you (autologous) or from your donor, usually from the blood by apheresis."),
        ("Conditioning", "About 5 to 10 days of chemotherapy, sometimes with radiation, to clear the diseased marrow and prepare the body."),
        ("Transplant day (Day 0)", "The stem cells are given through the central line, like a blood transfusion. It usually takes less than an hour to a few hours."),
        ("Engraftment", "New stem cells start making blood cells in about 10 to 14 days after an autologous transplant and 2 to 4 weeks after a donor transplant. You stay in a clean, HEPA-filtered BMT room."),
        ("Discharge", "Once blood counts recover and you can eat and drink well, usually about 2 to 3 weeks for an autologous and 4 to 6 weeks for a donor transplant."),
        ("Follow-up and recovery", "Frequent visits in the first 100 days, then regular long-term check-ups."),
    ]), label="bt-proc")
    tx = _sec(sec_head('Treatment', 'Bone marrow transplant <span class="grad-text">treatment options</span>', 'Treatment is planned around your disease, its stage, your age, your fitness and the donor available. Options include:', hid='bt-tx') + _cards([
        ("i-marrow", "Autologous stem cell transplant", "Your own stem cells are collected, stored and returned after high-dose chemotherapy."),
        ("i-marrow", "Tandem (double) autologous transplant", "Two planned autologous transplants a few months apart, for selected myeloma patients."),
        ("i-users", "Matched sibling donor transplant", "Stem cells from a fully matched brother or sister."),
        ("i-link", "Matched unrelated donor transplant", "Stem cells from a matched volunteer donor found through a registry."),
        ("i-users", "Haploidentical (half-matched) transplant", "Stem cells from a half-matched parent, child, brother or sister."),
        ("i-child", "Cord blood transplant", "Stem cells from stored umbilical cord blood, in selected cases."),
        ("i-flask", "Myeloablative conditioning", "Full-intensity chemotherapy, with or without radiation, before transplant."),
        ("i-flask", "Reduced-intensity conditioning", "Lower-dose conditioning for older patients or those with other health problems."),
        ("i-radiation", "Total body irradiation (TBI)", "Radiation to the whole body as part of conditioning, for selected conditions."),
        ("i-shield", "GVHD prevention and treatment", "Immune-suppressing therapy to stop donor cells from attacking the patient’s body."),
        ("i-syringe", "Donor lymphocyte infusion (DLI)", "Extra immune cells from the donor to treat relapse or boost the donor’s cells."),
        ("i-shield", "Infection prevention", "HEPA-filtered rooms, preventive antibiotics, antivirals and antifungals, and regular monitoring."),
        ("i-syringe", "Blood and platelet transfusions", "To support you until the new marrow starts working."),
        ("i-apple", "Nutrition support", "A dietitian-planned diet, and feeding support if eating is difficult."),
        ("i-syringe", "Vaccination after transplant", "Childhood and adult vaccines are repeated, as the transplant resets the immune system."),
        ("i-adult", "Physiotherapy and rehabilitation", "To rebuild strength and stamina."),
        ("i-chat", "Counselling and support", "Psychological support for patients, donors and families through the transplant journey."),
        ("i-clock", "Long-term follow-up care", "Checks for late effects on the heart, lungs, hormones, bones, eyes and fertility."),
    ]), tint=True, label="bt-tx")
    risks = _sec(sec_head('Risks', 'Risks and side effects of <span class="grad-text">bone marrow transplant</span>', 'A bone marrow transplant is a major treatment. Your transplant team watches closely for these risks and treats them early:', hid='bt-risk') + _conds([
        ("i-thermo", "Infections", "The most common risk while blood counts are low, and for months after a donor transplant."),
        ("i-heart", "Mouth sores, nausea, diarrhoea", "From conditioning chemotherapy. These usually settle as counts recover."),
        ("i-drop", "Low blood counts", "You may need red cell and platelet transfusions until the new marrow works."),
        ("i-shield", "Graft-versus-host disease (GVHD)", "After a donor transplant, the donor’s immune cells may attack the skin, gut or liver. It is treated with immune-suppressing medicines."),
        ("i-marrow", "Graft failure", "Rarely, the new stem cells do not engraft and further treatment is needed."),
        ("i-flask", "Organ problems", "Such as liver (veno-occlusive disease), kidney, lung or heart problems."),
        ("i-users", "Infertility", "Conditioning can affect fertility. Ask about sperm, egg or embryo freezing before treatment."),
        ("i-cells", "Relapse", "The original disease may come back in some patients."),
        ("i-clock", "Late effects", "Cataracts, thyroid and hormone changes, bone thinning, and a small risk of second cancers years later."),
    ], cols4=False) + _alert('Call your transplant team urgently', 'if you have a fever of 100.4°F (38°C) or more, chills, breathlessness, bleeding, severe diarrhoea, a new rash or yellow eyes after a transplant.'), label="bt-risk")
    life = _sec(_box('i-sun', 'Recovery and life after a bone marrow transplant', _p('Recovery takes time. Blood counts usually recover in weeks, but the immune system can take 6 months to 1 year or more to rebuild, especially after a donor transplant. These steps help:') + _ul(['Stay close to the hospital for the first 100 days if you live far away, so that check-ups are easy.', '<b>Prevent infections:</b> wash hands often, wear a mask in crowded places, and avoid people with colds, fever or chickenpox.', '<b>Eat safe food:</b> freshly cooked, hot food and boiled or filtered water. Avoid raw salads, street food, cut fruit kept outside and unpasteurised milk until your doctor allows.', 'Take every medicine on time, especially immune-suppressing and anti-infection medicines. Never stop them on your own.', 'Protect your skin from the sun, as GVHD and some medicines make the skin sensitive.', 'Stay gently active: short walks help rebuild strength.', 'Get your vaccines again on the schedule your transplant team gives you.', 'Return to work or school gradually, usually within a few months, as advised.']) + _p('Most transplant survivors return to normal daily life. Children go back to school, and adults return to work and family life.'), hid='bt-life'), tint=True, label="bt-life")
    faqs = [
        ("Is a bone marrow transplant a surgery?", "No. The stem cells are given through a vein, like a blood transfusion. There is no operation. Collecting stem cells from a donor is also usually done from the blood."),
        ("Is a bone marrow transplant painful?", "The transplant itself is not painful. Some patients have discomfort from mouth sores, nausea or tiredness caused by conditioning chemotherapy, and these are treated with medicines."),
        ("What is the success rate of bone marrow transplant?", "It depends on the disease, its stage, the patient’s age and health, and the donor match. Results are best when the transplant is done early. For example, children with thalassemia who receive a matched sibling transplant early have high cure rates. Your doctor can explain the expected outcome for your condition."),
        ("Who can be a bone marrow donor?", "A healthy brother or sister with a full HLA match is usually the first choice. A parent, child or sibling with a half match, or a matched unrelated volunteer from a registry, can also donate."),
        ("Is it safe to donate bone marrow or stem cells?", "Yes. Donation is safe for healthy donors. Most donors give stem cells from the blood by apheresis, which needs no surgery, and the body replaces the cells within a few weeks."),
        ("How long does the bone marrow transplant process take?", "Evaluation and preparation take a few weeks. The hospital stay is usually about 2 to 3 weeks for an autologous transplant and 4 to 6 weeks for a donor transplant. Close follow-up continues for the first 100 days and beyond."),
        ("What is the best age for a bone marrow transplant in thalassemia?", "Results are best when the transplant is done in early childhood, before iron overload damages the liver and heart. Families should get siblings HLA-tested soon after diagnosis."),
        ("What is graft-versus-host disease (GVHD)?", "GVHD happens when the donor’s immune cells attack the patient’s body, such as the skin, gut or liver. It occurs only after a donor transplant and is treated with immune-suppressing medicines."),
        ("How much does a bone marrow transplant cost in Bangalore?", "The cost depends on the type of transplant, the donor, the hospital stay and any complications. A donor transplant usually costs more than an autologous transplant. The clinic can share an estimate after evaluation. Eligible families may get support through schemes such as Coal India’s Thalassemia Bal Sewa Yojana, which gives up to ₹10 lakh for thalassemia major and aplastic anemia transplants (annual family income below ₹8 lakh)."),
        ("Can a bone marrow transplant cure blood cancer?", "A donor transplant can cure some leukemias and other blood cancers. An autologous transplant helps control myeloma and lymphoma and keeps them in remission longer."),
    ]
    page = cond_page(BMT_PAGE, "Bone Marrow Transplant in Bangalore | Dr. Neema Bhat",
                     "Bone marrow (stem cell) transplant in Bangalore with Dr. Neema Bhat, US-trained hematologist and BMT specialist with 100+ transplants, autologous, matched donor and half-matched transplants for adults and children.",
                     "Bone marrow transplant", ["Stem cell transplant", "BMT"], hero, [intro, who, types, donor, process, tx, risks, life], faqs,
                     "Quick answers to the questions families ask most about bone marrow transplants.",
                     "For transplants, she guides patients and families from evaluation and donor testing to the transplant and long-term follow-up.",
                     book_section("Considering a transplant?", "Has your doctor advised a transplant, or do you want to know if a transplant can help you or your child? Book a transplant consultation with Dr. Neema Bhat for bone marrow transplant in Bangalore today.", "bone-marrow-transplant"))
    # the condition schema type for a procedure page
    return page.replace('"@type":"MedicalCondition","name":"Bone marrow transplant"', '"@type":"MedicalProcedure","name":"Bone marrow transplant"', 1)



def anemia():
    T = "anemia treatment in Bangalore"
    faqs = [
        ("Which doctor should I see for anemia in Bangalore?", "A hematologist (blood specialist) is the right doctor for anemia that is moderate, severe, keeps coming back, or does not improve with iron tablets. Dr. Neema Bhat is a US-trained hematologist in Bangalore who treats all types of anemia in adults and children."),
        ("What hemoglobin level is considered anemia?", "The WHO defines anemia as hemoglobin below 13 g/dL in men, below 12 g/dL in non-pregnant women, and below 11 g/dL in pregnant women and young children."),
        ("Can anemia be cured permanently?", "Yes, most anemias caused by low iron, B12 or folate can be cured once the cause is corrected. Inherited types like thalassemia need long-term care, and some can be cured with a bone marrow transplant."),
        ("How long does anemia treatment take?", "Most people with iron deficiency feel better in 2 to 3 weeks, and hemoglobin returns to normal in about 2 months. Treatment usually continues for a few more months to rebuild iron stores."),
        ("What is the fastest way to treat anemia?", "The fastest safe treatment depends on the cause. For iron deficiency, an IV iron infusion can raise iron levels much faster than tablets. Blood transfusion is used only for severe anemia or emergencies."),
        ("Can anemia be treated without a blood transfusion?", "Yes. Most patients are treated with iron tablets, IV iron, vitamin B12 or folic acid, and by fixing the root cause. Transfusions are needed only in severe or special cases."),
        ("Does seeing a hemato-oncologist for anemia mean I have cancer?", "No. A hemato-oncologist treats all blood problems: common ones like anemia as well as blood cancers. Most anemia is caused by low iron or vitamins. Seeing a blood specialist simply means the cause is found faster and treated correctly."),
        ("Can anemia come back after treatment?", "It can, if the underlying cause, such as heavy periods, a poor diet or slow bleeding in the gut, is not fixed. Regular follow-up blood tests help prevent this."),
        ("How much does anemia treatment in Bangalore cost?", "Most anemia treatment, such as blood tests and iron or vitamin supplements, is affordable. Costs rise only for IV infusions, transfusions or specialised treatments. The clinic can share an estimate after your first consultation."),
        ("Can children and pregnant women get anemia treatment?", "Yes. Dr. Neema Bhat is a US board-certified pediatrician and hematologist, and she treats anemia in babies, children, teenagers and pregnant women with safe, age-appropriate care."),
    ]
    _, ld_faq = faq_block(faqs)
    ld_cond = ('  <script type="application/ld+json">{"@context":"https://schema.org","@type":"MedicalWebPage","name":"Anemia Treatment in Bangalore",'
               '"about":{"@type":"MedicalCondition","name":"Anemia","alternateName":["Anaemia","Low hemoglobin"]},'
               '"author":{"@type":"Physician","name":"Dr. Neema Bhat"}}</script>\n')


    who_rows = [("Adult men", "13 g/dL"), ("Adult women (not pregnant)", "12 g/dL"), ("Pregnant women", "11 g/dL"), ("Children (6 months to 5 years)", "11 g/dL")]
    who_html = "".join(f"<tr><td>{a}</td><td><b>{b}</b></td></tr>" for a, b in who_rows)

    symptoms = [
        ("i-activity", "Constant tiredness", "Feeling tired or weak all the time"),
        ("i-drop", "Paleness", "Pale skin, lips or inner eyelids"),
        ("i-lungs", "Breathlessness", "On stairs or while walking"),
        ("i-heart", "Fast heartbeat", "A fast or uneven heartbeat"),
        ("i-cells", "Dizziness", "Headaches or feeling light-headed"),
        ("i-thermo", "Cold hands &amp; feet", "Even in normal weather"),
        ("i-scale", "Brittle nails, hair fall", "Weak nails and thinning hair"),
        ("i-doc", "Poor focus", "Trouble concentrating at work or school"),
        ("i-flask", "Unusual cravings", "Ice, mud or chalk, a sign of low iron"),
    ]
    sym_html = "".join(f'<li data-fx="fade" style="--d:{(k % 3) * 0.06:.2f}s">{ic(i)}<b>{t}</b><span>{d}</span></li>' for k, (i, t, d) in enumerate(symptoms))

    causes = [
        ("i-flask", "Low iron, vitamin B12 or folate", "From diet, poor absorption, or vegetarian diets low in B12."),
        ("i-drop", "Blood loss", "Heavy periods, piles, stomach ulcers, or slow bleeding in the gut."),
        ("i-heart", "Pregnancy", "The growing baby needs extra iron."),
        ("i-shield", "Long-term illnesses", "Kidney disease, thyroid problems, diabetes, arthritis or infections."),
        ("i-users", "Inherited blood conditions", "Thalassemia and sickle cell disease."),
        ("i-cells", "Red cells breaking down early", "Called hemolytic anemia."),
        ("i-marrow", "Bone marrow problems", "Aplastic anemia, or blood cancers like leukemia and myeloma."),
        ("i-pill", "Certain medicines", "Some long-term medicines or chemotherapy."),
    ]
    causes_html = "".join(f'<li data-fx="fade" style="--d:{(k % 3) * 0.06:.2f}s"><b>{ic(i)}{t}</b><p>{d}</p></li>' for k, (i, t, d) in enumerate(causes))

    risk = ["Women with heavy periods, and pregnant or breastfeeding women", "Babies, young children and teenagers, who grow fast and need more iron",
            "Vegetarians and vegans, who may get too little vitamin B12", "Adults over 65", "People with kidney disease, diabetes, thyroid problems, IBD or celiac disease",
            "People who have had stomach or weight-loss surgery", "People who take painkillers (NSAIDs), acid-reducing tablets or metformin for a long time",
            "People with worm infections, which can cause slow blood loss", "Anyone with a family history of thalassemia or sickle cell disease"]
    untreated = [("Heart strain", "the heart pumps harder to deliver oxygen, which can lead to an enlarged heart or heart failure."),
                 ("Pregnancy problems", "higher risk of preterm birth, low birth weight and heavy bleeding during delivery."),
                 ("Slower growth in children", "delayed growth, poor school performance and frequent infections."),
                 ("Weak immunity and low energy", "that affect work and daily life."),
                 ("A missed diagnosis", "anemia can be the first sign of hidden bleeding, kidney disease or a blood cancer.")]
    li = lambda t: f'<li>{ic("i-check")}<span>{t}</span></li>'
    risk_html = "".join(li(t) for t in risk)
    untreated_html = "".join(li(f"<b>{a}:</b> {b}") for a, b in untreated)

    types = [
        ("Iron deficiency anemia", "The most common type. The body lacks iron to make hemoglobin."),
        ("Vitamin B12 &amp; folate deficiency", "Megaloblastic and pernicious anemia. Low B12 or folate makes red cells large and weak. Common in vegetarians."),
        ("Anemia of chronic disease", "Caused by long-term kidney, liver or inflammatory illness."),
        ("Hemolytic anemia", "Including autoimmune. Red cells are destroyed faster than the body can replace them."),
        ("Thalassemia", "An inherited condition where the body makes faulty hemoglobin."),
        ("Sickle cell anemia", "Inherited; red cells become sickle-shaped and block blood flow."),
        ("Aplastic anemia", "The bone marrow stops making enough blood cells."),
        ("Sideroblastic anemia", "The body cannot use iron properly to make hemoglobin."),
        ("Anemia in pregnancy &amp; children", "Special care for mothers-to-be, babies and teenagers."),
    ]
    types_html = "".join(f'<div class="card" data-fx="fade" style="--d:{(k % 3) * 0.06:.2f}s">{ic("i-drop")}<h3>{t}</h3><p>{d}</p></div>' for k, (t, d) in enumerate(types))

    tests = [("Complete Blood Count (CBC)", "Checks hemoglobin and the size and number of red cells."),
             ("Peripheral blood smear", "Looks at your blood cells under a microscope."),
             ("Iron studies", "Serum iron, ferritin and TIBC to measure iron stores."),
             ("Vitamin B12 and folate levels", "To find vitamin deficiencies."),
             ("Reticulocyte count", "Shows whether your bone marrow is making new cells."),
             ("Hemoglobin electrophoresis / HPLC", "To check for thalassemia or sickle cell."),
             ("Kidney, liver and thyroid tests", "To look for long-term illnesses behind the anemia."),
             ("Stool test or endoscopy", "If hidden bleeding is suspected."),
             ("Bone marrow test", "Only when needed, for aplastic anemia or blood cancers.")]
    tests_html = "".join(f'<li data-fx="fade" style="--d:{(k % 3) * 0.06:.2f}s"><span class="olist__n">{k + 1:02d}</span><div><b>{t}</b><p>{d}</p></div></li>' for k, (t, d) in enumerate(tests))

    treat = [("i-pill", "Iron tablets or syrup", "The usual iron deficiency anemia treatment for mild to moderate cases."),
             ("i-syringe", "IV iron infusion", "A faster option when tablets cause stomach upset, don’t work, or iron is needed quickly, for example in pregnancy or before surgery."),
             ("i-check", "Vitamin B12 &amp; folic acid", "B12 injections or tablets and folic acid for B12 and folate deficiency."),
             ("i-users", "Treating the root cause", "Such as heavy periods, gut bleeding, thyroid or kidney problems, with the right specialist."),
             ("i-pill", "Immune-calming medicines", "For autoimmune hemolytic anemia."),
             ("i-syringe", "Blood transfusion", "Only for severe anemia or emergencies."),
             ("i-syringe", "Transfusion &amp; iron chelation", "Regular transfusions with iron chelation for thalassemia."),
             ("i-award", "Immunosuppressive therapy", "For aplastic anemia."),
             ("i-marrow", "Bone marrow (stem cell) transplant", f'A possible cure for thalassemia, sickle cell disease and severe aplastic anemia. <a href="{BMT_PAGE}">Learn more</a>'),
             ("i-apple", "Diet &amp; lifestyle advice", "Simple Indian food choices to keep your hemoglobin healthy.")]
    treat_html = "".join(f'<div class="card" data-fx="fade" style="--d:{(k % 3) * 0.06:.2f}s">{ic(i)}<h3>{t}</h3><p>{d}</p></div>' for k, (i, t, d) in enumerate(treat))

    foods = [("Iron-rich foods", "ragi, green leafy vegetables (palak, methi, drumstick leaves), dals, rajma, chana, jaggery, dates, eggs, chicken, fish and meat."),
             ("Vitamin C with meals", "lemon, amla, orange or guava help your body absorb iron."),
             ("Vitamin B12 sources", "milk, curd, paneer, eggs and fish."),
             ("Avoid tea or coffee within one hour of meals", "it reduces iron absorption.")]
    foods_html = "".join(li(f"<b>{a}:</b> {b}") for a, b in foods)


    return head("Anemia Treatment in Bangalore | Dr. Neema Bhat, Hematologist",
                "Anemia treatment in Bangalore with Dr. Neema Bhat, US-trained hematologist with 10+ years of experience. Finds the cause of low hemoglobin and treats it, for adults and children at Apollo Hospitals, Bannerghatta Road.",
                ANEMIA_PAGE, LD_PHYSICIAN + ld_cond + ld_faq) + f"""
<body data-page="service">{ICONS}{header('service', ANEMIA_PAGE)}
  <main id="main">
{cond_hero("an-title", "Anemia Treatment", 'Anemia Treatment in <span class="grad-text">Bangalore</span>', f"Anemia means your blood has fewer healthy red blood cells or less hemoglobin than it needs, so less oxygen reaches your body and you feel tired, weak or breathless. Most anemia is treatable once the cause is found, and that is where the right {T} begins.", "anemia-cells.svg", "Illustration of red blood cells, some pale and fewer in number, representing anemia", "anaemia")}

    <section class="sec" aria-labelledby="what-title">
      <div class="wrap split split--top">
        <div>
          <p class="tag" data-fx="wipe-x">Overview</p>
          <h2 class="title" id="what-title" data-fx="wipe">What is <span class="grad-text">anemia?</span></h2>
          <p class="lead" data-fx="fade">Your red blood cells carry oxygen from your lungs to every part of your body. They use a protein called hemoglobin to do this. When hemoglobin drops below the healthy level, your organs get less oxygen. This is anemia.</p>
          <p class="lead" data-fx="fade">Anemia is very common in our state. About 48 out of every 100 women and two out of three young children in Karnataka have anemia (NFHS-5). Many people live with it for years, thinking tiredness is “normal”. It is not, and with timely {T}, you don’t have to put up with it.</p>
        </div>
        <div class="box" data-fx="fade">
          <h3>{ic('i-flask')}When is it anemia?</h3>
          <p class="box__sub">According to the World Health Organization, you have anemia if your hemoglobin is below:</p>
          <table class="htable"><thead><tr><th>Who</th><th>Hemoglobin below</th></tr></thead><tbody>{who_html}</tbody></table>
          <p class="box__sub">Anemia can be mild, moderate or severe. Even mild anemia is worth checking, because it is often an early sign of another problem.</p>
        </div>
      </div>
    </section>

    <section class="sec sec--tint" aria-labelledby="sym-title">
      <div class="wrap">
        {sec_head('Signs &amp; symptoms', 'Common signs of <span class="grad-text">anemia</span>', 'Anemia often develops slowly, so many people don’t notice it at first. Watch for:', hid='sym-title')}
        <ul class="sym sym--3">{sym_html}</ul>
        <div class="cols2 mt">
          <div class="box" data-fx="fade"><h3>{ic('i-users')}Anemia symptoms in women</h3><p class="box__sub">Women are more likely to have anemia because of monthly periods, pregnancy and breastfeeding. Heavy periods, constant tiredness and hair fall are common clues.</p></div>
          <div class="box" data-fx="fade" style="--d:.08s"><h3>{ic('i-child')}Anemia symptoms in children</h3><p class="box__sub">Children may look pale, eat poorly, get irritable, fall sick often or grow more slowly. Dr. Neema Bhat is a US board-certified pediatrician and pediatric hematologist, so children with anemia get specialised care.</p></div>
        </div>
        <p class="alert" data-fx="fade">{ic('i-heart')}<span><b>See a doctor urgently</b> if you have chest pain, fainting, severe breathlessness, or black or bloody stools.</span></p>
      </div>
    </section>

    <section class="sec" aria-labelledby="cause-title">
      <div class="wrap">
        {sec_head('Causes', 'What causes <span class="grad-text">anemia?</span>', 'Anemia is not one disease. It is a sign that something is wrong. The common causes are:', hid='cause-title')}
        <ul class="conds conds--4">{causes_html}</ul>
      </div>
    </section>

    <section class="sec sec--tint" aria-labelledby="risk-title">
      <div class="wrap cols2">
        <div class="box" data-fx="fade">
          <h3 id="risk-title">{ic('i-users')}Who is at risk of anemia?</h3>
          <p class="box__sub">Anyone can get anemia, but the risk is higher for:</p>
          <ul class="list">{risk_html}</ul>
        </div>
        <div class="box" data-fx="fade" style="--d:.08s">
          <h3>{ic('i-shield')}What happens if anemia is left untreated?</h3>
          <p class="box__sub">Mild anemia may feel like simple tiredness, but over time it can cause serious problems:</p>
          <ul class="list">{untreated_html}</ul>
        </div>
      </div>
    </section>

    <section class="sec" aria-labelledby="types-title">
      <div class="wrap">
        {sec_head('Types', 'Types of anemia <span class="grad-text">we treat</span>', center=True, hid='types-title')}
        <div class="cards3">{types_html}</div>
      </div>
    </section>

    <section class="sec sec--tint" aria-labelledby="dx-title">
      <div class="wrap">
        {sec_head('Diagnosis', 'How is anemia <span class="grad-text">diagnosed?</span>', 'Finding the right cause is the most important step. Dr. Neema Bhat may advise some of these anemia blood tests:', hid='dx-title')}
        <ol class="olist">{tests_html}</ol>
      </div>
    </section>

    <section class="sec" aria-labelledby="tx-title">
      <div class="wrap">
        {sec_head('Treatment', 'Anemia treatment options <span class="grad-text">in Bangalore</span>', f'Your {T} depends on the type and cause of your condition. Dr. Neema Bhat creates a plan for you that may include:', hid='tx-title')}
        <div class="cards3 cards3--5">{treat_html}</div>
        <p class="alert alert--warn" data-fx="fade">{ic('i-shield')}<span><b>Do not start iron tablets on your own for a long time.</b> Too much iron can harm the body, and the tablets may hide a more serious cause.</span></p>
      </div>
    </section>

    <section class="sec sec--tint" aria-labelledby="food-title">
      <div class="wrap cols2">
        <div class="box" data-fx="fade">
          <h3 id="food-title">{ic('i-sun')}Foods that help treat and prevent anemia</h3>
          <p class="box__sub">Food supports treatment but rarely fixes anemia alone. Include:</p>
          <ul class="list">{foods_html}</ul>
        </div>
        <div class="box" data-fx="fade" style="--d:.08s">
          <h3>{ic('i-users')}Prevention &amp; carrier testing</h3>
          <p class="box__sub">India’s national Anemia Mukt Bharat programme gives free iron and folic acid tablets to children, teenagers, and pregnant and breastfeeding women through government health centres.</p>
          <p class="box__sub">Inherited anemias such as thalassemia cannot be prevented with food. A simple thalassemia carrier test (HPLC) before marriage or pregnancy shows whether a couple could pass on the condition. If both partners are carriers, each child has a 1 in 4 chance of thalassemia major, so early counselling helps families plan.</p>
        </div>
      </div>
    </section>

{about_doctor("For anemia, she looks for the exact reason your hemoglobin is low and treats that cause, with clear explanations at every step.")}

{faq_section(faqs, 'Quick answers to the questions patients ask most about anemia and its treatment.')}

{book_section("Tired of feeling tired?", "Get your hemoglobin checked and find the real cause. Book a consultation for anemia treatment in Bangalore with Dr. Neema Bhat today.", "anaemia")}
  </main>
""" + footer()


# ------------------------------------------------------------------ CONDITION PAGES (shared parts)
def cond_hero(hid, crumb, h1, sub, art, alt, topic):
    return f"""
    <section class="phero" aria-labelledby="{hid}">
      <div class="wrap phero__in">
        <div>
          <ol class="crumbs"><li><a href="index.html">Home</a></li><li><a href="index.html#services">Services</a></li><li>{crumb}</li></ol>
          <h1 id="{hid}" data-fx="wipe">{h1}</h1>
          <p class="phero__sub" data-fx="fade" style="--d:.15s">{sub}</p>
          <div class="hero__acts" data-fx="fade" style="--d:.25s">
            <a class="btn btn--grad" href="contact.html?topic={topic}">Book a consultation{ic('i-go', 'ic ic--go')}</a>
            <a class="btn btn--line" href="tel:{PHONE_TEL}">{ic('i-phone')}{PHONE_DISPLAY}</a>
          </div>
        </div>
        <div class="phero__pic phero__pic--art" data-fx="iris" style="--d:.15s">
          <img src="assets/images/illustrations/{art}" alt="{alt}" width="400" height="400" fetchpriority="high">
        </div>
      </div>
    </section>"""


def about_doctor(focus):
    """Same 'About the doctor' block on every treatment page; `focus` is one sentence about this condition."""
    return f"""
    <section class="sec" aria-labelledby="why-title">
      <div class="wrap why">
        <div class="pic" data-fx="iris">
          <img src="assets/images/portrait-coat.webp" srcset="assets/images/portrait-coat-720.webp 720w, assets/images/portrait-coat.webp 1200w" sizes="(max-width: 900px) 90vw, 440px" alt="Dr. Neema Bhat in a white coat, arms folded, smiling" width="1200" height="1911" loading="lazy">
          <div class="pic__badge">{ic('i-award')}<div><b>Dr. Neema Bhat</b><span>MD (USA) · FAAP · Haemato-Oncologist</span></div></div>
        </div>
        <div>
          <p class="tag" data-fx="wipe-x">About the doctor</p>
          <h2 class="title" id="why-title" data-fx="wipe">Dr. <span class="grad-text">Neema Bhat</span></h2>
          <ul class="why__list">
            <li data-fx="fade">{ic('i-marrow')}<div><b>Speciality</b><span>Hematologist, Pediatric Oncologist &amp; Bone Marrow Transplant Specialist</span></div></li>
            <li data-fx="fade" style="--d:.06s">{ic('i-award')}<div><b>Education</b><span>MD (USA) · Fellowship (FAAP) in Pediatric Hematology, Oncology &amp; Bone Marrow Transplantation, Penn State Health, USA</span></div></li>
          </ul>
          <p class="lead" data-fx="fade">Dr. Neema Bhat is a Haemato-Oncologist in Bangalore with more than ten years of experience treating blood disorders and blood cancers in children and adults. {focus}</p>
          <div class="hero__acts" data-fx="fade"><a class="btn btn--line" href="about.html">Read more about her{ic('i-go', 'ic ic--go')}</a></div>
        </div>
      </div>
    </section>"""


def book_section(title, text, topic):
    """Same closing booking block on every treatment page (phone only, no address or timings)."""
    return f"""
    <section class="sec sec--tight" aria-labelledby="bk-title">
      <div class="wrap">
        <div class="cta" data-fx="iris">
          <div>
            <h2 id="bk-title">{title}</h2>
            <p>{text}</p>
            <ul class="cta__info">
              <li>{ic('i-phone')}<a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> · Call or WhatsApp</li>
            </ul>
          </div>
          <div class="cta__acts">
            <a class="btn btn--white" href="contact.html?topic={topic}">Book an Appointment{ic('i-go', 'ic ic--go')}</a>
            <a class="btn btn--line" href="{WA}" target="_blank" rel="noopener">{ic('i-wa')}WhatsApp</a>
          </div>
        </div>
        <p class="small">Medical disclaimer: This page is for general information only and is not a substitute for medical advice. Please consult a doctor for diagnosis and treatment.</p>
      </div>
    </section>"""


def _li(t):
    return f'<li>{ic("i-check")}<span>{t}</span></li>'


def _ul(items):
    return '<ul class="list">' + "".join(_li(t) for t in items) + "</ul>"


def _box(icon, title, inner, d=0, hid=""):
    idattr = f' id="{hid}"' if hid else ""
    return f'<div class="box" data-fx="fade" style="--d:{d:.2f}s"><h3{idattr}>{ic(icon)}{title}</h3>{inner}</div>'


def _p(t):
    return f'<p class="box__sub">{t}</p>'


def _sec(inner, tint=False, label=""):
    lab = f' aria-labelledby="{label}"' if label else ""
    return f'\n    <section class="sec{" sec--tint" if tint else ""}"{lab}>\n      <div class="wrap">{inner}\n      </div>\n    </section>'


def _cards(items, cls="cards3"):
    return f'<div class="{cls}">' + "".join(
        f'<div class="card" data-fx="fade" style="--d:{(k % 3) * 0.06:.2f}s">{ic(i)}<h3>{t}</h3><p>{d}</p></div>' for k, (i, t, d) in enumerate(items)) + "</div>"


def _conds(items, cols4=True):
    return f'<ul class="conds{" conds--4" if cols4 else ""}">' + "".join(
        f'<li data-fx="fade" style="--d:{(k % 3) * 0.06:.2f}s"><b>{ic(i)}{t}</b><p>{d}</p></li>' for k, (i, t, d) in enumerate(items)) + "</ul>"


def _sym(items, cls="sym sym--3"):
    return f'<ul class="{cls}">' + "".join(
        f'<li data-fx="fade" style="--d:{(k % 3) * 0.06:.2f}s">{ic(i)}<b>{t}</b><span>{d}</span></li>' for k, (i, t, d) in enumerate(items)) + "</ul>"


def _olist(items):
    return '<ol class="olist">' + "".join(
        f'<li data-fx="fade" style="--d:{(k % 3) * 0.06:.2f}s"><span class="olist__n">{k + 1:02d}</span><div><b>{t}</b><p>{d}</p></div></li>' for k, (t, d) in enumerate(items)) + "</ol>"


def _table(headers, rows):
    """Readable table that turns into stacked cards on phones."""
    th = "".join(f"<th>{h}</th>" for h in headers)
    trs = "".join("<tr>" + "".join(f'<td data-label="{headers[k]}">{"<b>" + c + "</b>" if k == 0 else c}</td>' for k, c in enumerate(r)) + "</tr>" for r in rows)
    return f'<div class="dtable-wrap" data-fx="fade"><table class="dtable"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'


def _alert(bold, rest, warn=False):
    return f'<p class="alert{" alert--warn" if warn else ""}" data-fx="fade">{ic("i-shield" if warn else "i-heart")}<span><b>{bold}</b> {rest}</span></p>'


def _steps(items):
    """Numbered sub-sections (e.g. the four parts of thalassemia care)."""
    return '<div class="tsteps">' + "".join(
        f'<div class="tstep" data-fx="fade" style="--d:{(k % 2) * 0.06:.2f}s"><span class="olist__n">{k + 1:02d}</span><div><h3>{t}</h3>{body}</div></div>' for k, (t, body) in enumerate(items)) + "</div>"


def cond_page(fname, title, desc, ld_name, alt_names, hero, sections, faqs, faq_intro, focus, book):
    _, ld_faq = faq_block(faqs)
    ld_page = ('  <script type="application/ld+json">{"@context":"https://schema.org","@type":"MedicalWebPage","name":"%s",'
               '"about":{"@type":"MedicalCondition","name":"%s","alternateName":[%s]},'
               '"author":{"@type":"Physician","name":"Dr. Neema Bhat"}}</script>\n') % (title.split(" | ")[0], ld_name, ",".join('"%s"' % a for a in alt_names))
    return head(title, desc, fname, LD_PHYSICIAN + ld_page + ld_faq) + f"""
<body data-page="service">{ICONS}{header('service', fname)}
  <main id="main">{hero}{''.join(sections)}
{about_doctor(focus)}
{faq_section(faqs, faq_intro)}
{book}
  </main>
""" + footer()


# ------------------------------------------------------------------ HEMATOLOGY (overview)
def hematology():
    T = "hematology treatment in Bangalore"
    hero = cond_hero("hm-title", "Hematology Treatment", 'Hematology Treatment in <span class="grad-text">Bangalore</span>',
                     f"Hematology is the branch of medicine that diagnoses and treats diseases of the blood, bone marrow and lymph nodes: anemia, bleeding and clotting problems, low or high blood counts, inherited conditions like thalassemia, and blood cancers. Many blood disorders can be cured or well controlled when they are found early.",
                     "hematology-cells.svg", "Illustration of red blood cells, a white blood cell and platelets", "hematology")
    intro = _sec(f"""
        <div class="split split--top">
          <div>
            <p class="tag" data-fx="wipe-x">Overview</p>
            <h2 class="title" id="hm-what" data-fx="wipe">What is <span class="grad-text">hematology?</span></h2>
            <p class="lead" data-fx="fade">Dr. Neema Bhat, a US-trained hematologist in Bangalore with 10+ years of experience, offers complete {T} for adults and children, from simple anemia to bone marrow transplant.</p>
            <p class="lead" data-fx="fade">Blood disorders are very common in India. About 48 out of every 100 women and two out of three young children in Karnataka have anemia (NFHS-5). In 2022, about 55,600 people in India were diagnosed with leukemia, 55,300 with lymphoma and 19,400 with multiple myeloma (National Cancer Registry Programme, ICMR). An abnormal blood report is often the first clue, and the right {T} starts with finding the exact cause.</p>
          </div>
          {_box('i-cells', 'Your blood, in simple words', _p('Your blood has three main types of cells, all made in the bone marrow:') + _ul(['<b>Red blood cells</b> carry oxygen to every part of your body.', '<b>White blood cells</b> fight infections.', '<b>Platelets</b> help your blood clot and stop bleeding.']) + _p('Your blood also contains clotting proteins that work with platelets to seal a cut. When any of these are too low, too high or not working properly, it is called a blood disorder.'))}
        </div>
        <div class="cols2 mt">
          {_box('i-doc', 'What does a hematologist do?', _p('A hematologist is a doctor who specialises in blood disorders. A hematologist:') + _ul(['Finds out why your blood counts or blood tests are abnormal', 'Treats anemia, bleeding and clotting disorders, and low or high blood counts', 'Treats blood cancers such as leukemia, lymphoma and myeloma (a hemato-oncologist)', 'Performs bone marrow tests and bone marrow (stem cell) transplants', 'Works with other doctors, such as gynaecologists, surgeons and kidney specialists, when a blood problem affects their care']))}
          {_box('i-child', 'Pediatric hematology', _p('A pediatric hematologist treats blood disorders in babies, children and teenagers. Dr. Neema Bhat is trained in both adult and pediatric hematology.') + _p('Children may look pale, bruise easily, bleed for a long time after a fall or vaccine, get infections often, or have swollen glands or a swollen tummy. Children with these signs should see a pediatric hematologist.'), 0.08)}
        </div>""", label="hm-what")
    signs = _sec(sec_head('Signs', 'Signs you should see a <span class="grad-text">hematologist</span>', 'Many blood disorders are first found on a routine blood test. See a hematologist if you have:', hid='hm-signs') + _sym([
        ("i-drop", "Low hemoglobin", "Anemia that keeps coming back or does not improve with iron tablets"),
        ("i-activity", "Constant tiredness", "Weakness, breathlessness or pale skin"),
        ("i-cells", "Easy bruising", "Small red or purple spots on the skin (petechiae)"),
        ("i-drop", "Frequent bleeding", "Nosebleeds, bleeding gums, or heavy or long periods"),
        ("i-shield", "Bleeding that won’t stop", "After a cut, tooth extraction or surgery"),
        ("i-heart", "Leg swelling or pain", "Swelling, pain or redness in one leg, possibly a clot (DVT)"),
        ("i-users", "Repeated clots", "Blood clots at a young age, or repeated clots or miscarriages"),
        ("i-flask", "Abnormal counts", "Low or high platelet, white cell or red cell counts on your report"),
        ("i-thermo", "Frequent infections", "Infections that are frequent or unusual"),
        ("i-cells", "Swollen lymph nodes", "Glands in the neck, armpit or groin"),
        ("i-scale", "Unexplained symptoms", "Fever, night sweats or weight loss without a clear reason"),
        ("i-bone", "Bone pain", "Especially in the back"),
    ]) + _alert('See a doctor urgently', 'if you have heavy bleeding that will not stop, sudden chest pain or breathlessness, sudden weakness on one side of the body, blood in vomit or black stools, high fever with very low white cell counts, or fainting.'), tint=True, label="hm-signs")
    causes = _sec(f"""<div class="cols2">
          {_box('i-flask', 'What causes blood disorders?', _p('Blood disorders have many causes. The common ones are:') + _ul(['<b>Nutritional deficiency:</b> low iron, vitamin B12 or folate.', '<b>Blood loss:</b> heavy periods, piles, ulcers or slow bleeding in the gut.', '<b>Inherited (genetic) conditions:</b> thalassemia, sickle cell disease, hemophilia and some clotting disorders.', '<b>Immune system problems:</b> the body attacks its own blood cells, as in ITP or autoimmune hemolytic anemia.', '<b>Long-term illnesses:</b> kidney disease, liver disease, thyroid problems and autoimmune diseases.', '<b>Infections:</b> such as dengue, malaria, viral infections and worm infections.', '<b>Medicines:</b> some painkillers, antibiotics, blood thinners and chemotherapy.', '<b>Bone marrow problems:</b> aplastic anemia, myelodysplastic syndromes and blood cancers.']), hid='hm-cause')}
          {_box('i-users', 'Who is at risk?', _p('The risk is higher for:') + _ul(['Women with heavy periods, and pregnant or breastfeeding women', 'Babies, children and teenagers, who grow fast', 'Vegetarians and vegans, who may get too little vitamin B12', 'Adults over 60', 'People with a family history of blood disorders', 'Couples where both partners are thalassemia carriers', 'People with long-term illnesses or who take certain medicines for a long time', 'People who smoke or have had radiation or chemotherapy', 'People who are overweight, inactive, or sit for long hours (higher clot risk)']), 0.08)}
        </div>""", label="hm-cause")
    untreated = _sec(sec_head('Complications', 'What happens if blood disorders are <span class="grad-text">left untreated?</span>', 'Some blood problems seem mild at first but can become serious over time:', hid='hm-untr') + _conds([
        ("i-heart", "Heart strain", "Long-term anemia makes the heart work harder and can lead to heart failure."),
        ("i-drop", "Dangerous bleeding", "Low platelets or clotting disorders can cause bleeding into joints, the gut or the brain."),
        ("i-lungs", "Blood clots", "An untreated clot in the leg can travel to the lungs (pulmonary embolism) and be life-threatening."),
        ("i-thermo", "Serious infections", "Low white cell counts make infections more likely and harder to treat."),
        ("i-shield", "Organ damage", "Iron overload from repeated transfusions can harm the heart and liver."),
        ("i-child", "Pregnancy problems", "Anemia and clotting disorders raise the risk of miscarriage, preterm birth and heavy bleeding."),
        ("i-micro", "Late cancer diagnosis", "An abnormal blood count can be the first sign of leukemia, lymphoma or myeloma. Early diagnosis improves treatment results."),
    ], cols4=False), tint=True, label="hm-untr")
    disorders = _sec(sec_head('Conditions', 'Blood disorders <span class="grad-text">we treat</span>', center=True, hid='hm-dis') + _table(
        ["Group", "Conditions", "What it means in simple words"], [
            ("Red blood cell disorders", f'<a href="{ANEMIA_PAGE}">Iron deficiency anemia</a>, vitamin B12 and folate deficiency, anemia of chronic disease, hemolytic anemia, polycythemia', "Too few red cells, red cells that break down early, or too many red cells."),
            ("Inherited blood disorders", f'<a href="{THAL_PAGE}">Thalassemia</a>, sickle cell disease, hereditary spherocytosis, G6PD deficiency', "Conditions passed down in families that affect how red cells are made or how long they last."),
            ("Platelet disorders", "ITP (immune thrombocytopenia), low platelets in dengue or pregnancy, high platelets (thrombocytosis)", "Too few or too many platelets, causing bleeding or clotting."),
            ("Bleeding disorders", "Hemophilia A and B, von Willebrand disease, other clotting factor deficiencies", "The blood does not clot properly, so bleeding lasts longer."),
            ("Clotting (thrombosis) disorders", "Deep vein thrombosis (DVT), pulmonary embolism, thrombophilia, antiphospholipid syndrome", "The blood clots too easily, blocking veins or arteries."),
            ("White blood cell disorders", "Low white cell count (neutropenia), high white cell count", "Too few white cells to fight infection, or too many for an unclear reason."),
            ("Bone marrow failure", "Aplastic anemia, pure red cell aplasia", "The bone marrow stops making enough blood cells."),
            ("Blood cancers", f'Acute and chronic <a href="{LEUK_PAGE}">leukemia</a>, Hodgkin and non-Hodgkin <a href="{LYMPH_PAGE}">lymphoma</a>, <a href="{MYEL_PAGE}">multiple myeloma</a>, myelodysplastic syndromes (MDS), myeloproliferative neoplasms (MPN)', "Cancers that start in the bone marrow, blood or lymph nodes."),
            ("Immune and rare disorders", "HLH (hemophagocytic lymphohistiocytosis), primary immunodeficiency disorders, thrombotic microangiopathy", "Rare conditions where the immune system or small blood vessels damage blood cells."),
            ("Children’s blood disorders", "Anemia, thalassemia, ITP, hemophilia and childhood leukemia", "Specialised care for babies, children and teenagers."),
        ]), label="hm-dis")
    dx = _sec(sec_head('Diagnosis', 'How are blood disorders <span class="grad-text">diagnosed?</span>', 'The right test depends on your symptoms and blood report. Dr. Neema Bhat may advise some of these tests:', hid='hm-dx') + _olist([
        ("Complete Blood Count (CBC)", "Checks hemoglobin, white cells and platelets."),
        ("Peripheral blood smear", "Looks at the shape and size of blood cells under a microscope."),
        ("Reticulocyte count", "Shows whether the bone marrow is making new red cells."),
        ("Iron studies, vitamin B12 and folate", "Find nutritional causes of anemia."),
        ("Hemoglobin electrophoresis / HPLC", "Checks for thalassemia and sickle cell disease."),
        ("Coagulation tests", "PT/INR, APTT, fibrinogen and D-dimer check how well your blood clots."),
        ("Clotting factor assays &amp; von Willebrand tests", "Diagnose hemophilia and other bleeding disorders."),
        ("Thrombophilia screening", "Looks for inherited or acquired causes of repeated blood clots."),
        ("Flow cytometry (immunophenotyping)", "Identifies abnormal cells in leukemia and lymphoma."),
        ("Bone marrow aspiration and biopsy", "Examines the bone marrow directly."),
        ("Cytogenetics, FISH &amp; molecular tests", "Find genetic changes that guide treatment of blood cancers."),
        ("Lymph node biopsy", "Diagnoses lymphoma."),
        ("Imaging", "Ultrasound, Doppler, CT or PET-CT find clots, enlarged lymph nodes or spleen, and check the spread of blood cancers."),
    ]), tint=True, label="hm-dx")
    tx = _sec(sec_head('Treatment', 'Hematology treatment <span class="grad-text">options</span>', 'Treatment depends on the type of blood disorder, its cause, your age and your overall health. Some conditions need only a short course of treatment, while others need long-term care.', hid='hm-tx') + _cards([
        ("i-apple", "Nutritional supplements", "Iron, vitamin B12 and folic acid as tablets, syrups or injections."),
        ("i-syringe", "IV iron infusion", "A faster way to replace iron when tablets do not work or cannot be taken."),
        ("i-users", "Treating the root cause", "Such as heavy periods, gut bleeding, infections, thyroid or kidney problems, with the right specialist."),
        ("i-syringe", "Blood transfusion", "Red cells, platelets or plasma, for severe anemia, bleeding or low counts."),
        ("i-cells", "Iron chelation therapy", "Removes extra iron in patients who need regular transfusions, such as in thalassemia."),
        ("i-shield", "Clotting factor replacement", "Including preventive (prophylaxis) therapy for hemophilia and other bleeding disorders."),
        ("i-lungs", "Anticoagulation therapy", "Blood-thinning treatment that treats and prevents blood clots, with regular monitoring."),
        ("i-shield", "Immune-suppressing therapy", "For ITP, autoimmune hemolytic anemia and aplastic anemia."),
        ("i-pill", "Count-boosting medicines", "To raise platelets, white cells or red cells when needed."),
        ("i-syringe", "Chemotherapy", "Anti-cancer medicines for leukemia, lymphoma and myeloma."),
        ("i-pill", "Targeted therapy", "Medicines that attack specific changes in cancer cells, often as tablets."),
        ("i-award", "Immunotherapy", "Monoclonal antibodies and other treatments that help the immune system fight blood cancers."),
        ("i-cells", "CAR-T cell therapy", "For selected relapsed blood cancers, where suitable and available."),
        ("i-marrow", "Autologous stem cell transplant", "Your own stem cells are returned after high-dose treatment, mainly for myeloma and lymphoma."),
        ("i-marrow", "Allogeneic (donor) stem cell transplant", f'Healthy stem cells from a matched or half-matched donor. It can cure thalassemia, sickle cell disease, aplastic anemia and some leukemias. <a href="{BMT_PAGE}">Learn more</a>'),
        ("i-drop", "Therapeutic phlebotomy", "Removing blood to lower high red cell counts or iron levels."),
        ("i-flask", "Plasmapheresis", "Plasma exchange removes harmful antibodies or proteins from the blood."),
        ("i-heart", "Supportive care", "Infection prevention, vaccines, pain relief and nutrition support."),
        ("i-chat", "Counselling &amp; palliative care", "Emotional support and symptom control for patients and families."),
        ("i-clock", "Watch and wait", "Active monitoring for mild or slow-growing conditions that do not need treatment yet."),
    ], "cards3 cards3--5") + _alert('Do not take iron tablets, blood thinners or steroids for a long time without a doctor’s advice.', 'Wrong or delayed treatment can hide a serious cause.', warn=True), label="hm-tx")
    living = _sec(f"""<div class="cols2">
          {_box('i-sun', 'Living well and preventing blood disorders', _p('Not every blood disorder can be prevented, but these steps help:') + _ul(['<b>Eat iron-rich foods:</b> ragi, green leafy vegetables (palak, methi, drumstick leaves), dals, rajma, chana, jaggery, dates, eggs, chicken, fish and meat.', '<b>Add vitamin C to meals</b> (lemon, amla, orange, guava) to help your body absorb iron, and avoid tea or coffee within one hour of meals.', '<b>Get enough vitamin B12:</b> milk, curd, paneer, eggs and fish. Vegetarians may need supplements.', '<b>Prevent blood clots:</b> stay active, drink enough water, and walk or stretch during long journeys.']), hid='hm-live')}
          {_box('i-shield', 'Protect yourself', _ul(['<b>Get a thalassemia carrier test (HPLC)</b> before marriage or pregnancy. If both partners are carriers, each child has a 1 in 4 chance of thalassemia major.', '<b>Protect yourself from infections:</b> use mosquito protection against dengue and malaria, and take deworming tablets as advised.', '<b>Avoid self-medication:</b> some painkillers and other medicines affect platelets and blood counts.', '<b>If you have a bleeding disorder:</b> tell your dentist and surgeon before any procedure, and carry a medical card.', 'Keep every follow-up appointment and repeat blood tests as advised.']) + _p('India’s Anemia Mukt Bharat programme gives free iron and folic acid tablets to children, teenagers, and pregnant and breastfeeding women through government health centres.'), 0.08)}
        </div>""", tint=True, label="hm-live")
    faqs = [
        ("What does a hematologist treat?", "A hematologist treats diseases of the blood, bone marrow and lymph nodes. This includes anemia, bleeding and clotting disorders, low or high blood counts, thalassemia, sickle cell disease and blood cancers like leukemia, lymphoma and myeloma."),
        ("When should I see a hematologist?", "See a hematologist if your blood report shows abnormal counts, if anemia does not improve with treatment, or if you have easy bruising, unusual bleeding, repeated blood clots, swollen glands or a family history of a blood disorder."),
        ("Is a hematologist the same as an oncologist?", "Not exactly. A hematologist treats all blood disorders, both non-cancerous and cancerous. A hemato-oncologist specialises in blood cancers. An oncologist treats cancers of other organs. Dr. Neema Bhat treats both blood disorders and blood cancers."),
        ("Does being referred to a hematologist mean I have cancer?", "No. Most people seen by a hematologist have non-cancerous problems like anemia, low platelets or clotting issues. A referral simply means a blood specialist will find the cause faster."),
        ("What happens at the first hematology appointment?", "The doctor will ask about your symptoms, medical and family history, and medicines. She will examine you and review your reports. You may need more blood tests, and rarely a bone marrow test."),
        ("What should I bring to my first visit?", "Bring all recent blood reports, scans, discharge summaries and a list of your current medicines. Older reports help show how your counts have changed over time."),
        ("Are blood disorders curable?", "Many are. Nutritional anemias are usually cured once the cause is fixed. Some conditions like hemophilia need lifelong care, while thalassemia, sickle cell disease, aplastic anemia and some blood cancers can be cured with a bone marrow transplant."),
        ("Is a bone marrow test painful?", "The area is numbed with local anaesthesia, so most people feel only pressure and brief discomfort. The test usually takes 15 to 30 minutes, and you can go home the same day."),
        ("Can children see a hematologist?", "Yes. Dr. Neema Bhat is a US board-certified pediatrician and pediatric hematologist. She treats babies, children and teenagers with anemia, thalassemia, ITP, hemophilia and childhood leukemia."),
        ("How much does hematology treatment in Bangalore cost?", "The cost depends on the condition. Blood tests and tablets are usually affordable, while transfusions, chemotherapy and bone marrow transplant cost more. The clinic can share an estimate after your first consultation."),
    ]
    return cond_page(HEMA_PAGE, "Hematology Treatment in Bangalore | Dr. Neema Bhat, Hematologist",
                     "Hematology treatment in Bangalore with Dr. Neema Bhat, US-trained hematologist with 10+ years of experience: anemia, bleeding and clotting disorders, thalassemia and blood cancers in adults and children.",
                     "Blood disorders", ["Hematologic diseases"], hero, [intro, signs, causes, untreated, disorders, dx, tx, living], faqs,
                     "Quick answers to the questions patients ask most about seeing a hematologist.",
                     "She finds out why your blood counts are abnormal and treats that cause, not just the numbers.",
                     book_section("Abnormal blood report?", "Unexplained tiredness, bruising or bleeding? Get it checked by a blood specialist. Book a consultation for hematology treatment in Bangalore with Dr. Neema Bhat today.", "hematology"))


# ------------------------------------------------------------------ THALASSEMIA
def thalassemia():
    T = "thalassemia treatment in Bangalore"
    hero = cond_hero("th-title", "Thalassemia Treatment", 'Thalassemia Treatment in <span class="grad-text">Bangalore</span>',
                     "Thalassemia is an inherited blood disorder in which the body cannot make enough healthy hemoglobin. Low levels cause anemia, tiredness and, in severe forms, a lifelong need for blood transfusions. The good news: thalassemia can be managed well, and for many children it can be cured.",
                     "thalassemia-cells.svg", "Illustration of small, pale red blood cells and a DNA strand, representing inherited thalassemia", "thalassemia")
    intro = _sec(f"""
        <div class="split split--top">
          <div>
            <p class="tag" data-fx="wipe-x">Overview</p>
            <h2 class="title" id="th-what" data-fx="wipe">What is <span class="grad-text">thalassemia?</span></h2>
            <p class="lead" data-fx="fade">Hemoglobin is made of two kinds of protein chains, called alpha and beta. In thalassemia, a change in the genes means the body makes too little of one chain. Red blood cells then become small, weak and break down early, which leads to anemia.</p>
            <p class="lead" data-fx="fade">Thalassemia is not an infection and not a cancer. It is passed from parents to children through genes, and it is present from birth.</p>
            <p class="lead" data-fx="fade">India has more children with thalassemia major than any other country: about 1 to 1.5 lakh children live with it, and 10,000 to 15,000 more are born every year (Union Health Ministry). With the right {T}, children and adults with thalassemia can grow, study, work and live full lives.</p>
          </div>
          {_box('i-users', 'How is thalassemia inherited?', _p('Thalassemia passes down when both parents carry a faulty gene. Carriers are usually healthy and often don’t know they carry it.') + _ul(['<b>If both parents are carriers:</b> each pregnancy has a 1 in 4 chance of a child with thalassemia major, a 2 in 4 chance of a carrier child and a 1 in 4 chance of an unaffected child.', '<b>If only one parent is a carrier:</b> children cannot get thalassemia major, but each child has a 1 in 2 chance of being a carrier.']))}
        </div>""", label="th-what")
    types = _sec(sec_head('Types', 'Types of <span class="grad-text">thalassemia</span>', center=True, hid='th-types') + _table(
        ["Type", "What it means", "Treatment needed"], [
            ("Thalassemia minor (trait or carrier)", "One faulty gene. Usually no symptoms or only mild anemia.", "Usually none. Important for marriage and pregnancy planning."),
            ("Thalassemia intermedia", "Moderate anemia that starts later in childhood.", "Regular check-ups; transfusions only at times."),
            ("Thalassemia major (Cooley’s anemia)", "Two faulty beta genes. Severe anemia from early childhood.", "Regular transfusions and iron removal for life, or a bone marrow transplant."),
            ("Alpha thalassemia", "Ranges from silent carrier to HbH disease to a severe form before birth.", "Depends on the type; many need no treatment."),
            ("HbE beta thalassemia", "A mix of HbE and beta thalassemia, more common in eastern India.", "Ranges from mild to transfusion-dependent."),
        ]), tint=True, label="th-types")
    signs = _sec(sec_head('Signs &amp; symptoms', 'Signs and symptoms of <span class="grad-text">thalassemia</span>', 'Thalassemia minor usually causes no symptoms. Children with thalassemia major usually show signs between 6 months and 2 years of age:', hid='th-sym') + _sym([
        ("i-activity", "Pale skin &amp; tiredness", "Looking pale and tiring easily"),
        ("i-child", "Poor feeding", "Irritability and slow weight gain"),
        ("i-drop", "Jaundice", "Yellow eyes or skin and dark urine"),
        ("i-heart", "Swollen tummy", "From an enlarged spleen or liver"),
        ("i-scale", "Slow growth", "And delayed puberty"),
        ("i-bone", "Bone changes", "In the face and skull, if treatment starts late"),
    ]) + f"""<div class="cols2 mt">
          {_box('i-adult', 'Thalassemia symptoms in adults', _p('Adults with thalassemia minor may have mild, lifelong anemia that does not improve with iron tablets. Adults with thalassemia intermedia may have tiredness, bone pain, gallstones or an enlarged spleen.'))}
          {_box('i-doc', 'When should you see a thalassemia specialist?', _ul(['Your baby or child is pale, feeding poorly or not gaining weight', 'Your blood report shows small red cells or low hemoglobin that does not improve with iron', 'You or your partner is a thalassemia carrier and you are planning marriage or a pregnancy', 'A family member has thalassemia', 'Your child needs blood transfusions and you want to know about a cure']), 0.08)}
        </div>""", label="th-sym")
    dx = _sec(sec_head('Diagnosis', 'How is thalassemia <span class="grad-text">diagnosed?</span>', 'Dr. Neema Bhat may advise some of these thalassemia diagnostic tests:', hid='th-dx') + _olist([
        ("Complete Blood Count (CBC)", "Shows low hemoglobin and small red cells (low MCV and MCH)."),
        ("Peripheral blood smear", "Shows the shape of the red cells under a microscope."),
        ("HPLC or hemoglobin electrophoresis", "The main thalassemia test. It measures HbA2 and HbF and confirms carriers and thalassemia major."),
        ("Iron studies (ferritin)", "To tell thalassemia minor apart from iron deficiency, which looks similar on a CBC."),
        ("DNA (genetic) test", "Finds the exact gene change. Useful for family planning and prenatal testing."),
        ("HLA typing", "Checks whether a brother or sister is a matching donor for a bone marrow transplant."),
        ("Prenatal testing", "If both parents are carriers, a test at 10 to 12 weeks of pregnancy (CVS) can show whether the baby is affected."),
    ]), tint=True, label="th-dx")
    tx = _sec(sec_head('Treatment', 'Thalassemia treatment <span class="grad-text">options</span>', f'Your {T} depends on the type and how severe it is. Thalassemia minor usually needs no treatment. For thalassemia major, care has four parts:', hid='th-tx') + _steps([
        ("Regular blood transfusions", _p('Most children with thalassemia major need safe, filtered blood every 2 to 4 weeks for life. Regular transfusions keep hemoglobin at a healthy level, so the child grows normally and the bones do not change shape.')),
        ("Iron chelation therapy", _p('Every transfusion adds iron that the body cannot remove. Over time this iron builds up in the heart, liver and glands. Iron chelation medicines (deferasirox and deferiprone tablets, or deferoxamine injections) remove the extra iron and protect these organs. They must be taken every day.')),
        ("Regular monitoring", _p('Serum ferritin is checked every few months. Older children and adults also need yearly heart and liver MRI scans (T2*) to measure iron, along with tests for growth, thyroid, diabetes and bone health.')),
        ("Supportive care", _ul(['Folic acid, calcium and vitamin D as advised', 'Vaccines, including hepatitis B', 'Hydroxyurea for some people with thalassemia intermedia or HbE beta thalassemia', 'Newer medicines that can reduce transfusion needs in some adults'])),
    ]) + _alert('Do not take iron tablets unless your doctor confirms you are low in iron.', 'People with thalassemia, including carriers, can build up too much iron.', warn=True), label="th-tx")
    bmt_sec = _sec(f"""
        <div class="split split--top">
          <div>
            <p class="tag" data-fx="wipe-x">A cure</p>
            <h2 class="title" id="th-bmt" data-fx="wipe">Bone marrow transplant: <span class="grad-text">the cure for thalassemia</span></h2>
            <p class="lead" data-fx="fade">A bone marrow (stem cell) transplant is currently the only established cure for thalassemia major in India. Healthy stem cells from a matched donor replace the patient’s bone marrow, so the body starts making normal red blood cells. After a successful transplant, the child no longer needs transfusions or iron chelation.</p>
            <div class="hero__acts" data-fx="fade"><a class="btn btn--line" href="{BMT_PAGE}">About bone marrow transplant{ic('i-go', 'ic ic--go')}</a></div>
          </div>
          {_box('i-marrow', 'What families should know', _ul(['<b>The best donor is a fully matched brother or sister.</b> Each sibling has a 1 in 4 chance of being a full match, so HLA typing of the whole family is the first step.', '<b>Earlier is better.</b> Results are best when the child is young, has had good chelation and has little iron damage to the liver.', '<b>Other donors:</b> if no sibling matches, a matched unrelated donor from a donor registry, or a half-matched parent, may be possible in an experienced centre.', '<b>Gene therapy</b> is approved in some countries and is being studied in India, but it is not yet routinely available here.']))}
        </div>""", tint=True, label="th-bmt")
    cost = _sec(f"""<div class="cols2">
          {_box('i-doc', 'Cost of thalassemia treatment in Bangalore', _p('Costs depend on the type of thalassemia and the treatment chosen:') + _ul(['<b>Lifelong transfusion care:</b> transfusions every few weeks, daily chelation medicines and regular tests. This is an ongoing monthly cost for life.', '<b>Bone marrow transplant:</b> a one-time cost that usually ranges from ₹15 to ₹25 lakh in India, depending on the donor type and the child’s condition.', '<b>Carrier test (HPLC):</b> a simple, low-cost blood test.']) + _p('The clinic can give you a personalised estimate after the first consultation.'), hid='th-cost')}
          {_box('i-heart', 'Financial help and free treatment options', _ul(['<b>Thalassemia Bal Sewa Yojana:</b> Coal India’s scheme gives up to ₹10 lakh towards a bone marrow transplant for eligible children aged 12 or younger, from families earning up to ₹8 lakh a year, at empanelled hospitals.', '<b>Day care and NGO support:</b> Bangalore has thalassemia day care centres and patient groups that help with transfusions and medicines, such as the Thalassaemia and Sickle Cell Society of Bangalore.', '<b>Insurance and CSR funds:</b> some insurance policies and company CSR programmes support transplant costs. The team can guide you through the paperwork.']), 0.08)}
        </div>""", label="th-cost")
    comp = _sec(sec_head('Complications', 'Complications of <span class="grad-text">thalassemia</span>', 'Without regular treatment, or if iron is not removed well, thalassemia can cause:', hid='th-comp') + _conds([
        ("i-heart", "Heart problems", "An irregular heartbeat and heart failure, from iron overload."),
        ("i-flask", "Liver damage", "And gallstones."),
        ("i-scale", "Hormone problems", "Diabetes, thyroid problems and delayed puberty."),
        ("i-activity", "Weak bones", "Osteoporosis and bone changes in the face."),
        ("i-shield", "Enlarged spleen", "And a higher risk of infections."),
        ("i-child", "Slow growth", "In children."),
    ], cols4=False) + _p('Good transfusion care, daily chelation and regular check-ups prevent most of these problems.'), tint=True, label="th-comp")
    prevent = _sec(f"""<div class="cols2">
          {_box('i-users', 'Preventing thalassemia: carrier test before marriage and pregnancy', _p('Thalassemia major can be prevented. A simple HPLC blood test shows whether you are a carrier. It is best done:') + _ul(['Before marriage, especially if someone in the family has thalassemia', 'Before planning a pregnancy, or early in pregnancy', 'For brothers and sisters of anyone with thalassemia']) + _p('If both partners are carriers, genetic counselling and a prenatal test at 10 to 12 weeks of pregnancy can show whether the baby is affected, so families can plan with full information.'), hid='th-prev')}
          {_box('i-sun', 'Living well with thalassemia', _ul(['Keep to the transfusion schedule and never skip chelation medicines', 'Eat a balanced diet; avoid iron-rich supplements and tonics unless prescribed', 'Stay active; most children can go to school and play sports', 'Track ferritin, growth and heart checks in one file and bring it to every visit', 'Connect with other families through local thalassemia support groups']), 0.08)}
        </div>""", label="th-prev")
    faqs = [
        ("Can thalassemia be cured permanently?", "Yes. A bone marrow transplant can cure thalassemia major permanently, especially when it is done early with a matched sibling donor. Without a transplant, thalassemia is managed lifelong with transfusions and iron chelation."),
        ("What is the best treatment for thalassemia major?", "For children with a matched donor, a bone marrow transplant is the best treatment because it is curative. For others, regular transfusions with good iron chelation give a long and active life."),
        ("How often do thalassemia patients need blood?", "Most people with thalassemia major need a transfusion every 2 to 4 weeks. The exact gap depends on their hemoglobin level, age and weight."),
        ("Is thalassemia minor dangerous?", "No. Thalassemia minor usually causes no symptoms or only mild anemia and needs no treatment. It matters mainly for family planning, because two carriers can have a child with thalassemia major."),
        ("Can a thalassemia minor person get married?", "Yes. A carrier can marry anyone. If both partners are carriers, they should have genetic counselling and prenatal testing in each pregnancy."),
        ("How long do thalassemia major patients live?", "With regular transfusions, daily chelation and good follow-up, many people with thalassemia major now live well into adulthood, study, work and have families. A successful transplant offers a normal life expectancy."),
        ("What kind of doctor treats thalassemia?", "A hematologist, especially a pediatric hematologist with bone marrow transplant experience, treats thalassemia. Dr. Neema Bhat is a US-trained hematologist in Bangalore who manages both transfusion care and transplant."),
        ("What is the thalassemia treatment cost in India?", "Lifelong transfusion care is an ongoing monthly cost. A bone marrow transplant usually costs ₹15 to ₹25 lakh, and schemes such as Thalassemia Bal Sewa Yojana can cover up to ₹10 lakh for eligible children."),
        ("Can I get free or low-cost treatment for thalassemia in Bangalore?", "Yes. Government schemes, CSR funds and NGO-run day care centres in Bangalore help with transfusions, medicines and transplant costs. The team can help you check which ones you qualify for."),
        ("Is thalassemia a blood cancer?", "No. Thalassemia is an inherited problem with hemoglobin production. It is not cancer and it is not contagious."),
    ]
    return cond_page(THAL_PAGE, "Thalassemia Treatment in Bangalore | Dr. Neema Bhat, Hematologist",
                     "Thalassemia treatment in Bangalore with Dr. Neema Bhat, US-trained hematologist and bone marrow transplant specialist: carrier testing, transfusion and chelation care, and curative transplant.",
                     "Thalassemia", ["Thalassaemia", "Cooley's anemia"], hero, [intro, types, signs, dx, tx, bmt_sec, cost, comp, prevent], faqs,
                     "Quick answers to the questions families ask most about thalassemia and its treatment.",
                     "For thalassemia, she guides families from carrier testing and transfusion care to a possible cure with bone marrow transplant.",
                     book_section("Expert thalassemia care, close by", "Whether you have just received a carrier report or your child needs transfusions, book a consultation for thalassemia treatment in Bangalore with Dr. Neema Bhat to understand your options, including a possible cure.", "thalassemia"))


# ------------------------------------------------------------------ LEUKEMIA
def leukemia():
    T = "leukemia treatment in Bangalore"
    hero = cond_hero("lk-title", "Leukemia Treatment", 'Leukemia Treatment in <span class="grad-text">Bangalore</span>',
                     "Leukemia is a cancer of the blood that starts in the bone marrow, where blood cells are made. The marrow makes too many abnormal white blood cells, which crowd out the healthy cells your body needs. Today, many types of leukemia can be treated very well, and many can be cured, especially in children.",
                     "leukemia-cells.svg", "Illustration of many abnormal white blood cells crowding out red blood cells, representing leukemia", "leukaemia")
    intro = _sec(f"""
        <div class="split split--top">
          <div>
            <p class="tag" data-fx="wipe-x">Overview</p>
            <h2 class="title" id="lk-what" data-fx="wipe">What is <span class="grad-text">leukemia?</span></h2>
            <p class="lead" data-fx="fade">Your bone marrow makes three kinds of blood cells: red cells that carry oxygen, white cells that fight infection and platelets that stop bleeding. In leukemia, a change in the DNA of a young blood cell makes it grow out of control. These leukemia cells fill the bone marrow, so the body cannot make enough normal blood cells. This leads to anemia, infections and bleeding.</p>
            <p class="lead" data-fx="fade">Leukemia is not contagious and, in most people, it is not inherited from parents.</p>
          </div>
          {_box('i-heart', 'You are not alone', _p('Hearing the words “blood cancer” is frightening. The right diagnosis, a clear plan and an experienced team make a real difference to the outcome.') + _p(f'With timely {T}, most children with the commonest type of leukemia are alive and well years later.'))}
        </div>""", label="lk-what")
    types = _sec(sec_head('Types', 'Types of <span class="grad-text">leukemia</span>', 'Doctors group leukemia by how fast it grows (acute or chronic) and by the type of white cell involved (lymphoid or myeloid).', hid='lk-types') + _table(
        ["Type", "Who it usually affects", "How it is treated"], [
            ("Acute lymphoblastic leukemia (ALL)", "Most common cancer in children; also seen in adults", "Chemotherapy in phases for about 2 to 3 years; immunotherapy or transplant for high-risk or relapsed cases"),
            ("Acute myeloid leukemia (AML)", "More common in adults; can occur in children", "Intensive chemotherapy; targeted medicines; transplant for many patients"),
            ("Acute promyelocytic leukemia (APL)", "A special type of AML", "Vitamin A-based medicine (ATRA) with arsenic trioxide; one of the most curable leukemias when treated quickly"),
            ("Chronic myeloid leukemia (CML)", "Mostly adults", "Daily targeted tablets (such as imatinib) that control it for years"),
            ("Chronic lymphocytic leukemia (CLL)", "Older adults", "Often only regular monitoring at first; tablets or other medicines when needed"),
        ]), tint=True, label="lk-types")
    signs = _sec(sec_head('Signs &amp; symptoms', 'Signs and symptoms of <span class="grad-text">leukemia</span>', 'Early symptoms can look like a viral fever or simple tiredness, which is why leukemia is sometimes found on a routine blood test. Watch for:', hid='lk-sym') + _sym([
        ("i-activity", "Tiredness", "Weakness and pale skin"),
        ("i-thermo", "Repeated fevers", "Fevers or infections that keep coming back"),
        ("i-drop", "Easy bleeding", "Bruising, bleeding gums or frequent nosebleeds"),
        ("i-cells", "Skin spots", "Tiny red or purple spots (petechiae)"),
        ("i-bone", "Bone or joint pain", "In children, limping or refusing to walk"),
        ("i-cells", "Swollen glands", "In the neck, armpits or groin"),
        ("i-heart", "Swollen tummy", "From an enlarged liver or spleen"),
        ("i-scale", "Weight loss", "Poor appetite and night sweats"),
        ("i-child", "Signs in children", "Paleness, repeated fever, unusual bruises, leg pain and tiredness that stops play"),
    ]) + _p('These symptoms usually have common causes, but if they last more than a week or two, a simple blood test is worth doing.') + _alert('Go to a hospital immediately', 'if there is bleeding that will not stop, a high fever with shivering, breathlessness, severe headache or confusion.'), label="lk-sym")
    causes = _sec(f"""<div class="cols2">
          {_box('i-flask', 'What causes leukemia? Risk factors', _p('In most people, the exact cause is not known. Leukemia is not caused by anything a parent did or did not do. Factors that raise the risk include:') + _ul(['Previous chemotherapy or radiation for another cancer', 'Genetic conditions such as Down syndrome', 'Long-term exposure to benzene and some industrial chemicals', 'Smoking (for AML)', 'Certain bone marrow disorders, such as myelodysplastic syndrome (MDS)', 'A family history, mainly for CLL']), hid='lk-cause')}
          {_box('i-doc', 'When should you see a blood cancer specialist?', _p('See a hematologist (blood cancer doctor) if:') + _ul(['Your blood report shows very high or very low white cells, low platelets or abnormal (blast) cells', 'You or your child has unexplained bruises, repeated fevers or bone pain with low blood counts', 'A doctor suspects leukemia and you want a confirmed diagnosis and a second opinion', 'Leukemia has come back after treatment, or you want to know about transplant or CAR-T']), 0.08)}
        </div>""", tint=True, label="lk-cause")
    dx = _sec(sec_head('Diagnosis', 'How is leukemia <span class="grad-text">diagnosed?</span>', 'A correct and complete diagnosis decides the right treatment. Dr. Neema Bhat may advise these tests:', hid='lk-dx') + _olist([
        ("CBC and peripheral smear", "Show abnormal white cell counts and leukemia (blast) cells."),
        ("Bone marrow aspiration and biopsy", "A small sample from the hip bone, taken under local anesthesia or sedation, confirms leukemia."),
        ("Flow cytometry", "Identifies the exact type, such as B-cell ALL, T-cell ALL or AML."),
        ("Cytogenetic and molecular tests", "Find gene changes (such as the Philadelphia chromosome) that guide treatment and predict outcome."),
        ("Lumbar puncture", "Checks whether leukemia cells have reached the brain and spinal fluid, mainly in ALL."),
        ("Other tests", "Imaging, heart checks before chemotherapy, and HLA typing of the family if a transplant may be needed."),
    ]), label="lk-dx")
    tx = _sec(sec_head('Treatment', 'Leukemia treatment <span class="grad-text">options</span>', f'Your {T} depends on the type of leukemia, its gene changes, the patient’s age and overall health. Treatment is planned to destroy the leukemia cells and let the bone marrow make healthy blood again.', hid='lk-tx') + _steps([
        ("Chemotherapy", _p('Chemotherapy is given in planned phases. Induction (about 4 to 6 weeks) aims to clear leukemia from the bone marrow, a state called remission. Consolidation removes any remaining cells. For ALL, a long maintenance phase of mostly oral tablets follows, so total treatment lasts about 2 to 3 years. Medicine is also given into the spinal fluid to protect the brain.')),
        ("Targeted therapy", _p('Targeted medicines attack a specific change in the leukemia cells: tablets such as imatinib and dasatinib for CML and Philadelphia-positive ALL, and ATRA with arsenic trioxide for APL. Many patients with CML only need daily tablets and regular blood tests.')),
        ("Immunotherapy and CAR-T cell therapy", _p('Antibody medicines help the immune system find and kill leukemia cells, mainly in ALL that has come back. In CAR-T therapy, the patient’s own immune cells are trained in a lab to attack the cancer. India approved its own CAR-T therapy in 2023 for some relapsed B-cell blood cancers, at a fraction of the cost abroad.')),
        ("Bone marrow (stem cell) transplant", _p(f'A transplant replaces diseased marrow with healthy stem cells from a donor. It is advised for high-risk AML, ALL that has come back, and some other cases. The donor can be a fully matched brother or sister, a matched unrelated donor from a registry, or a half-matched family member. <a href="{BMT_PAGE}">Learn more</a>')),
        ("Supportive care", _ul(['Blood and platelet transfusions during low-count periods', 'Quick treatment of fever and infections with antibiotics', 'Nutrition support and anti-nausea medicines', 'Fertility preservation advice for teenagers and adults before treatment starts'])),
    ]), tint=True, label="lk-tx")
    cure = _sec(sec_head('Outlook', 'Is leukemia curable? <span class="grad-text">Success rates</span>', 'Yes, many types of leukemia can be cured or controlled for many years. Results depend on the type, its gene changes, age and how well the leukemia responds to the first phase of treatment.', hid='lk-cure') + _conds([
        ("i-child", "Childhood ALL", "A large Indian study of 2,695 children found that 73 to 88 out of 100 were alive four years after treatment, depending on their risk group (Lancet Regional Health, Southeast Asia, 2025)."),
        ("i-award", "APL", "One of the most curable leukemias when diagnosed and treated without delay."),
        ("i-check", "CML", "Most people on daily targeted tablets live long, active lives."),
        ("i-marrow", "AML", "Harder to treat, but outcomes improve with the right chemotherapy and a transplant when needed."),
    ]), label="lk-cure")
    cost = _sec(f"""<div class="cols2">
          {_box('i-doc', 'Cost of leukemia treatment in Bangalore', _p('The cost depends on the type of leukemia, the treatment plan and the length of hospital stay:') + _ul(['<b>Chemotherapy for ALL:</b> spread over 2 to 3 years, with the highest costs in the first few months.', '<b>AML:</b> intensive chemotherapy needs longer hospital stays, so costs are higher.', '<b>CML:</b> mainly the ongoing cost of daily tablets and blood tests.', '<b>Bone marrow transplant:</b> a one-time cost that depends on the donor type.', '<b>CAR-T therapy:</b> about ₹30 to 35 lakh in India, compared with about ₹3.3 crore in the US.']) + _p('The clinic can give you a personalised estimate after the first consultation.'), hid='lk-cost')}
          {_box('i-heart', 'Financial help', _ul(['<b>Ayushman Bharat PM-JAY:</b> covers cancer care, including medical oncology and bone marrow transplants, up to ₹5 lakh per family per year for eligible families.', '<b>Insurance:</b> most health insurance plans cover chemotherapy and transplant; the team helps with pre-authorisation.', '<b>NGOs and CSR funds:</b> several charities support children with leukemia during treatment. The team can guide you to them.']), 0.08)}
        </div>""", tint=True, label="lk-cost")
    life = _sec(_box('i-sun', 'Life during and after leukemia treatment', _ul(['<b>Call the team at once if you get a fever (38°C or higher) during chemotherapy.</b> With low white cells, infections can become serious quickly.', 'Wash hands often, avoid crowds and eat freshly cooked food during low-count periods.', 'Hair loss from chemotherapy is temporary; hair grows back after treatment.', 'Children can usually return to school once the intensive phase is over.', 'After treatment, regular check-ups and blood tests watch for relapse and long-term effects.']), hid='lk-life'), label="lk-life")
    faqs = [
        ("Is leukemia curable?", "Many types are. Most children with ALL and most people with APL can be cured, and CML can be controlled for many years with daily tablets. AML is harder to treat, but a transplant improves the chances of cure."),
        ("Can leukemia in children be cured?", "Yes. Childhood ALL is one of the most treatable childhood cancers. In a large Indian study, 73 to 88 out of 100 children were alive four years after treatment, depending on their risk group."),
        ("What is the most effective treatment for leukemia?", "It depends on the type. Chemotherapy is the main treatment for ALL and AML, targeted tablets for CML, ATRA with arsenic for APL, and a bone marrow transplant for high-risk or relapsed leukemia."),
        ("How long does leukemia treatment take?", "ALL treatment takes about 2 to 3 years, though most of it is oral tablets at home after the first months. AML treatment usually takes about 6 months. CML tablets are taken long term."),
        ("Can leukemia be treated without chemotherapy?", "Some types can. CML is treated with targeted tablets, APL mainly with ATRA and arsenic, and early CLL may only need monitoring. ALL and AML usually need chemotherapy."),
        ("Will chemotherapy cause hair loss?", "Many chemotherapy medicines cause hair loss, but it is temporary. Hair usually grows back within a few months after treatment."),
        ("Can leukemia come back after treatment?", "Sometimes. That is why regular follow-up and blood tests continue after treatment. If it comes back, options include more chemotherapy, immunotherapy, CAR-T or a transplant."),
        ("Which doctor treats leukemia?", "A hematologist or hemato-oncologist, a blood cancer specialist, treats leukemia. Dr. Neema Bhat is a US-trained hematologist in Bangalore who treats leukemia in children and adults."),
        ("What is the leukemia treatment cost in India?", "It varies with the type and plan. CML needs ongoing tablet costs, ALL treatment is spread over 2 to 3 years, and transplants and CAR-T cost more. PM-JAY and health insurance cover many of these treatments."),
        ("Is leukemia hereditary?", "Usually not. Most leukemias are caused by gene changes that happen during a person’s life, not ones passed down from parents. Leukemia is also not contagious."),
    ]
    return cond_page(LEUK_PAGE, "Leukemia Treatment in Bangalore | Dr. Neema Bhat, Hemato-Oncologist",
                     "Leukemia treatment in Bangalore with Dr. Neema Bhat, US-trained hematologist and bone marrow transplant specialist: diagnosis, chemotherapy, targeted therapy and transplant for children and adults.",
                     "Leukemia", ["Leukaemia", "Blood cancer"], hero, [intro, types, signs, causes, dx, tx, cure, cost, life], faqs,
                     "Quick answers to the questions patients and families ask most about leukemia.",
                     "For leukemia, she plans every step: diagnosis, chemotherapy, targeted medicines and transplant, for children and adults.",
                     book_section("Early expert care matters", "If you or your child has an abnormal blood report or a leukemia diagnosis, book a consultation for leukemia treatment in Bangalore with Dr. Neema Bhat for a clear diagnosis, a personalised plan and a second opinion if you need one.", "leukaemia"))


# ------------------------------------------------------------------ MULTIPLE MYELOMA
def myeloma():
    T = "multiple myeloma treatment in Bangalore"
    hero = cond_hero("my-title", "Multiple Myeloma Treatment", 'Multiple Myeloma Treatment in <span class="grad-text">Bangalore</span>',
                     "Multiple myeloma is a blood cancer that starts in plasma cells, a type of white blood cell in the bone marrow. It can weaken bones, damage kidneys and lower your blood counts. Myeloma is not usually curable, but it is very treatable today, and many people live active lives for years.",
                     "myeloma-cells.svg", "Illustration of plasma cells in the bone marrow and a bone, representing multiple myeloma", "multiple-myeloma")
    intro = _sec(f"""
        <div class="split split--top">
          <div>
            <p class="tag" data-fx="wipe-x">Overview</p>
            <h2 class="title" id="my-what" data-fx="wipe">What is <span class="grad-text">multiple myeloma?</span></h2>
            <p class="lead" data-fx="fade">Your bone marrow makes plasma cells. Healthy plasma cells make antibodies that fight infections. In multiple myeloma, one plasma cell turns abnormal and starts making copies of itself. These myeloma cells crowd out healthy blood cells in the bone marrow.</p>
            <p class="lead" data-fx="fade">Myeloma cells also release a faulty antibody called M-protein (monoclonal protein). M-protein does not fight infection. It can build up in the blood and urine and damage the kidneys. It is called “multiple” myeloma because it often affects many bones at the same time, such as the spine, skull, ribs and hips.</p>
          </div>
          {_box('i-users', 'Who gets myeloma?', _p('Myeloma usually affects people over 50. It is slightly more common in men than in women, and it can run in families, though rarely.') + _p(f'About 19,400 people in India were diagnosed with multiple myeloma in 2022 (National Cancer Registry Programme, ICMR). Early signs like back pain and tiredness are often mistaken for age or a “weak back”. With timely {T}, the disease can be controlled before it harms your bones and kidneys.'))}
        </div>""", label="my-what")
    crab = _sec(sec_head('Signs &amp; symptoms', 'Common signs of <span class="grad-text">multiple myeloma</span>', 'Early myeloma may cause no symptoms and is sometimes found on a routine blood test. Doctors remember the main signs with the word CRAB:', hid='my-sym') + _table(
        ["Letter", "Stands for", "What you may notice"], [
            ("C", "High calcium", "Thirst, passing urine often, constipation, confusion, nausea"),
            ("R", "Renal (kidney) damage", "Swelling in the legs, less urine, foamy urine, high creatinine"),
            ("A", "Anemia", "Tiredness, weakness, breathlessness, pale skin"),
            ("B", "Bone damage", "Back, rib or hip pain, bones that break easily"),
        ]) + f'<div class="mt">{_sym([("i-bone", "Back pain", "That does not go away with rest or painkillers"), ("i-thermo", "Frequent infections", "Like pneumonia or urinary infections"), ("i-scale", "Weight loss", "Without trying"), ("i-adult", "Numbness or tingling", "In the hands and feet"), ("i-drop", "Easy bruising", "Or bleeding"), ("i-eye", "Blurred vision", "Headaches or dizziness (from thick blood)")])}</div>' + _alert('See a doctor urgently', 'if you have sudden severe back pain, weakness or numbness in the legs, trouble passing urine or stools, confusion, or very little urine. These can be signs of spinal cord pressure or kidney failure, which need emergency care.'), tint=True, label="my-sym")
    causes = _sec(f"""<div class="cols2">
          {_box('i-flask', 'What causes myeloma and who is at risk?', _p('The exact cause is not known. It starts with changes (mutations) in the DNA of a plasma cell. It is not contagious, and it is not caused by anything you ate or did. The risk is higher for:') + _ul(['People over 50, and especially over 60', 'Men, who get myeloma slightly more often than women', 'People with MGUS (monoclonal gammopathy of undetermined significance), a harmless-looking condition that can slowly turn into myeloma', 'People with a parent, brother or sister who had myeloma or MGUS', 'People who are overweight', 'People with long-term exposure to radiation, pesticides, benzene or some industrial chemicals']) + _p('Having a risk factor does not mean you will get myeloma. Most people with MGUS never develop it, but they need a blood test once or twice a year.'), hid='my-cause')}
          {_box('i-shield', 'What happens if myeloma is left untreated?', _p('Active myeloma keeps growing without treatment. Over time it can cause:') + _ul(['<b>Bone fractures:</b> weak spots (lytic lesions) in the spine can collapse, causing severe pain and loss of height.', '<b>Spinal cord pressure:</b> a collapsed bone can press on nerves and cause leg weakness or paralysis.', '<b>Kidney failure:</b> M-protein and high calcium can damage the kidneys, sometimes needing dialysis.', '<b>Serious infections:</b> low healthy antibodies make pneumonia and other infections more likely and more dangerous.', '<b>Severe anemia and bleeding problems</b> that affect energy and daily life.']) + _p('The good news: when myeloma is treated early, much of this damage can be prevented, and kidney function often improves.'), 0.08)}
        </div>""", label="my-cause")
    types = _sec(sec_head('Conditions', 'Types of myeloma and plasma cell disorders <span class="grad-text">we treat</span>', center=True, hid='my-types') + _cards([
        ("i-flask", "MGUS", "A small amount of M-protein with no symptoms. Not cancer, but needs regular blood tests."),
        ("i-clock", "Smoldering myeloma", "More abnormal plasma cells than MGUS, but no organ damage yet. Watched closely; some high-risk cases are treated early."),
        ("i-cells", "Active (symptomatic) myeloma", "Myeloma that is causing CRAB problems or is likely to soon. Needs treatment."),
        ("i-drop", "Light chain myeloma", "Myeloma cells make only part of the antibody (light chains). More likely to affect the kidneys."),
        ("i-doc", "Non-secretory myeloma", "A rare type that makes little or no M-protein, so it is harder to spot on blood tests."),
        ("i-bone", "Solitary plasmacytoma", "A single tumour of plasma cells in one bone or soft tissue. Often treated with radiation."),
        ("i-thermo", "Plasma cell leukemia", "A rare, fast-growing form where myeloma cells spill into the blood. Needs urgent treatment."),
        ("i-heart", "AL amyloidosis", "A related condition where light chains form deposits in the heart, kidneys or nerves."),
        ("i-shield", "Relapsed or refractory myeloma", "Myeloma that comes back or does not respond to earlier treatment. Newer drugs and therapies can help."),
    ]) + f"""<div class="split split--top mt">
          {_box('i-award', 'Stages of multiple myeloma', _p('Doctors use the Revised International Staging System (R-ISS). It looks at blood tests (beta-2 microglobulin, albumin and LDH) and genetic changes in the myeloma cells. Your stage and risk group help Dr. Neema Bhat choose how strong your treatment should be.'))}
          {_table(["Stage", "What it means"], [("Stage I", "Lower amount of disease and no high-risk genetic changes. Usually the best outlook."), ("Stage II", "Neither Stage I nor Stage III."), ("Stage III", "Higher amount of disease, plus high-risk genetic changes or high LDH. Needs more intensive treatment.")])}
        </div>""", tint=True, label="my-types")
    dx = _sec(sec_head('Diagnosis', 'How is multiple myeloma <span class="grad-text">diagnosed?</span>', 'Myeloma is diagnosed with a mix of blood, urine, bone marrow and imaging tests. These tests also give a baseline, so your doctor can see how well treatment is working. Dr. Neema Bhat may advise:', hid='my-dx') + _olist([
        ("Complete Blood Count (CBC)", "Checks for anemia and low blood counts."),
        ("Kidney tests and calcium level", "Serum creatinine and calcium."),
        ("SPEP and immunofixation", "Serum protein electrophoresis finds and measures M-protein in the blood."),
        ("Serum free light chain test", "Measures kappa and lambda light chains."),
        ("Urine tests (24-hour protein, UPEP)", "Check for light chains in the urine (Bence Jones protein)."),
        ("Beta-2 microglobulin, albumin and LDH", "Used for staging."),
        ("Bone marrow aspiration and biopsy", "Confirms the diagnosis and counts the plasma cells."),
        ("FISH and genetic tests", "Show whether the myeloma is standard-risk or high-risk."),
        ("Imaging", "PET-CT, whole-body low-dose CT or MRI finds bone damage that a simple X-ray may miss."),
    ]), label="my-dx")
    tx = _sec(sec_head('Treatment', 'Multiple myeloma treatment <span class="grad-text">options</span>', f'Your {T} depends on your stage, risk group, age, kidney function and overall health. Most patients follow these steps:', hid='my-tx') + _olist([
        ("Induction (first) treatment", "3 to 6 months of drug combinations to bring the myeloma under control."),
        ("Stem cell transplant", "For patients who are fit enough, to deepen the response."),
        ("Maintenance", "A lighter, long-term medicine to keep the myeloma from coming back."),
        ("Regular follow-up", "Blood tests to catch any return early."),
    ]) + '<p class="lead mt" data-fx="fade" style="max-width:none">Dr. Neema Bhat creates a plan for you that may include:</p>' + _cards([
        ("i-pill", "Combination drug therapy", "Usually three or four medicines together, such as bortezomib, lenalidomide and dexamethasone. Many are tablets or small injections under the skin, given as outpatient care."),
        ("i-pill", "Targeted antibody therapy", "Medicines like daratumumab that attach to myeloma cells and help the immune system destroy them."),
        ("i-marrow", "Autologous stem cell transplant", f'Your own stem cells are collected, you receive high-dose chemotherapy, and the cells are returned to rebuild healthy bone marrow. It helps many patients stay in remission longer. <a href="{BMT_PAGE}">Learn more</a>'),
        ("i-clock", "Maintenance therapy", "Usually a daily tablet such as lenalidomide after transplant or first treatment."),
        ("i-award", "Newer treatments for relapse", "Next-generation drugs, bispecific antibodies and CAR-T cell therapy, where suitable and available."),
        ("i-radiation", "Radiation therapy", "For painful bone lesions, spinal cord pressure or a single plasmacytoma."),
        ("i-pill", "Bone-strengthening medicines", "Monthly zoledronic acid or denosumab to reduce fractures and bone pain."),
        ("i-heart", "Supportive care", "Pain relief, treatment for high calcium, kidney protection, transfusions when needed, infection prevention and vaccines."),
        ("i-check", "Watch and wait", "For MGUS and most smoldering myeloma, with regular blood tests and no treatment until it is needed."),
    ]) + _alert('Myeloma care works best when started early.', 'Do not delay treatment while trying only painkillers, calcium tablets or home remedies for back pain.', warn=True), tint=True, label="my-tx")
    living = _sec(_box('i-sun', 'Living well with multiple myeloma', _p('Good daily habits support your treatment and protect your bones and kidneys:') + _ul(['<b>Drink enough water:</b> about 2 to 3 litres a day, unless your doctor limits fluids. This protects the kidneys.', '<b>Avoid painkillers like ibuprofen and diclofenac (NSAIDs):</b> they can harm the kidneys. Ask your doctor which pain medicine is safe.', '<b>Eat a balanced Indian diet:</b> dals, eggs, paneer, curd, fish or chicken for protein; fruits and vegetables for vitamins. Wash raw foods well, as infections are more likely during treatment.', 'Do not take calcium or herbal supplements without asking your doctor, as calcium may already be high.', '<b>Stay gently active:</b> walking and light exercise keep you strong, but avoid heavy lifting and sudden twisting to protect the spine.', '<b>Prevent infections:</b> wash hands often, avoid crowds when your counts are low, and take the vaccines your doctor advises (flu, pneumonia, shingles, COVID-19).', 'Visit a dentist before starting bone-strengthening injections, and keep good dental hygiene.', 'Keep every follow-up appointment, even when you feel well.']) + _p('Multiple myeloma cannot be prevented. But people with MGUS or a family history can get regular blood tests so that any change is found early.'), hid='my-live'), label="my-live")
    faqs = [
        ("Which doctor should I see for multiple myeloma in Bangalore?", "A hematologist or hemato-oncologist (blood cancer specialist) treats multiple myeloma. Dr. Neema Bhat is a US-trained hematologist in Bangalore and bone marrow transplant specialist who treats myeloma and related plasma cell disorders."),
        ("Is multiple myeloma curable?", "Multiple myeloma is usually not curable, but it is very treatable. Many patients go into remission and stay well for years with modern medicines, stem cell transplant and maintenance therapy."),
        ("What is the life expectancy with multiple myeloma?", "It depends on the stage, genetic risk, age and response to treatment. With today’s treatments, many people live 7 to 10 years or longer, and some live much longer."),
        ("What is the first sign of multiple myeloma?", "The most common early sign is bone pain, especially in the back or ribs. Tiredness from anemia, frequent infections and kidney problems are also common early clues."),
        ("Is a bone marrow transplant needed for myeloma?", "Not for everyone. An autologous stem cell transplant (using your own cells) is advised for patients who are fit enough, because it helps keep myeloma in remission longer. Your doctor will tell you if it suits you."),
        ("How long does myeloma treatment take?", "First treatment usually takes 3 to 6 months. If a transplant is planned, it follows soon after. Maintenance therapy then continues, often for 2 years or more."),
        ("Can myeloma come back after treatment?", "Yes, myeloma often returns after some time. That is why regular follow-up tests matter. If it comes back, there are many effective treatment options."),
        ("What is the difference between MGUS and myeloma?", "MGUS is a harmless-looking condition with a small amount of M-protein and no symptoms. Myeloma has more abnormal cells and causes damage to bones, kidneys or blood. About 1 in 100 people with MGUS develop myeloma or a related disease each year."),
        ("Is multiple myeloma hereditary?", "Myeloma is not directly inherited. Having a close family member with myeloma or MGUS slightly raises your risk, but most patients have no family history."),
        ("How much does multiple myeloma treatment in Bangalore cost?", "The cost depends on the drugs used, the number of cycles and whether a stem cell transplant is needed. The clinic can share an estimate after your first consultation and help you with insurance paperwork."),
    ]
    return cond_page(MYEL_PAGE, "Multiple Myeloma Treatment in Bangalore | Dr. Neema Bhat, Hemato-Oncologist",
                     "Multiple myeloma treatment in Bangalore with Dr. Neema Bhat, US-trained hematologist and bone marrow transplant specialist: diagnosis, staging, drug therapy, autologous transplant and long-term care.",
                     "Multiple myeloma", ["Myeloma", "Plasma cell myeloma"], hero, [intro, crab, causes, types, dx, tx, living], faqs,
                     "Quick answers to the questions patients ask most about multiple myeloma.",
                     "For multiple myeloma, she builds a treatment plan around your type of myeloma, your health and your goals.",
                     book_section("Back pain that won’t go away?", "Abnormal protein or calcium on your report? Get it checked by a specialist. Book a consultation for multiple myeloma treatment in Bangalore with Dr. Neema Bhat today.", "multiple-myeloma"))


# ------------------------------------------------------------------ LYMPHOMA
def lymphoma():
    T = "lymphoma treatment in Bangalore"
    hero = cond_hero("ly-title", "Lymphoma Treatment", 'Lymphoma Treatment in <span class="grad-text">Bangalore</span>',
                     "Lymphoma is a blood cancer that starts in lymphocytes, the infection-fighting white blood cells of the lymphatic system. It often first shows as a painless swelling in the neck, armpit or groin. Lymphoma is one of the most treatable cancers, and many types can be cured, especially when found early.",
                     "lymphoma-cells.svg", "Illustration of a swollen lymph node with lymphocytes, representing lymphoma", "lymphoma")
    intro = _sec(f"""
        <div class="split split--top">
          <div>
            <p class="tag" data-fx="wipe-x">Overview</p>
            <h2 class="title" id="ly-what" data-fx="wipe">What is <span class="grad-text">lymphoma?</span></h2>
            <p class="lead" data-fx="fade">Your lymphatic system is part of your immune system. It includes the lymph nodes (glands), spleen, thymus, tonsils and bone marrow, connected by thin tubes that carry a fluid called lymph. It helps your body fight infections.</p>
            <p class="lead" data-fx="fade">Lymphoma starts when lymphocytes (B cells, T cells or NK cells) change and grow out of control. These abnormal cells collect in the lymph nodes and other organs, causing swelling. Lymphoma can also start in, or spread to, organs outside the lymph nodes, such as the stomach, skin, brain or bone marrow.</p>
            <p class="lead" data-fx="fade">The right {T} starts with knowing the exact type. Dr. Neema Bhat, a US-trained hematologist and bone marrow transplant specialist with 10+ years of experience, treats all types of lymphoma in adults and children.</p>
          </div>
          {_box('i-cells', 'The two main groups', _ul(['<b>Hodgkin lymphoma:</b> has a special abnormal cell called the Reed-Sternberg cell. It is common in young adults and has very high cure rates.', '<b>Non-Hodgkin lymphoma (NHL):</b> a large group of more than 60 subtypes. Some grow slowly (indolent), while others grow fast (aggressive) but often respond well to treatment.']) + _p(f'About 55,300 people in India were diagnosed with lymphoma in 2022: about 11,700 with Hodgkin lymphoma and 43,600 with non-Hodgkin lymphoma (National Cancer Registry Programme, ICMR). Swollen glands are often mistaken for an infection or tuberculosis. If a lump does not go away, timely {T} can make a big difference.'))}
        </div>""", label="ly-what")
    signs = _sec(sec_head('Signs &amp; symptoms', 'Common signs of <span class="grad-text">lymphoma</span>', 'The most common sign is a painless swelling of the lymph nodes. Watch for:', hid='ly-sym') + _sym([
        ("i-cells", "Painless lump", "In the neck, armpit or groin that does not go away after 2 to 3 weeks"),
        ("i-thermo", "Recurring fever", "Fever that keeps coming back without an infection"),
        ("i-moon", "Night sweats", "Heavy sweats that soak your clothes or bedsheets"),
        ("i-scale", "Weight loss", "Losing weight without trying"),
        ("i-activity", "Tiredness", "Constant tiredness or weakness"),
        ("i-shield", "Itching", "Itching all over the body"),
        ("i-lungs", "Cough or breathlessness", "Cough or chest pain, from swollen glands in the chest"),
        ("i-heart", "Swollen tummy", "Or pain in the upper left side, from an enlarged spleen"),
        ("i-flask", "Poor appetite", "Loss of appetite or feeling full quickly"),
        ("i-users", "Frequent infections", "Infections that keep coming back"),
    ]) + _p('Fever, drenching night sweats and weight loss of more than 10% in 6 months are called B symptoms. They help doctors stage the lymphoma and plan treatment.') + f"""<div class="cols2 mt">
          {_box('i-child', 'Lymphoma symptoms in children', _p('Children may have swollen glands in the neck, a swollen tummy, cough or breathing difficulty, fever or tiredness. Dr. Neema Bhat is a US board-certified pediatric hematologist-oncologist, so children with lymphoma get specialised care.'))}
          {_box('i-heart', 'See a doctor urgently', _p('If you have sudden breathlessness, swelling of the face, neck or arms, severe tummy pain, weakness in the legs, or high fever with chills.'), 0.08)}
        </div>""", tint=True, label="ly-sym")
    causes = _sec(f"""<div class="cols2">
          {_box('i-flask', 'What causes lymphoma and who is at risk?', _p('In most people, the exact cause is not known. It starts with changes (mutations) in the DNA of a lymphocyte. Lymphoma is not contagious. The risk is higher for:') + _ul(['<b>Age:</b> Hodgkin lymphoma is more common in young adults (15 to 35) and in people over 55. Most non-Hodgkin lymphomas are more common after 60.', 'Men, who get lymphoma slightly more often than women', '<b>Weak immune system:</b> HIV infection, organ transplant patients, or people taking long-term immune-suppressing medicines', '<b>Autoimmune diseases:</b> such as rheumatoid arthritis, lupus, Sjogren’s syndrome and celiac disease', '<b>Certain infections:</b> Epstein-Barr virus (EBV), Helicobacter pylori (stomach), hepatitis B and C, and HTLV-1', '<b>Family history:</b> a parent, brother or sister with lymphoma', '<b>Chemical exposure:</b> long-term exposure to some pesticides, herbicides and solvents', 'Previous cancer treatment with chemotherapy or radiation']) + _p('Most people with these risk factors never get lymphoma, and many people with lymphoma have no known risk factor.'), hid='ly-cause')}
          {_box('i-shield', 'What happens if lymphoma is left untreated?', _p('Aggressive lymphomas can grow within weeks, and even slow-growing types can change over time. Without treatment, lymphoma can cause:') + _ul(['<b>Spread to other organs:</b> such as the liver, lungs, bone marrow, brain or spinal cord.', '<b>Pressure on vital structures:</b> swollen glands in the chest can press on the windpipe or a large vein (superior vena cava syndrome), causing breathlessness and face swelling.', '<b>Bone marrow failure:</b> low blood counts lead to anemia, infections and bleeding.', 'Serious infections because the immune system is weakened.', '<b>Kidney problems:</b> from blocked urine flow or from fast-growing lymphoma cells breaking down (tumour lysis).', 'Fewer treatment choices and a lower chance of cure.']) + _p('The good news: most lymphomas respond well to treatment, and many people are cured when treatment starts early.'), 0.08)}
        </div>""", label="ly-cause")
    types = _sec(sec_head('Types', 'Types of lymphoma <span class="grad-text">we treat</span>', center=True, hid='ly-types') + _table(
        ["Type of lymphoma", "What it means in simple words"], [
            ("Classical Hodgkin lymphoma", "The most common type of Hodgkin lymphoma. Often affects young adults and is usually curable."),
            ("Nodular lymphocyte-predominant Hodgkin lymphoma", "A rare, slow-growing type of Hodgkin lymphoma."),
            ("Diffuse large B-cell lymphoma (DLBCL)", "The most common non-Hodgkin lymphoma. Grows fast but is often curable."),
            ("Follicular lymphoma", "A common slow-growing lymphoma. Can often be watched or treated gently for years."),
            ("Mantle cell lymphoma", "A less common type that can be slow or fast-growing."),
            ("Marginal zone and MALT lymphoma", "Slow-growing types. MALT lymphoma of the stomach is often linked to H. pylori infection."),
            ("Burkitt lymphoma", "A very fast-growing type, more common in children and young adults. Needs urgent treatment and is often curable."),
            ("Small lymphocytic lymphoma (SLL)", "The lymph node form of chronic lymphocytic leukemia (CLL). Usually slow-growing."),
            ("T-cell and NK-cell lymphomas", "Less common types, including peripheral T-cell, anaplastic large cell and NK/T-cell lymphoma."),
            ("Lymphoblastic lymphoma", "A fast-growing type, mostly in children and teenagers, treated like leukemia."),
            ("Primary CNS lymphoma", "Lymphoma that starts in the brain, spinal cord or eyes."),
            ("Lymphoma in children", "Specialised care for Hodgkin, Burkitt, lymphoblastic and anaplastic large cell lymphoma in children."),
        ]) + f"""<div class="split split--top mt">
          {_box('i-award', 'Stages of lymphoma', _p('Doctors use the Lugano staging system to stage most lymphomas, based on where the lymphoma is found. Stage I and II are called early (limited) stage, and Stage III and IV are called advanced stage. Even advanced-stage lymphoma is often curable.'))}
          {_table(["Stage", "What it means"], [("Stage I", "One lymph node area or one organ is affected."), ("Stage II", "Two or more lymph node areas on the same side of the diaphragm (the muscle under the lungs)."), ("Stage III", "Lymph node areas on both sides of the diaphragm, or nodes above the diaphragm with the spleen."), ("Stage IV", "Lymphoma has spread outside the lymph nodes, such as to the liver, lungs or bone marrow.")])}
        </div>""", tint=True, label="ly-types")
    dx = _sec(sec_head('Diagnosis', 'How is lymphoma <span class="grad-text">diagnosed?</span>', 'A biopsy is the only way to confirm lymphoma and find its exact type. Dr. Neema Bhat may advise:', hid='ly-dx') + _olist([
        ("Physical examination", "Checks the lymph nodes, liver and spleen."),
        ("Lymph node biopsy", "The whole node (excisional) or a core needle sample is removed and examined. A fine needle aspiration (FNAC) alone is usually not enough."),
        ("Immunohistochemistry", "Special stains on the biopsy identify the exact type of lymphoma."),
        ("Flow cytometry", "Studies the cells in blood, bone marrow or fluid samples."),
        ("Cytogenetics, FISH &amp; molecular tests", "Find genetic changes that help classify the lymphoma and guide treatment."),
        ("Blood tests", "CBC, kidney and liver function, LDH, uric acid and beta-2 microglobulin."),
        ("Viral tests", "Hepatitis B, hepatitis C and HIV, which matter before treatment."),
        ("PET-CT scan", "Shows where the lymphoma is in the body and is used for staging and checking response."),
        ("CT or MRI scan", "Used in some cases, including for the brain and spine."),
        ("Bone marrow biopsy", "In selected cases, to check if lymphoma has reached the bone marrow."),
        ("Lumbar puncture", "In some fast-growing lymphomas, to check the fluid around the brain and spine."),
        ("Heart and lung tests", "An echocardiogram and lung function tests before treatment."),
    ]), label="ly-dx")
    tx = _sec(sec_head('Treatment', 'Lymphoma treatment <span class="grad-text">options</span>', 'Treatment depends on the type of lymphoma, its stage, how fast it is growing, your age and your overall health. Some slow-growing lymphomas need no treatment at first, while fast-growing types need treatment straight away.', hid='ly-tx') + _cards([
        ("i-clock", "Watch and wait", "Active monitoring for some slow-growing lymphomas with no symptoms, with regular check-ups and scans."),
        ("i-syringe", "Chemotherapy", "Anti-cancer medicines given in planned cycles, usually as a combination. Most cycles are given as daycare treatment."),
        ("i-shield", "Chemoimmunotherapy", "Chemotherapy given together with a monoclonal antibody, the standard first treatment for most B-cell lymphomas."),
        ("i-award", "Monoclonal antibody therapy", "Antibodies that attach to markers on lymphoma cells, such as CD20. Also used as maintenance in some slow-growing lymphomas."),
        ("i-pill", "Targeted therapy", "Medicines, often tablets, that block signals lymphoma cells need to grow, such as BTK inhibitors."),
        ("i-pill", "Antibody-drug conjugates", "Antibodies that carry an anti-cancer medicine directly to lymphoma cells."),
        ("i-shield", "Immune checkpoint inhibitors", "Immunotherapy that helps the immune system attack lymphoma cells, mainly for relapsed Hodgkin lymphoma."),
        ("i-link", "Bispecific antibodies", "Newer immunotherapy that links immune cells to lymphoma cells, for relapsed lymphomas, where suitable and available."),
        ("i-cells", "CAR-T cell therapy", "The patient’s own immune cells are modified to attack lymphoma, for selected relapsed or refractory lymphomas."),
        ("i-radiation", "Radiation therapy", "Targeted radiation to affected lymph node areas, alone in early-stage disease or after chemotherapy."),
        ("i-marrow", "Autologous stem cell transplant", f'High-dose chemotherapy followed by return of your own stem cells, for lymphoma that relapses or is high-risk. <a href="{BMT_PAGE}">Learn more</a>'),
        ("i-marrow", "Allogeneic (donor) stem cell transplant", "For selected patients with relapsed or aggressive lymphoma."),
        ("i-check", "Treating the infection behind it", "For example, antibiotics for H. pylori in stomach MALT lymphoma, or antiviral treatment in hepatitis C-related lymphoma."),
        ("i-doc", "CNS prophylaxis", "Treatment to prevent lymphoma from spreading to the brain in high-risk patients."),
        ("i-heart", "Supportive care", "Prevention of infections and tumour lysis, hepatitis B protection, count-boosting medicines and transfusions when needed."),
        ("i-users", "Fertility preservation counselling", "Sperm or egg freezing before treatment for young patients."),
        ("i-chat", "Counselling &amp; palliative care", "Emotional support and symptom control for patients and families, at any stage of treatment."),
    ]) + _alert('Lymphoma treatment works best when the full course is completed.', 'Do not stop or delay treatment because the swelling has gone down.', warn=True), tint=True, label="ly-tx")
    life = _sec(_box('i-sun', 'Living well during and after lymphoma treatment', _p('These steps help you stay strong and lower the risk of problems during treatment:') + _ul(['<b>Check for fever:</b> a temperature of 100.4°F (38°C) or more during chemotherapy needs urgent medical attention.', '<b>Prevent infections:</b> wash hands often, avoid crowds and sick people when counts are low, and take the vaccines your doctor advises. Live vaccines are usually avoided during treatment.', '<b>Eat safe, healthy food:</b> freshly cooked home food, enough protein (dal, eggs, paneer, curd, fish, chicken), fruits and boiled or filtered water.', 'Drink plenty of fluids, especially in the first days of chemotherapy, to protect the kidneys.', '<b>Stay gently active:</b> walking and light exercise reduce tiredness.', '<b>Look after your mouth and skin:</b> use a soft toothbrush, and protect skin treated with radiation from the sun.', 'Avoid smoking and alcohol, and check with your doctor before taking herbal or home remedies.', 'Keep every follow-up appointment. Check-ups catch any relapse early and look for late effects on the heart, lungs, thyroid and fertility.']) + _p('Lymphoma cannot usually be prevented. But a swollen gland, fever or weight loss that does not go away should always be checked early.'), hid='ly-life'), label="ly-life")
    faqs = [
        ("Which doctor should I see for lymphoma in Bangalore?", "A hematologist or hemato-oncologist (blood cancer specialist) treats lymphoma. Dr. Neema Bhat is a US-trained hematologist in Bangalore who treats all types of lymphoma in adults and children."),
        ("Is lymphoma curable?", "Many lymphomas are curable. Most people with Hodgkin lymphoma and many with aggressive non-Hodgkin lymphoma, such as DLBCL, are cured with treatment. Slow-growing lymphomas are usually not cured but can be controlled for many years."),
        ("Does every swollen lymph node mean lymphoma?", "No. Most swollen glands are caused by infections and go away in 2 to 3 weeks. A painless lump that stays, grows, or comes with fever, night sweats or weight loss should be checked by a doctor."),
        ("How is lymphoma different from TB of the lymph nodes?", "Both can cause swollen glands, fever and weight loss, so they are often confused in India. A proper biopsy tells them apart. Never start TB treatment without a confirmed diagnosis."),
        ("What is the difference between Hodgkin and non-Hodgkin lymphoma?", "Hodgkin lymphoma has a special cell called the Reed-Sternberg cell and usually spreads in an orderly way from one lymph node group to the next. Non-Hodgkin lymphoma is a larger group with many subtypes that behave differently."),
        ("How long does lymphoma treatment take?", "Most treatment is given in cycles every 2 to 3 weeks, for about 3 to 6 months. Some slow-growing lymphomas need maintenance therapy for longer, while others need only watching."),
        ("Is chemotherapy the only treatment for lymphoma?", "No. Many patients receive chemotherapy combined with immunotherapy. Radiation, targeted therapy, stem cell transplant and CAR-T cell therapy are also used, depending on the type and stage."),
        ("Can lymphoma come back after treatment?", "Yes, it can, especially in slow-growing types. Regular follow-up helps find it early. If it returns, many effective treatments, including stem cell transplant, are available."),
        ("Can children get lymphoma?", "Yes. Hodgkin, Burkitt and lymphoblastic lymphomas are seen in children and teenagers, and most children are cured with treatment. Dr. Neema Bhat is a US board-certified pediatric hematologist-oncologist."),
        ("How much does lymphoma treatment cost in Bangalore?", "The cost depends on the type of lymphoma, the medicines used, the number of cycles, and whether radiation or a transplant is needed. The clinic can share an estimate after your first consultation."),
    ]
    return cond_page(LYMPH_PAGE, "Lymphoma Treatment in Bangalore | Dr. Neema Bhat, Hemato-Oncologist",
                     "Lymphoma treatment in Bangalore with Dr. Neema Bhat, US-trained hematologist and bone marrow transplant specialist: Hodgkin and non-Hodgkin lymphoma care for adults and children.",
                     "Lymphoma", ["Hodgkin lymphoma", "Non-Hodgkin lymphoma"], hero, [intro, signs, causes, types, dx, tx, life], faqs,
                     "Quick answers to the questions patients ask most about lymphoma.",
                     "For lymphoma, she plans treatment around the exact subtype, stage and risk, not a one-size-fits-all approach.",
                     book_section("A lump that will not go away?", "Fever, night sweats or weight loss without a reason? Get it checked by a blood cancer specialist. Book a consultation for lymphoma treatment in Bangalore with Dr. Neema Bhat today.", "lymphoma"))


# ------------------------------------------------------------------ PEDIATRIC ONCOLOGY
def pediatric_oncology():
    T = "pediatric oncology treatment in Bangalore"
    hero = cond_hero("po-title", "Pediatric Oncology", 'Pediatric Oncology Treatment in <span class="grad-text">Bangalore</span>',
                     "Pediatric oncology is the specialised care of babies, children and teenagers with cancer and serious blood disorders. Childhood cancers are rare, but most of them respond very well to treatment, and many children are cured.",
                     "pediatric-oncology.svg", "Illustration of a child with a heart and blood cells, representing childhood cancer care", "pediatric-oncology")
    intro = _sec(f"""
        <div class="split split--top">
          <div>
            <p class="tag" data-fx="wipe-x">Overview</p>
            <h2 class="title" id="po-what" data-fx="wipe">What is <span class="grad-text">pediatric oncology?</span></h2>
            <p class="lead" data-fx="fade">Pediatric oncology is the branch of medicine that diagnoses and treats cancer in babies, children and teenagers, usually from birth up to 18 years of age. A pediatric hemato-oncologist treats both childhood blood cancers and blood disorders.</p>
            <p class="lead" data-fx="fade">With the right {T}, children can finish treatment and go back to school, play and a normal life. Dr. Neema Bhat, a US board-certified pediatrician and pediatric hematologist-oncologist with 10+ years of experience, treats childhood blood cancers, solid tumours and blood disorders, including bone marrow transplant.</p>
            <p class="lead" data-fx="fade">About 3 out of every 100 cancer patients in India are children under 15, and leukemia makes up about 40% of childhood cancers (Indian Pediatrics study). In high-income countries, more than 80% of children with cancer survive (WHO). Early diagnosis and expert care help Indian children get the same chance.</p>
          </div>
          {_box('i-child', 'Childhood cancers are different', _ul(['They usually start in growing cells, such as the blood, brain, kidneys, nerves, bones and muscles.', 'They are rarely linked to lifestyle, such as diet or smoking.', 'They often grow fast, but they also usually respond well to treatment.', 'Treatment doses and medicines are planned for a child’s age, weight and growing body.']) + _p('Children are not small adults. They need a team trained to care for their bodies, their development and their emotions, along with support for the whole family.'))}
        </div>""", label="po-what")
    signs = _sec(sec_head('Warning signs', 'Warning signs of cancer <span class="grad-text">in children</span>', 'Most of these signs are caused by common, harmless illnesses. But if a sign lasts more than two weeks, keeps coming back, or gets worse, see a doctor. Watch for:', hid='po-sym') + _sym([
        ("i-activity", "Paleness &amp; tiredness", "Paleness, tiredness or weakness that does not go away"),
        ("i-drop", "Easy bruising", "Small red spots on the skin, or unusual bleeding (nose, gums)"),
        ("i-thermo", "Repeated fever", "Fever or infections that keep coming back without a clear cause"),
        ("i-cells", "A lump or swelling", "In the tummy, neck, armpit, groin or any part of the body"),
        ("i-cells", "Swollen glands", "That do not shrink after a few weeks"),
        ("i-bone", "Bone or joint pain", "Limping, or pain that wakes the child at night"),
        ("i-brain", "Morning headaches", "Headaches, especially in the morning, with vomiting"),
        ("i-adult", "Changes in walking", "Balance, vision or behaviour, or new fits (seizures)"),
        ("i-eye", "Eye changes", "A white glow in the pupil in photos, a new squint, or eye swelling"),
        ("i-scale", "Weight loss", "Loss of appetite or night sweats"),
        ("i-heart", "Swollen tummy", "A swollen or hard tummy"),
        ("i-users", "In teenagers", "A painless lump in the testicle"),
    ]) + _alert('See a doctor urgently', 'if your child has a high fever with very pale skin or bleeding, breathing difficulty, severe headache with vomiting, a fit, sudden weakness of the legs, or is unusually drowsy.'), tint=True, label="po-sym")
    causes = _sec(f"""<div class="cols2">
          {_box('i-flask', 'What causes cancer in children?', _p('In most children, the cause of cancer is not known. Childhood cancer usually starts from random changes (mutations) in the genes of growing cells. It is not caused by anything the parents did or did not do, and it is not contagious. A small number of children have a higher risk because of:') + _ul(['<b>Inherited genetic conditions:</b> such as Down syndrome (higher risk of leukemia), Li-Fraumeni syndrome, neurofibromatosis and hereditary retinoblastoma', 'A family history of retinoblastoma or certain inherited cancer syndromes', 'Some immune system disorders that are present from birth', '<b>Previous cancer treatment:</b> chemotherapy or radiation given for an earlier cancer', '<b>Certain infections:</b> such as Epstein-Barr virus (EBV), linked to some lymphomas, and HIV']) + _p('Because most childhood cancers cannot be prevented, early diagnosis is the most important step for a good outcome.'), hid='po-cause')}
          {_box('i-clock', 'Why early treatment matters', _p('Childhood cancers often grow quickly, so a delay of even a few weeks can change the outcome. If cancer in a child is not treated early:') + _ul(['The cancer can spread to other organs, making it harder to treat.', 'Serious complications can develop, such as severe infections, bleeding, kidney problems or pressure on the brain or spinal cord.', 'More intensive treatment may be needed, which can increase the risk of long-term side effects.', 'The chance of cure drops, especially for leukemia, retinoblastoma and solid tumours.', 'Vision, limbs or organs may be lost in cancers like retinoblastoma and bone tumours that could otherwise be saved.']) + _p('The good news: when found early and treated at a specialised centre, most childhood cancers can be controlled, and many can be cured.'), 0.08)}
        </div>""", label="po-cause")
    types = _sec(sec_head('Conditions', 'Childhood cancers and blood disorders <span class="grad-text">we treat</span>', center=True, hid='po-types') + _table(
        ["Condition", "What it means in simple words"], [
            (f'<a href="{LEUK_PAGE}">Acute lymphoblastic leukemia (ALL)</a>', "The most common childhood cancer. Abnormal white cells fill the bone marrow. Most children are cured with treatment."),
            ("Acute myeloid leukemia (AML) and chronic myeloid leukemia (CML)", "Other blood cancers that start in the bone marrow."),
            (f'Hodgkin and non-Hodgkin <a href="{LYMPH_PAGE}">lymphoma</a>', "Cancers of the lymph nodes and immune system, often showing as painless swollen glands."),
            (f'<a href="{BRAIN_PAGE}">Brain and spinal cord tumours</a>', "Growths in the brain or spine that can cause headaches, vomiting, or problems with walking or vision."),
            ("Neuroblastoma", "A tumour of nerve cells, often in the tummy, mostly in children under 5."),
            ("Wilms tumour (nephroblastoma)", "A kidney tumour in young children, often found as a swelling in the tummy."),
            ("Retinoblastoma", "An eye cancer in babies and young children, often seen as a white glow in the pupil."),
            ("Bone tumours (osteosarcoma, Ewing sarcoma)", "Cancers of the bone, usually in older children and teenagers, causing pain or swelling."),
            ("Rhabdomyosarcoma and other soft tissue sarcomas", "Cancers of the muscles and soft tissues."),
            ("Hepatoblastoma", "A liver tumour in young children."),
            ("Germ cell tumours", "Tumours of the ovaries, testes or other parts of the body."),
            ("Histiocytic disorders (LCH, HLH)", "Rare conditions where certain immune cells grow or act abnormally."),
            ("Childhood blood disorders", f'<a href="{THAL_PAGE}">Thalassemia</a>, sickle cell disease, aplastic anemia, ITP, hemophilia and severe <a href="{ANEMIA_PAGE}">anemia</a>.'),
        ]), tint=True, label="po-types")
    dx = _sec(sec_head('Diagnosis', 'How is childhood cancer <span class="grad-text">diagnosed?</span>', 'Dr. Neema Bhat chooses tests based on your child’s symptoms and age. Painful tests are done under sedation or anaesthesia so that your child is comfortable. Tests may include:', hid='po-dx') + _olist([
        ("Physical examination and history", "Including growth, development and family history."),
        ("CBC and peripheral smear", "Check blood counts and look for abnormal cells."),
        ("Blood chemistry tests", "Kidney and liver function, LDH, uric acid and electrolytes."),
        ("Tumour markers", "Such as AFP, beta-hCG and urine catecholamines for certain tumours."),
        ("Bone marrow aspiration and biopsy", "To diagnose leukemia and check if other cancers have spread to the marrow."),
        ("Flow cytometry", "Identifies the exact type of leukemia or lymphoma."),
        ("Cytogenetics, FISH &amp; molecular tests", "Find genetic changes that guide treatment and predict risk."),
        ("Imaging", "Ultrasound, X-ray, CT, MRI or PET-CT to find the tumour and check its spread."),
        ("Biopsy", "A small sample of the tumour or lymph node is examined to confirm the diagnosis."),
        ("Lumbar puncture (spinal tap)", "Checks whether cancer cells are in the fluid around the brain and spine."),
        ("Eye examination under anaesthesia", "For suspected retinoblastoma."),
        ("Heart, hearing and kidney tests", "Before treatment, as a baseline."),
    ]), label="po-dx")
    tx = _sec(sec_head('Treatment', 'Pediatric oncology treatment <span class="grad-text">options</span>', 'Treatment depends on the type of cancer, its stage and risk group, the child’s age and overall health. Most children receive a combination of treatments, planned by a team of specialists.', hid='po-tx') + _cards([
        ("i-syringe", "Risk-adapted chemotherapy", "Anti-cancer medicines given in planned cycles, with doses based on the child’s risk group, weight and age. Many cycles can be given as daycare treatment."),
        ("i-pill", "Targeted therapy", "Medicines that attack specific changes in cancer cells, such as in some leukemias."),
        ("i-shield", "Immunotherapy", "Monoclonal antibodies and other treatments that help the immune system fight cancer cells."),
        ("i-cells", "CAR-T cell therapy", "For selected children with relapsed leukemia or lymphoma, where suitable and available."),
        ("i-stetho", "Surgery", "To remove solid tumours such as Wilms tumour, neuroblastoma, liver and bone tumours, including limb-sparing surgery for bone cancers."),
        ("i-radiation", "Radiation therapy", "Carefully planned radiation for certain tumours, using techniques that protect healthy growing tissue."),
        ("i-marrow", "Bone marrow (stem cell) transplant", f'Autologous or donor transplant for high-risk or relapsed leukemia, neuroblastoma and other cancers, and for blood disorders like thalassemia and aplastic anemia. <a href="{BMT_PAGE}">Learn more</a>'),
        ("i-link", "Central line or port", "A long-term line to give medicines and take blood without repeated needle pricks."),
        ("i-drop", "Supportive care", "Transfusions, prevention and treatment of infections, anti-sickness medicines and fertility preservation counselling for teenagers."),
        ("i-heart", "Pain management &amp; palliative care", "To keep the child comfortable at every stage of treatment."),
        ("i-apple", "Nutrition support", "A diet plan to maintain weight and strength during treatment."),
        ("i-chat", "Psychological and child-life support", "Counselling and play therapy for the child, brothers and sisters, and parents."),
        ("i-clock", "Long-term follow-up", "Survivorship care: regular checks for growth, learning, heart, hormone and fertility effects after treatment ends."),
    ]) + _alert('Never stop or change treatment on your own, even if your child looks well.', 'Completing the full treatment plan gives the best chance of cure.', warn=True), tint=True, label="po-tx")
    care = _sec(_box('i-users', 'Caring for your child during and after treatment', _p('Parents play a big part in their child’s recovery. These steps help:') + _ul(['<b>Prevent infections:</b> wash hands often, keep the child away from people with fever, cough or chickenpox, and keep the central line or port clean and dry.', '<b>Check for fever:</b> a temperature of 100.4°F (38°C) or more during treatment is an emergency. Go to the hospital straight away.', '<b>Give safe food:</b> freshly cooked, hot home food and boiled or filtered water. Avoid street food, raw salads and cut fruit kept outside.', '<b>Encourage eating and drinking:</b> small, frequent meals help when appetite is low.', '<b>Look after the mouth:</b> gentle brushing with a soft brush and regular mouthwash as advised.', 'Follow the vaccine schedule your oncologist gives. Live vaccines are usually avoided during treatment.', '<b>Keep life as normal as possible:</b> play, schooling (at home or in school, as allowed) and time with family support your child’s emotional health.', '<b>Look after yourself too:</b> talk to the care team, counsellors and other parents for support.', 'Keep every follow-up visit after treatment ends. Survivorship care checks growth, learning, heart, hormones and fertility for years.']) + _p('Most children who finish treatment return to school and grow up to lead healthy, active lives.'), hid='po-care'), label="po-care")
    faqs = [
        ("Who is the right doctor for cancer in children in Bangalore?", "A pediatric oncologist or pediatric hemato-oncologist is the right specialist. Dr. Neema Bhat is a US board-certified pediatric hematologist-oncologist in Bangalore who treats childhood cancers and blood disorders."),
        ("What is the most common cancer in children?", "Leukemia, especially acute lymphoblastic leukemia (ALL), is the most common childhood cancer. In India, lymphomas and brain tumours are the next most common."),
        ("Can childhood cancer be cured?", "Yes, many childhood cancers can be cured. In high-income countries, more than 80% of children with cancer survive. Results are best when treatment starts early at a specialised centre and is completed fully."),
        ("What are the early signs of cancer in children?", "Common signs are paleness, easy bruising, repeated fever, a lump or swelling, bone pain, morning headaches with vomiting, and a white glow in the eye. See a doctor if any sign lasts more than two weeks."),
        ("Did I cause my child’s cancer?", "No. Most childhood cancers happen because of random gene changes in growing cells. They are not caused by anything parents did or did not do."),
        ("How long does childhood cancer treatment take?", "It depends on the cancer. Some solid tumours are treated in 6 to 12 months. Treatment for ALL usually takes about 2 to 3 years, though most of it is given as outpatient care."),
        ("Will my child need to stay in hospital throughout treatment?", "No. Children stay in hospital for some intensive phases, but much of the treatment is given as daycare or outpatient care, and children live at home."),
        ("Can my child go to school during cancer treatment?", "Many children can go back to school during the less intensive phases of treatment, when blood counts are safe. Your doctor will advise when it is safe."),
        ("What are the side effects of chemotherapy in children?", "Common side effects are hair loss, nausea, mouth sores, tiredness and a higher risk of infections. Most go away after treatment, and the care team helps manage them."),
        ("Will treatment affect my child’s growth or future fertility?", "Some treatments can affect growth, hormones or fertility. The team plans treatment to reduce these risks, discusses fertility preservation for teenagers, and checks for late effects during follow-up."),
    ]
    return cond_page(PEDONC_PAGE, "Pediatric Oncology Treatment in Bangalore | Dr. Neema Bhat",
                     "Pediatric oncology treatment in Bangalore with Dr. Neema Bhat, US board-certified pediatric hematologist-oncologist: childhood leukemia, lymphoma, solid tumours and blood disorders, including bone marrow transplant.",
                     "Childhood cancer", ["Pediatric cancer", "Pediatric oncology"], hero, [intro, signs, causes, types, dx, tx, care], faqs,
                     "Quick answers to the questions parents ask most about childhood cancer.",
                     "For children, she cares for the whole child, not only the cancer, with clear explanations for parents and support at every stage.",
                     book_section("Worried about a sign in your child?", "Or need a second opinion on a diagnosis? Early care makes a difference. Book a consultation for pediatric oncology treatment in Bangalore with Dr. Neema Bhat today.", "pediatric-oncology"))


# ------------------------------------------------------------------ BRAIN TUMOR
def brain_tumor():
    T = "brain tumor treatment in Bangalore"
    hero = cond_hero("br-title", "Brain Tumor Treatment", 'Brain Tumor Treatment in <span class="grad-text">Bangalore</span>',
                     "A brain tumor is an abnormal growth of cells in the brain or in the tissues around it. Some are benign (not cancer) and grow slowly, while others are malignant and grow fast. Many brain tumors can be removed or well controlled when found early, and the right treatment depends on the exact type.",
                     "brain-tumor.svg", "Illustration of a brain with a highlighted tumor, representing brain tumor treatment", "brain-tumor")
    intro = _sec(f"""
        <div class="split split--top">
          <div>
            <p class="tag" data-fx="wipe-x">Overview</p>
            <h2 class="title" id="br-what" data-fx="wipe">What is a <span class="grad-text">brain tumor?</span></h2>
            <p class="lead" data-fx="fade">Your brain controls everything you do: thinking, speaking, moving, seeing and breathing. A brain tumor forms when cells in or around the brain (such as the nerves, the pituitary gland or the coverings of the brain) grow out of control and form a mass. Both benign and malignant tumors can cause serious problems because the skull has no room to expand.</p>
            <p class="lead" data-fx="fade">A tumor can cause problems in two ways: by pressing on or damaging nearby brain tissue, and by blocking the flow of fluid around the brain, which raises pressure inside the skull. Even a benign brain tumor can be serious if it grows in an important area. That is why every brain tumor needs expert care.</p>
            <p class="lead" data-fx="fade">Dr. Neema Bhat, a US-trained pediatric hematologist-oncologist with 10+ years of experience, works with neurosurgeons and radiation oncologists to plan complete {T}, with special expertise in children.</p>
          </div>
          {_box('i-doc', 'Two main groups', _ul(['<b>Primary brain tumors</b> start in the brain or its surrounding tissues. They can be benign or malignant.', '<b>Secondary (metastatic) brain tumors</b> start in another part of the body, such as the lungs, breast or kidney, and spread to the brain. In adults, these are more common than primary brain tumors.']) + _p(f'India sees over 28,000 new brain tumor cases every year (IARC data). Brain tumors are also among the most common cancers in children, after leukemia and lymphoma. Early signs like headaches and vomiting are easy to ignore, so timely {T} can protect brain function and quality of life.'))}
        </div>""", label="br-what")
    signs = _sec(sec_head('Signs &amp; symptoms', 'Common signs of a <span class="grad-text">brain tumor</span>', 'Symptoms depend on the size and location of the tumor. Watch for:', hid='br-sym') + _sym([
        ("i-brain", "Headaches", "New, getting worse, or worse in the morning or when lying down"),
        ("i-flask", "Nausea or vomiting", "Especially in the morning"),
        ("i-brain", "Fits (seizures)", "Especially for the first time in an adult"),
        ("i-eye", "Vision problems", "Blurred or double vision, or loss of side vision"),
        ("i-activity", "Weakness or numbness", "In an arm, leg or one side of the body"),
        ("i-bone", "Balance problems", "Trouble with walking or coordination"),
        ("i-chat", "Speech problems", "Trouble speaking or understanding words"),
        ("i-users", "Behaviour changes", "Changes in memory, mood or personality"),
        ("i-moon", "Unusual sleepiness", "Or confusion"),
        ("i-cells", "Hearing changes", "Hearing loss or ringing in one ear"),
        ("i-heart", "Hormone problems", "Irregular periods, unusual growth or milk production (pituitary tumors)"),
    ]) + f"""<div class="cols2 mt">
          {_box('i-child', 'Brain tumor symptoms in children', _p('Children may have morning headaches with vomiting, unsteady walking, a squint, a head tilt, delayed or lost milestones, early or delayed puberty, poor growth, or a drop in school performance. In babies, the head may grow too fast or the soft spot on the head may bulge. Dr. Neema Bhat is a US board-certified pediatric hematologist-oncologist, so children with brain tumors get specialised care.'))}
          {_box('i-heart', 'See a doctor urgently', _p('If you or your child has a sudden severe headache, repeated vomiting, a first fit, sudden weakness on one side, sudden loss of vision, or becomes very drowsy or hard to wake.'), 0.08)}
        </div>""", tint=True, label="br-sym")
    causes = _sec(f"""<div class="cols2">
          {_box('i-flask', 'What causes brain tumors and who is at risk?', _p('In most people, the exact cause is not known. It starts with changes (mutations) in the genes of brain cells. Brain tumors are not contagious, and current research has not shown that mobile phones cause them. The risk is higher for:') + _ul(['<b>Age:</b> some types are more common in children, and others in adults over 50', '<b>Radiation exposure:</b> previous radiation to the head, such as for an earlier cancer', '<b>Inherited genetic conditions:</b> neurofibromatosis type 1 and 2, tuberous sclerosis, Li-Fraumeni syndrome, von Hippel-Lindau disease and Gorlin syndrome', 'Family history of brain tumors', '<b>Weak immune system:</b> such as HIV infection or after an organ transplant, which raises the risk of primary CNS lymphoma', '<b>Other cancers:</b> lung, breast, kidney cancer and melanoma can spread to the brain']) + _p('Most people with these risk factors never develop a brain tumor, and most people with a brain tumor have no known risk factor.'), hid='br-cause')}
          {_box('i-shield', 'What happens if a brain tumor is left untreated?', _p('Because the skull cannot expand, even a small growing tumor can cause serious harm:') + _ul(['<b>Raised pressure in the skull:</b> severe headaches, vomiting, vision loss and drowsiness, which can become life-threatening.', '<b>Hydrocephalus:</b> a blocked flow of brain fluid causes fluid build-up, which may need emergency treatment.', '<b>Permanent nerve damage:</b> loss of vision, hearing, speech, movement or memory.', 'Uncontrolled seizures that affect daily life and safety.', '<b>Hormone problems:</b> pituitary and some childhood tumors can affect growth, puberty, thyroid and other hormones.', '<b>Spread within the brain and spine:</b> some malignant tumors, like medulloblastoma, can spread through the brain fluid.', '<b>Fewer treatment choices:</b> larger tumors are harder to remove safely.']) + _p('The good news: many brain tumors can be removed completely or controlled for years when they are treated early by an experienced team.'), 0.08)}
        </div>""", label="br-cause")
    types = _sec(sec_head('Types', 'Types of brain tumors <span class="grad-text">we treat</span>', center=True, hid='br-types') + _table(
        ["Type of brain tumor", "What it means in simple words"], [
            ("Glioma (astrocytoma, oligodendroglioma)", "Tumors from the brain’s support cells (glial cells). They can be slow- or fast-growing."),
            ("Glioblastoma", "The most aggressive type of glioma, mostly in adults. Needs surgery, radiation and chemotherapy."),
            ("Pilocytic astrocytoma and other low-grade gliomas", "Slow-growing tumors, common in children. Often cured with surgery alone."),
            ("Medulloblastoma", "The most common malignant brain tumor in children. Starts at the back of the brain (cerebellum). Many children are cured."),
            ("Ependymoma", "A tumor from the cells lining the fluid spaces of the brain and spinal cord."),
            ("Diffuse midline glioma (including DIPG)", "A fast-growing tumor in the brainstem or midline of the brain, mostly in children."),
            ("Craniopharyngioma", "A benign tumor near the pituitary gland that can affect vision, growth and hormones."),
            ("Germ cell tumors", "Tumors in the middle of the brain, mostly in children and young adults. Many respond very well to treatment."),
            ("Atypical teratoid/rhabdoid tumor (AT/RT)", "A rare, fast-growing tumor in very young children."),
            ("Meningioma", "Usually a benign tumor from the brain’s covering (meninges). The most common primary brain tumor in adults."),
            ("Pituitary tumors", "Mostly benign tumors of the pituitary gland that can affect hormones and vision."),
            ("Vestibular schwannoma (acoustic neuroma)", "A benign tumor on the hearing and balance nerve."),
            ("Primary CNS lymphoma", f'<a href="{LYMPH_PAGE}">Lymphoma</a> that starts in the brain, spinal cord or eyes. Treated mainly with chemotherapy.'),
            ("Brain metastases", "Cancer that has spread to the brain from another organ."),
            ("Spinal cord tumors", "Tumors in or around the spinal cord that can cause back pain, weakness or numbness."),
        ]) + f"""<div class="split split--top mt">
          {_box('i-award', 'Grades of brain tumors', _p('Doctors grade brain tumors from 1 to 4 using the World Health Organization (WHO) classification, based on how the cells look and their genetic changes.') + _p('Today, genetic (molecular) tests on the tumor are as important as the grade, because they help choose the most effective treatment.'))}
          {_table(["Grade", "What it means"], [("Grade 1", "Slow-growing, least aggressive. Often curable with surgery."), ("Grade 2", "Slow-growing but can come back or become higher grade over time."), ("Grade 3", "Malignant, grows faster and spreads into nearby brain tissue."), ("Grade 4", "The most aggressive, fast-growing tumors, such as glioblastoma and medulloblastoma.")])}
        </div>""", tint=True, label="br-types")
    dx = _sec(sec_head('Diagnosis', 'How is a brain tumor <span class="grad-text">diagnosed?</span>', 'Diagnosis needs both imaging and a tissue sample in most cases. Tests may include:', hid='br-dx') + _olist([
        ("Neurological examination", "Checks vision, hearing, balance, strength, reflexes and thinking."),
        ("MRI of the brain with contrast", "The main test to see the size, location and features of the tumor."),
        ("Advanced MRI", "MR spectroscopy, perfusion MRI and functional MRI, to study the tumor and plan safe surgery."),
        ("CT scan", "Useful in emergencies, and to look for bleeding, swelling or calcium in the tumor."),
        ("MRI of the whole spine", "For tumors that can spread through the brain fluid, such as medulloblastoma."),
        ("PET-CT scan", "In selected cases, such as lymphoma or to look for a cancer elsewhere in the body."),
        ("Biopsy or surgery", "A tissue sample is taken to confirm the diagnosis and grade."),
        ("Molecular and genetic tests", "Such as IDH, 1p/19q, MGMT, BRAF and H3 K27M, which classify the tumor and guide treatment."),
        ("Lumbar puncture", "Checks the brain fluid for tumor cells in some tumor types."),
        ("Tumor markers", "AFP and beta-hCG in blood and brain fluid for germ cell tumors."),
        ("Eye and visual field tests", "For tumors near the optic nerves or pituitary gland."),
        ("Hormone tests", "For pituitary tumors and tumors near the hypothalamus."),
        ("Hearing, heart and kidney tests", "Before chemotherapy or radiation, as a baseline."),
    ]), label="br-dx")
    tx = _sec(sec_head('Treatment', 'Brain tumor treatment <span class="grad-text">options</span>', 'Treatment depends on the type, grade, size and location of the tumor, its genetic features, and the patient’s age and overall health. Most patients are treated by a team of neurosurgeons, radiation oncologists and medical or pediatric oncologists.', hid='br-tx') + _cards([
        ("i-clock", "Active monitoring", "Regular MRI scans for small, slow-growing benign tumors that cause no symptoms."),
        ("i-stetho", "Surgery (craniotomy)", "To remove as much of the tumor as is safely possible, using neuronavigation and intraoperative monitoring to protect healthy brain."),
        ("i-brain", "Awake brain surgery", "For tumors near areas that control speech or movement, in selected adults."),
        ("i-stetho", "Endoscopic surgery", "Minimally invasive surgery, including surgery through the nose for pituitary and skull base tumors."),
        ("i-micro", "Stereotactic biopsy", "A precise needle biopsy for deep tumors that cannot be removed safely."),
        ("i-radiation", "Radiation therapy", "Precise techniques such as IMRT and image-guided radiation to target the tumor and spare healthy tissue."),
        ("i-radiation", "Stereotactic radiosurgery", "A single or few high-dose, highly focused radiation treatments for small tumors and brain metastases."),
        ("i-radiation", "Craniospinal radiation", "Radiation to the whole brain and spine for tumors that spread through the brain fluid, such as medulloblastoma."),
        ("i-child", "Proton beam therapy", "For selected children and young adults, to reduce long-term side effects, where suitable and available."),
        ("i-syringe", "Chemotherapy", "Anti-cancer medicines given by mouth, into a vein, or into the brain fluid, often with or after surgery and radiation."),
        ("i-syringe", "High-dose chemotherapy with stem cell rescue", f'For selected high-risk childhood brain tumors, such as some medulloblastomas, AT/RT and germ cell tumors, and to avoid radiation in very young children. <a href="{BMT_PAGE}">Learn more</a>'),
        ("i-pill", "Targeted therapy", "Medicines chosen based on genetic changes in the tumor, such as BRAF, IDH or NTRK changes."),
        ("i-shield", "Immunotherapy &amp; clinical trials", "For selected tumors, where suitable and available."),
        ("i-pill", "Steroids", "To reduce swelling around the tumor and ease symptoms."),
        ("i-brain", "Anti-seizure medicines", "To prevent and control fits."),
        ("i-stetho", "Shunt or endoscopic surgery for hydrocephalus", "To drain or bypass blocked brain fluid."),
        ("i-scale", "Hormone replacement", "For patients with pituitary or hypothalamic hormone problems."),
        ("i-adult", "Rehabilitation", "Physiotherapy, occupational therapy and speech therapy to regain function."),
        ("i-users", "Neuropsychology and school support", "To help with memory, learning and returning to school or work."),
        ("i-chat", "Counselling &amp; palliative care", "Emotional support and symptom control for patients and families, at any stage of treatment."),
        ("i-check", "Long-term follow-up", "Regular MRI scans and checks for late effects on growth, hormones, hearing and learning."),
    ]) + _alert('Brain tumor care works best when planned together from the start.', 'Surgery, radiation and medical treatment should be coordinated by one team.', warn=True), tint=True, label="br-tx")
    life = _sec(_box('i-sun', 'Living well and recovery after brain tumor treatment', _p('Recovery is different for every patient. These steps help:') + _ul(['Take medicines exactly as advised, especially steroids and anti-seizure medicines. Never stop them suddenly.', '<b>Know seizure first aid:</b> turn the person on their side, keep them safe, and seek help if a fit lasts more than 5 minutes.', 'Do not drive until your doctor says it is safe, especially after a seizure or brain surgery.', '<b>Keep up with rehabilitation:</b> physiotherapy, speech therapy and occupational therapy work best when done regularly.', '<b>Prevent infections during chemotherapy:</b> wash hands often, avoid crowds when counts are low, and get urgent help for a fever of 100.4°F (38°C) or more.', '<b>Eat well and stay active:</b> freshly cooked food, enough protein and gentle walking help rebuild strength.', '<b>Support children’s learning:</b> tell the school about the child’s treatment, and ask about extra time or learning support if needed.', '<b>Look after emotional health:</b> mood changes are common. Talk to your care team or a counsellor.', 'Keep every follow-up MRI and visit, even when you feel well. Early detection of any regrowth gives more treatment choices.']) + _p('Brain tumors usually cannot be prevented. But new or worsening headaches with vomiting, a first fit or changes in vision or walking should always be checked early.'), hid='br-life'), label="br-life")
    faqs = [
        ("Which doctor should I see for a brain tumor in Bangalore?", "Brain tumors are treated by a team. A neurosurgeon performs surgery, a radiation oncologist gives radiation, and a medical or pediatric oncologist gives chemotherapy and other medical treatment. For children, a pediatric oncologist like Dr. Neema Bhat coordinates the overall care."),
        ("Are all brain tumors cancer?", "No. Many brain tumors, such as most meningiomas and pituitary tumors, are benign. But even benign tumors can cause serious problems because of where they grow, so they still need expert care."),
        ("Is a brain tumor curable?", "Many are. Benign and low-grade tumors can often be cured with surgery. Some childhood tumors, like medulloblastoma and germ cell tumors, have good cure rates with combined treatment. Aggressive tumors like glioblastoma are harder to cure, but treatment can control them and improve quality of life."),
        ("What are the early signs of a brain tumor?", "Common early signs are new or worsening headaches (often in the morning), vomiting, a first seizure, vision changes, weakness on one side, and changes in behaviour or balance."),
        ("Is every headache a sign of a brain tumor?", "No. Most headaches are caused by tension, migraine, sinus problems or eye strain. See a doctor if a headache is new and keeps getting worse, wakes you from sleep, or comes with vomiting, fits, vision problems or weakness."),
        ("Does every brain tumor need surgery?", "No. Some small benign tumors are only monitored, some are treated with radiosurgery, and some, like germ cell tumors and CNS lymphoma, are treated mainly with chemotherapy and radiation."),
        ("What is the most common brain tumor in children?", "Low-grade gliomas, such as pilocytic astrocytoma, are the most common. Medulloblastoma is the most common malignant brain tumor in children."),
        ("Can a brain tumor come back after treatment?", "Yes, some tumors can come back, especially higher-grade tumors. Regular follow-up MRI scans help find any regrowth early, when more treatment choices are available."),
        ("What are the side effects of brain tumor treatment?", "Side effects depend on the treatment and include tiredness, hair loss, nausea, and a higher infection risk with chemotherapy. In children, treatment can affect growth, hormones, hearing and learning, so long-term follow-up is important."),
        ("Will my child be able to go back to school?", "Most children return to school after or even during treatment. Some may need extra learning support, physiotherapy or speech therapy, which the care team helps arrange."),
    ]
    return cond_page(BRAIN_PAGE, "Brain Tumor Treatment in Bangalore | Dr. Neema Bhat",
                     "Brain tumor treatment in Bangalore with Dr. Neema Bhat, US-trained pediatric hematologist-oncologist: coordinated care with neurosurgeons and radiation oncologists, with special expertise in children.",
                     "Brain tumor", ["Brain tumour", "CNS tumor"], hero, [intro, signs, causes, types, dx, tx, life], faqs,
                     "Quick answers to the questions patients and families ask most about brain tumors.",
                     "For brain tumors, she works with neurosurgeons, radiation oncologists, radiologists and pathologists so that each step is coordinated, with special focus on children.",
                     book_section("Headaches with vomiting, or a first fit?", "Or an MRI report showing a brain tumor? Get an expert opinion early. Book a consultation for brain tumor treatment in Bangalore with Dr. Neema Bhat today.", "brain-tumor"))


# ------------------------------------------------------------------ PRIVACY POLICY
PRIVACY_UPDATED = "30 October 2026"


def privacy():
    def block(hid, title, inner):
        return f'<section class="legal__block" aria-labelledby="{hid}"><h2 id="{hid}">{title}</h2>{inner}</section>'
    P = lambda t: f"<p>{t}</p>"
    UL = lambda items: "<ul>" + "".join(f"<li>{t}</li>" for t in items) + "</ul>"
    body = "".join([
        block("pp-who", "Who we are", P(f"This website is run for Dr. Neema Bhat, Hematologist, Pediatric Oncologist and Bone Marrow Transplant specialist in Bangalore. In this policy, “we”, “us” and “our” mean Dr. Neema Bhat and her clinic team. You can reach us on <a href=\"tel:{PHONE_TEL}\">{PHONE_DISPLAY}</a> (call or WhatsApp).")),
        block("pp-collect", "Information we collect", P("We only collect the information we need to answer your questions and arrange appointments.") + UL([
            "<b>Booking requests.</b> The booking form on the Contact page does not store anything on our website or server. When you press “Send on WhatsApp”, the details you typed (patient’s name, phone number, the reason for the visit and any note) are placed into a WhatsApp message on your own phone or computer. Nothing is sent until you press send inside WhatsApp.",
            "<b>Calls and WhatsApp messages.</b> When you call or message us, we receive your phone number and whatever you choose to tell us, such as the patient’s name, age and health concern.",
            "<b>Technical information.</b> Like all websites, our hosting provider automatically records basic technical details when you visit, such as your IP address, browser type, the pages you open and the time of the visit. These server logs are used only to keep the website working and secure.",
        ])),
        block("pp-use", "How we use your information", UL([
            "To reply to you and arrange, confirm or change appointments.",
            "To prepare for your consultation and provide medical care.",
            "To keep the website secure and working properly.",
        ]) + P("We do not sell, rent or trade your personal information, and we do not use it for advertising.")),
        block("pp-cookies", "Cookies and browser storage", P("This website does not use advertising or tracking cookies, and it does not use analytics tools.") + UL([
            "Your browser may remember small preferences for this website on your own device, such as which layout you chose for the treatments list on a phone. This stays on your device and is not sent to us.",
            "The map on the Contact page is provided by Google Maps. Google may set its own cookies when the map loads. Please see Google’s privacy policy for details.",
        ])),
        block("pp-third", "Third-party services", P("When you use WhatsApp, Google Maps, or open links to hospital or review websites, those services handle your information under their own privacy policies. We are not responsible for how they use it.")),
        block("pp-health", "Health information", P("Please do not share detailed medical reports or sensitive health information through social media or public channels. Bring your reports to your consultation, or share them through the channel the clinic team suggests. Any health information you share with us is kept confidential and used only for your care.")),
        block("pp-keep", "How long we keep information and how we protect it", P("We keep appointment and contact details only as long as needed for your care and for legal and medical record-keeping requirements. We take reasonable steps to protect your information from loss, misuse and unauthorised access.")),
        block("pp-rights", "Your rights", P("Under India’s Digital Personal Data Protection Act, 2023, you can ask us to:") + UL([
            "tell you what personal information we hold about you,",
            "correct or update it,",
            "delete it, where we are not required to keep it by law,",
            "withdraw your consent to us using it.",
        ]) + P(f"To make a request or raise a concern, call or WhatsApp us on <a href=\"tel:{PHONE_TEL}\">{PHONE_DISPLAY}</a>.")),
        block("pp-children", "Children", P("Many of our patients are children. Information about a child should be shared by a parent or guardian.")),
        block("pp-changes", "Changes to this policy", P(f"We may update this policy from time to time. The latest version will always be on this page. Last updated: {PRIVACY_UPDATED}.")),
        block("pp-medical", "Medical disclaimer", P("The information on this website is for general awareness only and is not a substitute for medical advice. Please consult a doctor for diagnosis and treatment.")),
    ])
    return head("Privacy Policy | Dr. Neema Bhat",
                "Privacy policy for the Dr. Neema Bhat website: what information is collected, how it is used and your rights.",
                "privacy-policy.html") + f"""
<body data-page="legal">{ICONS}{header('legal', 'privacy-policy.html')}
  <main id="main">
    <section class="phero" aria-labelledby="pp-title">
      <div class="wrap phero__in">
        <div>
          <ol class="crumbs"><li><a href="index.html">Home</a></li><li>Privacy Policy</li></ol>
          <h1 id="pp-title" data-fx="wipe">Privacy <span class="grad-text">Policy</span></h1>
          <p class="phero__sub" data-fx="fade" style="--d:.15s">How we collect, use and protect your information when you use this website. Last updated: {PRIVACY_UPDATED}.</p>
        </div>
      </div>
    </section>
    <section class="sec">
      <div class="wrap legal">{body}</div>
    </section>
  </main>
""" + footer()


# ------------------------------------------------------------------ 404
def not_found():
    links = "".join(f'<li><a href="{svc_href(s)}">{ic(SVC_ICON_BY_SLUG.get(s, "i-micro"))}{n}</a></li>' for n, s, c, _ in SERVICES)
    return head("Page not found | Dr. Neema Bhat",
                "The page you are looking for could not be found.",
                "404.html", '  <meta name="robots" content="noindex, follow">\n') + f"""
<body data-page="error">{ICONS}{header('error')}
  <main id="main">
    <section class="nf">
      <div class="wrap nf__in">
        <p class="nf__code" aria-hidden="true">404</p>
        <h1>Sorry, this page could not be found</h1>
        <p class="lead">The page may have moved, or the address may have a typing mistake. These links will help you find what you need.</p>
        <div class="hero__acts" style="justify-content:center">
          <a class="btn btn--grad" href="index.html">Go to the home page{ic('i-go', 'ic ic--go')}</a>
          <a class="btn btn--line" href="contact.html">{ic('i-cal')}Book an appointment</a>
        </div>
        <ul class="nf__links">{links}</ul>
      </div>
    </section>
  </main>
""" + footer()


# ------------------------------------------------------------------ COMING SOON (stand-alone, no header/footer)
def coming_soon():
    return f"""<!doctype html>
<html lang="en-IN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Coming Soon | Dr. Neema Bhat</title>
  <meta name="description" content="The new website of Dr. Neema Bhat, Hematologist and Pediatric Oncologist in Bangalore, is coming soon.">
  <meta name="robots" content="noindex, nofollow">
  <link rel="icon" type="image/png" href="assets/images/logo-mark.png">
  <link rel="stylesheet" href="assets/css/styles.css?v={asset_v('assets/css/styles.css')}">
</head>
<body class="soon">{ICONS}
  <main class="soon__in">
    <img class="soon__logo" src="assets/images/logo.png" alt="Dr. Neema Bhat, Hematologist and Pediatric Oncologist" width="928" height="275">
    <p class="tag">{ic('i-clock')}Coming soon</p>
    <h1>Our new website is <span class="grad-text">almost ready</span></h1>
    <p class="lead">Dr. Neema Bhat, Hematologist, Pediatric Oncologist and Bone Marrow Transplant specialist in Bangalore. To book an appointment now, please call or WhatsApp.</p>
    <div class="hero__acts" style="justify-content:center">
      <a class="btn btn--grad" href="tel:{PHONE_TEL}">{ic('i-phone')}{PHONE_DISPLAY}</a>
      <a class="btn btn--line" href="{WA}" target="_blank" rel="noopener">{ic('i-wa')}WhatsApp</a>
    </div>
    <p class="soon__note">OPD at Apollo Hospitals, Bannerghatta Road, Bangalore</p>
  </main>
</body>
</html>
"""


# ================================================================== HOSTINGER (PHP) EXPORT
# `python3 build.py` also writes a ready-to-upload copy of the site to ./hostinger/
# (and hostinger.zip). It uses PHP includes so the header and footer live in one file each:
#   includes/header.php, includes/footer.php, includes/config.php (Coming Soon on/off switch)
import re as _re
import shutil as _shutil
import zipfile as _zipfile
from datetime import date as _date

PHP_MODE = False
HOST_DIR = ROOT / "hostinger"


def _clean_links(text):
    """Rewrite page links to clean addresses (/about) and asset paths to root-relative (/assets/...)."""
    text = _re.sub(r'(?<=["\'])index\.html(?=[#"\'])', "/", text)
    text = _re.sub(r'(?<=["\'])([a-z0-9-]+)\.html(?=[?#"\'])', r"/\1", text)
    text = _re.sub(_re.escape(SITE_URL) + r'/([a-z0-9-]+)\.html', SITE_URL + r'/\1', text)
    text = _re.sub(r'(?<=["\'\s,(])assets/', "/assets/", text)
    text = text.replace('href="manifest.webmanifest"', 'href="/manifest.webmanifest"')
    return text


def _php_header_template():
    """Header include: the menu marks the current page with PHP instead of being copied into every page."""
    html = _header_html("", "", php=True)
    # active top-level item
    html = html.replace('@@CUR:home@@', "<?= $nb_active === 'home' ? ' aria-current=\"page\"' : '' ?>")
    html = html.replace('@@CUR:about@@', "<?= $nb_active === 'about' ? ' aria-current=\"page\"' : '' ?>")
    html = html.replace('@@CUR:contact@@', "<?= $nb_active === 'contact' ? ' aria-current=\"page\"' : '' ?>")
    html = html.replace('@@CUR:service@@', "<?= $nb_active === 'service' ? ' aria-current=\"page\"' : '' ?>")
    # current page inside Services
    for n, s, c, _ in SERVICES:
        h = svc_href(s)
        html = html.replace(f'href="{h}">', f'href="{h}"<?= $nb_current === \'{h}\' ? \' aria-current="page"\' : \'\' ?>>')
    return "<?php /* Shared site header: edit the menu here once and every page updates. */ ?>\n" + ICONS + html


def _php_footer_template():
    html = _footer_html("@@FAB@@")
    html = html.replace('href="@@FAB@@"', "href=\"<?= !isset($nb_fab) || $nb_fab ? 'contact.html' : '#wizard' ?>\"")
    return "<?php /* Shared site footer: edit once and every page updates. */ ?>" + html


CONFIG_PHP = """<?php
/* ------------------------------------------------------------------
   Site settings
   ------------------------------------------------------------------ */

// COMING SOON PAGE ON / OFF
//   true  = visitors see the Coming Soon page (the site is hidden)
//   false = the website is live
define('COMING_SOON', false);

// While Coming Soon is ON, you can still view the real site by opening
//   https://drneemabhat.com/?preview=neema2026
// once in your browser (it remembers you for 7 days). Change this word to keep it private.
define('PREVIEW_KEY', 'neema2026');

define('SITE_URL', '@@SITE@@');

/* ------------------------------------------------------------------ */
if (COMING_SOON && empty($nb_is_coming_soon)) {
    if (isset($_GET['preview']) && hash_equals(PREVIEW_KEY, (string) $_GET['preview'])) {
        setcookie('nb_preview', '1', ['expires' => time() + 7 * 86400, 'path' => '/', 'secure' => true, 'httponly' => true, 'samesite' => 'Lax']);
        $_COOKIE['nb_preview'] = '1';
    }
    if (empty($_COOKIE['nb_preview'])) {
        http_response_code(503);           // tells Google "temporarily unavailable", so nothing is de-indexed
        header('Retry-After: 86400');
        header('X-Robots-Tag: noindex');
        $nb_is_coming_soon = true;
        include __DIR__ . '/../coming-soon.php';
        exit;
    }
}
"""

HTACCESS = """# ==================================================================
#  Dr. Neema Bhat website: server rules for Hostinger (Apache)
# ==================================================================

Options -Indexes -MultiViews
DirectoryIndex index.php
ErrorDocument 404 /404.php
AddDefaultCharset UTF-8

<IfModule mod_rewrite.c>
RewriteEngine On

# 1. Use one address only: https and WITHOUT "www" (www addresses are never indexed)
RewriteCond %{HTTP_HOST} ^www\\.(.+)$ [NC]
RewriteRule ^ https://%1%{REQUEST_URI} [L,R=301]
RewriteCond %{HTTPS} off
RewriteCond %{HTTP:X-Forwarded-Proto} !https
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

# 2. Block private folders and hidden files
RewriteRule ^includes/ - [F,L]
RewriteRule (^|/)\\.(?!well-known/) - [F,L]

# 3. Old or long addresses -> clean addresses (301 = permanent redirect)
#    /index.php, /index.html -> /      /about.php, /about.html -> /about
RewriteCond %{THE_REQUEST} \\s/+index(?:\\.php|\\.html)?[\\s?] [NC]
RewriteRule ^ / [L,R=301]
RewriteCond %{THE_REQUEST} \\s/+([a-z0-9/-]+?)\\.(?:php|html)[\\s?] [NC]
RewriteRule ^ /%1 [L,R=301]
#    remove a trailing slash: /about/ -> /about
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.+)/$ /$1 [L,R=301]

# 4. YOUR OWN REDIRECTS: add one line per old page, for example:
# Redirect 301 /old-page /new-page
# Redirect 301 /services/anemia /anemia-treatment

# 5. Clean address -> PHP file (/about serves about.php)
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteCond %{DOCUMENT_ROOT}/$1.php -f
RewriteRule ^([a-z0-9-]+)$ /$1.php [L]
</IfModule>

# Never serve config, source or backup files
<FilesMatch "\\.(ini|log|sh|sql|bak|py|md|zip|env|lock|json)$">
  Require all denied
</FilesMatch>
<Files "manifest.webmanifest">
  Require all granted
</Files>

<IfModule mod_headers.c>
  Header always set X-Content-Type-Options "nosniff"
  Header always set X-Frame-Options "SAMEORIGIN"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
  Header always set Permissions-Policy "camera=(), microphone=(), geolocation=(), payment=(), usb=()"
  Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
  Header always set Cross-Origin-Opener-Policy "same-origin"
  Header always set Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-src https://www.google.com https://maps.google.com; base-uri 'self'; form-action 'self'; frame-ancestors 'self'; object-src 'none'; upgrade-insecure-requests"
  Header unset X-Powered-By
  # Safety net: never index anything served on a www address
  <If "%{HTTP_HOST} =~ /^www\\./i">
    Header always set X-Robots-Tag "noindex, nofollow"
  </If>
  # Caching: CSS/JS are versioned (?v=), so they can be cached for a year
  <FilesMatch "\\.(css|js|woff2)$">
    Header set Cache-Control "public, max-age=31536000, immutable"
  </FilesMatch>
  <FilesMatch "\\.(webp|png|jpg|jpeg|svg|ico)$">
    Header set Cache-Control "public, max-age=2592000"
  </FilesMatch>
</IfModule>

<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css text/plain text/xml application/javascript application/json application/xml image/svg+xml application/manifest+json
</IfModule>

<IfModule mod_mime.c>
  AddType application/manifest+json .webmanifest
  AddType image/webp .webp
  AddType font/woff2 .woff2
</IfModule>
"""


def _sitemap():
    today = _date.today().isoformat()
    pages = [("", "1.0", "weekly"), ("about", "0.8", "monthly"), ("contact", "0.8", "monthly")]
    pages += [(svc_href(s)[:-5], "0.9", "monthly") for n, s, c, _ in SERVICES]
    pages += [("privacy-policy", "0.3", "yearly")]
    urls = "".join(f"  <url><loc>{SITE_URL}/{p}</loc><lastmod>{today}</lastmod><changefreq>{f}</changefreq><priority>{pr}</priority></url>\n" for p, pr, f in pages)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n'


def _robots():
    return f"""User-agent: *
Allow: /
Disallow: /includes/
Disallow: /coming-soon
Disallow: /404

Sitemap: {SITE_URL}/sitemap.xml
"""


def _llms():
    svc = "\n".join(f"- [{n}]({SITE_URL}/{svc_href(s)[:-5]}): {d}" for n, s, c, d in SERVICES)
    return f"""# Dr. Neema Bhat: Hematologist, Pediatric Oncologist and Bone Marrow Transplant Specialist in Bangalore

> Dr. Neema Bhat is a US-trained Haemato-Oncologist in Bangalore, India, with more than ten years of experience treating blood disorders and blood cancers in children and adults, including bone marrow (stem cell) transplantation. MD (USA) and Fellowship (FAAP) in Pediatric Hematology, Oncology and Bone Marrow Transplantation, Penn State Health, USA.

- OPD: Apollo Hospitals, Bannerghatta Road, Bangalore (Monday to Saturday, 11 AM to 4 PM)
- Evenings: Therapy Clinic (Monday to Saturday, 5 to 7 PM)
- Fridays: Apollo One and Apollo Cradle, Hosa Road, Electronic City (2 to 4 PM)
- Appointments: call or WhatsApp {PHONE_DISPLAY}

## Main pages

- [Home]({SITE_URL}/): Overview of services, first visit, OPD timings and FAQs
- [About Dr. Neema Bhat]({SITE_URL}/about): Training, career and approach to care
- [Contact and booking]({SITE_URL}/contact): Booking request, phone, WhatsApp and directions

## Treatments

{svc}

## Optional

- [Privacy Policy]({SITE_URL}/privacy-policy)

Information on this website is for general awareness and is not a substitute for medical advice.
"""


def export_hostinger(pages):
    """pages: list of (filename.html, function). Writes ./hostinger and ./hostinger.zip."""
    global PHP_MODE
    if HOST_DIR.exists():
        _shutil.rmtree(HOST_DIR)
    (HOST_DIR / "includes").mkdir(parents=True)
    _shutil.copytree(ROOT / "assets", HOST_DIR / "assets")
    PHP_MODE = True
    try:
        for name, fn in pages:
            html = fn()
            stem = name[:-5]
            top = "<?php require_once __DIR__ . '/includes/config.php'; ?>"
            if stem == "404":
                top = "<?php http_response_code(404); require_once __DIR__ . '/includes/config.php'; ?>"
            if stem == "coming-soon":
                top = ("<?php\n$nb_is_coming_soon = true;\nrequire_once __DIR__ . '/includes/config.php';\n"
                       "// Opened directly while the site is live: send visitors to the home page.\n"
                       "if (!COMING_SOON && basename($_SERVER['SCRIPT_FILENAME']) === 'coming-soon.php' && !headers_sent()) { header('Location: /', true, 302); exit; }\n?>")
            if "includes/header.php" in html:
                html = html.replace(ICONS, "", 1)
            (HOST_DIR / f"{stem}.php").write_text(_clean_links(top + html), encoding="utf-8")
        (HOST_DIR / "includes" / "header.php").write_text(_clean_links(_php_header_template()), encoding="utf-8")
        (HOST_DIR / "includes" / "footer.php").write_text(_clean_links(_php_footer_template()), encoding="utf-8")
    finally:
        PHP_MODE = False
    (HOST_DIR / "includes" / "config.php").write_text(CONFIG_PHP.replace("@@SITE@@", SITE_URL), encoding="utf-8")
    (HOST_DIR / "includes" / ".htaccess").write_text("Require all denied\n", encoding="utf-8")
    (HOST_DIR / ".htaccess").write_text(HTACCESS, encoding="utf-8")
    (HOST_DIR / "robots.txt").write_text(_robots(), encoding="utf-8")
    (HOST_DIR / "sitemap.xml").write_text(_sitemap(), encoding="utf-8")
    (HOST_DIR / "llms.txt").write_text(_llms(), encoding="utf-8")
    (HOST_DIR / "manifest.webmanifest").write_text(_clean_links((ROOT / "manifest.webmanifest").read_text()).replace('"index.html"', '"/"'), encoding="utf-8")
    with _zipfile.ZipFile(ROOT / "hostinger.zip", "w", _zipfile.ZIP_DEFLATED) as z:
        for f in sorted(HOST_DIR.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(HOST_DIR))
    print("built hostinger/ and hostinger.zip")


PAGES = [("index.html", home), ("about.html", about), ("contact.html", contact), (BMT_PAGE, bmt), (ANEMIA_PAGE, anemia),
         (HEMA_PAGE, hematology), (THAL_PAGE, thalassemia), (LEUK_PAGE, leukemia), (MYEL_PAGE, myeloma), (LYMPH_PAGE, lymphoma),
         (PEDONC_PAGE, pediatric_oncology), (BRAIN_PAGE, brain_tumor), ("privacy-policy.html", privacy), ("404.html", not_found),
         ("coming-soon.html", coming_soon)]

if __name__ == "__main__":
    for name, fn in PAGES:
        (ROOT / name).write_text(fn(), encoding="utf-8")
        print("built", name)
    export_hostinger(PAGES)
