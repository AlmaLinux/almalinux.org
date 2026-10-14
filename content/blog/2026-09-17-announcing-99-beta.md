---
title: "AlmaLinux 9.9 Beta Now Available!"
type: blog
author:
  name: "Eduard Abdullin"
  bio: "The Release and Automation Engineer."
  image: /users/eduard-abdullin.jpg
date: "2026-09-17"
images:
  - /blog-images/2026/2026-09-17-99-beta.png
post:
  title: 'AlmaLinux 9.9 Beta "Chartreuse Bobcat" is now available for x86_64, aarch64, ppc64le, and s390x. GCC Toolset 16 lands in Enterprise Linux 9, Node.js 26 and PHP 8.4 arrive as new module streams, and fapolicyd reaches 2.0. Help us test it before the stable release.'
  image: /blog-images/2026/2026-09-17-99-beta.png
---

Hello Community!

The AlmaLinux OS Foundation is announcing the availability of AlmaLinux 9.9 Beta "Chartreuse Bobcat" for all supported architectures:

- Intel/AMD (x86_64)
- ARM64 (aarch64)
- IBM PowerPC (ppc64le)
- IBM Z (s390x)

Beta ISOs are available at [vault.almalinux.org](https://vault.almalinux.org/9.9-beta/isos/).

A usual reminder: this is a **BETA** release. It should not be used for production installations. The provided upgrade instructions should not be used on production machines unless you don't mind if something breaks. If you are looking to see how things are going to work in stable, you are on the right track.

## Release Notes and More Information

AlmaLinux 9.9 Beta introduces new compiler toolsets, new module streams, and improved security. This release adds GCC Toolset 16 alongside updated LLVM and Rust toolsets, and brings Node.js 26 and PHP 8.4 as new module streams. Virtualization support is updated with the latest versions of libvirt and QEMU-KVM, and the graphics stack is refreshed with Mesa. Security is improved with updates to SSSD, SELinux policies, crypto-policies, Keylime, and Clevis, keeping your system safe and reliable.

You can read the full release notes for this version on the wiki: [AlmaLinux OS 9.9 Beta Release Notes](https://wiki.almalinux.org/release-notes/9.9-beta.html).

## fapolicyd reaches 2.0

The file access policy daemon jumps from 1.4.5 to 2.0.1 in this release — a major version rather than the usual point update. fapolicyd sits in the execution path of every binary on a hardened system, so a new major version is worth a careful look before it reaches your production hosts.

If you run fapolicyd, this is the part of the release we would most like to see tested. Do your existing rules and trust database carry over cleanly? Please tell us what you find on the [9 Beta Forum](https://forums.almalinux.org/c/devel/9-beta/34).

## What can you do to help?

Your input into testing and feedback is crucial and essential for successful production releases.

Please, report any bugs you may see on the [Bug Tracker](https://bugs.almalinux.org/). Also, join us in the [AlmaLinux Community Chat](https://chat.almalinux.org) and ~testing Channel, post a question on our [9 Beta Forum](https://forums.almalinux.org/c/devel/9-beta/34), on our AlmaLinux Community on [Reddit](https://reddit.com/r/almalinux) or catch us on [X](https://twitter.com/almalinux).

Enjoy this Beta release, let us know what you think and stay tuned.

**Happy Testing!**
