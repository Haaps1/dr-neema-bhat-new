/* ==========================================================================
   Dr. Neema Bhat — site interactions
   ========================================================================== */

/* Contact details — update here and every phone link / label on the page follows. */
const CONFIG = {
  phoneDisplay: '+91 78997 56677',
  phoneE164: '+917899756677',
  whatsapp: '917899756677', // digits only, with country code
};

(() => {
  'use strict';

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];

  /* ---------- Contact config ---------- */
  $$('[data-phone-link]').forEach((a) => { a.href = `tel:${CONFIG.phoneE164}`; });
  $$('[data-whatsapp-link]').forEach((a) => { a.href = `https://wa.me/${CONFIG.whatsapp}`; });
  $$('[data-phone-text]').forEach((el) => { el.textContent = CONFIG.phoneDisplay; });
  $$('[data-year]').forEach((el) => { el.textContent = new Date().getFullYear(); });

  /* ---------- Reveal on scroll ---------- */
  const reveal = $$('[data-reveal]');
  if (reduceMotion || !('IntersectionObserver' in window)) {
    reveal.forEach((el) => el.classList.add('is-in'));
  } else {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.1 });
    reveal.forEach((el) => io.observe(el));
  }

  /* ---------- Header ---------- */
  const header = $('.header');
  const onScroll = () => header.classList.toggle('is-scrolled', window.scrollY > 8);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  const nav = $('#nav');
  const menuBtn = $('.menu-btn');
  const setMenu = (open) => {
    nav.classList.toggle('is-open', open);
    menuBtn.setAttribute('aria-expanded', String(open));
    menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  };
  menuBtn.addEventListener('click', () => setMenu(!nav.classList.contains('is-open')));
  nav.addEventListener('click', (e) => { if (e.target.closest('a')) setMenu(false); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setMenu(false); });

  // Logo returns to the top of the home page
  $$('[data-home]').forEach((a) => a.addEventListener('click', (e) => {
    e.preventDefault();
    setMenu(false);
    window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
    if (location.hash) history.replaceState(null, '', location.pathname + location.search);
  }));

  // Highlight the current section in the menu
  const links = $$('.nav a[href^="#"]:not(.btn)');
  if ('IntersectionObserver' in window) {
    const spy = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        links.forEach((a) => a.classList.toggle('is-active', a.getAttribute('href') === `#${e.target.id}`));
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    links.forEach((a) => { const s = $(a.getAttribute('href')); if (s) spy.observe(s); });
    new IntersectionObserver(([e]) => { if (e.isIntersecting) links.forEach((a) => a.classList.remove('is-active')); }, { rootMargin: '-45% 0px -50% 0px' }).observe($('.hero'));
  }

  /* ---------- Hero headline: rotating specialty ---------- */
  const rot = $('[data-rotator]');
  if (rot && !reduceMotion) {
    const words = rot.dataset.words.split('|');
    const el = $('.rotator__word', rot);
    let i = 0, paused = false;
    const title = rot.closest('h1');
    title.addEventListener('pointerenter', () => { paused = true; });
    title.addEventListener('pointerleave', () => { paused = false; });
    setInterval(() => {
      if (paused || document.hidden) return;
      el.classList.add('is-out');
      setTimeout(() => {
        i = (i + 1) % words.length;
        el.textContent = words[i];
        el.classList.remove('is-out');
        el.classList.add('is-in');
        requestAnimationFrame(() => requestAnimationFrame(() => el.classList.remove('is-in')));
      }, 350);
    }, 2800);
  }

  /* ---------- Count-up numbers ---------- */
  const counters = $$('[data-count]');
  if (counters.length && !reduceMotion && 'IntersectionObserver' in window) {
    const cio = new IntersectionObserver((entries) => entries.forEach((e) => {
      if (!e.isIntersecting) return;
      const el = e.target, end = +el.dataset.count, t0 = performance.now();
      const step = (t) => { const k = Math.min(1, (t - t0) / 1400); el.textContent = Math.round(end * (1 - Math.pow(1 - k, 3))); if (k < 1) requestAnimationFrame(step); };
      el.textContent = '0'; requestAnimationFrame(step);
      cio.unobserve(el);
    }), { threshold: 0.6 });
    counters.forEach((el) => cio.observe(el));
  }

  /* ---------- OPD timings: highlight today (India time) ---------- */
  const week = $('[data-week]');
  if (week) {
    const istDay = new Date(Date.now() + (330 + new Date().getTimezoneOffset()) * 60000).getDay();
    $$(`tr[data-day="${istDay}"]`, week).forEach((tr) => tr.classList.add('is-today'));
  }

  /* ---------- Gallery lightbox ---------- */
  const lb = $('#lightbox');
  const shots = $$('[data-gallery] button');
  if (lb && shots.length && typeof lb.showModal === 'function') {
    const img = $('img', lb), cap = $('figcaption', lb);
    let idx = 0, opener = null;
    const show = (n) => {
      idx = (n + shots.length) % shots.length;
      const b = shots[idx];
      img.src = b.dataset.full; img.alt = $('img', b).alt;
      cap.textContent = b.parentElement.querySelector('p')?.textContent || '';
    };
    shots.forEach((b, n) => b.addEventListener('click', () => { opener = b; show(n); lb.showModal(); }));
    $('.lightbox__close', lb).addEventListener('click', () => lb.close());
    $('.lightbox__nav--prev', lb).addEventListener('click', () => show(idx - 1));
    $('.lightbox__nav--next', lb).addEventListener('click', () => show(idx + 1));
    lb.addEventListener('keydown', (e) => { if (e.key === 'ArrowLeft') show(idx - 1); if (e.key === 'ArrowRight') show(idx + 1); });
    lb.addEventListener('click', (e) => { if (e.target === lb) lb.close(); });
    lb.addEventListener('close', () => opener?.focus());
  }

  /* ---------- Appointment form → WhatsApp ---------- */
  const form = $('#appt-form');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      let first = null;
      ['#f-name', '#f-phone'].forEach((sel) => {
        const input = $(sel, form);
        const ok = input.checkValidity() && input.value.trim() !== '';
        input.closest('.field').classList.toggle('is-invalid', !ok);
        input.setAttribute('aria-invalid', String(!ok));
        if (!ok && !first) first = input;
      });
      const note = $('.form__note', form);
      if (first) { note.textContent = 'Please add the patient’s name and a valid phone number.'; first.focus(); return; }
      const d = new FormData(form);
      const msg = [
        'Hello, I would like to request an appointment with Dr. Neema Bhat.',
        `Patient: ${d.get('name')} (${d.get('who')})`,
        `Phone: ${d.get('phone')}`,
        `Reason: ${d.get('topic')}`,
        d.get('message') ? `Notes: ${d.get('message')}` : '',
      ].filter(Boolean).join('\n');
      note.textContent = 'Opening WhatsApp with your request…';
      window.open(`https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(msg)}`, '_blank', 'noopener');
    });
    $$('input', form).forEach((i) => i.addEventListener('input', () => i.closest('.field')?.classList.remove('is-invalid')));
  }
})();
