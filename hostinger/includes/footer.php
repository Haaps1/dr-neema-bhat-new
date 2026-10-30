<?php /* Shared site footer: edit once and every page updates. */ ?>
  <footer class="foot">
    <div class="wrap">
      <div class="foot__grid">
        <div>
          <img class="foot__logo" src="/assets/images/logo.png" alt="Dr. Neema Bhat" width="928" height="275" loading="lazy">
          <p>Hematologist, Pediatric Oncologist and Bone Marrow Transplant specialist in Bangalore.</p>
          <ul style="margin-top:18px">
            <li><a href="tel:+917899756677">+91 78997 56677</a></li>
            <li><a href="https://wa.me/917899756677" target="_blank" rel="noopener">WhatsApp</a></li>
            <li>Apollo Hospitals, Bannerghatta Road, Bengaluru</li>
          </ul>
          <ul class="social" aria-label="Social media"><li><a href="#" target="_blank" rel="noopener" aria-label="Dr. Neema Bhat on Facebook"><svg class="ic"><use href="#i-fb"/></svg></a></li><li><a href="#" target="_blank" rel="noopener" aria-label="Dr. Neema Bhat on Instagram"><svg class="ic"><use href="#i-ig"/></svg></a></li><li><a href="#" target="_blank" rel="noopener" aria-label="Dr. Neema Bhat on LinkedIn"><svg class="ic"><use href="#i-in"/></svg></a></li><li><a href="#" target="_blank" rel="noopener" aria-label="Dr. Neema Bhat on YouTube"><svg class="ic"><use href="#i-yt"/></svg></a></li></ul>
        </div>
        <div><h2>Pages</h2><ul><li><a href="/">Home</a></li><li><a href="/about">About</a></li><li><a href="/contact">Contact</a></li><li><a href="/privacy-policy">Privacy Policy</a></li></ul></div>
        <div class="foot__wide"><h2>Treatments</h2><ul class="foot__cols"><li><a href="/hematology-treatment">Hematology Treatment</a></li><li><a href="/anemia-treatment">Anemia Treatment</a></li><li><a href="/thalassemia-treatment">Thalassemia Treatment</a></li><li><a href="/leukemia-treatment">Leukemia Treatment</a></li><li><a href="/lymphoma-treatment">Lymphoma Treatment</a></li><li><a href="/multiple-myeloma-treatment">Multiple Myeloma Treatment</a></li><li><a href="/pediatric-oncology-treatment">Pediatric Oncology</a></li><li><a href="/brain-tumor-treatment">Brain Tumor Treatment</a></li><li><a href="/bone-marrow-transplant">Bone Marrow Transplant</a></li></ul></div>
      </div>
      <div class="foot__base"><p>© <span data-year>2026</span> Dr. Neema Bhat. All rights reserved.</p><p>Information on this website is for general awareness and is not a substitute for medical advice.</p></div>
    </div>
  </footer>

  <nav class="dock" aria-label="Quick actions">
    <a href="https://wa.me/917899756677" target="_blank" rel="noopener"><svg class="ic"><use href="#i-wa"/></svg><span>WhatsApp</span></a>
    <a href="tel:+917899756677"><svg class="ic"><use href="#i-phone"/></svg><span>Call</span></a>
    <a class="dock__book" href="<?= !isset($nb_fab) || $nb_fab ? '/contact' : '#wizard' ?>"><svg class="ic"><use href="#i-cal"/></svg><span>Book</span></a>
  </nav>
  <dialog class="lb" id="lb" aria-label="Photo viewer"><button class="lb__x" type="button" aria-label="Close">×</button><button class="lb__nav lb__nav--p" type="button" aria-label="Previous">‹</button><figure><img src="" alt=""><figcaption></figcaption></figure><button class="lb__nav lb__nav--n" type="button" aria-label="Next">›</button></dialog>
  <script src="/assets/js/main.js?v=66ea9d72" defer></script>
</body>
</html>
