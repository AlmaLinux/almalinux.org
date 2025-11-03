---
title: "This Distro Should Not Exist - AlmaLinux 8.6 for IBM Z"
type: blog
author:
  name: "Jack Aboutboul"
  bio: "-"
  image: /users/jack.jpg
date: "2022-10-07"
post:
  title: "A mythical distribution with no upstream equivalent. Why did we do it? Because we can!"
  image: /blog-images/8.6forZ.png
---

Hello, IBM Z fans and Linux world at large. Today we have an interesting story to share about a new release - AlmaLinux 8.6 for s390x. The thing is, this release should not exist! Let's explain.

In general, we build an AlmaLinux release by consuming upstream sources from the [CentOS git](https://git.centos.org/) and pulling those into our [AlmaLinux Git Server](https://git.almalinux.org/) which are then built using by the [AlmaLinux Build System](https://github.com/AlmaLinux/build-system). While the CentOS project built releases for a few architectures, CentOS 8 was never built for IBM Z!

## Why We Did it

It's pretty easy to consume upstream and bake a distro and we've gotten pretty good at that, in fact we always were. But, we like to challenge ourselves, so that we can learn and grow while at the same time bringing goodness to the community. This is what motivated us to release projects like [ELevate](/elevate) which let you migrate from CentOS 7.x to any 8.x of your choice. So, we thought to ourselves, instead of re-building from upstream, let's try and build a distro that doesn't yet exist!

## How We Did it

In the middle of last year, [Sine Nomine](https://www.sinenomine.net/) joined the AlmaLinux Foundation as member. They previously used to build a very popular Linux for Z called [ClefOS](https://www.sinenomine.net/offerings/linux/ClefOS) but after the announcement of CentOS Stream they were looking for a direction forward. Eventually we got linked up and decided to work on supporting Z together for a long time under the AlmaLinux OS umbrella. Kurt, Neale and crew are truly incredible mavens when it comes to anything mainframe related and we're so glad to have them as part of our community.

CentOS 8 is built upon Fedora 28 so Kurt and Neale worked together with the by now world famous Andrew Lukoshko, our OS Architect, and AlmaLinux community member Eduard Abdullin to bootstrap the build from Fedora sources and packages. While a more detailed write up of the whole process is forthcoming, suffice it to say, this was quite an adventure which took months in order to work out the dependency chain, build all the required dependencies, build an initial base build as a root and then rebuild all the packages for Z architecture.

## Announcing AlmaLinux 8.6 for IBM Z Architecture

Without further ado, the AlmaLinux OS Foundation announces that AlmaLinux 8.6 for s390x has finally arrived! The release is waiting for you on the nearest [mirror](https://mirrors.almalinux.org/isos). Grab it and join us on the [AlmaLinux Community Chat](https://chat.almalinux.org/) to talk about this engineering marvel!

## AlmaLinux Joins the OpenMainframe Project

As part of this announcement we've also joined the [OpenMainframe Project](https://www.openmainframeproject.org/) and their Linux Distribution Working Group to help further support and promote Linux on Z.

Release Notes and How To Help
As usual, check out the AlmaLinux 8.6 [Release Notes](https://wiki.almalinux.org/release-notes/8.6.html) for details and changelog.

## Special Mentions

Well first, the AlmaLinux Team would like to thank the [Fedora Project](https://fedoraproject.org/) for their decades of service to the community, serving as a the bedrock of our ecosystem. We'd also like to thank [Sine Nomine](https://www.sinenomine.net/) and Neale Ferguson for their assistance and support. We'd also like to thank [Marist College](https://www.marist.edu/) for all their technical assistance as well. We'd like to give a special shout out to community member Eduard Abdullin who spent many a sleepless night working on the builds.

We are deeply grateful for their help making AlmaLinux 8 for this architecture available.

## How to Help

Join our incredible Community on the [Chat](https://chat.almalinux.org/), [Reddit](https://reddit.com/r/almalinux) or [Twitter](https://twitter.com/almalinux). Post a question, discuss stuff, and file [bug reports](https://bugs.almalinux.org/). As always happy hacking!

**Thank you for always rooting for us and choosing AlmaLinux!**
