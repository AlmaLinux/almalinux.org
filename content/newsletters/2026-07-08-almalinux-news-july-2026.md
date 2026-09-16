---
title: "AlmaLinux News for July '26"
type: newsletters
date: "2026-07-08"
summary: "AlmaLinux Day: LA 2026 is July 18th and the speakers have been announced, AlmaLinux OS is now Common Criteria certified, patched kernels are out for Januscape, Bad Epoll, and IPV6_FRAG_ESCAPE, and you have until July 16th to join the foundation and vote in the rescheduled election."
image: /newsletter-images/jul-26.png
draft: false
---

Welcome to this month's newsletter! Here's what you may have missed in the past few weeks.

## Quick Notes

- [AlmaLinux Day: LA 2026](/almalinux-day-los-angeles-2026/) is around the corner: July 18th! The speakers and sessions have been announced, and you can check them out on our website. We'll also be at SIGGRAPH and Academy Open Source Days. Looking forward to seeing everyone in LA!
- Our rescheduled election is also coming soon! Make sure you have **joined the foundation by July 16th** in the [new Account and Election portal](https://accounts.almalinux.org) to ensure you get to cast your vote or run for the election. Learn more in [this blog post](/blog/2026-06-10-new-bylaws-and-2026-election/).

## New on the AlmaLinux Blog

**Two kernel vulnerabilities, Januscape and Bad Epoll: Call for testing**

We are shipping patched kernels for two serious Linux kernel vulnerabilities and would like your help verifying them before they go to production. The first, Januscape (CVE-2026-53359), is a flaw in KVM/x86 with several distinct impacts. The second, Bad Epoll (CVE-2026-46242), is a use-after-free in the kernel's epoll subsystem that lets an unprivileged local user escalate to root.

[Read more in this blog post](/blog/2026-07-06-januscape-bad-epoll/).

**IPV6_FRAG_ESCAPE vulnerability: Fixed!**

A new Linux kernel local-privilege-escalation flaw has been disclosed in the IPv6 fragmentation code, and it is serious: an unprivileged user inside a container can use it to escape to a root shell on the host. Patched kernels are now in production.

[Get more information in this blog post](/blog/2026-06-30-ipv6-frag-escape/).

**AlmaLinux OS is Common Criteria certified**

AlmaLinux OS 9.2 is now certified under [Common Criteria](https://www.commoncriteriaportal.org/), the international standard (ISO/IEC 15408) for independently evaluating the security of IT products. We couldn't have made this happen without [Cybertrust Co., Ltd.](https://www.cybertrust.co.jp/english/), a longtime platinum sponsor of the AlmaLinux OS Foundation. The work was led and carried by Cybertrust engineers who are themselves members of the Foundation. That is exactly the kind of collaboration that makes AlmaLinux what it is: sponsors and contributors investing in the project together.

[Learn more in this blog post](/blog/2026-06-24-common-criteria-certification/).

## AlmaLinux Events (2026)

We've got big plans for 2026! Here's a look at the upcoming events we're currently planning to attend in the next few months:

- July 16: [BayLISA](https://www.meetup.com/baylisa/) - Say hi to benny!
- July 18: [AlmaLinux Day: LA](/almalinux-day-los-angeles-2026/) - Say hi to the whole crew!
- July 19-20: [Academy Open Source Days](https://events.linuxfoundation.org/open-source-days/) - Say hi to the whole crew!
- July 19-23: [SIGGRAPH](https://s2026.siggraph.org/) - Say hi to the whole crew!
- August 6: [FOSSY](https://fossy.us/) - Say hi to benny!

If you have thoughts on other events that we should attend, let us know! Our global community is growing quickly, and we love to connect with them wherever they are.

## Stay Connected

Sign up for the [Newsletters mailing list](https://lists.almalinux.org/mailman3/lists/newsletters.lists.almalinux.org/) or [subscribe on LinkedIn](https://www.linkedin.com/newsletters/almalinux-news-7123058222835376128/) to make sure you catch every update.
