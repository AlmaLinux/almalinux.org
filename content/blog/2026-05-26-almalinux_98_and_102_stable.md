---
title: "General Availability of AlmaLinux OS 9.8 and 10.2 Stable!"
type: blog
author:
  name: "Andrew Lukoshko"
  bio: "AlmaLinux Lead Architect and ALESCo Chairman"
  image: /users/alukoshko.jpg
date: "2026-05-26"
images:
  - /blog-images/2026/almalinux98and102stable.png
post:
  title: "General Availability of AlmaLinux OS 9.8 and 10.2 Stable!"
  image: /blog-images/2026/almalinux98and102stable.png
---

# AlmaLinux OS 9.8 and 10.2 Stable Now Available

Hello Community! The AlmaLinux OS Foundation is announcing the general availability of two stable releases at once: [AlmaLinux OS 9.8](https://mirrors.almalinux.org/isos.html) codenamed "Olive Jaguar" and [AlmaLinux OS 10.2](https://mirrors.almalinux.org/isos.html) codenamed "Lavender Lion"!

This is the first time we have ever shipped two AlmaLinux releases on the same day, and it's a milestone we're proud of. It's the direct result of concerted effort by our Build, Core, and Infrastructure SIGs on our release engineering procedures. This work resulted in better automation, tighter QA pipelines, and a build system that can carry two parallel release trains without one slowing the other down.

Shipping both versions is made possible by [the goals we set for 2026](/blog/2026-03-10-almalinux-in-2026), and seeing it land is the proof that the work paid off. The payoff lands with you, too. As a user, you no longer have to wait another week for the second version to be released. Same day, same quality, both versions.

## AlmaLinux OS 9.8 "Olive Jaguar"

AlmaLinux 9.8 (kernel `5.14.0-687.5.3.el9_8`) introduces new compiler toolsets, updated module streams, and improved security. This release adds Python 3.14 as a new package, brings new streams for MariaDB, PostgreSQL, and Ruby, and ships an updated Node.js 24 module stream. Container and virtualization support is updated with the latest versions of Podman, Buildah, libvirt, QEMU-KVM, and skopeo. Security is improved with updates to OpenSSL, OpenSSH, GnuTLS, SELinux policies, and crypto-policies.

AlmaLinux 9.8 also ships an [ALESCo](/blog/2024-05-21-introducing-alesco)-approved kernel backport ahead of upstream: a fix for excessive CPU consumption by `systemd` and `ps` during task cleanup. We originally submitted [the fix](https://github.com/torvalds/linux/commit/d919a1e79bac890421537cf02ae773007bf55e6b) to CentOS Stream 9, but its inclusion was deferred to at least RHEL 9.9 — so ALESCo voted to include it in 9.8 now. If you've been seeing that CPU spike during task cleanup, it's fixed today instead of a quarter from now.

Installation ISOs are available on the mirrors now for all 4 architectures:

- [Intel/AMD (x86_64)](https://mirrors.almalinux.org/isos/x86_64/9.8.html)
- [ARM64 (aarch64)](https://mirrors.almalinux.org/isos/aarch64/9.8.html)
- [IBM PowerPC (ppc64le)](https://mirrors.almalinux.org/isos/ppc64le/9.8.html)
- [IBM Z (s390x)](https://mirrors.almalinux.org/isos/s390x/9.8.html)

Torrents are available as well at:

- [Intel/AMD (x86_64)](https://repo.almalinux.org/almalinux/9.8/isos/x86_64/AlmaLinux-9.8-x86_64.torrent)
- [ARM64 (aarch64)](https://repo.almalinux.org/almalinux/9.8/isos/aarch64/AlmaLinux-9.8-aarch64.torrent)
- [IBM PowerPC (ppc64le)](https://repo.almalinux.org/almalinux/9.8/isos/ppc64le/AlmaLinux-9.8-ppc64le.torrent)
- [IBM Z (s390x)](https://repo.almalinux.org/almalinux/9.8/isos/s390x/AlmaLinux-9.8-s390x.torrent)

You can read the full release notes for this version on the wiki: [AlmaLinux OS 9.8 Release Notes](https://wiki.almalinux.org/release-notes/9.8.html).

## AlmaLinux OS 10.2 "Lavender Lion"

AlmaLinux 10.2 (kernel `6.12.0-211.7.3.el10_2`) introduces updated compiler toolsets, new language and database packages, and improved security. This release adds Python 3.14, PostgreSQL 18, MariaDB 11.8, Ruby 4.0, and PHP 8.4 as new packages, alongside SDL3, libkrun, trustee, and FIDO Device Onboard tooling. The desktop sees GNOME 49. Container and virtualization support is updated with the latest versions of Podman, Buildah, libvirt, QEMU-KVM, and skopeo. Security is improved with updates to OpenSSL, OpenSSH, SSSD, SELinux policies, crypto-policies, and Keylime.

AlmaLinux 10.2 also brings i686 userspace packages — enabling legacy 32-bit software, CI pipelines, and containerized workloads on AlmaLinux 10. We [first landed i686 in Kitten 10 back in April](/blog/2026-04-16-almalinux-kitten-10-i686); 10.2 is where it crosses into stable.

10.2 continues to ship AlmaLinux's deviations from upstream that we've written about before: [Btrfs support](/blog/2025-10-21-announcing-btrfs-support-in-almalinux-10-1) including the ability to boot from a Btrfs volume, the [CRB repository enabled by default](/blog/2025-09-08-enabling-crb-by-default-for-almalinux10), and a parallel [x86_64_v2 build with matching EPEL coverage](/blog/2025-06-26-epel-v2-now-covers-almalinux-10-stable) for older hardware.

New in this release: KVM for IBM POWER is fully enabled in the virtualization stack (graduating from the [9.6 tech preview](/blog/2025-05-20-almalinux_96_release)), frame pointers are re-enabled by default so system-wide profiling works out of the box, SPICE support is back for both server and client applications, and Firefox and Thunderbird ship as regular RPMs in the system repositories. 10.2 also re-adds a long list of older storage and networking drivers (Adaptec, Dell PERC, HP, Mellanox, QLogic, Emulex, LSI, Broadcom) that upstream had disabled — see the release notes' [Extended hardware support](https://wiki.almalinux.org/release-notes/10.2.html#extended-hardware-support) section for the full table.

Installation ISOs are available on the mirrors now for all supported architectures:

- [Intel/AMD (x86_64)](https://mirrors.almalinux.org/isos/x86_64/10.2.html)
- [Intel/AMD (x86_64_v2)](https://mirrors.almalinux.org/isos/x86_64_v2/10.2.html)
- [ARM64 (aarch64)](https://mirrors.almalinux.org/isos/aarch64/10.2.html)
- [IBM PowerPC (ppc64le)](https://mirrors.almalinux.org/isos/ppc64le/10.2.html)
- [IBM Z (s390x)](https://mirrors.almalinux.org/isos/s390x/10.2.html)

Torrents are available as well at:

- [Intel/AMD (x86_64)](https://repo.almalinux.org/almalinux/10.2/isos/x86_64/AlmaLinux-10.2-x86_64.torrent)
- [Intel/AMD (x86_64_v2)](https://repo.almalinux.org/almalinux/10.2/isos/x86_64_v2/AlmaLinux-10.2-x86_64_v2.torrent)
- [ARM64 (aarch64)](https://repo.almalinux.org/almalinux/10.2/isos/aarch64/AlmaLinux-10.2-aarch64.torrent)
- [IBM PowerPC (ppc64le)](https://repo.almalinux.org/almalinux/10.2/isos/ppc64le/AlmaLinux-10.2-ppc64le.torrent)
- [IBM Z (s390x)](https://repo.almalinux.org/almalinux/10.2/isos/s390x/AlmaLinux-10.2-s390x.torrent)

You can read the full release notes for this version on the wiki: [AlmaLinux OS 10.2 Release Notes](https://wiki.almalinux.org/release-notes/10.2.html).

## ISOs, Live Images, Cloud and Containers

AlmaLinux also offers a variety of Cloud, Container and Live Images for both 9.8 and 10.2. The builds for these get kicked off as soon as the public repositories are ready.

**The following images are expected to be available shortly.**

- [Container](https://wiki.almalinux.org/containers/) images including Platform and UBI alternatives. We provide a wide variety of containers for your use.
- [LXC/LXD](https://images.linuxcontainers.org/images/almalinux/)
- [Live Media](https://wiki.almalinux.org/LiveMedia.html) for GNOME, GNOME-mini, KDE, XFCE, MATE and more.
- Cloud Images
  - [AWS](https://wiki.almalinux.org/cloud/AWS.html) for x86_64 and AArch64 EC2 Instances
  - [Azure](https://wiki.almalinux.org/cloud/Azure.html) for x86_64 and AArch64 VMs
  - [Google Cloud](https://wiki.almalinux.org/cloud/Google.html)
  - [Generic Cloud/Cloud-init](https://wiki.almalinux.org/cloud/Generic-cloud-on-local.html) for all supported architectures including x86_64_v2
  - [OpenNebula](https://wiki.almalinux.org/cloud/OpenNebula.html) for x86_64 and AArch64 architectures
  - [Oracle Cloud Infrastructure](https://wiki.almalinux.org/cloud/OCI.html) for x86_64 and AArch64 Instances
- [Vagrant Boxes](https://app.vagrantup.com/almalinux):
  - Libvirt
  - VirtualBox
  - Hyper-V
  - VMWare for x86_64 and AArch64
  - Parallels for AArch64
- [Raspberry Pi](https://wiki.almalinux.org/documentation/raspberry-pi.html)
- [Windows Subsystem for Linux](https://wiki.almalinux.org/documentation/wsl.html) for x86_64 and AArch64

## Recent CVE patches included

Both 9.8 and 10.2 ship with patches for the run of high-profile CVEs we've covered on the blog over the last month, so if you're installing fresh or upgrading as-yet-unpactched versions of 9.7 or 10.1, you'll get these alongside the rest of the release:

- [Copy Fail (CVE-2026-31431)](/blog/2026-05-01-cve-2026-31431-copy-fail)
- [Dirty FRAG](/blog/2026-05-07-dirty-frag)
- [Fragnesia (CVE-2026-46300)](/blog/2026-05-13-fragnesia-cve-2026-46300)
- [nginx Rift (CVE-2026-42945)](/blog/2026-05-13-nginx-rift-cve-2026-42945)
- [SSH Keysign Pwn (CVE-2026-46333)](/blog/2026-05-15-ssh-keysign-pwn-cve-2026-46333)

## What can you do to help?

Your input into testing and feedback is crucial and essential for successful production releases. Thanks to everyone who has helped us with testing, especially in the last month!

Please, report any bugs you may see on the [Bug Tracker](https://bugs.almalinux.org/). Also, pop into the [AlmaLinux Community Chat](https://chat.almalinux.org) and join our Testing Channel, post a question on our [9.8 Forum](https://forums.almalinux.org/c/devel/9/36) or [10.2 Forum](https://forums.almalinux.org/c/devel/10/), on our AlmaLinux Community on [Reddit](https://reddit.com/r/almalinux) or catch us on [X](https://x.com/almalinux).

Please report any bugs you may see on the [Bug Tracker](https://bugs.almalinux.org/).

**Enjoy the releases and have fun!**
