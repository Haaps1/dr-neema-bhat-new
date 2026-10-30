<?php
/* ==================================================================
   SHARED <head> FOR EVERY PAGE
   Each page sets $nb_title, $nb_desc and $nb_canonical, then includes this file.
   Add tags for ALL pages in the GLOBAL TAGS box below.
   ================================================================== */
$nb_url = SITE_URL . ($nb_canonical === '' ? '/' : $nb_canonical);
?>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title><?= $nb_title ?></title>
  <meta name="description" content="<?= $nb_desc ?>">
  <meta name="theme-color" content="#ffffff">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  <link rel="canonical" href="<?= $nb_url ?>">
  <link rel="manifest" href="/manifest.webmanifest">
  <meta property="og:type" content="website">
  <meta property="og:url" content="<?= $nb_url ?>">
  <meta property="og:title" content="<?= $nb_title ?>">
  <meta property="og:description" content="<?= $nb_desc ?>">
  <meta property="og:image" content="<?= SITE_URL ?>/assets/images/portrait-scrubs-720.webp">
  <meta name="twitter:card" content="summary_large_image">
  <script>document.documentElement.classList.add('js');</script>
  <link rel="icon" type="image/png" href="/assets/images/logo-mark.png">
  <link rel="apple-touch-icon" href="/assets/images/logo-mark.png">
  <link rel="preload" href="/assets/fonts/poppins-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/roboto-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/css/styles.css?v=c33e8bef">

<?php /* ======================= GLOBAL TAGS =======================
   Paste here anything that must be on EVERY page, for example:
     - Google Tag Manager (head part) or Google Analytics (gtag.js)
     - Google Search Console / Bing verification <meta> tag
     - Meta (Facebook) Pixel
   For Google Tag Manager's <noscript> (body) part, use the BODY TAGS box
   at the top of includes/header.php.
   ============================================================ */ ?>


<?php /* ===================== END GLOBAL TAGS ===================== */ ?>

<?php /* ================= GLOBAL SCHEMA (JSON-LD) =================
   Structured data added to EVERY page. Edit the details below or paste
   more <script type="application/ld+json"> blocks.
   Page-only schema (FAQs, medical condition) is inside each page file.
   ============================================================ */ ?>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"Physician","name":"Dr. Neema Bhat","description":"Hematologist, Pediatric Oncologist and Bone Marrow Transplant specialist in Bangalore.","url":"https://drneemabhat.com/","image":"https://drneemabhat.com/assets/images/portrait-scrubs.webp","telephone":"+91-78997-56677","medicalSpecialty":["Hematologic","Oncologic","Pediatric"],"alumniOf":{"@type":"Hospital","name":"Penn State Health"},
   "hospitalAffiliation":[{"@type":"Hospital","name":"Apollo Hospitals, Bannerghatta Road"},{"@type":"Hospital","name":"Apollo One & Apollo Cradle, Electronic City"},{"@type":"Hospital","name":"Bhagawan Mahaveer Jain Hospital"}],
   "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"11:00","closes":"16:00","description":"OPD, Apollo Hospitals, Bannerghatta Road"},{"@type":"OpeningHoursSpecification","dayOfWeek":"Friday","opens":"14:00","closes":"16:00","description":"Apollo One & Apollo Cradle, Hosa Road, Electronic City"},{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],"opens":"17:00","closes":"19:00","description":"Therapy Clinic"}],
   "address":{"@type":"PostalAddress","addressLocality":"Bengaluru","addressRegion":"Karnataka","addressCountry":"IN"},"areaServed":"Bangalore"}
  </script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"WebSite","name":"Dr. Neema Bhat","url":"https://drneemabhat.com/","inLanguage":"en-IN"}
  </script>
<?php /* =============== END GLOBAL SCHEMA =============== */ ?>
