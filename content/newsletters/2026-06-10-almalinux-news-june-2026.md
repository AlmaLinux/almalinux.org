---
title: "AlmaLinux News for June '26"
type: newsletters
date: "2026-06-10"
summary: "AlmaLinux 10.2 and 9.8 are now available, patched kernels for CIFSwitch, ssh-keysign-pwn, NGINX Rift, and Fragnesia are in production, AlmaLinux Day: LA 2026 is July 18th, and our rescheduled election is coming soon."
image: /newsletter-images/june-26.png
draft: false
---

Welcome to this month's newsletter! Here's what you may have missed in the past few weeks.

## Quick Notes

- AlmaLinux 10.2 and 9.8 are now available! Learn more in the "New on the AlmaLinux Blog" section below.
- If you'll be at SELF, Flock to Fedora, and/or DevConf, come find us!
- [AlmaLinux Day: LA 2026](/almalinux-day-los-angeles-2026/) is so soon — July 18th! We'll be announcing the speakers soon, so make sure you reserve your spot today.
- Our rescheduled election will be coming soon! Make sure you have joined the foundation in the [new Account and Election portal](https://accounts.almalinux.org) to ensure you get to cast your vote, and learn more in [this blog post](/blog/2026-06-10-new-bylaws-and-2026-election/).

## New on the AlmaLinux Blog

**New bylaws, New election process: What to expect in 2026**

We have new bylaws and a new election process! The 2026 election is coming up fast, so make sure you join the foundation so that you get a say.

[Learn more and check out the schedule in this blog post](/blog/2026-06-10-new-bylaws-and-2026-election/).

**CIFSwitch (CVE-2026-46243) Patches Released**

A new Linux local-root vulnerability (CVE-2026-46243, nicknamed CIFSwitch by its discoverer Asim Manizada) was disclosed on oss-security after the linux-distros embargo expired. Patched kernels are now in production.

[Learn more in this blog post](/blog/2026-05-28-cifswitch/).

**General Availability of AlmaLinux OS 9.8 and 10.2 Stable!**

AlmaLinux 10.2 "Lavender Lion" and 9.8 "Olive Jaguar" are now available! This is the first time we have ever shipped two AlmaLinux releases on the same day. It's the direct result of concerted effort by our Build, Core, and Infrastructure SIGs on our release engineering procedures. This work resulted in better automation, tighter QA pipelines, and a build system that can carry two parallel release trains without one slowing the other down.

[Check out the release notes and get the releases by checking out this blog post](/blog/2026-05-26-almalinux_98_and_102_stable/).

**AlmaLinux Day: LA — Venue Confirmed at E-Central Downtown LA**

We have a venue! AlmaLinux Day: Los Angeles will take place Saturday, July 18, 2026, at the E-Central Downtown Los Angeles Hotel at 1020 S Figueroa St — and you can [register now](https://events.almalinux.org/event/189/).

[Learn more in this blog post](/blog/2026-05-19-aldla-venue-announced/).

**ssh-keysign-pwn (CVE-2026-46333) Patches Released**

The fourth in a string of recent local-root Linux kernel disclosures, CVE-2026-46333, has been named ssh-keysign-pwn after one of the two public exploits. AlmaLinux 9 and 10 are both vulnerable. The public exploits work reliably on both, so patched kernels have been rolled out to production repositories/mirrors.

[More details in this blog post](/blog/2026-05-15-ssh-keysign-pwn-cve-2026-46333/).

**NGINX Rift (CVE-2026-42945) Patches Released**

A heap-based buffer overflow in nginx's ngx_http_rewrite_module (CVE-2026-42945, nicknamed NGINX Rift) allows an unauthenticated attacker to crash a worker process, or potentially achieve remote code execution on hosts with ASLR disabled, by sending a single crafted HTTP request. The flaw has been in the rewrite module for roughly 18 years and affects every version of nginx Open Source from 0.6.27 through 1.30.0, as well as nginx Plus R32 through R36. Patched nginx packages have been rolled out to the AlmaLinux production repositories for every supported release.

[To find out more, check out this blog post](/blog/2026-05-13-nginx-rift-cve-2026-42945/).

**Fragnesia (CVE-2026-46300) Patches Released**

Less than a week after Dirty Frag, researcher William Bowling of the V12 security team has disclosed a third Linux kernel local-root flaw in the same broad code area (IPsec ESP / rxrpc) that they have named Fragnesia, tracked as CVE-2026-46300. The patched kernels are now rolling out to production repositories/mirrors!

[Learn more in this blog post](/blog/2026-05-13-fragnesia-cve-2026-46300/).

## AlmaLinux Events (2026)

We've got big plans for 2026! Here's a look at the upcoming events we're currently planning to attend in the next few months:

- June 12-14: [Southeast Linux Fest](https://southeastlinuxfest.org/) — Say hi to benny and Jonathan!
- June 14-16: [Flock to Fedora](https://fedoraproject.org/flock/2026/) — Say hi to Andrew!
- June 18-19: [DevConf](https://www.devconf.info/cz/) — Say hi to Andrew!
- July 16: [BayLISA](https://www.meetup.com/baylisa/events/315062292/?eventOrigin=group_upcoming_events) — Say hi to benny!
- July 18: [AlmaLinux Day: LA](/almalinux-day-los-angeles-2026/) — Say hi to the whole crew!
- July 19-20: [Academy Open Source Days](https://events.linuxfoundation.org/open-source-days/) — Say hi to the whole crew
- July 19-23: [SIGGRAPH](https://s2026.siggraph.org/) — Say hi to the whole crew

If you have thoughts on other events that we should attend, let us know! Our global community is growing quickly, and we love to connect with them wherever they are.

## Stay Connected

Sign up for the [Newsletters mailing list](https://lists.almalinux.org/mailman3/lists/newsletters.lists.almalinux.org/) or [subscribe on LinkedIn](https://www.linkedin.com/newsletters/almalinux-news-7123058222835376128/) to make sure you catch every update.
