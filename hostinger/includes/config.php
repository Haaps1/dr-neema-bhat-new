<?php
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

define('SITE_URL', 'https://drneemabhat.com');

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
