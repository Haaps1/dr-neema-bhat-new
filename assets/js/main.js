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
    // horizontal rails: reveal items as they're dragged/swiped into view
    document.addEventListener('pointerup', () => setTimeout(check, 400));
    $$('.stack, [data-rail]').forEach((r) => r.addEventListener('scroll', check, { passive: true }));
    check();
  }

  /* ---------- App bar ---------- */
  const bar = $('.appbar');
  const hero = $('.hero, .phero');
  let lastY = scrollY;
  const onScroll = raf(() => {
    const y = scrollY;
    const past = hero ? y > hero.offsetHeight - 80 : y > 10;
    bar.classList.toggle('is-solid', past || y > 30 && !hero);
    bar.classList.toggle('is-hidden', y > 400 && y > lastY + 4 && !sheet?.classList.contains('is-open'));
    if (y < lastY - 4) bar.classList.remove('is-hidden');
    lastY = y;
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

  /* ---------- Buttons: liquid fill from pointer, magnet, tap ripple ---------- */
  $$('.btn').forEach((b) => {
    b.addEventListener('pointerenter', (e) => { const r = b.getBoundingClientRect(); b.style.setProperty('--mx', `${e.clientX - r.left}px`); b.style.setProperty('--my', `${e.clientY - r.top}px`); });
    b.addEventListener('pointerleave', (e) => { const r = b.getBoundingClientRect(); b.style.setProperty('--mx', `${e.clientX - r.left}px`); b.style.setProperty('--my', `${e.clientY - r.top}px`); });
  });
  if (fine && !reduce) {
    $$('.magnet').forEach((m) => {
      m.addEventListener('pointermove', (e) => { const r = m.getBoundingClientRect(); m.style.transform = `translate(${(e.clientX - r.left - r.width / 2) * 0.2}px, ${(e.clientY - r.top - r.height / 2) * 0.3}px)`; });
      m.addEventListener('pointerleave', () => { m.style.transform = ''; });
    });
  }
  if (!fine) {
    document.addEventListener('pointerdown', (e) => {
      const t = e.target.closest('.btn, .scard, .ccard, .choice span, .seg button, .appbar__icon, .fab, .sheet__nav a, .sheet__nav button');
      if (!t || reduce) return;
      const r = t.getBoundingClientRect(); const s = Math.max(r.width, r.height) * 2.2;
      const dot = document.createElement('span'); dot.className = 'ripple';
      Object.assign(dot.style, { width: `${s}px`, height: `${s}px`, left: `${e.clientX - r.left - s / 2}px`, top: `${e.clientY - r.top - s / 2}px` });
      if (getComputedStyle(t).position === 'static') t.style.position = 'relative';
      t.style.overflow = 'hidden'; t.appendChild(dot); setTimeout(() => dot.remove(), 650);
    });
  }

  /* ---------- Custom cursor ---------- */
  if (fine && !reduce) {
    document.documentElement.classList.add('has-cursor');
    const ring = $('.cursor'), dot = $('.cursor-dot');
    let x = innerWidth / 2, y = innerHeight / 2, rx = x, ry = y;
    addEventListener('pointermove', (e) => { x = e.clientX; y = e.clientY; dot.style.transform = `translate(${x}px, ${y}px)`; });
    (function loop() { rx += (x - rx) * 0.18; ry += (y - ry) * 0.18; ring.style.transform = `translate(${rx}px, ${ry}px)`; requestAnimationFrame(loop); })();
    document.addEventListener('pointerover', (e) => {
      ring.classList.toggle('is-view', !!e.target.closest('.shot__img, .mosaic figure'));
      ring.classList.toggle('is-link', !!e.target.closest('a, button, label, summary') && !e.target.closest('.shot__img'));
    });
  }

  /* ---------- Hero: pointer glow + decoding headline ---------- */
  const glowHost = $('[data-glow]');
  if (glowHost && fine && !reduce) {
    glowHost.addEventListener('pointermove', (e) => {
      const r = glowHost.getBoundingClientRect();
      glowHost.style.setProperty('--gx', `${((e.clientX - r.left) / r.width) * 100}%`);
      glowHost.style.setProperty('--gy', `${((e.clientY - r.top) / r.height) * 100}%`);
    });
  }
  const scr = $('[data-scramble]');
  if (scr && !reduce) {
    const words = scr.dataset.scramble.split('|');
    const glyphs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+×#';
    let wi = 0;
    const decode = (to) => new Promise((done) => {
      const from = scr.textContent; const len = Math.max(from.length, to.length); let f = 0;
      const q = [...Array(len)].map((_, i) => ({ from: from[i] || '', to: to[i] || '', start: Math.floor(Math.random() * 14), end: 14 + Math.floor(Math.random() * 18) }));
      (function tick() {
        let out = '', finished = 0;
        q.forEach((c) => {
          if (f >= c.end) { finished++; out += c.to; }
          else if (f >= c.start) out += c.to === ' ' ? ' ' : glyphs[Math.floor(Math.random() * glyphs.length)];
          else out += c.from;
        });
        scr.textContent = out; f++;
        if (finished === q.length) done(); else requestAnimationFrame(tick);
      })();
    });
    setInterval(async () => { if (document.hidden) return; wi = (wi + 1) % words.length; await decode(words[wi]); }, 3200);
  }

  /* ---------- Hero art: 3D tilt with pointer ---------- */
  const scene = $('[data-tilt-scene]');
  if (scene && fine && !reduce) {
    const arch = $('.arch', scene);
    glowHost?.addEventListener('pointermove', (e) => {
      const nx = e.clientX / innerWidth - 0.5, ny = e.clientY / innerHeight - 0.5;
      arch.style.transform = `perspective(1000px) rotateY(${nx * 8}deg) rotateX(${-ny * 6}deg)`;
    });
    glowHost?.addEventListener('pointerleave', () => { arch.style.transform = ''; });
    arch.style.transition = 'transform .8s cubic-bezier(.16,1,.3,1)';
  }

  /* ---------- Scroll-lit statement (words light up as you read) ---------- */
  const lit = $('[data-lit]');
  if (lit) {
    const words = $$('.w', lit);
    const update = raf(() => {
      const r = lit.getBoundingClientRect();
      const p = clamp((innerHeight * 0.82 - r.top) / (r.height + innerHeight * 0.35), 0, 1);
      const n = Math.round(p * words.length);
      words.forEach((w, i) => w.classList.toggle('is-lit', i < n));
    });
    if (reduce) words.forEach((w) => w.classList.add('is-lit'));
    else { addEventListener('scroll', update, { passive: true }); update(); }
  }

  /* ---------- Stacking service cards ---------- */
  const stack = $('[data-stack]');
  if (stack) {
    const cards = $$('.scard', stack);
    const desk = matchMedia('(min-width: 901px)');
    const update = raf(() => {
      if (!desk.matches || reduce) return;
      cards.forEach((c, i) => {
        const next = cards[i + 1]; if (!next) return;
        const a = c.getBoundingClientRect(), b = next.getBoundingClientRect();
        const overlap = clamp((a.bottom - b.top) / a.height, 0, 1);
        c.style.setProperty('--s', (1 - overlap * 0.05).toFixed(4));
      });
    });
    addEventListener('scroll', update, { passive: true }); update();
    // mobile rail dots
    const dots = $('[data-dots-for="stack"]');
    if (dots) {
      dots.innerHTML = cards.map(() => '<i></i>').join('');
      const ds = $$('i', dots);
      const mark = raf(() => {
        const i = Math.round(stack.scrollLeft / (cards[0].offsetWidth + 14));
        ds.forEach((d, k) => d.classList.toggle('is-on', k === i));
      });
      stack.addEventListener('scroll', mark, { passive: true }); mark();
    }
    // flash a card when arriving via #svc-… (from the Services menu)
    const flash = () => {
      const t = location.hash.startsWith('#svc-') && $(location.hash);
      if (!t) return;
      if (!desk.matches) stack.scrollTo({ left: t.offsetLeft - 20, behavior: reduce ? 'auto' : 'smooth' });
      t.classList.remove('is-flash'); void t.offsetWidth; t.classList.add('is-flash');
    };
    addEventListener('hashchange', flash); setTimeout(flash, 700);
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

  /* ---------- Draggable rail with momentum ---------- */
  const rail = $('[data-rail]');
  if (rail) {
    const track = $('.rail__track', rail);
    const bar = $('.rail__bar i');
    let x = 0, v = 0, dragging = false, sx = 0, lx = 0, moved = 0;
    const max = () => Math.min(0, rail.clientWidth - track.scrollWidth - parseFloat(getComputedStyle(rail).paddingLeft));
    const render = () => {
      track.style.transform = `translate3d(${x}px,0,0)`;
      const m = max(); const p = m ? x / m : 0;
      if (bar) bar.style.setProperty('--rp', `${p * 233}%`);
    };
    rail.addEventListener('pointerdown', (e) => { dragging = true; moved = 0; sx = e.clientX - x; lx = e.clientX; v = 0; rail.classList.add('is-drag'); rail.setPointerCapture(e.pointerId); });
    rail.addEventListener('pointermove', (e) => { if (!dragging) return; v = e.clientX - lx; lx = e.clientX; moved += Math.abs(v); x = clamp(e.clientX - sx, max() - 60, 60); render(); });
    const end = () => {
      if (!dragging) return; dragging = false; rail.classList.remove('is-drag');
      (function glide() { if (dragging) return; v *= 0.93; x += v; const m = max(); if (x > 0) x += (0 - x) * 0.2; if (x < m) x += (m - x) * 0.2; render(); if (Math.abs(v) > 0.3 || x > 0.5 || x < m - 0.5) requestAnimationFrame(glide); })();
    };
    rail.addEventListener('pointerup', end); rail.addEventListener('pointercancel', end);
    rail.addEventListener('click', (e) => { if (moved > 6) { e.stopPropagation(); e.preventDefault(); } }, true);
    rail.addEventListener('wheel', (e) => { if (Math.abs(e.deltaX) > Math.abs(e.deltaY)) { e.preventDefault(); x = clamp(x - e.deltaX, max(), 0); render(); } }, { passive: false });
    rail.setAttribute('tabindex', '0'); rail.setAttribute('aria-label', 'Photo gallery — use arrow keys to scroll');
    rail.addEventListener('keydown', (e) => { if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { x = clamp(x + (e.key === 'ArrowRight' ? -300 : 300), max(), 0); track.style.transition = 'transform .6s cubic-bezier(.16,1,.3,1)'; render(); setTimeout(() => { track.style.transition = ''; }, 600); } });
    addEventListener('resize', () => { x = clamp(x, max(), 0); render(); });
    render();
  }

  /* ---------- Lightbox (iris open) ---------- */
  const lb = $('#lb');
  const items = $$('.shot__img, [data-gallery] figure');
  if (lb && items.length && lb.showModal) {
    const img = $('img', lb), cap = $('figcaption', lb); let i = 0, from = null;
    const show = (k) => {
      i = (k + items.length) % items.length; const it = items[i];
      img.classList.remove('is-ready'); img.src = it.dataset.full; img.alt = $('img', it).alt;
      cap.textContent = it.dataset.cap || $('figcaption', it)?.textContent || '';
      img.onload = () => requestAnimationFrame(() => img.classList.add('is-ready'));
    };
    items.forEach((it, k) => {
      it.addEventListener('click', () => { from = it; show(k); lb.showModal(); });
      it.addEventListener('keydown', (e) => { if (e.key === 'Enter' && it.tagName === 'FIGURE') { from = it; show(k); lb.showModal(); } });
    });
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

  /* ---------- About: tilt cards + scroll-drawn path ---------- */
  if (fine && !reduce) $$('[data-tilt]').forEach((c) => {
    c.addEventListener('pointermove', (e) => { const r = c.getBoundingClientRect(); c.style.setProperty('--ry', `${((e.clientX - r.left) / r.width - 0.5) * 10}deg`); c.style.setProperty('--rx', `${(0.5 - (e.clientY - r.top) / r.height) * 10}deg`); });
    c.addEventListener('pointerleave', () => { c.style.setProperty('--rx', '0deg'); c.style.setProperty('--ry', '0deg'); });
  });
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

  /* ---------- Service page: type switch, journey, cell diagram ---------- */
  const sw = $('[data-switch]');
  if (sw) {
    const tabs = $$('[role="tab"]', sw);
    const set = (t, focus) => {
      tabs.forEach((x) => { const on = x === t; x.setAttribute('aria-selected', String(on)); x.tabIndex = on ? 0 : -1; const p = $('#' + x.getAttribute('aria-controls')); p.hidden = !on; if (on) { p.classList.remove('is-new'); void p.offsetWidth; p.classList.add('is-new'); } });
      sw.dataset.v = t.id === 'tab-allo' ? 'allo' : 'auto'; if (focus) t.focus();
    };
    tabs.forEach((t, k) => { t.addEventListener('click', () => set(t)); t.addEventListener('keydown', (e) => { if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { e.preventDefault(); set(tabs[1 - k], true); } }); });
  }
  const jr = $('[data-journey]');
  if (jr) {
    const steps = $$('.jstep', jr), line = $('.journey__line i', jr);
    const upd = raf(() => {
      const r = jr.getBoundingClientRect(); const p = clamp((innerHeight * 0.75 - r.top) / (r.height + innerHeight * 0.2), 0, 1);
      if (line) line.style.setProperty('--p', p.toFixed(4));
      steps.forEach((s, i) => s.classList.toggle('is-on', matchMedia('(max-width: 1100px)').matches ? s.getBoundingClientRect().top < innerHeight * 0.75 : p >= i / (steps.length - 1) - 0.02));
    });
    if (reduce) steps.forEach((s) => s.classList.add('is-on')); else { addEventListener('scroll', upd, { passive: true }); upd(); }
  }
  const cv = $('[data-cellviz]');
  if (cv && 'IntersectionObserver' in window) new IntersectionObserver(([e], o) => { if (e.isIntersecting) { cv.classList.add('is-in'); o.disconnect(); } }, { threshold: 0.3 }).observe(cv);
  else cv?.classList.add('is-in');

  /* ---------- Contact: 3-step request → WhatsApp ---------- */
  const wz = $('#wizard');
  if (wz) {
    const steps = $$('.wz-step', wz), dots = $$('.dots i', wz);
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
