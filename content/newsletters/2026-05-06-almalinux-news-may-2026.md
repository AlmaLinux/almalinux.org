---
title: "AlmaLinux News for May '26"
type: newsletters
date: "2026-05-06"
summary: "AlmaLinux 10.2 Beta and 9.8 Beta are now available, patched kernels for Copy Fail and Dirty Frag are in production, the AlmaLinux Day: LA 2026 CFP closes June 5th, and our rescheduled election is coming soon."
image: /newsletter-images/may-26.png
draft: false
---

Welcome to this month's newsletter! Here's what you may have missed so far this year.

## Quick Notes

- AlmaLinux 10.2 Beta and 9.8 Beta are now available! Learn more in the "New on the AlmaLinux Blog" section below.
- Because Dirty Frag and Copy Fail affected every supported AlmaLinux release, patched kernels for both have been rolled out to production repositories/mirrors. Learn more below!
- AlmaLinux Day: LA 2026 is fast approaching! The CFP closes June 5th, but the first round of acceptances will be sent out next week. [Submit your talk or panel idea soon!](https://sessionize.com/almalinux-day-los-angeles/)
- Our rescheduled election will be coming soon! Make sure you have registered in the [new Account and Election portal](https://accounts.almalinux.org) to ensure you get to cast your vote.

## New on the AlmaLinux Blog

**Dirty Frag (CVE-2026-43284, CVE-2026-43500) Patches Released**

A week after Copy Fail, researcher Hyunwoo Kim disclosed a second Linux kernel flaw in the same broad area — IPsec ESP and rxrpc — that they have named Dirty Frag. Like the previous Copy Fail vulnerability, Dirty Frag immediately yields root on all major distributions. Every supported AlmaLinux release is affected. As of May 8, patched kernels have been rolled out to production repositories/mirrors.

[Learn more in this blog post](/blog/2026-05-07-dirty-frag/).

**AlmaLinux 10.2 Beta Now Available!**

AlmaLinux 10.2 Beta "Lavender Lion" is now available! Help us test Python 3.14, PostgreSQL 18, MariaDB 11.8, Ruby 4.0, PHP 8.4, refreshed container and virtualization stacks, and the new i686 userspace before the stable release.

[Here's a link to the blog post announcement](/blog/2026-05-04-announcing-102-beta/).

**Copy Fail (CVE-2026-31431) Patches Released**

On April 29, the team at Xint Code disclosed a Linux kernel flaw they have named Copy Fail, tracked as CVE-2026-31431. Every supported AlmaLinux release is affected. If you run AlmaLinux on a multi-tenant host, container build farm, CI runner, or any system where untrusted users can get a shell, this one matters. As of May 1, patched kernels are now in production.

[Here's more information in this blog post](/blog/2026-05-01-cve-2026-31431-copy-fail/).

**Linux Kernel 6.18 Testing for Raspberry Pi**

The kernel of Raspberry Pi OS is planning a move to 6.18, the next upstream LTS kernel version. We are also considering migrating our AlmaLinux images for Raspberry Pi to the 6.18 kernel, and we now offer a pre-release Raspberry Pi kernel for users interested in these cutting-edge updates.

[To read more, check out this blog post](/blog/2026-04-29-linux-6-18-in-testing-for-rpi/).

**AlmaLinux 9.8 Beta Now Available!**

Announcing the availability of AlmaLinux 9.8 Beta "Olive Jaguar!" Supported architectures include Intel/AMD (x86_64), ARM64 (aarch64), IBM PowerPC (ppc64le), and IBM Z (s390x). Beta ISOs are available at [repo.almalinux.org](https://repo.almalinux.org). A usual reminder: this is a BETA release and should not be used for production installations.

[Read the release notes and more in this blog post](/blog/2026-04-23-announcing-98-beta/).

**California's New Age Verification Law: What It Means for AlmaLinux**

You may be aware of a new age verification law in California. While we don't like this legislation, it may require operating systems to implement digital age verification, and communicate the results of this verification to applications working on top of our AlmaLinux.

[Learn more in this blog post](/blog/2026-04-21-california-age-verification-law/).

## AlmaLinux Events (2026)

We've got big plans for 2026! Here's a look at the upcoming events we're currently planning to attend in the next few months:

- May 6-8: [HPC Admin Tech](https://www.hpcadmintech.com/)
- May 18-20: [Open Source Summit NA](https://cd.foundation/event/open-source-summit-north-america-2026/)
- June 5-7: [Flock to Fedora](https://fedoraproject.org/flock/2026/)
- June 12-14: [Southeast Linux Fest](https://southeastlinuxfest.org/)
- June 18-19: [DevConf](https://www.devconf.info/cz/)
- July 18: [AlmaLinux Day: LA](/almalinux-day-los-angeles-2026/)
- July 19-20: [Academy Open Source Days](https://events.linuxfoundation.org/open-source-days/)
- July 19-23: [SIGGRAPH](https://s2026.siggraph.org/)

If you have thoughts on other events that we should attend, let us know! Our global community is growing quickly, and we love to connect with them wherever they are.

## Stay Connected

Sign up for the [Newsletters mailing list](https://lists.almalinux.org/mailman3/lists/newsletters.lists.almalinux.org/) or [subscribe on LinkedIn](https://www.linkedin.com/newsletters/almalinux-news-7123058222835376128/) to make sure you catch every update.
