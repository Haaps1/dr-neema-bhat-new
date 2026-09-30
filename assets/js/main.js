/* ==========================================================================
   Dr. Neema Bhat — interactions
   ========================================================================== */

/* Contact details — update here and on the pages (build.py). */
const CONFIG = { whatsapp: '917899756677' };

/* OPD schedule: day index (0 = Sunday) → slots [time, place, kind] */
const SCHEDULE = (() => {
  const opd = ['11 AM – 4 PM', 'Apollo Bannerghatta Road — OPD', 'o'];
  const eve = ['5 – 7 PM', 'Therapy Clinic', 't'];
  const ecity = ['2 – 4 PM', 'Apollo One & Apollo Cradle, Hosa Road, Electronic City', 'e'];
  return { 0: [], 1: [opd, eve], 2: [opd, eve], 3: [opd, eve], 4: [opd, eve], 5: [opd, ecity, eve], 6: [opd, eve] };
})();
const DAYS = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
const DAYS_LONG = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

(() => {
  'use strict';
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const raf = (fn) => { let t = 0; return (...a) => { if (!t) t = requestAnimationFrame(() => { t = 0; fn(...a); }); }; };

  $$('[data-year]').forEach((el) => { el.textContent = new Date().getFullYear(); });

  /* ---------- Page transition (circle curtain) ---------- */
  const curtain = $('.curtain');
  const fromNav = sessionStorage.getItem('nb-nav') === '1';
  sessionStorage.removeItem('nb-nav');
  if (curtain && fromNav && !reduce) {
    curtain.classList.add('is-enter');
    requestAnimationFrame(() => requestAnimationFrame(() => {
      curtain.classList.remove('is-enter');
      curtain.classList.add('is-leave');
      setTimeout(() => curtain.classList.remove('is-leave'), 900);
    }));
  }
  document.addEventListener('click', (e) => {
    const a = e.target.closest('a[href]');
    if (!a || reduce || e.metaKey || e.ctrlKey || e.shiftKey || a.target === '_blank') return;
    const url = new URL(a.href, location.href);
    if (url.origin !== location.origin || !/\.html$|\/$/.test(url.pathname)) return;
    if (url.pathname === location.pathname) return; // same-page anchors scroll normally
    e.preventDefault();
    curtain.style.setProperty('--cx', `${e.clientX || innerWidth / 2}px`);
    curtain.style.setProperty('--cy', `${e.clientY || innerHeight / 2}px`);
    curtain.classList.add('is-cover');
    sessionStorage.setItem('nb-nav', '1');
    setTimeout(() => { location.href = url.href; }, 650);
  });
  window.addEventListener('pageshow', (e) => { if (e.persisted) curtain?.classList.remove('is-cover'); });

  /* ---------- Reveal effects ---------- */
  // Position-based check: clip-path hidden elements are ignored by IntersectionObserver in Chrome.
  let pending = $$('[data-fx]');
  const reveal = (el) => {
    el.classList.add('is-in');
    const d = parseFloat(getComputedStyle(el).getPropertyValue('--d')) || 0;
    setTimeout(() => el.classList.add('is-done'), 1600 + d * 1000);
  };
  if (reduce) pending.forEach((el) => { el.classList.add('is-in', 'is-done'); });
  else {
    const check = raf(() => {
      const edge = innerHeight * 0.92;
      pending = pending.filter((el) => {
        const r = el.getBoundingClientRect();
        if (r.top < edge && r.bottom > 0 && (r.width || r.height)) { reveal(el); return false; }
        return true;
      });
    });
    addEventListener('scroll', check, { passive: true });
    addEventListener('resize', check);
    // service rail: reveal cards as they're swiped into view
    document.addEventListener('pointerup', () => setTimeout(check, 400));
    $$('[data-svc]').forEach((r) => r.addEventListener('scroll', check, { passive: true }));
    check();
  }

  /* ---------- Header: always visible, shadow + scroll progress ---------- */
  const bar = $('.bar');
  const onScroll = raf(() => {
    const y = scrollY;
    bar.classList.toggle('is-scrolled', y > 8);
    const max = document.documentElement.scrollHeight - innerHeight;
    bar.style.setProperty('--prog', max > 0 ? (y / max).toFixed(4) : 0);
    const wzBox = $('#wizard')?.getBoundingClientRect();
    const formOnScreen = wzBox && wzBox.top < innerHeight && wzBox.bottom > 0;
    $('.fab')?.classList.toggle('is-shown', y > 380 && !formOnScreen);
  });
  addEventListener('scroll', onScroll, { passive: true });

  // Services dropdown (hover on desktop, click/keyboard everywhere)
  const drop = $('.has-drop');
  if (drop) {
    const btn = $('button', drop);
    const set = (o) => { drop.classList.toggle('is-open', o); btn.setAttribute('aria-expanded', String(o)); };
    btn.addEventListener('click', () => set(!drop.classList.contains('is-open')));
    if (fine) { drop.addEventListener('pointerenter', () => set(true)); drop.addEventListener('pointerleave', () => set(false)); }
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') set(false); });
    document.addEventListener('click', (e) => { if (!drop.contains(e.target)) set(false); });
  }

  // Mobile bottom sheet
  const sheet = $('#sheet');
  const opener = $('[data-sheet-open]');
  const setSheet = (o) => {
    sheet.classList.toggle('is-open', o);
    sheet.setAttribute('aria-hidden', String(!o));
    opener?.setAttribute('aria-expanded', String(o));
    document.documentElement.style.overflow = o ? 'hidden' : '';
    if (o) $('a, button', $('.sheet__panel'))?.focus({ preventScroll: true });
  };
  opener?.addEventListener('click', () => setSheet(true));
  $$('[data-sheet-close]').forEach((b) => b.addEventListener('click', () => setSheet(false)));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && sheet?.classList.contains('is-open')) setSheet(false); });
  $$('[data-acc]').forEach((b) => b.addEventListener('click', () => {
    const li = b.closest('li'); const o = !li.classList.contains('is-open');
    li.classList.toggle('is-open', o); b.setAttribute('aria-expanded', String(o));
  }));
  // swipe the sheet down to close
  const panel = $('.sheet__panel');
  if (panel) {
    let y0 = null;
    panel.addEventListener('touchstart', (e) => { if (panel.scrollTop <= 0) y0 = e.touches[0].clientY; }, { passive: true });
    panel.addEventListener('touchmove', (e) => { if (y0 === null) return; const dy = Math.max(0, e.touches[0].clientY - y0); panel.style.transform = `translateY(${dy}px)`; }, { passive: true });
    panel.addEventListener('touchend', (e) => {
      if (y0 === null) return; const dy = e.changedTouches[0].clientY - y0; y0 = null; panel.style.transform = '';
      if (dy > 90) setSheet(false);
    });
  }

  /* ---------- Tap ripple (touch devices) ---------- */
  if (!fine) {
    document.addEventListener('pointerdown', (e) => {
      const t = e.target.closest('.btn, .stp, .svc, .ccard, .choice span, .seg button, .bar__icon, .fab, .sheet__nav a, .sheet__nav button');
      if (!t || reduce) return;
      const r = t.getBoundingClientRect(); const s = Math.max(r.width, r.height) * 2.2;
      const dot = document.createElement('span'); dot.className = 'ripple';
      Object.assign(dot.style, { width: `${s}px`, height: `${s}px`, left: `${e.clientX - r.left - s / 2}px`, top: `${e.clientY - r.top - s / 2}px` });
      if (getComputedStyle(t).position === 'static') t.style.position = 'relative';
      t.style.overflow = 'hidden'; t.appendChild(dot); setTimeout(() => dot.remove(), 650);
    });
  }

  /* ---------- Hero title: smooth crossfade (fixed box, nothing shifts) ---------- */
  const fader = $('[data-fader]');
  if (fader && !reduce) {
    const words = $$('span', fader); let wi = 0;
    // size the box to the widest word so the layout never moves
    const fit = () => { fader.style.minWidth = `${Math.max(...words.map((w) => w.scrollWidth))}px`; };
    fit(); addEventListener('resize', fit);
    setInterval(() => {
      if (document.hidden) return;
      words[wi].classList.remove('is-on'); wi = (wi + 1) % words.length; words[wi].classList.add('is-on');
    }, 2800);
  }

  /* ---------- Services: rail dots on mobile + flash from menu ---------- */
  const grid = $('[data-svc]');
  if (grid) {
    const cards = $$('.svc', grid);
    const dots = $('[data-dots-for="svc"]');
    if (dots) {
      dots.innerHTML = cards.map(() => '<i></i>').join('');
      const ds = $$('i', dots);
      const mark = raf(() => {
        const i = Math.round(grid.scrollLeft / (cards[0].offsetWidth + 12));
        ds.forEach((d, k) => d.classList.toggle('is-on', k === i));
      });
      grid.addEventListener('scroll', mark, { passive: true }); mark();
    }
    const flash = () => {
      const t = location.hash.startsWith('#svc-') && $(location.hash);
      if (!t) return;
      if (grid.scrollWidth > grid.clientWidth) grid.scrollTo({ left: t.offsetLeft - 18, behavior: reduce ? 'auto' : 'smooth' });
      t.classList.remove('is-flash'); void t.offsetWidth; t.classList.add('is-flash');
    };
    addEventListener('hashchange', flash); setTimeout(flash, 700);

    // mobile: the card rail advances on its own; any touch pauses it for a while
    if (!reduce) {
      let idle = 0, visible = false;
      const pause = () => { idle = Date.now() + 6000; };
      ['pointerdown', 'touchstart', 'wheel', 'focusin'].forEach((ev) => grid.addEventListener(ev, pause, { passive: true }));
      if ('IntersectionObserver' in window) new IntersectionObserver(([e]) => { visible = e.isIntersecting; }, { threshold: 0.5 }).observe(grid);
      setInterval(() => {
        if (!visible || document.hidden || Date.now() < idle || grid.scrollWidth <= grid.clientWidth + 4) return;
        const step = cards[0].offsetWidth + 12;
        const atEnd = grid.scrollLeft + grid.clientWidth >= grid.scrollWidth - 8;
        grid.scrollTo({ left: atEnd ? 0 : grid.scrollLeft + step, behavior: 'smooth' });
      }, 3000);
    }
  }

  /* ---------- Count-up numbers ---------- */
  const nums = $$('[data-count]');
  if (nums.length && 'IntersectionObserver' in window && !reduce) {
    const io = new IntersectionObserver((ents) => ents.forEach((en) => {
      if (!en.isIntersecting) return;
      const el = en.target, end = +el.dataset.count, t0 = performance.now();
      el.closest('[data-num]')?.classList.add('is-in');
      (function step(t) { const k = Math.min(1, (t - t0) / 1800); el.textContent = Math.round(end * (1 - Math.pow(1 - k, 4))); if (k < 1) requestAnimationFrame(step); })(t0);
      io.unobserve(el);
    }), { threshold: 0.6 });
    nums.forEach((n) => { n.textContent = '0'; io.observe(n); });
  } else $$('[data-num]').forEach((n) => n.classList.add('is-in'));

  /* ---------- Clickable steps: line fills on scroll; tap a step to open its details ---------- */
  $$('[data-stepper]').forEach((list) => {
    const btns = $$('.stp', list);
    const panel = list.nextElementSibling?.classList.contains('stp-panel') ? list.nextElementSibling : null;
    const n = btns.length; let manual = false; let cur = -1;
    const select = (k, fromUser) => {
      if (fromUser) manual = true;
      if (k === cur && !fromUser) return;
      cur = k;
      list.style.setProperty('--p', n > 1 ? (k / (n - 1)).toFixed(4) : 1);
      btns.forEach((b, i) => {
        b.classList.toggle('is-on', i <= k); b.classList.toggle('is-active', i === k);
        b.setAttribute('aria-pressed', String(i === k));
      });
      if (panel) {
        const b = btns[k];
        $('.stp-panel__n', panel).textContent = String(k + 1).padStart(2, '0');
        $('h3', panel).textContent = $('.stp__t b', b).textContent;
        $('p', panel).textContent = $('.stp__more', b).textContent;
        $('[data-prev]', panel).disabled = k === 0; $('[data-next]', panel).disabled = k === n - 1;
        panel.classList.remove('is-new'); void panel.offsetWidth; panel.classList.add('is-new');
      }
    };
    btns.forEach((b, k) => b.addEventListener('click', () => select(k, true)));
    if (panel) {
      $('[data-prev]', panel).addEventListener('click', () => select(Math.max(0, cur - 1), true));
      $('[data-next]', panel).addEventListener('click', () => select(Math.min(n - 1, cur + 1), true));
    }
    list.addEventListener('keydown', (e) => {
      const d = e.key === 'ArrowRight' || e.key === 'ArrowDown' ? 1 : e.key === 'ArrowLeft' || e.key === 'ArrowUp' ? -1 : 0;
      if (!d || !e.target.closest('.stp')) return;
      e.preventDefault(); const k = clamp(cur + d, 0, n - 1); select(k, true); btns[k].focus();
    });
    select(0);
    // until the visitor taps a step, progress follows the scroll position
    const upd = raf(() => {
      if (manual) return;
      const r = list.getBoundingClientRect();
      const p = clamp((innerHeight * 0.7 - r.top) / Math.max(r.height, 1), 0, 1);
      select(Math.min(n - 1, Math.floor(p * n)));
    });
    if (!reduce) { addEventListener('scroll', upd, { passive: true }); upd(); }
  });

  /* ---------- Lightbox (iris open) ---------- */
  const lb = $('#lb');
  const items = $$('.reel__track > figure button, .collage button');
  if (lb && items.length && lb.showModal) {
    const img = $('img', lb), cap = $('figcaption', lb); let i = 0, from = null;
    const show = (k) => {
      i = (k + items.length) % items.length; const it = items[i];
      img.classList.remove('is-ready'); img.src = it.dataset.full; img.alt = $('img', it).alt;
      cap.textContent = it.dataset.cap || $('figcaption', it)?.textContent || '';
      img.onload = () => requestAnimationFrame(() => img.classList.add('is-ready'));
    };
    items.forEach((it, k) => it.addEventListener('click', () => { from = it; show(k); lb.showModal(); }));
    // duplicated reel copies open the matching original
    $$('.reel__dup button').forEach((it, k) => it.addEventListener('click', () => { from = items[k]; show(k); lb.showModal(); }));
    $('.lb__x', lb).addEventListener('click', () => lb.close());
    $('.lb__nav--p', lb).addEventListener('click', () => show(i - 1));
    $('.lb__nav--n', lb).addEventListener('click', () => show(i + 1));
    lb.addEventListener('keydown', (e) => { if (e.key === 'ArrowLeft') show(i - 1); if (e.key === 'ArrowRight') show(i + 1); });
    lb.addEventListener('click', (e) => { if (e.target === lb) lb.close(); });
    lb.addEventListener('close', () => from?.focus());
  }

  /* ---------- OPD day picker ---------- */
  const istDay = new Date(Date.now() + (330 + new Date().getTimezoneOffset()) * 60000).getDay();
  $$('[data-days]').forEach((box) => {
    const seg = $('.seg', box), slots = $('.slots', box), thumb = $('.seg__thumb', seg);
    const order = [1, 2, 3, 4, 5, 6, 0];
    order.forEach((d) => {
      const b = document.createElement('button');
      b.type = 'button'; b.setAttribute('role', 'tab'); b.dataset.day = d;
      b.setAttribute('aria-label', DAYS_LONG[d] + (d === istDay ? ' (today)' : ''));
      b.innerHTML = `${DAYS[d]}${d === istDay ? '<span class="today" aria-hidden="true"></span>' : ''}`;
      seg.appendChild(b);
    });
    const btns = $$('button', seg);
    const ICON = { o: 'i-hosp', e: 'i-hosp', t: 'i-moon' };
    const pick = (d, focus) => {
      btns.forEach((b, k) => {
        const on = +b.dataset.day === d;
        b.setAttribute('aria-selected', String(on)); b.tabIndex = on ? 0 : -1;
        if (on) { seg.style.setProperty('--t', k); if (focus) b.focus(); }
      });
      const s = SCHEDULE[d];
      slots.innerHTML = s.length
        ? s.map(([t, p, k], n) => `<div class="slot slot--${k} is-new" style="--k:${n}"><span class="slot__ic"><svg class="ic"><use href="#${ICON[k]}"/></svg></span><div><time>${t}</time><span>${p}</span></div></div>`).join('')
        : '<div class="slot slot--off is-new" style="--k:0">No regular OPD on Sunday — call or WhatsApp for urgent needs.</div>';
    };
    btns.forEach((b, k) => {
      b.addEventListener('click', () => pick(+b.dataset.day));
      b.addEventListener('keydown', (e) => {
        const dir = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
        if (dir) { e.preventDefault(); pick(+btns[(k + dir + 7) % 7].dataset.day, true); }
      });
    });
    pick(istDay);
  });

  /* ---------- About: scroll-drawn career path ---------- */
  const path = $('[data-path]');
  if (path) {
    const line = $('.path__line i', path), steps = $$('.step', path);
    const upd = raf(() => {
      const r = path.getBoundingClientRect(); const mark = innerHeight * 0.6;
      line.style.setProperty('--p', clamp((mark - r.top) / r.height, 0, 1).toFixed(4));
      steps.forEach((s) => s.classList.toggle('is-on', s.getBoundingClientRect().top < mark));
    });
    if (reduce) { line.style.setProperty('--p', 1); steps.forEach((s) => s.classList.add('is-on')); }
    else { addEventListener('scroll', upd, { passive: true }); upd(); }
  }

  /* ---------- Service page: type switch, cell diagram ---------- */
  const sw = $('[data-switch]');
  if (sw) {
    const tabs = $$('[role="tab"]', sw);
    const set = (t, focus) => {
      tabs.forEach((x) => { const on = x === t; x.setAttribute('aria-selected', String(on)); x.tabIndex = on ? 0 : -1; const p = $('#' + x.getAttribute('aria-controls')); p.hidden = !on; if (on) { p.classList.remove('is-new'); void p.offsetWidth; p.classList.add('is-new'); } });
      sw.dataset.v = t.id === 'tab-allo' ? 'allo' : 'auto'; if (focus) t.focus();
    };
    tabs.forEach((t, k) => { t.addEventListener('click', () => set(t)); t.addEventListener('keydown', (e) => { if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { e.preventDefault(); set(tabs[1 - k], true); } }); });
  }
  const cv = $('[data-cellviz]');
  if (cv && 'IntersectionObserver' in window) new IntersectionObserver(([e], o) => { if (e.isIntersecting) { cv.classList.add('is-in'); o.disconnect(); } }, { threshold: 0.3 }).observe(cv);
  else cv?.classList.add('is-in');

  /* ---------- Contact: 3-step request → WhatsApp ---------- */
  const wz = $('#wizard');
  if (wz) {
    const steps = $$('.wz-step', wz), dots = $$('.progress i', wz);
    const back = $('[data-wz-back]', wz), next = $('[data-wz-next]', wz), send = $('[data-wz-send]', wz), status = $('[data-wz-status]', wz);
    let s = 0;
    const go = (n) => {
      s = n; steps.forEach((st, i) => st.classList.toggle('is-active', i === s));
      dots.forEach((d, i) => d.classList.toggle('is-on', i <= s));
      back.hidden = s === 0; next.hidden = s === steps.length - 1; send.hidden = s !== steps.length - 1;
      status.textContent = `Step ${s + 1} of ${steps.length}`;
      $('input, textarea', steps[s])?.focus({ preventScroll: true });
    };
    // preselect topic from ?topic=slug (links from service cards)
    const want = new URLSearchParams(location.search).get('topic');
    if (want) { const r = $(`input[data-slug="${CSS.escape(want)}"]`, wz); if (r) r.checked = true; }
    next.addEventListener('click', () => go(Math.min(s + 1, steps.length - 1)));
    back.addEventListener('click', () => go(Math.max(s - 1, 0)));
    wz.addEventListener('submit', (e) => {
      e.preventDefault();
      let bad = null;
      ['#w-name', '#w-phone'].forEach((sel) => { const i = $(sel, wz); const ok = i.checkValidity() && i.value.trim(); i.closest('.field').classList.toggle('is-bad', !ok); i.setAttribute('aria-invalid', String(!ok)); if (!ok && !bad) bad = i; });
      if (bad) { bad.focus(); return; }
      const d = new FormData(wz);
      const msg = ['Hello, I would like to book an appointment with Dr. Neema Bhat.', `Patient: ${d.get('name')} (${d.get('who')})`, `Phone: ${d.get('phone')}`, `Concern: ${d.get('topic')}`, d.get('message') ? `Notes: ${d.get('message')}` : ''].filter(Boolean).join('\n');
      window.open(`https://wa.me/${CONFIG.whatsapp}?text=${encodeURIComponent(msg)}`, '_blank', 'noopener');
    });
    $$('input', wz).forEach((i) => i.addEventListener('input', () => i.closest('.field')?.classList.remove('is-bad')));
  }

  onScroll();
})();
