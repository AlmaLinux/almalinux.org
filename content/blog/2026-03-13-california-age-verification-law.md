---
title: "California's New Age Verification Law: What It Means for AlmaLinux"
type: blog
author:
  name: "benny Vasquez"
  bio: "Chair, board of directors"
  image: /users/benny.jpeg
date: 2026-03-13
images:
  - /blog-images/2026/2026-03-13-california-age-verification.png
post:
  title: "California's New Age Verification Law: What It Means for AlmaLinux"
  image: /blog-images/2026/2026-03-13-california-age-verification.png
---

Some of you may have seen news about California's AB-1043, the "Digital Age Assurance Act," and are wondering what it means for AlmaLinux and other Linux distributions. This is a reasonable question, so I wanted to share what we know and where we stand.

## What is AB-1043?

[AB-1043](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260AB1043) was signed into law in October 2025 and becomes operative on January 1, 2027. At a high level, it requires operating system providers and application stores to implement digital age verification signals. Here's what the law requires:

**Operating system providers** must provide an interface during account setup that asks the account holder (a parent, guardian, or adult user) to input the user's birth date or age. The OS then sends an "age bracket signal" to applications via a real-time API, categorizing users into one of four age brackets:

- Under 13
- 13 to 15
- 16 to 17
- 18 and older

**Application developers** must request these age signals when their applications are downloaded and launched, and treat them as the primary indicator of a user's age. Developers are prohibited from requesting more information than necessary or sharing these signals with third parties.

**Covered application stores** (platforms that distribute third-party applications) have their own set of obligations around passing these signals along.

The penalties for non-compliance are significant: up to $2,500 per affected child for negligent violations and $7,500 per affected child for intentional violations, enforced by the California Attorney General.

## What does this mean for Linux distributions?

This is where things get interesting — and uncertain. The law was written with commercial mobile and desktop operating systems in mind (think iOS, Android, Windows), and the language around "operating system providers" and "account setup" doesn't map neatly onto how Linux distributions work. Most Linux distributions, including AlmaLinux, don't have centralized account systems, app stores with mandatory registration, or the kind of tightly controlled software distribution pipelines that this law assumes.

There are also significant open questions about how this law interacts with open source software distribution more broadly. Is a package repository an "application store"? Is a Linux distribution an "operating system provider" in the way the law intends? These are not questions with clear answers right now.

## Where AlmaLinux stands

Our current plan is straightforward: **we are going to wait and see how this plays out**.

There are two things we're watching closely:

1. **The courts.** Laws like this often face legal challenges, and AB-1043 is no exception. There are real First Amendment and privacy concerns that are likely to be tested in court before the January 2027 operative date. We want to see how those challenges resolve before making any changes to how we operate.

2. **How Red Hat handles it.** As a downstream distribution, how Red Hat Enterprise Linux chooses to address (or not address) these requirements will significantly influence how we respond. If RHEL implements changes related to age verification compliance, those changes will flow downstream to us and we'll evaluate them at that point.

In the meantime, we don't believe this law requires immediate action on our part. The law's requirements are primarily aimed at commercial platforms with centralized app distribution and account management — not community-driven Linux distributions.

## We'll keep you informed

If anything changes — whether through court rulings, regulatory guidance, or upstream decisions from Red Hat — we'll communicate that to you. As always, transparency is a core value for us, and we won't make decisions about something like this without keeping you in the loop.

If you have questions or concerns, come talk to us on the [AlmaLinux Community Chat](https://chat.almalinux.org/) or reach out on the [mailing lists](https://lists.almalinux.org/).
