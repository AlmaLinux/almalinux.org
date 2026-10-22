---
title: "Node.js (CVE-2026-105482, CVE-2026-105483, CVE-2026-106069, CVE-2026-111497): Patched packages available in testing"
type: blog
author:
  name: "Andrew Lukoshko"
  bio: "AlmaLinux Lead Architect"
  image: /users/alukoshko.jpg
date: "2026-10-22"
images:
  - /blog-images/2026/2026-10-22-nodejs-security.png
post:
  title: "The Node.js October 2026 security releases fix four High severity flaws, including a Brotli decoder bug that can lead to remote code execution. Patched Node.js 22 and 24 and brotli packages for AlmaLinux 8, 9, and 10 are in the testing repository now. Help us verify them before they go to production."
  image: /blog-images/2026/2026-10-22-nodejs-security.png
---

The Node.js project published its [October 2026 security releases](https://nodejs.org/en/blog/vulnerability/october-2026-security-releases) on 2026-10-21, fixing ten vulnerabilities across the 22.x, 24.x, and 26.x release lines. Four of them are rated **High**, including an out-of-bounds write in the Brotli decoder that the Node.js project says permits remote code execution. **AlmaLinux 8, 9, and 10 all ship affected Node.js versions.**

Patched packages for Node.js 22 and 24, along with a patched `brotli` library, are available in the testing repository today, and we would like your help verifying them before we release them to production.

More information about the vulnerabilities:

- Node.js security release announcement: <https://nodejs.org/en/blog/vulnerability/october-2026-security-releases>

## What we are fixing

For this first round of updates, we are fixing the High severity issues in Node.js 22 and 24:

- **[CVE-2026-105482](https://www.cve.org/CVERecord?id=CVE-2026-105482):** `dns.resolve` truncates names that contain a NUL character. Affects Node.js 22 and 24.
- **[CVE-2026-105483](https://www.cve.org/CVERecord?id=CVE-2026-105483):** TLS certificate hostname check bypass when the IP address is written with fullwidth digits. Affects Node.js 24 only.
- **[CVE-2026-106069](https://www.cve.org/CVERecord?id=CVE-2026-106069):** TLS certificate hostname check bypass when the host loosely resolves to an IP address. Affects Node.js 22 and 24.
- **[CVE-2026-111497](https://www.cve.org/CVERecord?id=CVE-2026-111497):** Out-of-bounds write in the Brotli decoder that permits remote code execution. Affects Node.js 22 and 24.

The patch for CVE-2026-106069 also fixes **[CVE-2026-106072](https://www.cve.org/CVERecord?id=CVE-2026-106072)** (Medium), where non-canonical IPv4 hostnames let DNS names in a certificate authenticate IP endpoints.

The remaining Medium and Low severity issues, and the bundled dependency updates listed in the Node.js announcement, are not part of this update. They will be addressed in a later update.

### Why brotli is being updated

Node.js on AlmaLinux does not use its own bundled copy of Brotli (a compression library). It is built against the system `brotli` library instead. That means the fix for CVE-2026-111497 goes into the `brotli` package, and updating it protects Node.js and every other program on the system that decompresses Brotli data with it.

## Patching ahead of our upstream

Security is a top priority at AlmaLinux. At the time of writing, Red Hat has not released updates for these issues. Our core team has backported the upstream fixes to the Node.js 22 and 24 packages and to `brotli` on every supported AlmaLinux release.

Because the fixes are backported, the Node.js version numbers do not change to match upstream. Upstream fixed these issues in Node.js 22.23.4 and 24.22.1, while our patched packages stay at 22.23.2 and 24.21.0 with the `.alma.1` suffix in the release.

These packages are available **in the testing repository today**. After the community has helped verify them, we will release them to the production repositories. This post will be updated when that happens.

## Patched package versions

Install the version listed for your release, or higher.

**AlmaLinux 8**

- `nodejs:22` stream: `nodejs-22.23.2-2.module+el8.10.0+24957+74108fbf.alma.1`
- `nodejs:24` stream: `nodejs-24.21.0-1.module+el8.10.0+24927+ed3d907a.alma.1`
- `brotli-1.0.6-4.el8_10.alma.1`

**AlmaLinux 9**

- `nodejs:22` stream: `nodejs-22.23.2-2.module+el9.8.0+24958+80b2ac6e.alma.1`
- `nodejs:24` stream: `nodejs-24.21.0-1.module+el9.8.0+24924+cd677006.alma.1`
- `brotli-1.0.9-10.el9_8.alma.1`

**AlmaLinux 10**

- Default (Node.js 22, `nodejs` packages): `nodejs-22.23.2-3.el10_2.alma.1`
- Node.js 24 (`nodejs24` packages): `nodejs24-24.21.0-1.el10_2.alma.1`
- `brotli-1.1.0-8.el10_2.alma.1`

## Help us test

```bash
sudo dnf install -y almalinux-release-testing
sudo dnf upgrade 'nodejs*' '*brotli*' --enablerepo=almalinux-testing
```

Then restart any services that run Node.js applications so they load the patched code.

Confirm with `rpm -q nodejs` (or `rpm -q nodejs24` for Node.js 24 on AlmaLinux 10) and `rpm -qa '*brotli*'` against the versions above. Don't rely on `node --version`: our fixes are backported, so the upstream Node.js version number doesn't change.

If you do not want the testing repo enabled afterwards (and on a production box you almost certainly do not), disable it once you have updated:

```bash
sudo dnf config-manager --disable almalinux-testing
```

If you run into anything, please let us know in [AlmaLinux chat](https://chat.almalinux.org) or on [bugs.almalinux.org](https://bugs.almalinux.org).

## Thanks

Thanks to the researchers who found and reported these vulnerabilities, and to the Node.js security team and release team for developing the fixes and coordinating the release.

Thanks to the AlmaLinux core team for turning around patched builds for every supported release. And thank you in advance to everyone in the community who helps us test these packages. That's the part that gets them safely into production.

## Stay informed

Remaining aware of these vulnerabilities and acting quickly can keep your systems and data safe. Follow the AlmaLinux Blog, join the [Mattermost Community Chat](https://chat.almalinux.org/), and subscribe to the [Announce](https://lists.almalinux.org/mailman3/lists/announce.lists.almalinux.org/) and [Security](https://lists.almalinux.org/mailman3/lists/security.lists.almalinux.org/) mailing lists to stay informed. We will update this post when the patched packages move from testing to production.

## Changelog

- **2026-10-22:** Initial post published. Patched Node.js 22 and 24 and `brotli` packages available in `almalinux-testing` for AlmaLinux 8, 9, and 10.
