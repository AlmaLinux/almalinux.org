---
title: "AlmaLinux OS 10.3 and 9.9 are now available"
type: blog
author:
  name: "Andrew Lukoshko"
  bio: "AlmaLinux Lead Architect and ALESCo Chairman"
  image: /users/alukoshko.jpg
date: "2026-11-16"
images:
  - /blog-images/2026/almalinux99and103stable.png
post:
  title: 'AlmaLinux OS 10.3 "Mauve Lion" and 9.9 "Chartreuse Bobcat" are out today. ModSecurity returns to AlmaLinux 10, Podman 6 arrives with a new configuration layout, and GCC Toolset 16 lands on both versions. Here are the changes to check before you upgrade.'
  image: /blog-images/2026/almalinux99and103stable.png
---

Hello Community! The AlmaLinux OS Foundation is announcing the general availability of [AlmaLinux OS 10.3](https://mirrors.almalinux.org/isos.html) codenamed "Mauve Lion" and [AlmaLinux OS 9.9](https://mirrors.almalinux.org/isos.html) codenamed "Chartreuse Bobcat"!

This is the second time we've shipped both versions on the same day. Thank you to everyone who installed the betas in September and told us what broke. Your reports on the forums, the bug tracker, and in the ~testing channel shaped what ships today.

## AlmaLinux OS 10.3 "Mauve Lion"

AlmaLinux 10.3 (kernel `6.12.0-264.7.1.el10_3`) brings new compiler toolsets, post-quantum cryptography updates, and a major new version of the container tools. It adds GCC Toolset 16, LLVM Toolset 22, Rust 1.97, Go 1.27, and GDB 17.2, and Node.js 26 is available as a preview. Security updates include fapolicyd 2.0, Keylime 7.14, audit 4.2 with post-quantum TLS for remote logging, and libreswan 5.4 with ML-KEM post-quantum key exchange.

### ModSecurity is back

The `mod_security` web application firewall and the OWASP Core Rule Set (CRS) are back in AlmaLinux 10. They shipped in AlmaLinux 8 and 9 but were missing from 10.0 through 10.2.

It's a big version jump. AlmaLinux 9 carries ModSecurity 2.9.6 with CRS 3.3, and 10.3 ships ModSecurity 2.9.14 with CRS 4.22. CRS 4 reorganized the rule set, so if you're bringing rules or tuning over from an AlmaLinux 9 server, plan to review them before you put 10.3 in front of production traffic.

### Podman 6

The container tools move to Podman 6, and the vendor default configuration moves from `/etc/containers` to `/usr/share/containers`. Anything you've put in `/etc/containers` is kept during the upgrade and still takes precedence over the vendor defaults. Rootful and rootless storage settings now live in separate drop-in directories, and you can set defaults for rootless containers in `/etc/containers/containers.rootless.conf.d/` without touching rootful ones.

Podman 6 also removes several older components, so check these before you upgrade a container host:

- CNI networking is gone, and Netavark is the only network backend.
- The BoltDB database backend is gone, and Podman uses SQLite.
- slirp4netns is replaced by pasta for rootless networking.
- cgroups v1 is no longer supported.
- Firewall rules are managed with nftables instead of iptables.

### Still here from earlier 10.x releases

10.3 keeps the things that make AlmaLinux 10 different from upstream: [Btrfs support](/blog/2025-10-21-announcing-btrfs-support-in-almalinux-10-1) including booting from a Btrfs volume, the [CRB repository enabled by default](/blog/2025-09-08-enabling-crb-by-default-for-almalinux10), a parallel [x86_64_v2 build with matching EPEL coverage](/blog/2025-06-26-epel-v2-now-covers-almalinux-10-stable) for older hardware, [i686 userspace packages](/blog/2026-04-16-almalinux-kitten-10-i686) for 32-bit software and CI pipelines, KVM for IBM POWER, frame pointers enabled by default, SPICE support, and the re-enabled storage and network drivers listed in the [Extended hardware support](https://wiki.almalinux.org/release-notes/10.3.html#extended-hardware-support) section of the release notes.

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

## AlmaLinux OS 9.9 "Chartreuse Bobcat"

AlmaLinux 9.9 (kernel `5.14.0-741.11.1.el9_9`) brings GCC Toolset 16 to AlmaLinux 9 alongside the existing GCC Toolset 15, with LLVM Toolset 22, Rust 1.97, Go 1.27, and GDB 17.2. PHP 8.4 arrives as a new module stream, and Node.js 26 is available as a preview module stream. Security updates include fapolicyd 2.0, Keylime 7.14, and opencryptoki 3.27 with ML-DSA and ML-KEM post-quantum key types.

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

Three changes land in both 10.3 and 9.9, and each one can change how an existing system behaves.

**authselect no longer merges groups by default.** If your systems combine group records from more than one source, such as local files and SSSD, enable it again after upgrading with `authselect enable-feature with-group-merging`. Turning it off by default speeds up group lookups on systems that don't need it.

**fapolicyd moves from 1.4 to 2.0.** The file access policy daemon now makes decisions in parallel and updates its policy and trust database as a single transaction. It runs in the path of every program on a hardened system, so please test your existing rules and trust database on a non-production host first.

**GCC Toolset 16 defaults to C++20.** The default C++ standard moves from `gnu++17` to `gnu++20`. If your project isn't ready for that, pass `-std=gnu++17` when you build with the new toolset. The system compiler doesn't change.

## Cloud, container, and live images

We also build cloud, container, and live images for both 10.3 and 9.9. Those builds start as soon as the public repositories are ready, so they'll show up over the next few days.

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
- [Vagrant boxes](https://app.vagrantup.com/almalinux) for Libvirt, VirtualBox, Hyper-V, VMware (x86_64 and AArch64), and Parallels (AArch64)
- [Raspberry Pi](https://wiki.almalinux.org/documentation/raspberry-pi.html)
- [Windows Subsystem for Linux](https://wiki.almalinux.org/documentation/wsl.html) for x86_64 and AArch64

## Recent security fixes included

Both releases include the fixes for the vulnerabilities we've covered on the blog since the betas, so a fresh install of 10.3 or 9.9 is already patched for:

- [PwnEscape (CVE-2026-99999)](/blog/2026-10-16-pwnescape-cve-2026-99999)
- [php2shell (CVE-2026-109618, CVE-2026-109619)](/blog/2026-10-21-php2shell-cve-2026-109618-cve-2026-109619)
- [ZDI-CAN-33367](/blog/2026-10-23-zdi-can-33367)
- [CVE-2026-98432](/blog/2026-10-30-cve-2026-98432)
- [CVE-2026-98276](/blog/2026-11-06-cve-2026-98276)

## Tell us how it goes

Please install it, upgrade a test machine, and tell us what you find. Report bugs on the [Bug Tracker](https://bugs.almalinux.org/), join us in the ~testing channel on the [AlmaLinux Community Chat](https://chat.almalinux.org), or post on the [10.3 Forum](https://forums.almalinux.org/c/devel/10/) or [9.9 Forum](https://forums.almalinux.org/c/devel/9/36). You can also find us on [Reddit](https://reddit.com/r/almalinux) and [X](https://x.com/almalinux).

**Enjoy the releases!**
