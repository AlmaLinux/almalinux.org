# AlmaLinux.org Design System

Version 1.0 · Last updated 2026-07-09

Adopted by: _pending Marketing SIG approval (date recorded on adoption)_

A reference for contributors working on the almalinux.org website: brand colors, components, and the conventions that keep the site consistent.

## Table of contents

1. [Principles](#1-principles)
2. [Brand colors](#2-brand-colors)
3. [Logo and brand assets](#3-logo-and-brand-assets)
4. [Tier accent colors](#4-tier-accent-colors)
5. [Button taxonomy](#5-button-taxonomy)
6. [Typography](#6-typography)
7. [Voice and tone](#7-voice-and-tone)
8. [Iconography](#8-iconography)
9. [SCSS organization](#9-scss-organization)
10. [i18n conventions](#10-i18n-conventions)
11. [Component patterns](#11-component-patterns)
12. [Layout & spacing utilities](#12-layout--spacing-utilities)
13. [Image guidelines](#13-image-guidelines)
14. [Accessibility](#14-accessibility)
15. [Forbidden patterns](#15-forbidden-patterns)
16. [Presentations](#16-presentations)
17. [How to add a new design element](#17-how-to-add-a-new-design-element)
18. [Changelog](#18-changelog)

## 1. Principles

User experience is the success metric for everything built for almalinux.org. If visitors hit a moment of uncomfortable or confusing user experience, the work has failed regardless of how clean the underlying code is. Whenever possible, visitors should never be the ones to discover a problem. The deployment safeguards are not bureaucracy or box-ticking, they are how we keep mistakes away from the people who visit the site.

When you weigh a tradeoff (thorough versus fast, refactor versus ship, add a test versus skip it), lean toward whatever protects the visitor's experience. A slower path that ships a clear, accessible page is better than a quick one that leaves visitors to deal with the rough edges.

## 2. Brand colors

The palette below is generated from `assets/scss/variables.scss`, the single source of truth. Edit colors there (including the `// @usage` comments), then run `npm run generate:design-colors` to refresh this table.

<!-- BEGIN GENERATED: brand-colors -->

### Base colors

| Variable              | Hex       | Usage                                 |
| --------------------- | --------- | ------------------------------------- |
| `$al-body-background` | `#0f4266` | Default page background               |
| `$al-link-color`      | `#c4e1ff` | Inline text links on dark backgrounds |

### Brand colors

| Variable                | Hex       | Usage                                    |
| ----------------------- | --------- | ---------------------------------------- |
| `$al-c-brand-primary`   | `#0069da` | Primary buttons, active links, key CTAs  |
| `$al-c-brand-secondary` | `#86da2f` | Secondary accents and highlights         |
| `$al-c-brand-tertiary`  | `#ffcb12` | Warning buttons and attention highlights |

### Brand palette

| Variable                         | Hex       | Usage                                         |
| -------------------------------- | --------- | --------------------------------------------- |
| `$al-c-science-blue`             | `#0069da` | Brand blue, same value as brand-primary       |
| `$al-c-science-blue-dark`        | `#004bbc` | Darker blue, hover/pressed states             |
| `$al-c-science-blue-lighter`     | `#1e87f8` | Lighter blue, subtle accents                  |
| `$al-c-science-blue-light`       | `#2891ff` | Lightest blue, backgrounds and tints          |
| `$al-c-atlantis`                 | `#86da2f` | Brand green, same value as brand-secondary    |
| `$al-c-atlantis-dark`            | `#68bc11` | Darker green, hover/pressed states            |
| `$al-c-atlantis-lighter`         | `#a4f84d` | Lighter green, subtle accents                 |
| `$al-c-atlantis-light`           | `#aeff57` | Lightest green, backgrounds and tints         |
| `$al-c-candlelight`              | `#ffcb12` | Brand yellow, same value as brand-tertiary    |
| `$al-c-candlelight-dark`         | `#e1ad00` | Darker yellow, hover/pressed states           |
| `$al-c-candlelight-lighter`      | `#ffe930` | Lighter yellow, subtle accents                |
| `$al-c-candlelight-light`        | `#fff33a` | Lightest yellow, backgrounds and tints        |
| `$al-c-black-pearl`              | `#082336` | Dark surface, deep-band section backgrounds   |
| `$al-c-black-pearl-dark`         | `#000518` | Darkest surface, near-black fills and text    |
| `$al-c-black-pearl-lighter`      | `#264154` | Lighter dark surface, raised cards            |
| `$al-c-black-pearl-light`        | `#304b5e` | Lightest dark surface, borders on dark        |
| `$al-c-soft-peach`               | `#faf5f5` | Light surface, light-band section backgrounds |
| `$al-c-soft-peach-dark`          | `#dcd7d7` | Muted light surface, borders on light         |
| `$al-c-soft-peach-lighter`       | `#ffffff` | White, light cards and fills                  |
| `$al-c-soft-peach-light`         | `#ffffff` | White, light surfaces                         |
| `$al-c-sunburnt-cyclops`         | `#ff4649` | Error and danger states                       |
| `$al-c-sunburnt-cyclops-dark`    | `#e1282b` | Darker red, error hover/pressed               |
| `$al-c-sunburnt-cyclops-lighter` | `#ff6467` | Lighter red, error accents                    |
| `$al-c-sunburnt-cyclops-light`   | `#ff6e71` | Lightest red, error backgrounds               |

<!-- END GENERATED: brand-colors -->

### Pantone reference

Print (spot color) equivalents from the AlmaLinux Brand Book. Hex is the source of truth for screen; use these Pantone values for print and merchandise. This table is maintained by hand (the generated table above does not include it). Colors not listed have no Pantone equivalent in the Brand Book.

**Logo colors** (the five core brand colors used in the mark):

| Color                 | Hex       | Pantone    |
| --------------------- | --------- | ---------- |
| Logo blue             | `#0069da` | 2172 C     |
| Logo light blue (CTA) | `#24c2ff` | 298 C      |
| Logo green            | `#86da2f` | 2285 C     |
| Logo yellow           | `#ffcb12` | 116 C      |
| Logo red              | `#ff4649` | Warm Red C |

**Full ramps:**

| Variable                         | Hex       | Pantone    |
| -------------------------------- | --------- | ---------- |
| `$al-c-science-blue-dark`        | `#004bbc` | 2132 C     |
| `$al-c-science-blue`             | `#0069da` | 2172 C     |
| `$al-c-science-blue-lighter`     | `#1e87f8` | 2727 C     |
| `$al-c-science-blue-light`       | `#2891ff` | 2727 C     |
| `$al-c-atlantis-dark`            | `#68bc11` | 369 C      |
| `$al-c-atlantis`                 | `#86da2f` | 2285 C     |
| `$al-c-atlantis-lighter`         | `#a4f84d` | 2283 C     |
| `$al-c-atlantis-light`           | `#aeff57` | 2283 C     |
| `$al-c-candlelight-dark`         | `#e1ad00` | 110 C      |
| `$al-c-candlelight`              | `#ffcb12` | 116 C      |
| `$al-c-candlelight-lighter`      | `#ffe930` | 107 C      |
| `$al-c-candlelight-light`        | `#fff33a` | 101 C      |
| `$al-c-sunburnt-cyclops-dark`    | `#e1282b` | 1795 C     |
| `$al-c-sunburnt-cyclops`         | `#ff4649` | Warm Red C |
| `$al-c-sunburnt-cyclops-lighter` | `#ff6467` | 2345 C     |
| `$al-c-sunburnt-cyclops-light`   | `#ff6e71` | 2345 C     |
| `$al-c-black-pearl-dark`         | `#000518` | Black 6 C  |
| `$al-c-black-pearl`              | `#082336` | 539 C      |
| `$al-c-black-pearl-lighter`      | `#264154` | 7477 C     |
| `$al-c-black-pearl-light`        | `#304b5e` | 4161 C     |

The CTA / light blue `#24c2ff` (Pantone 298 C) is a Brand Book logo color; it is not a `variables.scss` token today (it is defined in `_bundle-extras.scss` as `al-cta-blue`).

## 3. Logo and brand assets

The AlmaLinux brand assets live in `static/branding/`. The **AlmaLinux Brand Book** (`static/branding/brand-book.html`, published at [/branding/brand-book.html](https://almalinux.org/branding/brand-book.html)) is the authority for anything this section does not cover; when the two disagree, the Brand Book wins. These assets are also surfaced publicly on the [/branding](https://almalinux.org/branding/) page for contributors and the community to download.

**Primary logo (wordmark).** The site navbar uses `/images/logo.svg`, the horizontal AlmaLinux logo. The full color logo is `static/branding/Almalinux-logo-color.png`, with a white version for dark backgrounds at `static/branding/Almalinux-logo-white.svg`.

**Icon (the "A" mark).** The standalone mark is `static/branding/AlmaLinux Icon.svg` (and `.png`), with a circular variant `AlmaLinux Icon Circle.svg` and monochrome `icon-bw.svg` / `icon-gray.svg`. The footer uses the small mark at `/images/icon.svg`.

**"Powered by AlmaLinux" badges.** For showing that a project or product runs on AlmaLinux, use the ready-made badges: `Powered-by-AL-White` and `Powered-by-Dark-AL` (each in SVG, PNG, and PDF). Do not recreate these by hand.

**Favicons and app icons.** The full favicon set lives in `static/fav/` (`favicon.ico`, 16/32 PNGs, `apple-touch-icon.png`, the `android-chrome` sizes, `safari-pinned-tab.svg`, and `site.webmanifest`). If the icon ever changes, regenerate the whole set together so every platform stays consistent.

**Usage rules:**

- Prefer the SVG source. Fall back to PNG only where SVG is not supported.
- Use the white logo on dark backgrounds (the default site background) and the color logo on light surfaces. Keep strong contrast (see [§14](#14-accessibility)).
- Keep clear space around the logo of at least the height of the "A" mark. Do not crowd it with text or other graphics.
- Do not recolor, stretch, squash, rotate, add shadows or effects, or place the logo on a busy or low-contrast background.
- Do not typeset the word "AlmaLinux" as a stand-in for the logo, and do not rebuild the logo from the font.

## 4. Tier accent colors

The Foundation has six membership tiers. Each tier has an accent color used for dots, name text, and card borders on the `/foundation` and `/members` pages.

The four paid tiers use one accent across both pages:

| Tier     | Accent    | Reads as      | Set in                                      |
| -------- | --------- | ------------- | ------------------------------------------- |
| Silver   | `#14b8a6` | Teal          | `members.scss` `[data-tier="silver"]` + dot |
| Ruby     | `#ff6e71` | Light red     | `members.scss` `[data-tier="ruby"]` + dot   |
| Gold     | `#e9b94a` | Muted gold    | `members.scss` `[data-tier="gold"]` + dot   |
| Platinum | `#e8eef5` | Silvery white | `members.scss` `.is-platinum` + dot         |

The two free tiers (Individual and Mirror) are shown differently on each page and do not share a single accent:

- On `/members` they are spotlight cards: Individual uses `--accent: #86da2f` (atlantis green), Mirror uses `--accent: #ffcb12` (candlelight yellow).
- On `/foundation` they are list rows with a colored dot: Individual `#c4e1ff`, Mirror `#86da2f`.

Implementation: the paid-tier accents are set through `[data-tier="..."]` attribute selectors (and `.is-platinum`) in `assets/scss/members.scss`; the foundation tier list sets its dot colors inline in `layouts/foundation/single.html`. There is no shared `--tier-accent` custom property today. When you add a tier or show tiers on a new page, reuse the paid-tier hexes above so a tier stays recognizable across the site.

Accessibility: the Ruby accent started as a darker red that failed contrast against the dark card background and was corrected to `#ff6e71`. That is why every tier accent needs a contrast check against the surface it sits on (see [§14](#14-accessibility)).

## 5. Button taxonomy

A call-to-action button combines Bootstrap's base `btn` class with a custom `al-cta-*` color class defined in `assets/scss/_bundle-extras.scss`, for example `class="btn btn-lg al-cta-blue"`. The `al-cta-*` classes set color only; spacing is the template's job via Bootstrap utilities (`gap`, `me-*`, `px-*`).

**CTA color classes** (`_bundle-extras.scss`):

- `al-cta-blue` is the default primary CTA: bright blue `#24c2ff` (hover `#0bbbff`) with dark text. It covers most CTAs on the site.
- `al-cta-blue-deep` is a deeper blue (`$al-c-science-blue-light`) for the rare case where `al-cta-blue` lacks contrast on a lighter background.
- `al-cta-green` is the one approved green CTA (`$al-c-atlantis`), reserved for event registration and certification sign-up actions ("Register", "Get Certified"). It is not a general-purpose CTA; use `al-cta-blue` everywhere else.
- `al-cta-yellow` is a yellow CTA (`$al-c-candlelight`) for attention and highlight cases; it supports an inline icon image.

**Sizing and layout modifiers:**

- `btn-sm` / `btn-lg` are Bootstrap's standard size modifiers.
- `al-btn-min` (`_bundle-extras.scss`) sets `min-width: 136px` so adjacent buttons line up to a common width.
- `btn-row` / `btn-box` are not part of this system: they are page-local layout helpers defined inside the `<style>` blocks of the certification list templates, not global button classes.

**Bootstrap buttons:** `btn-primary` (and occasionally `btn-warning`) also appear, mostly on application and membership-apply actions. For brand consistency on marketing CTAs, prefer `al-cta-blue` over `btn-primary`.

**Rule:** never use Bootstrap's `btn-success`. For a green button, use `al-cta-green` within its approved purpose. Green is not a brand action color outside that context.

Real CTA from `layouts/index.html` (the homepage hero, live at <https://almalinux.org/>):

```html
<a href="..." class="btn btn-lg px-4 me-md-2 text-nowrap al-cta-blue">...</a>
```

## 6. Typography

Font stacks are defined in `assets/scss/variables.scss`:

- `$al-font-family` is a system-UI stack used for body text.
- `$al-font-family-accent` is a Montserrat-led stack used for headings and display type. `main.scss` applies it to every heading level, `h1` to `h6`.
- `$al-font-family-mono` is the monospace stack for code.

Base size: `$al-font-base-size` is `16px`. Text colors: `$al-font-color` (`#fefefe`) for text on the dark site background, and `$al-font-color-light` (`#000518`) for text on light surfaces.

**Naming rules:**

- "AlmaLinux" keeps its capital A and capital L in prose. Never write "Almalinux" or "almalinux"; lowercase is correct only in URLs, file paths, and package names.

**Casing convention:** headings use Title Case; bullet and list items use sentence case.

## 7. Voice and tone

The website speaks for a community project run by volunteers, not a corporation. The copy should sound like a helpful person who is glad you are here.

- **Warm and human.** Welcome newcomers without talking down to them. Write the way you would explain something to a colleague you like.
- **Plain over polished.** Say the thing directly. Prefer short, clear sentences and everyday words over jargon or buzzwords. If a term needs explaining, explain it briefly.
- **Confident, not hype.** State what is true and useful. Skip breathless superlatives ("revolutionary", "world-class") and fear-based messaging. The work speaks for itself.
- **Inclusive and neutral.** Address the reader as "you". When a person's pronouns are not known, use they/them; do not guess from a name.
- **Consistent and specific.** Name things the same way every time and prefer concrete detail over vague claims.

Mechanics that carry the voice (see also [§6](#6-typography)):

- "AlmaLinux" is one word, capital A and L, in all visible copy.
- No long dashes (em-dashes or en-dashes). Use a colon, a period, or parentheses instead.
- "AlmaLinux Day" always takes a colon: "AlmaLinux Day: Tokyo", "AlmaLinux Day: LA".
- Headings use Title Case; body lists use sentence case.

## 8. Iconography

The site uses [Bootstrap Icons](https://icons.getbootstrap.com/), applied as `<i class="bi bi-name"></i>` (for example `bi-github`, `bi-calendar`, `bi-download`). The icon font is defined in `assets/scss/bootstrap-icons.scss`.

Icons add interest and scannability, but a page crowded with them reads as noise. Use them with restraint:

- **Support meaning, do not decorate.** An icon works best as a small label beside text (a calendar beside a date, a download arrow beside a download link) or in compact UI like nav items and cards. If a word is clearer on its own, use the word.
- **Reuse before adding.** Before introducing a new icon, check what the site already uses (`grep -rho 'bi-[a-z-]*' layouts/`) and reuse the established one so the same idea reads the same way everywhere. Icons already in common use include `bi-github`, `bi-calendar` / `bi-calendar-event`, `bi-download`, `bi-check-circle-fill`, `bi-people-fill`, and `bi-code-square`.
- **Inherit color.** Let an icon take the color of the surrounding text. Do not introduce a new accent color just for an icon.
- **Keep it accessible** (see [§14](#14-accessibility)). An icon that carries meaning on its own needs an accessible label (adjacent visible text or an `aria-label`). A purely decorative icon should be hidden from assistive technology with `aria-hidden="true"`.

## 9. SCSS organization

`assets/scss/main.scss` is the bundle entry point. It imports, in order: `variables`, `functions`, `bootstrap`, then one stylesheet per page or section, and finally `bundle-extras`. `main.scss` also holds the site-wide base styles: body, primary navbar, MOTD bar, footer, and shared utilities.

Files in `assets/scss/`:

- `variables.scss` is the design-token file (colors, fonts, sizing) and the source of truth for the §2 color palette.
- `functions.scss` holds SCSS helpers (for example `al-shadow`).
- `bootstrap.scss` / `bootstrap-icons.scss` are vendor imports.
- `_bundle-extras.scss` holds shared, site-wide custom styles, including the `al-cta-*` buttons and assorted utilities (imported as `./bundle-extras`).
- Page and section stylesheets: one file per page or major section, named after it (for example `home.scss`, `blog.scss`, `members.scss`, `alesco.scss`). To style a new page, add a file here and `@import` it in `main.scss` before `bundle-extras`. Some are partials prefixed with `_` and imported without the underscore (for example `_foundation.scss`, imported as `./foundation`).
- `partials/common/` holds `header.scss` and `footer.scss`.

The compiled `.css` and `.css.map` files in this directory are build artifacts; edit the `.scss` source only.

**Where to add styles:** page-only styles go in that page's file; styles reused across pages go in `_bundle-extras.scss`; a new design token goes in `variables.scss`.

**Class naming:** page-scoped classes are prefixed by page (`al-foundation-*`, `al-members-*`). Shared component classes use a plain `al-*` prefix (for example `al-cta-blue`, `al-sponsor-tier-block`).

**Color workflow:** after editing color variables in `variables.scss`, run `npm run generate:design-colors` to refresh §2. The husky pre-commit hook runs the generator's `--check` whenever `variables.scss` is staged and fails the commit if you forget.

## 10. i18n conventions

- All user-facing copy in templates must be wrapped in `{{ i18n "key" }}`.
- `i18n/en.json` is generated. Never hand-edit it.
- Workflow for copy and template changes: add the `{{ i18n }}` tags, then run `python3 find_missing_i18n_strings.py`. That script (and only that script) updates `en.json`: it adds missing keys and removes unused ones. Stage the result and commit.
- Do **not** run `setup-pages-for-supported-languages.py` for ordinary copy or template edits. It scaffolds per-language pages and is only for adding or changing the set of supported languages.
- Non-English translation happens in [Weblate](https://hosted.weblate.org/engage/almalinux/), not in-repo. Do not edit the non-English locale files. See the README's [Localization and Translation](README.md#localization-and-translation) section and the [translation guide](https://wiki.almalinux.org/Help-translating-site.html).
- Known limitation: event-page markdown body content is not currently translatable.

## 11. Component patterns

Reusable layout patterns across the site. This is a representative catalog, not an exhaustive list; the SCSS in `assets/scss/` is the source of truth for the exact rules. The foundation and members patterns below have live references at <https://almalinux.org/foundation/> and <https://almalinux.org/members/>.

**Spotlight card 2-up** (`al-members-spotlight` / `al-members-spotlight-card`, members free-tier section). Two accent cards side by side, each with an eyebrow, heading, lead, image, an `al-members-stats` strip, and a CTA. The accent comes from a `--accent` custom property set by the `.indiv` / `.mirror` modifier:

```html
<div class="al-members-spotlight">
  <div class="al-members-spotlight-card indiv">
    <div class="eyebrow">...</div>
    <h3>Individual Member</h3>
    <div class="al-members-stats">...</div>
    <div class="ctas"><a class="btn btn-primary">Apply as Individual</a></div>
  </div>
  <div class="al-members-spotlight-card mirror">...</div>
</div>
```

**Comparison matrix** (`al-members-matrix`, members paid-tier section). A CSS grid (`grid-template-columns: 1.4fr repeat(4, 1fr)`) of `head` cells per `[data-tier]`, `group-row` band headers spanning all columns, `cell center` values per tier, and a `footer-row` of CTAs. It collapses to a single column under 992px, labeling each value with its tier via `content: attr(data-tier)`.

**Foundation tier list** (`al-foundation-membership-tiers`, foundation page). A two-column list where each row is a colored `.dot`, a `.name`, and a `.price`:

```html
<ul class="al-foundation-membership-tiers">
  <li>
    <span class="dot" style="background: #14b8a6;"></span>
    <span class="name">Silver</span>
    <span class="price">$2,500/yr</span>
  </li>
</ul>
```

**Sponsor logo wall** (`layouts/partials/common/foundation-members.html`). A shared partial used by both the foundation and members pages. Each tier is an `al-sponsor-tier-block` with an `al-sponsor-tier-label` and an `al-sponsor-tier-logos is-{platinum,gold,ruby,...}` row of lazy-loaded logo links. Check this partial before adding sponsor markup to any page.

**Platinum strip** (`al-members-platinum-strip`, members page). A horizontal highlight band for the premium sponsor tier.

**Long-scroll deep-band layout.** The foundation and members pages are long single-scroll pages built from alternating deep-band sections (dark backgrounds with `al-py-lg` vertical rhythm). Reuse this banding rather than inventing new section spacing.

The following patterns are used site-wide:

**Table of contents and back-to-top** (`al-page-toc`, `al-back-to-top`, `main.scss`). A sticky sidebar table of contents for long-form pages, with small inline back-to-top links beside headings. The `al-page-toc-flat` variant hides nested entries.

**Table card** (`al-table-card`, `main.scss`). A compact reference table that floats beside article body text. The `al-table-card--block` variant never floats, for narrow columns.

**MOTD announcement bar** (`#al-motd`, `main.scss`). A site-wide notice bar below the navbar for announcements; the navbar takes a `.with-motd` modifier when it is present. The link variants `al-motd-event` (green) and `al-motd-election` (ruby) tint the message for context.

**"Trusted by" marquee** (`al-trusted-by-marquee`, `home.scss`; partial `layouts/partials/common/trusted-by.html`). A continuously scrolling logo strip on the homepage. It pauses on hover and disables its animation under `prefers-reduced-motion` (see [§14](#14-accessibility)).

**Persona cards** (`al-persona-card`, `_bundle-extras.scss`; partial `layouts/partials/get-almalinux/persona-cards.html`). A row of quick-link cards on the get-almalinux page that route visitors by audience (users, developers, sysadmins).

**Event schedule** (`al-schedule` / `al-sched-*`, `event-schedule.scss`; shortcode `layouts/shortcodes/event-schedule.html`). A two-column morning/afternoon schedule rendered from a Sessionize JSON export, with collapsible session descriptions. Used on event pages.

**ALESCo RFC cards** (`al-rfc-*`, `alesco.scss`). The proposal-lifecycle UI on the `/alesco` page: status-label pills, a lifecycle stepper, and proposal cards rendered client-side from the GitHub API.

## 12. Layout & spacing utilities

Two custom vertical-spacing utilities exist today, both in `main.scss`:

- `al-py-lg` applies `3rem` top and bottom padding, used on deep-band sections.
- `al-py-md` applies `2.5rem` top and bottom padding.

For everything else, use Bootstrap's spacing utilities (`m-*`, `p-*`, `gap-*`, `me-*`) and the grid (`.container`, `.row`, responsive `col-*` classes, and Bootstrap breakpoints) rather than writing custom media queries. The `.container` max-width widens to `1320px` at the `1400px` breakpoint (`_bundle-extras.scss`). A few page-local helpers exist (for example `gap-30`); prefer the Bootstrap utilities for new work.

## 13. Image guidelines

- **Format preference:** SVG > PNG > JPG. Use SVG for logos and icons, PNG for screenshots or images that need transparency, and JPG for photographs.
- **Optimizing PNGs:** compress PNGs (hero, OG, screenshots) with `pngquant` before committing (`brew install pngquant`): `pngquant --quality=70-95 --force --strip --output /tmp/opt.png <input.png>`, check the result for gradient banding, then replace the original. It typically cuts size 80-90% with no visible loss. Keep hero and OG images as PNG (best social-platform compatibility), not WebP.
- **Blog header images:** 1280×720 (16:9), following `static/blog-images/blog_images_template.svg`. Keep each file at or under 500 KB (optimize before committing, and prefer JPG for photo-heavy headers). The exported file goes in `static/blog-images/` and serves from `/blog-images/`. See [contributing-blog-posts.md](contributing-blog-posts.md) for the full workflow.
- **Board headshots:** 130px.
- **File locations:** `/static/board/` (board photos), `/static/brands/` (sponsor and partner logos), `/static/branding/` (official AlmaLinux logo and brand assets, see [§3](#3-logo-and-brand-assets)), `/static/membership-images/` (membership imagery), `/static/blog-images/` (blog header and in-post images).
- Use `loading="lazy"` on below-the-fold images (the sponsor logos already do).
- Every meaningful image needs descriptive `alt` text (see §14). Use an empty `alt=""` only for purely decorative images.

## 14. Accessibility

- **Color contrast must meet WCAG AA:** 4.5:1 for normal text, 3:1 for large text and UI components. Check any text-on-color and every tier accent against the surface behind it.
- **Example:** the Ruby tier accent was flagged for failing contrast and corrected to `#ff6e71`. This is why tier accents are always contrast-checked (see [§4](#4-tier-accent-colors)).
- Every image needs descriptive `alt` text; reserve empty `alt=""` for purely decorative images.
- Maintain a logical heading hierarchy: one `<h1>` per page, no skipped levels.
- Give each major page section a stable `id` so it can be linked to directly, both for deep links and for in-page navigation. Use short, lowercase, hyphenated anchors (for example `id="colors"`). Surface a small, always-visible anchor indicator beside the heading (a subtle `#` link, using the shared `.al-anchor` class in `_bundle-extras.scss`) so readers can see and copy the link.
- Blog post bodies start at `H2`. The post title is the page's only `<h1>` (rendered by `layouts/blog/single.html`), so never add a second `<h1>` in the post body. See [contributing-blog-posts.md](contributing-blog-posts.md).
- Respect `prefers-reduced-motion`: any animation (for example the homepage "Trusted by" marquee) must pause or disable itself for visitors who ask for reduced motion.

## 15. Forbidden patterns

- Never use Bootstrap's `btn-success`. For a green CTA, use `al-cta-green` within its approved purpose (see [§5](#5-button-taxonomy)).
- Never hand-edit `i18n/en.json` (see [§10](#10-i18n-conventions)).
- Never lowercase "AlmaLinux" in prose (see [§6](#6-typography)).
- Avoid raw hex colors in page or component SCSS when a `$al-c-*` variable exists for that color (see [§2](#2-brand-colors)). Some legacy raw hex remains and is being migrated; do not add more.
- Always check `layouts/partials/common/` for an existing shared partial before adding markup to a page. Do not duplicate (for example the sponsor logo wall in `foundation-members.html`).

## 16. Presentations

This section is guidance for building AlmaLinux talk decks: think defaults and a shared vocabulary, not a rulebook. The aim is decks that feel recognizably AlmaLinux while leaving room for the speaker's own style. A few things stay fixed (the brand colors, the two fonts, the logo rules, accessibility, and the voice); everything else below is a strong starting point you can adapt to the talk.

> **Note:** Representing the AlmaLinux OS Foundation anywhere requires official approval. You may always present yourself as a member of the community, but make it clear that you are not representing the Foundation unless you have explicit permission to do so.

Slides are their own medium, so this reconciles our brand system with what most common presentation builders need. Decks are usually **1920x1080 (16:9)**, one idea per slide. A reusable deck template (PPTX or Google Slides) is maintained separately, outside this repository. Ask in the marketing channel on chat.almalinux.org for the most current one.

**Fonts (fixed).** Use Montserrat for headings and display (weights 600 to 800, tight tracking near `-0.02em`) and Arial for body. Both render natively in Google Slides and PowerPoint, so exported decks stay faithful. Use monospace only inside code blocks, and keep to these two families. (The website uses the system-UI body stack in [§6](#6-typography); Arial is the deliberate choice for slide portability.)

**Color (palette fixed, use flexible).** Use the exact palette from [§2](#2-brand-colors). Lean dark: most slides sit on Black Pearl `#082336`, page background `#0f4266`, or the darkest `#000518`, and rotating between them gives a deck rhythm. Yellow `#ffcb12` reads as the signature highlight, and keeping it to about one moment per slide keeps it special. The other brand colors work well as accents, such as card top-borders, eyebrow labels, and timeline bars. A few things stay firm: green is a reserved action color rather than a general fill, text on yellow or green is the dark ink `#000518` (never white), and every pairing must meet WCAG AA (see [§14](#14-accessibility)).

**Section dividers** are the natural home for a full brand-color background. Cycle the palette across sections so consecutive dividers differ, which keeps the chapters distinct. On bright dividers (yellow, green, CTA blue), flip the text and logo to navy for contrast. Keep the divider itself simple, with a small "Section 0N" label, the icon, a big centered title, a one-line description, and a faint oversized mark bleeding off a corner.

**Most content slides share a dependable skeleton** that you can adapt as the slide needs. A quiet header sits at the top, with a small colored dot plus the event and city on the left and the white AlmaLinux logo on the right. The reading order then runs eyebrow to headline to content, and a footer closes the slide with a short section label on the left and an `NN / NN` slide number on the right. Generous margins, roughly 90px top and bottom and 104px left and right, keep it breathing, and a `56x4px` accent-blue underline bar under the headline is a nice signature detail when it fits.

**A starting type scale (1920x1080, adjust to taste):**

| Element                      | Size         | Font                |
| ---------------------------- | ------------ | ------------------- |
| Hero display (title/closing) | 150 to 200px | Montserrat 800      |
| Divider title                | ~200px       | Montserrat 800      |
| Slide headline               | 76 to 104px  | Montserrat 700      |
| Lede / subtitle              | 30 to 36px   | Arial               |
| Body and bullets             | 26 to 32px   | Arial               |
| Card title                   | 30 to 32px   | Montserrat 700      |
| Card body                    | 22 to 24px   | Arial               |
| Eyebrow / labels             | 20 to 24px   | Arial bold, colored |
| Header / footer              | 20 to 22px   | Arial, muted        |

The point is big, legible type: these slides are read from the back of a room, so keep body copy comfortably large (roughly 24px and up).

**Draw from a shared component toolkit** rather than treating it as a checklist. It includes cards (rounded panels on a lighter navy, hairline border, optional colored top-border), tables (hairline separators, bold headers, an optional faint-yellow "hero" row, and small status pills), pills, code blocks (near-black panel, colored spans), callouts (warning, info, and do-vs-don't), timeline bars (a year grid with a "today" marker), and a big-number treatment for one-stat moments.

**Logo (fixed rules).** Use the official files, never recreated (see [§3](#3-logo-and-brand-assets)). Put the white wordmark on dark slides (the default), the navy wordmark on bright dividers, and the icon-only mark in divider corners and on the end slide, kept around 30 to 38px tall in the header.

**Voice.** The voice is casual and peer-to-peer, aimed at sysadmins, researchers, and community folks rather than a boardroom. Use sentence case for titles and prose, and keep the brand naming rules from [§7](#7-voice-and-tone). A signature closer, "No drama, just Linux," and bookending the deck (the closing slide echoing the title) both land well.

**Restraint** is the intangible that ties it together: one idea per slide, white space as a feature, and no clip-art or decorative gradients for their own sake. When a fact is missing, leave a visible `[SUPPLY: ...]` placeholder rather than inventing one.

**Reach for these slide archetypes** as the talk needs them: title, speaker intro, agenda table, section divider, lede plus cards, card grids, bullets plus code, timeline, pull quote, data table, numbered process steps, full-bleed image plus overlay, bullets plus screenshot, callouts, demo break, closing statement, and thanks / Q&A. Mix and match.

## 17. How to add a new design element

1. Propose the change in a GitHub issue or PR and discuss it with the Marketing SIG. See the README's [Contributing - Code and Design](README.md#contributing---code-and-design) section for the overall workflow.
2. Add any new tokens to the correct SCSS file. For a new color, add it to `variables.scss` with a `// @usage` comment, then run `npm run generate:design-colors`.
3. Add a real example of the component to an actual page. Do not commit unused CSS.
4. Document the element in the relevant `DESIGN.md` section.
5. Bump the "Last updated" date in the header and add a [§18](#18-changelog) entry.

## 18. Changelog

- **v1.0** (2026-07-01): Initial design system documentation, proposed to the Marketing SIG for adoption.
- **(2026-07-06):** Added a note pointing to the public /branding assets page.
- **(2026-07-07):** Added the Pantone reference from the Brand Book and corrected the brand red to `#ff4649`.
- **(2026-07-09):** Added the Presentations section, and required a stable `id` on major page sections.
