---
title: "Introducing AlmaLinux Astra: Self-Service Memberships and Elections Portal"
type: blog
author:
  name: "Alex Iribarren"
  bio: "Director, AlmaLinux OS Foundation"
  image: /board/alexiribarren.jpg
date: 2026-03-10
images:
  - /blog-images/2026/astra_hero.png
post:
  title: "Introducing AlmaLinux Astra: a new self-service portal for AlmaLinux Foundation members"
  image: /blog-images/2026/astra_hero.png
---

Today we’re rolling out **[AlmaLinux Astra](https://github.com/AlmaLinux/astra)**: a new self-service platform for identity, organizations, memberships, and elections for the AlmaLinux OS Foundation.

Astra is built to keep workflows clear, accountable, and easy to audit. It helps contributors and communities move from “who are you?” to “you can participate” with fewer manual handoffs and more transparent status updates.

Astra will replace the current [Noggin](https://github.com/fedora-infra/noggin)-based system at https://accounts.almalinux.org. It’s inspired by Noggin, but built entirely from scratch using [Django](https://www.djangoproject.com/).

# Identity and security

Two important features remain at the core of AlmaLinux Accounts (and are worth calling out as we expand what the platform does):

- **FreeIPA-backed account login** — Sign in with a single AlmaLinux Accounts identity (your username) and use that identity across memberships, elections, Mattermost, etc.

- **Two-factor authentication (OTP/2FA)** — Enable one-time passwords as an extra sign-in factor. This significantly reduces account-takeover risk if a password is reused or leaked.

# Memberships, with clearer workflows

Astra expands AlmaLinux Accounts beyond “login” into a structured system for membership management.

## Structured membership applications

Astra introduces **structured membership applications** so you can apply for different membership types (for example, individual vs mirror vs sponsorship) from a simple interface.

On the back end, it gives the Membership Committee the information they need to review applications and automates parts of the workflow (like sending email notifications). The goal is straightforward: clearer applications and faster review because applicants answer the right questions up front.

## Prerequisite checks for sensitive actions

Some actions (notably membership-related submissions) require prerequisites such as agreeing to required terms (like a Code of Conduct agreement) and providing a country code when needed for compliance checks.

Astra makes those requirements explicit and enforces them consistently. If you’re missing something, you’ll be redirected to complete it before you can submit a membership request.

## Organization profiles (coming soon)

Organization profiles are coming soon to Astra. The goal is to highlight contributing sponsor members and provide a self-service portal for organization representatives.

# Elections: all AlmaLinux elections will use Astra

While this started out as a project to help make managing memberships easier for the Membership Committee, this is the biggest and most exciting part of the project.

**All AlmaLinux OS Foundation elections going forward will be conducted through Astra.** To vote, you must:

- Have an AlmaLinux Accounts login at https://accounts.almalinux.org
- Have a valid, active AlmaLinux OS Foundation membership linked to that account

To make this transition easier, we will **pre-seed Astra with our current member list**, using email addresses and full names to match members with their current AlmaLinux Accounts login. If you already have an AlmaLinux Accounts login and you don't see your membership registered when you log in, [contact us](mailto:astra@almalinux.org) with your username, email address and full name and we'll sort it out.

However, many existing members do not yet have an AlmaLinux Accounts login. If you’re currently a member and you don’t have an account yet, you will need to create one in order to remain a member of the AlmaLinux OS Foundation and to be eligible to vote in future elections. We will be sending out targetted emails inviting you to create an account, and once you do we'll be able to associate your membership to it.

## Ranked-choice elections with deterministic tallying

As mentioned, we will be using Astra for all things around voting an elections. Your vote will continue to be anonymous, but there are a few things that will make it easier for the Membership and Election Committees to manage our elections. 

First, Astra includes ranked-choice voting, where eligible members vote by ranking candidates. 

Results are computed using a documented Meek STV (high-precision) method with deterministic tallying, which means results are proportional, transparent, and reproducible for recounts.

Astra also supports **vote receipts** and publishing **audit artifacts** for community verification.

The intent is to strengthen trust in election integrity while aiming to protect vote anonymity after elections close.

{{< figure src="/blog-images/2026/astra_election1.png" width="50%" class="text-center" >}}

{{< figure src="/blog-images/2026/astra_election2.png" width="50%" class="text-center" >}}

{{< figure src="/blog-images/2026/astra_election3.png" width="50%" class="text-center" >}}

# What you should do now

If you want to participate in AlmaLinux governance—especially voting in elections—please take a few minutes to make sure you’re ready:

- If you don’t already have an AlmaLinux Accounts login, create one at https://accounts.almalinux.org
- If you do have an account, log in and make sure your information is up to date
- Consider enabling OTP/2FA on your account
- If you’re applying for (or renewing) membership, complete any prerequisites Astra prompts you for

If you have questions about memberships, reach out to the Membership Committee at [membership@almalinux.org](mailto:membership@almalinux.org). For election-specific questions, you can reach the Election Committee at [elections@almalinux.org](mailto:elections@almalinux.org). Finally, if you have any general problems with Astra or have some suggestions reach out to [astra@almalinux.org](mailto:astra@almalinux.org).

Thank you for helping us keep AlmaLinux governance transparent, secure, and community-driven.
