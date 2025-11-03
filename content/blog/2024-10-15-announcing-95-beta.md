---
title: "Announcing AlmaLinux 9.5 Beta!"
type: blog
author:
  name: "Eduard Abdullin"
  bio: "The Release and Automation Engineer."
  image: /users/eduard-abdullin.jpg
date: "2024-10-15"
images:
  - /blog-images/2024/2024-10-15-95-beta.png
post:
  title: "Announcing AlmaLinux 9.5 Beta!"
  image: /blog-images/2024/2024-10-15-95-beta.png
---

Hello Community!

The AlmaLinux OS Foundation is announcing the availability of AlmaLinux 9.5 Beta "Teal Serval" for all supported architectures:

- Intel/AMD (x86_64)
- ARM64 (aarch64)
- IBM PowerPC (ppc64le)
- IBM Z (s390x)

Beta ISOs are available at [repo.almalinux.org](https://repo.almalinux.org/almalinux/9.5-beta/isos/).

A usual reminder: this is a **BETA** release. It should not be used for production installations. The provided upgrade instructions should not be used on production machines unless you don't mind if something breaks. If you are looking to see how things are going to work in stable, you are on the right track.

## Keeping Betas in our Release Process

Eariler this year, Red Hat [updated](https://www.redhat.com/en/blog/upcoming-improvements-red-hat-enterprise-linux-minor-release-betas) their minor release process.

> _Starting with RHEL 9.5, minor release versions will be simplified. This means releasing packages earlier, and continuously, while reserving documentation, full installation media and virtual machine images for the full release._

We have decided to keep our existing release process as is to ensure that our thorough testing can be done both by the Core SIG and by our Community.

## Release Notes and More Information

AlmaLinux 9.5 Beta aims to improve performance, development tooling, and security. Updated module streams offer better support for web applications. New versions of compilers provide access to the latest features and optimizations that improve performance and enable better code generation. The release also introduces improvements to system performance monitoring, visualization, and system performance data collecting. Security updates are directed at strengthening cryptography, while SELinux policies enforce stricter access controls. Additionally, crypto-policies offer stronger encryption, improving the overall security of the system.

You can read the full release notes for this version on the wiki: [AlmaLinux OS 9.5 Beta Release Notes](https://wiki.almalinux.org/release-notes/9.5-beta.html).

## What you can do to help?

Your input into testing and feedback is crucial and essential for successful production releases.
Please, report any bugs you may see on the [Bug Tracker](https://bugs.almalinux.org/). Also, pop into the [AlmaLinux Community Chat](https://chat.almalinux.org) and join our Testing Channel, post a question on our [9.5 Beta Forum](https://forums.almalinux.org/c/devel/9-beta/34), on our AlmaLinux Community on [Reddit](https://reddit.com/r/almalinux) or catch us on [X](https://twitter.com/almalinux).

Enjoy this Beta release, let us know what you think and stay tuned.

**Happy Testing!**
