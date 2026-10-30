<?php require_once __DIR__ . '/includes/config.php'; ?><!doctype html>
<html lang="en-IN">
<head>
<?php
$nb_title = 'Contact Dr. Neema Bhat | Book an Appointment in Bangalore';
$nb_desc = 'Book an appointment with Dr. Neema Bhat, Hematologist and Pediatric Oncologist. OPD at Apollo Hospitals, Bannerghatta Road. Call or WhatsApp +91 78997 56677.';
$nb_canonical = '/contact';
include __DIR__ . '/includes/head.php';
?>
</head>
<body data-page="contact"><?php $nb_active = 'contact'; $nb_current = ''; include __DIR__ . '/includes/header.php'; ?>

  <main id="main">
    <section class="phero" aria-labelledby="c-title">
      <div class="wrap phero__in">
        <div>
          <ol class="crumbs"><li><a href="/">Home</a></li><li>Contact</li></ol>
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
              <label class="choice"><input type="radio" name="who" value="Child" checked><span><svg class="ic"><use href="#i-child"/></svg>A child</span></label>
              <label class="choice"><input type="radio" name="who" value="Adult"><span><svg class="ic"><use href="#i-adult"/></svg>An adult</span></label>
            </div>
          </div>
          <div class="wz-step">
            <h3>What is it about?</h3>
            <div class="choices"><label class="choice"><input type="radio" name="topic" value="Hematology Treatment" data-slug="hematology" checked><span><svg class="ic"><use href="#i-micro"/></svg>Hematology Treatment</span></label><label class="choice"><input type="radio" name="topic" value="Anemia Treatment" data-slug="anaemia"><span><svg class="ic"><use href="#i-drop"/></svg>Anemia Treatment</span></label><label class="choice"><input type="radio" name="topic" value="Thalassemia Treatment" data-slug="thalassemia"><span><svg class="ic"><use href="#i-link"/></svg>Thalassemia Treatment</span></label><label class="choice"><input type="radio" name="topic" value="Leukemia Treatment" data-slug="leukaemia"><span><svg class="ic"><use href="#i-cells"/></svg>Leukemia Treatment</span></label><label class="choice"><input type="radio" name="topic" value="Lymphoma Treatment" data-slug="lymphoma"><span><svg class="ic"><use href="#i-ribbon"/></svg>Lymphoma Treatment</span></label><label class="choice"><input type="radio" name="topic" value="Multiple Myeloma Treatment" data-slug="multiple-myeloma"><span><svg class="ic"><use href="#i-bone"/></svg>Multiple Myeloma Treatment</span></label><label class="choice"><input type="radio" name="topic" value="Pediatric Oncology" data-slug="pediatric-oncology"><span><svg class="ic"><use href="#i-child"/></svg>Pediatric Oncology</span></label><label class="choice"><input type="radio" name="topic" value="Brain Tumor Treatment" data-slug="brain-tumor"><span><svg class="ic"><use href="#i-brain"/></svg>Brain Tumor Treatment</span></label><label class="choice"><input type="radio" name="topic" value="Bone Marrow Transplant" data-slug="bone-marrow-transplant"><span><svg class="ic"><use href="#i-marrow"/></svg>Bone Marrow Transplant</span></label><label class="choice"><input type="radio" name="topic" value="Second opinion" data-slug="second-opinion"><span><svg class="ic"><use href="#i-doc"/></svg>Second opinion</span></label></div>
          </div>
          <div class="wz-step">
            <h3>Your details</h3>
            <div class="field"><label for="w-name">Patient’s name</label><input id="w-name" name="name" type="text" autocomplete="name" required><span class="field__err">Please enter the patient’s name</span></div>
            <div class="field"><label for="w-phone">Phone number</label><input id="w-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" required pattern="[0-9+\s\-]{8,}"><span class="field__err">Please enter a valid phone number</span></div>
            <div class="field"><label for="w-msg">Anything else? (optional)</label><textarea id="w-msg" name="message" rows="3"></textarea></div>
          </div>
          <div class="wz-nav">
            <button class="btn btn--line" type="button" data-wz-back hidden>Back</button>
            <button class="btn btn--grad" type="button" data-wz-next style="margin-left:auto">Continue<svg class="ic ic--go"><use href="#i-go"/></svg></button>
            <button class="btn btn--grad" type="submit" data-wz-send hidden style="margin-left:auto">Send on WhatsApp<svg class="ic"><use href="#i-wa"/></svg></button>
          </div>
          <p class="wz-note">For medical emergencies, please visit the nearest emergency department.</p>
        </form>

        <div>
          <div class="ccards">
            <a class="ccard" href="tel:+917899756677"><svg class="ic"><use href="#i-phone"/></svg><span><small>Call</small><b>+91 78997 56677</b></span><svg class="ic ic--go"><use href="#i-go"/></svg></a>
            <a class="ccard" href="https://wa.me/917899756677" target="_blank" rel="noopener"><svg class="ic"><use href="#i-wa"/></svg><span><small>WhatsApp</small><b>+91 78997 56677</b></span><svg class="ic ic--go"><use href="#i-go"/></svg></a>
            <a class="ccard" href="https://www.google.com/maps/search/?api=1&amp;query=Apollo+Hospitals+Bannerghatta+Road+Bengaluru" target="_blank" rel="noopener"><svg class="ic"><use href="#i-pin"/></svg><span><small>OPD · Directions</small><b>Apollo Hospitals, Bannerghatta Road</b></span><svg class="ic ic--go"><use href="#i-go"/></svg></a>
          </div>
          <div class="map"><iframe title="Map showing Apollo Hospitals, Bannerghatta Road, Bengaluru" src="https://maps.google.com/maps?q=Apollo%20Hospitals%2C%20Bannerghatta%20Road%2C%20Bengaluru&amp;z=15&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
        </div>
      </div>
    </section>

    <section class="sec sec--tint" id="timings" aria-labelledby="t-title">
      <div class="wrap where">
        <div>
          <p class="tag" data-fx="wipe-x">OPD timings</p>
          <h2 class="title" id="t-title" data-fx="wipe">Where to find her, <span class="grad-text">day by day</span></h2>
          <p class="lead" data-fx="fade">Please call or WhatsApp +91 78997 56677 to confirm before visiting.</p>
          <ul class="hosp"><li><svg class="ic"><use href="#i-pin"/></svg><div><b>Apollo Hospitals, Bannerghatta Road</b><span>OPD · Mon – Sat, 11 AM – 4 PM</span></div></li><li><svg class="ic"><use href="#i-pin"/></svg><div><b>Therapy Clinic</b><span>Evenings · Mon – Sat, 5 – 7 PM</span></div></li><li><svg class="ic"><use href="#i-pin"/></svg><div><b>Apollo One &amp; Apollo Cradle, Electronic City</b><span>Hosa Road · Fridays, 2 – 4 PM</span></div></li><li><svg class="ic"><use href="#i-pin"/></svg><div><b>Bhagawan Mahaveer Jain Hospital</b><span>Bone Marrow Transplant Unit</span></div></li></ul>
        </div>
        <div>
          <p class="lead" style="margin:0 0 12px;color:var(--navy);font-weight:500">Pick a day to see her schedule</p>
          <div data-days>
          <div class="seg" role="tablist" aria-label="Day of the week"><span class="seg__thumb" aria-hidden="true"></span></div>
          <div class="slots" role="tabpanel" aria-live="polite"></div>
        </div>
          <div class="notes">
            <div class="note"><b>Second Wednesday of every month · 10 AM – 1 PM:</b> Janappana and Ramnagara OPD, then Apollo Bannerghatta Road and the Therapy Clinic as usual.</div>
            <div class="note"><b>SOS availability:</b> Digvish Hospital · AV Hospital (Outer Ring Road) · Promed Hospital (Banashankari 2nd Stage)</div>
          </div>
        </div>
      </div>
    </section>
  </main>
<?php $nb_fab = false; include __DIR__ . '/includes/footer.php'; ?>
