# Security headers

The [`_headers`](./_headers) file configures response headers for every page Cloudflare Pages serves. If you're landing here because you added a new third-party embed and something broke, jump to [Troubleshooting](#troubleshooting).

## What's in there

```
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Content-Security-Policy-Report-Only: ...
```

The first two prevent the site from being iframed anywhere else and stop browsers from MIME-sniffing files into something unexpected. Nothing interesting to tune there.

The Content-Security-Policy is the big one. It tells the browser which origins are allowed to load scripts, stylesheets, fonts, images, iframes, etc. Right now it's in **Report-Only mode**, which means browsers log violations to the DevTools Console but don't actually block anything. The plan is to flip it to enforcing mode (drop the `-Report-Only` suffix) once we're confident nothing legitimate trips it.

## How the current policy was built

Every external origin the site loads from was found by crawling all 286 pages from the sitemap and inventorying `<script src>`, `<link href>`, `<iframe src>`, `<img src>`, stylesheet URLs inside CSS, and URLs mentioned in inline scripts. That's where the allowlist of `cdn.jsdelivr.net`, `fonts.googleapis.com`, `matomo.almalinux.org`, `youtube.com`, `fosstodon.org`, `sessionize.com`, etc. comes from.

The policy also allows `'unsafe-inline'` for scripts and styles. That's not great — it's the one thing keeping the CSP from fully defending against XSS. It's there because our Hugo templates have inline `<script>` and `<style>` blocks (Matomo bootstrap, the footer toggle handlers, 33 inline style blocks across the site). Pulling those into external files is a worthwhile follow-up that would let us drop `'unsafe-inline'` entirely.

## Troubleshooting

### I added a YouTube/Mastodon/widget embed and the browser console shows "Refused to load" or "violates Content Security Policy"

The embed loads a resource from an origin the policy doesn't allow. The error message tells you exactly which directive rejected it and what URL:

```
Refused to load the script 'https://example.com/thing.js' because it
violates the following Content Security Policy directive: "script-src ..."
```

Add `https://example.com` to the named directive in `_headers`. Common gotchas:

- **A script embed usually needs more than just `script-src`.** Widgets typically also fetch stylesheets (`style-src`), render an iframe back to their domain (`frame-src`), and make XHR calls (`connect-src`). After adding to `script-src`, reload and look for follow-up violations.
- **Third parties sometimes load from a different domain than the embed script.** Sessionize's widget is on `sessionize.com` but its stylesheets come from `sessionize.blob.core.windows.net`. Fonts from Google come from `fonts.gstatic.com` even though the CSS is at `fonts.googleapis.com`.
- **Relative URLs don't need to be allowed.** Only external origins (starting with `https://`) need allowlisting. `/images/foo.png` is covered by `'self'`.

### The console shows CSP violations in Report-Only mode but nothing's broken on the page

That's expected — Report-Only alerts but doesn't block. The point is to catch violations before we flip to enforcing. Fix them so that when we flip the header to `Content-Security-Policy` (no `-Report-Only`), real visitors don't hit broken functionality.

### How do I verify a page that includes embeds is covered before deploying?

Easy! Push to a branch, let the preview site deploy, then open the page, open DevTools → Console and look for violations.

### I see these errors but they're NOT CSP

Pre-existing bugs you'll see in Console when testing CSP changes. None of them are caused by the CSP, and fixing them is out of scope when you're just adding an origin:

- `TypeError: Cannot read properties of null (reading 'addEventListener')` — the footer inline script tries to wire up click handlers to `#contributor`, `#mirror`, `#sponsor` elements that only exist on the `/contribute/` page. Needs a null check.
- `Failed to load resource ... bootstrap-icons.woff / .woff2 (404)` — our compiled SCSS references `./fonts/bootstrap-icons.woff2` but we don't ship those font files. Icons still render because we also load bootstrap-icons from jsDelivr, which works.
- `The Content Security Policy directive 'upgrade-insecure-requests' is ignored when delivered in a report-only policy` — this directive doesn't function in Report-Only mode (per spec). It was removed from the policy to reduce noise, and should be added back when we flip to enforcing.
- Anything from `Grammarly.js`, `web-client-content-script.js`, `base.js`, `paletteBuilder.js`, `content-main.js`, `abFiltersChannel` — browser extensions, not our code.
- `[Violation] Permissions policy violation: compute-pressure / unload is not allowed` — YouTube's player and Grammarly hitting permission policies set by the embed context. Not our CSP.

## When we flip to enforcing

Rename the header from `Content-Security-Policy-Report-Only` to `Content-Security-Policy` and re-add `upgrade-insecure-requests` to the end of the directive list. That's the whole change — but don't do it without at least a week of Report-Only deploy to catch anything the initial audit missed.
