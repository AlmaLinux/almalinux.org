---
title: "PHP 2026-11-19 security release: Patched packages released"
type: blog
author:
  name: "Andrew Lukoshko"
  bio: "AlmaLinux Lead Architect"
  image: /users/alukoshko.jpg
date: "2026-11-19"
post:
  title: "PHP's 2026-11-19 security release fixes a batch of vulnerabilities, several of them rated critical, including remote code execution and PHP-FPM request smuggling. Patched PHP packages for the supported PHP streams on AlmaLinux 8, 9, and 10 are available in the production repositories. Update now."
header:
  template: vulnerability
  title: "PHP 2026-11-19 critical CVE: Patched"
  subtitle: "Updates are available"
---

The PHP project published a [critical security release](https://www.php.net/archive/2026.php#2026-11-18-1) today, 2026-11-19, with PHP [8.2.36](https://www.php.net/archive/2026.php#2026-11-19-1), [8.3.37](https://www.php.net/archive/2026.php#2026-11-19-2), [8.4.28](https://www.php.net/archive/2026.php#2026-11-19-3), and [8.5.13](https://www.php.net/archive/2026.php#2026-11-19-4). It fixes a batch of vulnerabilities, several of them rated **9.2 (Critical)**, including flaws that can lead to remote code execution and request smuggling in PHP-FPM. According to PHP's announcement, the issues rated critical require either non-default configuration or uncommon setups. **AlmaLinux 8, 9, and 10 all ship affected PHP versions.**

Patched packages for the supported PHP streams on AlmaLinux 8, 9, and 10 are available in the production repositories. To update, run:

```bash
sudo dnf clean metadata && sudo dnf upgrade 'php*'
sudo systemctl restart php-fpm
```

If you use mod_php on AlmaLinux 8, restart Apache with `sudo systemctl restart httpd` instead. Most mirrors sync every few hours, so if the update is not available to you yet, try again a little later.

## What is fixed

The table lists each vulnerability and the PHP versions that received a fix for it in AlmaLinux. Each CVE links to PHP's advisory. Severity scores are the CVSS scores from those advisories.

| CVE                                                                                       | Issue                                                                       | CVSS           | PHP versions patched    |
| ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | -------------- | ----------------------- |
| [CVE-2026-129289](https://github.com/php/php-src/security/advisories/GHSA-qc49-hpvq-g2w6) | PHP-FPM request smuggling through an unread HTTP request body               | 9.2 (Critical) | 7.4, 8.0, 8.2, 8.3, 8.4 |
| [CVE-2026-129496](https://github.com/php/php-src/security/advisories/GHSA-gr4f-wgx5-jpfv) | Timezone cache use-after-free can lead to remote code execution             | 9.2 (Critical) | 7.4, 8.0, 8.2, 8.3, 8.4 |
| [CVE-2026-126714](https://github.com/php/php-src/security/advisories/GHSA-fm2m-fjf5-v3cp) | Partially overwritten session files can lead to remote code execution       | 9.2 (Critical) | 7.4, 8.0, 8.2, 8.3, 8.4 |
| [CVE-2026-115560](https://github.com/php/php-src/security/advisories/GHSA-658j-r8rw-q6mx) | Session serializer mismatch can lead to remote code execution               | 9.2 (Critical) | 8.2, 8.3, 8.4           |
| [CVE-2026-129481](https://github.com/php/php-src/security/advisories/GHSA-g3vh-838c-65v7) | Use-after-free after interrupted session shutdown                           | 9.2 (Critical) | 8.2, 8.3, 8.4           |
| [CVE-2026-129474](https://github.com/php/php-src/security/advisories/GHSA-8mjj-2r7p-4hg2) | Use-after-free in magic method backtraces can lead to remote code execution | 9.2 (Critical) | 7.4, 8.0, 8.2, 8.3      |
| [CVE-2026-129291](https://github.com/php/php-src/security/advisories/GHSA-jm4m-qfqx-967m) | PHP-FPM epoll use-after-free can lead to local privilege escalation         | 8.8 (High)     | 7.4, 8.0, 8.2, 8.3, 8.4 |
| [CVE-2026-127960](https://github.com/php/php-src/security/advisories/GHSA-mmf9-xm3v-hg2x) | Denial of service through folded HTTP response headers                      | 8.7 (High)     | 7.4, 8.0, 8.2, 8.3, 8.4 |
| [CVE-2026-128064](https://github.com/php/php-src/security/advisories/GHSA-f6gg-rchx-xw8j) | Mixed-case HTTPS and FTPS URLs can expose data in plaintext                 | 8.2 (High)     | 7.4, 8.0, 8.2, 8.3, 8.4 |
| [CVE-2026-128090](https://github.com/php/php-src/security/advisories/GHSA-68fq-fh7h-f8gr) | PHAR OpenSSL signature bypass via algorithm downgrade                       | 7.7 (High)     | 7.4, 8.0, 8.2, 8.3, 8.4 |
| [CVE-2026-129538](https://github.com/php/php-src/security/advisories/GHSA-5j3f-64r7-f564) | PHP-CGI out-of-bounds read and write during PATH_INFO correction            | 6.9 (Medium)   | 7.4, 8.0, 8.2, 8.3, 8.4 |
| [CVE-2026-15353](https://github.com/php/php-src/security/advisories/GHSA-q23r-hr55-xmpg)  | SOAP information disclosure through malformed array dimensions              | 6.3 (Medium)   | 7.4, 8.0, 8.2, 8.3, 8.4 |
| [CVE-2026-129506](https://github.com/php/php-src/security/advisories/GHSA-4646-p932-gw34) | SOAP use-after-free when processing DTD entity references                   | 6.3 (Medium)   | 7.4, 8.0, 8.2, 8.3, 8.4 |
| [CVE-2026-129501](https://github.com/php/php-src/security/advisories/GHSA-x8r7-mg3g-74hg) | Double free during DOM XML serialization                                    | 6.3 (Medium)   | 8.4                     |
| [CVE-2026-129292](https://github.com/php/php-src/security/advisories/GHSA-3mg3-cr28-46gc) | PHP-FPM status endpoint XSS via unescaped user and script fields            | 5.3 (Medium)   | 7.4, 8.0, 8.2, 8.3, 8.4 |

Our fixes are backported, so the upstream PHP version number of a package does not change. Check the package version, not `php -v`.

## Patched package versions

Install the version listed for your release and stream, or higher. Confirm with `rpm -q php-common` (or `rpm -q php8.4-common` for PHP 8.4 on AlmaLinux 10).

**AlmaLinux 8**

- `php:7.4` stream: `php-7.4.33-8.module_el8.10.0+4379+4cffe92b.alma.1`
- `php:8.2` stream: `php-8.2.35-1.module_el8.10.0+4381+cf144917.alma.1`

**AlmaLinux 9**

- Default (PHP 8.0): `php-8.0.30-8.el9_8.1.alma.1`
- `php:8.2` stream: `php-8.2.35-1.module_el9.9.0+360+bfa5da00.alma.1`
- `php:8.3` stream: `php-8.3.36-1.module_el9.9.0+361+ab310fe6.alma.1`
- `php:8.4` stream: `php-8.4.27-1.module_el9.9.0+362+e3c29387.alma.1`

**AlmaLinux 10**

- Default (PHP 8.3): `php-8.3.36-1.el10_2.alma.1`
- PHP 8.4 (`php8.4` packages): `php8.4-8.4.27-2.el10_3.1.alma.1`

Our packages only update PHP installed from AlmaLinux's own repositories. If you get PHP from somewhere else, such as a web hosting control panel, a hosting provider, or a third-party repository, check with that vendor for their fixes and timeline.

## Straight to production

Security is a top priority at AlmaLinux. Several of these flaws are rated critical, and PHP announced the release in advance as a critical one, so these packages were released directly to the production repositories rather than going through the testing repository first.

The PHP project released fixes for PHP 8.2 and later. AlmaLinux also ships PHP 7.4 on AlmaLinux 8 and PHP 8.0 on AlmaLinux 9, and those needed the fixes backported.

### Retired streams

This update covers the PHP streams that are still supported. `php:7.2`, `php:7.3`, and `php:8.0` on AlmaLinux 8, and `php:8.1` on AlmaLinux 9, have reached the end of their [RHEL Application Streams life cycle](https://access.redhat.com/support/policy/updates/rhel-app-streams-life-cycle) and are **not part of this update**. If you are on one of them, plan to move to a supported stream.

`php:7.2` is still the default stream on AlmaLinux 8, so if you installed PHP there without choosing a stream, that is what you have. The [php2shell post](/blog/2026-10-21-php2shell-cve-2026-109618-cve-2026-109619/#retired-streams) explains how to check your stream and switch.

If you run into anything with the updated packages, please let us know in [AlmaLinux chat](https://chat.almalinux.org) or on [bugs.almalinux.org](https://bugs.almalinux.org).

## Thanks

Thanks to **[TuxCare Inc](https://tuxcare.com/)** for providing the patches for this update.

Thanks to the researchers who found and reported these flaws (credited in PHP's advisories), to the PHP developers who wrote the fixes, and to the PHP security team for coordinating the release.

## Stay informed

Remaining aware of these vulnerabilities and acting quickly can keep your systems and data safe. Follow the AlmaLinux Blog, join the [Mattermost Community Chat](https://chat.almalinux.org/), and subscribe to the [Announce](https://lists.almalinux.org/mailman3/lists/announce.lists.almalinux.org/) and [Security](https://lists.almalinux.org/mailman3/lists/security.lists.almalinux.org/) mailing lists to stay informed.

## Changelog

- **2026-11-19:** Initial post published. Patched PHP packages released to the production repositories for the supported PHP streams on AlmaLinux 8, 9, and 10.
