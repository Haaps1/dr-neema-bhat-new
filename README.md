# Dr. Neema Bhat — Website

Static website for Dr. Neema Bhat, Hematologist & Pediatric Oncologist, Bangalore.
No build step: open `index.html`, or publish the folder with GitHub Pages or any static host.

```
index.html              The page (SEO meta + Physician structured data)
assets/css/styles.css   Design (colours and fonts in :root at the top)
assets/js/main.js       Menu, headline rotation, gallery viewer, OPD "today", form → WhatsApp
assets/images/          Logo, three portraits, gallery photos (full size + 760w)
assets/fonts/           Self-hosted Poppins (headings) & Roboto (body)
```

**Design:** clean, clinical layout — navy `#0f265d`, teal `#4fb6bb`, white.

## Updating content
- **Phone / WhatsApp:** `CONFIG` at the top of `assets/js/main.js` (the number also appears in `index.html` as a fallback).
- **OPD timings:** the table in the "OPD timings" section of `index.html`.
- **Testimonials:** currently placeholders marked "Sample" — replace with genuine reviews shared with the patient's consent.
