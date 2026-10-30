<?php http_response_code(404); require_once __DIR__ . '/includes/config.php'; ?><!doctype html>
<html lang="en-IN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>Page not found | Dr. Neema Bhat</title>
  <meta name="description" content="The page you are looking for could not be found.">
  <meta name="theme-color" content="#ffffff">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  <link rel="canonical" href="https://drneemabhat.com/404">
  <link rel="manifest" href="/manifest.webmanifest">
  <meta property="og:type" content="website">
  <meta property="og:title" content="Page not found | Dr. Neema Bhat">
  <meta property="og:description" content="The page you are looking for could not be found.">
  <meta property="og:image" content="https://drneemabhat.com/assets/images/portrait-scrubs-720.webp">
  <script>document.documentElement.classList.add('js');</script>
  <link rel="icon" type="image/png" href="/assets/images/logo-mark.png">
  <link rel="apple-touch-icon" href="/assets/images/logo-mark.png">
  <link rel="preload" href="/assets/fonts/poppins-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/roboto-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/css/styles.css?v=c33e8bef">
  <meta name="robots" content="noindex, follow">
</head>
<body data-page="error"><?php $nb_active = 'error'; $nb_current = ''; include __DIR__ . '/includes/header.php'; ?>

  <main id="main">
    <section class="nf">
      <div class="wrap nf__in">
        <p class="nf__code" aria-hidden="true">404</p>
        <h1>Sorry, this page could not be found</h1>
        <p class="lead">The page may have moved, or the address may have a typing mistake. These links will help you find what you need.</p>
        <div class="hero__acts" style="justify-content:center">
          <a class="btn btn--grad" href="/">Go to the home page<svg class="ic ic--go"><use href="#i-go"/></svg></a>
          <a class="btn btn--line" href="/contact"><svg class="ic"><use href="#i-cal"/></svg>Book an appointment</a>
        </div>
        <ul class="nf__links"><li><a href="/hematology-treatment"><svg class="ic"><use href="#i-micro"/></svg>Hematology Treatment</a></li><li><a href="/anemia-treatment"><svg class="ic"><use href="#i-drop"/></svg>Anemia Treatment</a></li><li><a href="/thalassemia-treatment"><svg class="ic"><use href="#i-link"/></svg>Thalassemia Treatment</a></li><li><a href="/leukemia-treatment"><svg class="ic"><use href="#i-cells"/></svg>Leukemia Treatment</a></li><li><a href="/lymphoma-treatment"><svg class="ic"><use href="#i-ribbon"/></svg>Lymphoma Treatment</a></li><li><a href="/multiple-myeloma-treatment"><svg class="ic"><use href="#i-bone"/></svg>Multiple Myeloma Treatment</a></li><li><a href="/pediatric-oncology-treatment"><svg class="ic"><use href="#i-child"/></svg>Pediatric Oncology</a></li><li><a href="/brain-tumor-treatment"><svg class="ic"><use href="#i-brain"/></svg>Brain Tumor Treatment</a></li><li><a href="/bone-marrow-transplant"><svg class="ic"><use href="#i-marrow"/></svg>Bone Marrow Transplant</a></li></ul>
      </div>
    </section>
  </main>
<?php $nb_fab = true; include __DIR__ . '/includes/footer.php'; ?>
