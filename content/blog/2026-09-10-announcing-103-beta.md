---
title: "AlmaLinux 10.3 Beta Now Available!"
type: blog
author:
  name: "Eduard Abdullin"
  bio: "The Release and Automation Engineer."
  image: /users/eduard-abdullin.jpg
date: "2026-09-10"
images:
  - /blog-images/2026/2026-09-10-103-beta.png
post:
  title: 'AlmaLinux 10.3 Beta "Mauve Lion" is now available for x86_64, x86_64_v2, i686, aarch64, ppc64le, and s390x. ModSecurity and the OWASP Core Rule Set return to Enterprise Linux 10, Podman 6 moves container configuration out of /etc, and GCC Toolset 16, Node.js 26 and a .NET 11 preview arrive. Help us test it before the stable release.'
  image: /blog-images/2026/2026-09-10-103-beta.png
---

Hello Community!

The AlmaLinux OS Foundation is announcing the availability of AlmaLinux 10.3 Beta "Mauve Lion" for all supported architectures:

- Intel/AMD (x86_64)
- Intel/AMD (x86_64_v2)
- Intel/AMD 32-bit (i686)
- ARM64 (aarch64)
- IBM PowerPC (ppc64le)
- IBM Z (s390x)

Beta ISOs are available at [repo.almalinux.org](https://repo.almalinux.org/almalinux/10.3-beta/isos/).

A usual reminder: this is a **BETA** release. It should not be used for production installations. The provided upgrade instructions should not be used on production machines unless you don't mind if something breaks. If you are looking to see how things are going to work in stable, you are on the right track.

## Release Notes and More Information

AlmaLinux 10.3 Beta introduces new compiler toolsets, new language runtimes, and improved security. This release adds GCC Toolset 16 alongside updated LLVM and Rust toolsets, and brings Node.js 26 and a .NET 11 preview as new packages. Virtualization support is updated with the latest versions of libvirt and QEMU-KVM, and the graphics stack is refreshed with Mesa. Security is improved with updates to OpenSSL, OpenSSH, SSSD, SELinux policies, crypto-policies, and audit, keeping your system safe and reliable.

You can read the full release notes for this version on the wiki: [AlmaLinux OS 10.3 Beta Release Notes](https://wiki.almalinux.org/release-notes/10.3-beta.html).

## ModSecurity returns to Enterprise Linux 10

The `mod_security` web application firewall and the OWASP Core Rule Set are back. They shipped in AlmaLinux 8 and 9, but were absent from AlmaLinux 10.0 through 10.2 — this is the first Enterprise Linux 10 release to carry them.

The jump is a large one. AlmaLinux 9 has ModSecurity 2.9.6 with CRS 3.3, while 10.3 Beta ships 2.9.14 with CRS 4.22. CRS 4 is a rework of the rule set rather than a routine update, so rules and tuning carried over from the 3.3 series are unlikely to drop straight in.

If you run ModSecurity today, this is the part of the release we would most like to see tested. Does your existing rule set survive the move to CRS 4? We would very much like to hear about it on the [10 Beta Forum](https://forums.almalinux.org/c/devel/10-beta/).

## Podman 6 moves container configuration out of /etc

The container stack moves as a unit here — Podman 6.1.0, Buildah 1.45.0, skopeo 1.24.0, crun 1.29.1, and netavark and aardvark-dns 2.1.0 — and `containers-common` 6.0 relocates the vendor defaults from `/etc/containers` to `/usr/share/containers`, adding vendor drop-in configuration for `containers.conf`, `storage.conf` and `registries.conf`.

Anything you placed under `/etc/containers` is preserved on upgrade and still takes precedence. Because the pieces have to move together, the packaging enforces it with hard conflicts against older Podman, Buildah and skopeo.

Upgrades of existing container hosts are the path most worth exercising, rootless setups in particular, since rootful and rootless storage defaults are now separate drop-in files. The full container stack for this release is listed in the [Changelog](https://wiki.almalinux.org/release-notes/10.3-beta.html#changelog) section of the release notes.

If you run containers on AlmaLinux, please put an upgrade through its paces and tell us what you find on the [10 Beta Forum](https://forums.almalinux.org/c/devel/10-beta/).

## What can you do to help?

Your input into testing and feedback is crucial and essential for successful production releases.

Please, report any bugs you may see on the [Bug Tracker](https://bugs.almalinux.org/). Also, join us in the [AlmaLinux Community Chat](https://chat.almalinux.org) and ~testing Channel, post a question on our [10 Beta Forum](https://forums.almalinux.org/c/devel/10-beta/), on our AlmaLinux Community on [Reddit](https://reddit.com/r/almalinux) or catch us on [X](https://twitter.com/almalinux).

Enjoy this Beta release, let us know what you think and stay tuned.

**Happy Testing!**
