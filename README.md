# Dr. Neema Bhat — Website

Static multi-page website for Dr. Neema Bhat, Hematologist & Pediatric Oncologist, Bangalore.
No server needed: publish the folder with GitHub Pages or any static host.

## Pages
| Page | File |
|---|---|
| Home | `index.html` |
| About | `about.html` |
| Contact (3-step booking → WhatsApp) | `contact.html` |
| Service: Bone Marrow Transplant | `bone-marrow-transplant.html` |

The **Services** menu lists all nine services; Bone Marrow Transplant opens its own page,
the others jump to their card on the home page (and "Book" links preselect them on the contact form).

## Editing
The pages are generated from shared parts in **`build.py`** (header, menu, footer, services list, page content).
Edit `build.py`, then run:

```
python3 build.py
```

- **Colours & fonts:** `:root` at the top of `assets/css/styles.css` (navy `#0f265d`, teal `#4fb6bb`, Poppins + Roboto).
- **OPD timings:** `SCHEDULE` at the top of `assets/js/main.js` (day picker) and the notes in `build.py`.
- **Phone / WhatsApp:** `PHONE_*` / `WA` in `build.py` and `CONFIG` in `assets/js/main.js`.

## Motion & mobile
- Reveals use mask wipes, iris (circle) openings and diagonal reveals — no slide or blur effects.
- Decoding headline, scroll-lit statement, stacking service cards, draggable photo rail,
  scroll-drawn timelines, count-up rings, magnetic buttons, custom cursor and a circular page transition.
- On phones: app bar, bottom-sheet menu (swipe down to close), swipeable service cards with dots,
  day-picker tabs, floating Book button, tap ripples; installable via `manifest.webmanifest`.
- All motion is disabled for visitors who prefer reduced motion.
