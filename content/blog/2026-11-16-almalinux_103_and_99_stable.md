---
title: "AlmaLinux OS 10.3 and 9.9 are now available"
type: blog
author:
  name: "Andrew Lukoshko"
  bio: "AlmaLinux Lead Architect and ALESCo Member"
  image: /users/alukoshko.jpg
date: "2026-11-16"
description: 'AlmaLinux OS 10.3 "Mauve Lion" and 9.9 "Chartreuse Bobcat" were released on November 16, 2026, with ModSecurity, Podman 6, and GCC Toolset 16.'
images:
  - /blog-images/2026/almalinux99and103stable.png
post:
  title: 'AlmaLinux OS 10.3 "Mauve Lion" and 9.9 "Chartreuse Bobcat" are out today. AlmaLinux 10 gets ModSecurity back and moves to Podman 6. Both versions add GCC Toolset 16, and both kernels include security fixes that would otherwise have been lost on upgrade. Here are the changes to check before you upgrade.'
  image: /blog-images/2026/almalinux99and103stable.png
---

Hello Community! The AlmaLinux OS Foundation is announcing the general availability of [AlmaLinux OS 10.3](https://mirrors.almalinux.org/isos.html) codenamed "Mauve Lion" and [AlmaLinux OS 9.9](https://mirrors.almalinux.org/isos.html) codenamed "Chartreuse Bobcat"!

Thank you to everyone who tested the [10.3 beta](/blog/2026-09-10-announcing-103-beta) and [9.9 beta](/blog/2026-09-17-announcing-99-beta).

## Release highlights

AlmaLinux OS 10.3 "Mauve Lion":

- Released: November 16, 2026
- Kernel: `6.12.0-264.16.1.el10_3`
- Compatible with: Red Hat Enterprise Linux (RHEL) 10.3
- Architectures: x86_64, x86_64_v2, aarch64, ppc64le, s390x, i686 userspace
- What's new:
  - ModSecurity returns (2.9.14 with OWASP CRS 4.22.0)
  - Podman 6.1.1, with container configuration moved to /usr/share/containers
  - GCC Toolset 16
  - Node.js 26.12.1
  - .NET 11 (preview)

AlmaLinux OS 9.9 "Chartreuse Bobcat":

- Released: November 16, 2026
- Kernel: `5.14.0-741.22.1.el9_9`
- Compatible with: Red Hat Enterprise Linux (RHEL) 9.9
- Architectures: x86_64, aarch64, ppc64le, s390x
- What's new:
  - GCC Toolset 16
  - fapolicyd 2.0.1
  - authselect group merging is now opt-in
  - .NET 11
  - Node.js 26

## AlmaLinux OS 10.3 "Mauve Lion" {#10-3}

AlmaLinux 10.3 (kernel `6.12.0-264.16.1.el10_3`) adds GCC Toolset 16, LLVM Toolset 22, Rust 1.97, Go 1.27, GDB 17.2, and Node.js 26. Security updates include fapolicyd 2.0, Keylime 7.14, audit 4.2 with post-quantum TLS for remote logging, and libreswan 5.4 with ML-KEM post-quantum key exchange.

### ModSecurity is back

The `mod_security` web application firewall and the OWASP Core Rule Set (CRS) are back in AlmaLinux 10. They shipped in AlmaLinux 8 and 9 but were not included in 10.0 through 10.2.

This release is a big version bump. AlmaLinux 9 ships ModSecurity 2.9.6 with CRS 3.3, and 10.3 ships ModSecurity 2.9.14 with CRS 4.22. CRS 4 reorganized the rule set, so if you're bringing rules or tuning over from an AlmaLinux 9 server, plan to review them before you put 10.3 in front of production traffic.

### Podman 6

The container tools move to Podman 6, and the vendor default configuration moves from `/etc/containers` to `/usr/share/containers`. Anything you've put in `/etc/containers` is kept during the upgrade and still takes precedence over the vendor defaults. Rootful and rootless storage settings now live in separate drop-in directories, and you can set defaults for rootless containers in `/etc/containers/containers.rootless.conf.d/` without touching rootful ones.

Podman 6 also removes several older components, so check these before you upgrade a container host:

- CNI networking is gone, and Netavark is the only network backend.
- The BoltDB database backend is gone, and Podman uses SQLite.
- slirp4netns is replaced by pasta for rootless networking.
- cgroups v1 is no longer supported.
- Firewall rules are managed with nftables instead of iptables.

### Still here from earlier 10.x releases

These AlmaLinux 10 features from earlier releases are still in 10.3:

- [Btrfs support](/blog/2025-10-21-announcing-btrfs-support-in-almalinux-10-1), including booting from a Btrfs volume
- The [CRB repository enabled by default](/blog/2025-09-08-enabling-crb-by-default-for-almalinux10)
- A parallel [x86_64_v2 build with matching EPEL coverage](/blog/2025-06-26-epel-v2-now-covers-almalinux-10-stable) for older hardware
- [i686 userspace packages](/blog/2026-04-16-almalinux-kitten-10-i686) for 32-bit software and CI pipelines
- KVM for IBM POWER, frame pointers enabled by default, and SPICE support
- Storage and network drivers that upstream disabled, listed in the [Extended hardware support](https://wiki.almalinux.org/release-notes/10.3.html#extended-hardware-support) section of the release notes

Installation ISOs are available on the mirrors now for all supported architectures:

- [Intel/AMD (x86_64)](https://mirrors.almalinux.org/isos/x86_64/10.3.html)
- [Intel/AMD (x86_64_v2)](https://mirrors.almalinux.org/isos/x86_64_v2/10.3.html)
- [ARM64 (aarch64)](https://mirrors.almalinux.org/isos/aarch64/10.3.html)
- [IBM PowerPC (ppc64le)](https://mirrors.almalinux.org/isos/ppc64le/10.3.html)
- [IBM Z (s390x)](https://mirrors.almalinux.org/isos/s390x/10.3.html)

Torrents are available as well:

- [Intel/AMD (x86_64)](https://repo.almalinux.org/almalinux/10.3/isos/x86_64/AlmaLinux-10.3-x86_64.torrent)
- [Intel/AMD (x86_64_v2)](https://repo.almalinux.org/almalinux/10.3/isos/x86_64_v2/AlmaLinux-10.3-x86_64_v2.torrent)
- [ARM64 (aarch64)](https://repo.almalinux.org/almalinux/10.3/isos/aarch64/AlmaLinux-10.3-aarch64.torrent)
- [IBM PowerPC (ppc64le)](https://repo.almalinux.org/almalinux/10.3/isos/ppc64le/AlmaLinux-10.3-ppc64le.torrent)
- [IBM Z (s390x)](https://repo.almalinux.org/almalinux/10.3/isos/s390x/AlmaLinux-10.3-s390x.torrent)

You can read the full release notes on the wiki: [AlmaLinux OS 10.3 Release Notes](https://wiki.almalinux.org/release-notes/10.3.html).

## AlmaLinux OS 9.9 "Chartreuse Bobcat" {#9-9}

AlmaLinux 9.9 (kernel `5.14.0-741.22.1.el9_9`) adds GCC Toolset 16, LLVM Toolset 22, Rust 1.97, Go 1.27, and GDB 17.2. GCC Toolset 15 is still available. PHP 8.4 and Node.js 26 are new module streams. Security updates include fapolicyd 2.0, Keylime 7.14, and opencryptoki 3.27 with ML-DSA and ML-KEM post-quantum key types.

AlmaLinux 9.9 also keeps the [ALESCo](/blog/2024-05-21-introducing-alesco)-approved kernel fix we first shipped in 9.8, which stops `systemd` and `ps` from using excessive CPU during task cleanup. Upstream hasn't picked it up for 9.9, so we're continuing to carry it.

Installation ISOs are available on the mirrors now for all 4 architectures:

- [Intel/AMD (x86_64)](https://mirrors.almalinux.org/isos/x86_64/9.9.html)
- [ARM64 (aarch64)](https://mirrors.almalinux.org/isos/aarch64/9.9.html)
- [IBM PowerPC (ppc64le)](https://mirrors.almalinux.org/isos/ppc64le/9.9.html)
- [IBM Z (s390x)](https://mirrors.almalinux.org/isos/s390x/9.9.html)

Torrents are available as well:

- [Intel/AMD (x86_64)](https://repo.almalinux.org/almalinux/9.9/isos/x86_64/AlmaLinux-9.9-x86_64.torrent)
- [ARM64 (aarch64)](https://repo.almalinux.org/almalinux/9.9/isos/aarch64/AlmaLinux-9.9-aarch64.torrent)
- [IBM PowerPC (ppc64le)](https://repo.almalinux.org/almalinux/9.9/isos/ppc64le/AlmaLinux-9.9-ppc64le.torrent)
- [IBM Z (s390x)](https://repo.almalinux.org/almalinux/9.9/isos/s390x/AlmaLinux-9.9-s390x.torrent)

You can read the full release notes on the wiki: [AlmaLinux OS 9.9 Release Notes](https://wiki.almalinux.org/release-notes/9.9.html).

## Changes to check before you upgrade either version

These changes apply to both 10.3 and 9.9.

**authselect no longer merges groups by default.** If your systems combine group records from more than one source, such as local files and SSSD, enable it again after upgrading with `authselect enable-feature with-group-merging`. Turning it off by default speeds up group lookups on systems that don't need it.

**fapolicyd moves from 1.4 to 2.0.** The file access policy daemon now makes decisions in parallel and updates its policy and trust database as a single transaction. It runs in the path of every program on a hardened system, so please test your existing rules and trust database on a non-production host first.

**GCC Toolset 16 defaults to C++20.** The default C++ standard moves from `gnu++17` to `gnu++20`. If your project isn't ready for that, pass `-std=gnu++17` when you build with the new toolset. The system compiler doesn't change.

## Cloud, container, and live images

Live Media, Generic Cloud, and OpenNebula images for 10.3 and 9.9 are available now, and the rest of the images below will be out later today. The Raspberry Pi images will follow shortly.

- [Container](https://wiki.almalinux.org/containers/) images, including Platform and UBI alternatives
- [LXC/LXD](https://images.linuxcontainers.org/images/almalinux/)
- [Live Media](https://wiki.almalinux.org/LiveMedia.html) for GNOME, GNOME-mini, KDE, XFCE, MATE and more
- Cloud images
  - [AWS](https://wiki.almalinux.org/cloud/AWS.html) for x86_64 and AArch64 EC2 instances
  - [Azure](https://wiki.almalinux.org/cloud/Azure.html) for x86_64 and AArch64 VMs
  - [Google Cloud](https://wiki.almalinux.org/cloud/Google.html)
  - [Generic Cloud/Cloud-init](https://wiki.almalinux.org/cloud/Generic-cloud-on-local.html) for all supported architectures including x86_64_v2
  - [OpenNebula](https://wiki.almalinux.org/cloud/OpenNebula.html) for x86_64 and AArch64
  - [Oracle Cloud Infrastructure](https://wiki.almalinux.org/cloud/OCI.html) for x86_64 and AArch64 instances
- [Vagrant boxes](https://vagrant.almalinux.org) for libvirt, VirtualBox, VMware, and Hyper-V on x86_64 (plus an x86_64_v2 box for 10.3), and VirtualBox, VMware, and Parallels on AArch64, now served from [our own catalog](/blog/2026-11-02-vagrant-catalog)
- [Raspberry Pi](https://wiki.almalinux.org/documentation/raspberry-pi.html)
- [Windows Subsystem for Linux](https://wiki.almalinux.org/documentation/wsl.html) for x86_64 and AArch64

## Security fixes included

Both releases include the fixes for the vulnerabilities we've covered on the blog since the betas:

- [PwnEscape (CVE-2026-99999)](/blog/2026-10-16-pwnescape-cve-2026-99999)
- [php2shell (CVE-2026-109618, CVE-2026-109619)](/blog/2026-10-21-php2shell-cve-2026-109618-cve-2026-109619)
- [ZDI-CAN-33367](/blog/2026-10-23-zdi-can-33367)
- [CVE-2026-98432](/blog/2026-10-30-cve-2026-98432)
- [CVE-2026-98276](/blog/2026-11-06-cve-2026-98276)

When we compared the new kernels with the last 9.8 and 10.2 kernels, we found security patches included in 9.8 and 10.2, but missing in these releases. The last RHEL 9.8 kernel had fixes for 43 CVEs that aren't in the RHEL 9.9 kernel, and the last RHEL 10.2 kernel had fixes for 30 CVEs that aren't in the RHEL 10.3 kernel. We don't know why they were left out, and we didn't want updating to bring those vulnerabilities back, so we added the fixes back into both AlmaLinux kernels.

Both kernels also include fixes that the community asked us for and that have never been in RHEL, including the CVE-2026-98276 fix listed above. That's 1 additional CVE on 9.9 and 6 on 10.3. In total, the AlmaLinux 9.9 kernel carries fixes for 44 CVEs that RHEL 9.9 doesn't have yet, and the AlmaLinux 10.3 kernel carries fixes for 36.

Every CVE is listed with its score and a short description in the release notes for [9.9](https://wiki.almalinux.org/release-notes/9.9.html#kernel-security-fixes-not-available-in-rhel-9-9) and [10.3](https://wiki.almalinux.org/release-notes/10.3.html#kernel-security-fixes-not-available-in-rhel-10-3).

## Tell us how it goes

Please install it, upgrade a test machine, and tell us what you find. Report bugs on the [Bug Tracker](https://bugs.almalinux.org/), talk to us in [AlmaLinux Community Chat](https://chat.almalinux.org), or post on the [10.3 Forum](https://forums.almalinux.org/c/devel/10-beta/42) or [9.9 Forum](https://forums.almalinux.org/c/devel/9-stable/36). You can also find us on [Reddit](https://reddit.com/r/almalinux) and [X](https://x.com/almalinux).

**Enjoy the releases!**
