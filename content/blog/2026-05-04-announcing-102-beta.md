---
title: "AlmaLinux 10.2 Beta Now Available!"
type: blog
author:
  name: "Eduard Abdullin"
  bio: "The Release and Automation Engineer."
  image: /users/eduard-abdullin.jpg
date: "2026-05-04"
images:
  - /blog-images/2026/2026-05-04-102-beta.png
post:
  title: 'AlmaLinux 10.2 Beta "Lavender Lion" is now available for x86_64, x86_64_v2, i686, aarch64, ppc64le, and s390x. Help us test Python 3.14, PostgreSQL 18, MariaDB 11.8, Ruby 4.0, PHP 8.4, refreshed container and virtualization stacks, and the new i686 userspace before the stable release.'
  image: /blog-images/2026/2026-05-04-102-beta.png
---

Hello Community!

The AlmaLinux OS Foundation is announcing the availability of AlmaLinux 10.2 Beta "Lavender Lion" for all supported architectures:

- Intel/AMD (x86_64)
- Intel/AMD (x86_64_v2)
- Intel/AMD 32-bit (i686)
- ARM64 (aarch64)
- IBM PowerPC (ppc64le)
- IBM Z (s390x)

Beta ISOs are available at [repo.almalinux.org](https://repo.almalinux.org/almalinux/10.2-beta/isos/).

A usual reminder: this is a **BETA** release. It should not be used for production installations. The provided upgrade instructions should not be used on production machines unless you don't mind if something breaks. If you are looking to see how things are going to work in stable, you are on the right track.

## Release Notes and More Information

AlmaLinux 10.2 Beta introduces updated compiler toolsets, new language and database packages, and improved security. This release adds Python 3.14, PostgreSQL 18, MariaDB 11.8, Ruby 4.0, and PHP 8.4 as new packages, alongside SDL3, libkrun, trustee, and FIDO Device Onboard tooling. Container and virtualization support is updated with the latest versions of Podman, Buildah, libvirt, QEMU-KVM, and skopeo. Security is improved with updates to OpenSSL, OpenSSH, SSSD, SELinux policies, crypto-policies, and Keylime, keeping your system safe and reliable.

AlmaLinux 10.2 Beta also brings i686 userspace packages — enabling legacy 32-bit software, CI pipelines, and containerized workloads on AlmaLinux 10.

You can read the full release notes for this version on the wiki: [AlmaLinux OS 10.2 Beta Release Notes](https://wiki.almalinux.org/release-notes/10.2-beta.html).

## What can you do to help?

Your input into testing and feedback is crucial and essential for successful production releases.

Please, report any bugs you may see on the [Bug Tracker](https://bugs.almalinux.org/). Also, join us in the [AlmaLinux Community Chat](https://chat.almalinux.org) and ~testing Channel, post a question on our [10.2 Beta Forum](https://forums.almalinux.org/c/devel/10-beta/), on our AlmaLinux Community on [Reddit](https://reddit.com/r/almalinux) or catch us on [X](https://twitter.com/almalinux).

Enjoy this Beta release, let us know what you think and stay tuned.

**Happy Testing!**
