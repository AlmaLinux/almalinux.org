---
title: "AlmaLinux 10.1 Beta Now Available!"
type: blog
author:
  name: "Eduard Abdullin"
  bio: "The Release and Automation Engineer."
  image: /users/eduard-abdullin.jpg
date: "2025-10-21"
images:
  - /blog-images/2025/2025-10-21-10-1-beta.png
post:
  title: "AlmaLinux 10.1 Beta Now Available!"
  image: /blog-images/2025/2025-10-21-10-1-beta.png
---

Hello Community!

The AlmaLinux OS Foundation is announcing the availability of AlmaLinux 10.1 Beta "Heliotrope Lion" for all supported architectures:

- Intel/AMD (x86_64)
- Intel/AMD (x86_64_v2)
- ARM64 (aarch64)
- IBM PowerPC (ppc64le)
- IBM Z (s390x)

Beta ISOs are available at [repo.almalinux.org](https://repo.almalinux.org/almalinux/10.1-beta/isos/).

A usual reminder: this is a **BETA** release. It should not be used for production installations. The provided upgrade instructions should not be used on production machines unless you don't mind if something breaks. If you are looking to see how things going to work in stable, you are on the right track.

## Release Notes and More Information

AlmaLinux 10.1 Beta now supports the Btrfs filesystem, which has already been available in AlmaLinux OS Kitten since 2025-09-10. Btrfs support encompasses both kernel and userspace enablement, and it is now possible to install AlmaLinux OS on a Btrfs filesystem from the very beginning. Initial enablement was scoped to the installer and storage management stack, and broader support within the AlmaLinux software collection for Btrfs features is forthcoming.

AlmaLinux 10.1 Beta also brings performance improvements, updated developer toolsets, and includes the latest GCC, LLVM, and Rust versions. This release also introduces updates to debugging and networking utilities for smoother and more efficient performance. Container and virtualization support deliver new versions of Podman, Buildah, Libvirt, and QEMU-KVM. Security is improved with updated SELinux policies, OpenSSL, and SSSD to keep your systems safe, stable, and reliable.

You can read the full release notes for this version on the wiki: [AlmaLinux OS 10.1 Beta Release Notes](https://wiki.almalinux.org/release-notes/10.1-beta.html).

## What you can do to help?

Your input into testing and feedback is crucial and essential for successful production releases.
Please, report any bugs you may see on the [Bug Tracker](https://bugs.almalinux.org/). Also, join us in the [AlmaLinux Community Chat](https://chat.almalinux.org) and ~testing Channel, post a question on our [10.1 Beta Forum](https://forums.almalinux.org/c/devel/10-beta/42), on our AlmaLinux Community on [Reddit](https://reddit.com/r/almalinux) or catch us on [X](https://twitter.com/almalinux).

Enjoy this Beta release, let us know what you think and stay tuned.

**Happy Testing!**
