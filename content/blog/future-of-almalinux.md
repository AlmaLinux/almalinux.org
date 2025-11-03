---
title: "The Future of AlmaLinux is Bright"
type: blog
author:
  name: "benny Vasquez"
  bio: "Chair of the Board, AlmaLinux OS Foundation"
  image: /users/benny.jpeg
date: "2023-07-13"
post:
  title: "We're diverging from 1:1, but keeping AlmaLinux OS Free and Open, Forever"
  image: /blog-images/23.07.13.future.png
---

It’s been a whirlwind few weeks here at AlmaLinux, and I’m elated to be able to finally share this update.

## The future of AlmaLinux OS

In case you missed it, [Red Hat announced](https://www.redhat.com/en/blog/furthering-evolution-centos-stream) they will no longer be providing the means for downstream clones to continue to be 1:1 binary copies of Red Hat Enterprise Linux (RHEL). Very quickly, both [Jack](https://almalinux.org/blog/our-value-is-our-values/) and [I shared](https://almalinux.org/blog/impact-of-rhel-changes/) some initial thoughts, but we intentionally took our time deciding the next right step for AlmaLinux OS. After much discussion, the AlmaLinux OS Foundation board today has decided to drop the aim to be 1:1 with RHEL. AlmaLinux OS will instead aim to be binary compatible with RHEL\*.

_We will continue to aim to produce an enterprise-grade, long-term distribution of Linux that is aligned and binary compatible with RHEL in response to our community’s needs, to the extent it is possible to do, and such that software that runs on RHEL will run the same on AlmaLinux._
-- From yesterday's meeting notes: [Minutes - Board Meeting #23 July, 2023](https://drive.google.com/file/d/13q6udmzAEqHIoPf2cQJ-QJrYosaFWd_m/view)

## What this change means for users of AlmaLinux OS

For a typical user, this will mean very little change in your use of AlmaLinux. Red Hat-compatible applications will still be able to run on AlmaLinux OS, and your installs of AlmaLinux will continue to receive timely security updates. The most remarkable potential impact of the change is that we will no longer be held to the line of “bug-for-bug compatibility” with Red Hat, and that means that we can now accept bug fixes outside of Red Hat’s release cycle. While that means some AlmaLinux OS users may encounter bugs that are not in Red Hat, we may also accept patches for bugs that have not yet been accepted upstream, or shipped downstream.

## Changes to our development process

As one might anticipate, the change in our goals will require changes in our development and build processes.

One of the first things you will see is that we will include comments in our patches that include a link to where we got the patch that’s been applied (like [Grafana’s release ](https://git.almalinux.org/rpms/grafana/src/branch/a9/SPECS/grafana.spec#L74)yesterday). This change is helpful for several reasons, but it helps us specifically further our goal of transparency.

We will also start asking anyone who [reports bugs in AlmaLinux OS](https://bugs.almalinux.org/) to attempt to test and replicate the problem in CentOS Stream as well, so we can focus our energy on correcting it in the right place.

## What’s next?

Now that we will no longer be holding ourselves to being a 1:1 Red Hat downstream rebuild, we are taking some time to consider the possibilities around what that means. We will continue to provide updates around that process and will include the members of the AlmaLinux OS Foundation in that conversation and decision-making process as well.

There are also a ton of exciting developments and partnerships in the works that we will be able to announce in the coming weeks and months.

## Commitment to Open Source

While all of these changes open up a lot of opportunities, we want to be clear about the fact that we are still dedicated to being good open source citizens. We’ll continue to contribute upstream in Fedora and CentOS Stream and to the greater Enterprise Linux ecosystem, just as we have been doing since our inception, and we invite our community to do the same!

## Thank you, and how to help!

I want to say thank you to everyone who has reached out with interest and offers of assistance in the last few weeks, and to our users for making it clear that they understand and continue to see our value in the Enterprise Linux ecosystem.

Thanks also to our individual [sponsors](https://github.com/sponsors/AlmaLinux) and [backers](https://opencollective.com/almalinux-os-foundation) in addition to our corporate sponsors. You are the biggest part of the reason we can continue to provide AlmaLinux OS free forever.

If you have any interest in helping us out, there are a ton of ways to get involved. For folks that have time to offer: the Infrastructure and Cloud SIGs are always welcoming more folks, and the Marketing and Membership committees are looking for help, too! If you want to show support but don’t have much time, just joining the foundation is a great way to [join us](https://almalinux.org/members/). You can also convince your company to become a sponsor or just back us yourself as an individual [on GitHub](https://github.com/sponsors/AlmaLinux) or [OpenCollective](https://opencollective.com/almalinux-os-foundation).

There’s a lot of work to be done, and we are very excited to welcome you.

–-

\* [Binary/ABI compatibility](https://en.wikipedia.org/wiki/Application_binary_interface) in our case means working to ensure that applications built to run on RHEL (or RHEL clones) can run without issue on AlmaLinux. Adjusting to this expectation removes our need to ensure that everything we release is an exact copy of the source code that you would get with RHEL. This includes kernel compatibility and application compatibility.
