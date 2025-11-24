---
title: "General Availability of AlmaLinux OS 10.1 Stable!"
type: blog
author:
  name: "Eduard Abdullin"
  bio: "The Release and Automation Engineer."
  image: /users/eduard-abdullin.jpg
date: "2025-11-24"
images:
  - /blog-images/2025/almalinux101stable.png
post:
  title: "General Availability of AlmaLinux OS 10.1 Stable!"
  image: /blog-images/2025/almalinux101stable.png
---

# AlmaLinux OS 10.1 Stable Now Available

Hello Community! The AlmaLinux OS Foundation is announcing the general availability of [AlmaLinux OS 10.1](https://mirrors.almalinux.org/isos.html) codenamed "Heliotrope Lion"!

Installation ISOs are available on the mirrors now for all architectures:

- [Intel/AMD (x86_64)](https://mirrors.almalinux.org/isos/x86_64/10.1.html)
- [Intel/AMD (x86_64_v2)](https://mirrors.almalinux.org/isos/x86_64_v2/10.1.html)
- [ARM64 (aarch64)](https://mirrors.almalinux.org/isos/aarch64/10.1.html)
- [IBM PowerPC (ppc64le)](https://mirrors.almalinux.org/isos/ppc64le/10.1.html)
- [IBM Z (s390x)](https://mirrors.almalinux.org/isos/s390x/10.1.html)

Torrents are available as well at:

- [Intel/AMD (x86_64)](https://repo.almalinux.org/almalinux/10.1/isos/x86_64/AlmaLinux-10.1-x86_64.torrent)
- [Intel/AMD (x86_64_v2)](https://repo.almalinux.org/almalinux/10.1/isos/x86_64_v2/AlmaLinux-10.1-x86_64.torrent)
- [ARM64 (aarch64)](https://repo.almalinux.org/almalinux/10.1/isos/aarch64/AlmaLinux-10.1-aarch64.torrent)
- [IBM PowerPC (ppc64le)](https://repo.almalinux.org/almalinux/10.1/isos/ppc64le/AlmaLinux-10.1-ppc64le.torrent)
- [IBM Z (s390x)](https://repo.almalinux.org/almalinux/10.1/isos/s390x/AlmaLinux-10.1-s390x.torrent)

## ISOs, Live Images, Cloud and Containers

AlmaLinux also offers a variety of Cloud, Container and Live Images. The builds for these get kicked off as soon as the public repository is ready.

**The following images are expected to be available shortly.**

- [Container](https://wiki.almalinux.org/containers/) images including Platform and UBIs alternatives. We provide a wide variety of containers for your use.
- [LXC/LXD](https://images.linuxcontainers.org/images/almalinux/)
- [Live Media](https://wiki.almalinux.org/LiveMedia.html)
- Cloud Images
  - [AWS](https://wiki.almalinux.org/cloud/AWS.html) for x86_64 and AArch64 EC2 Instances
  - [Azure](https://wiki.almalinux.org/cloud/Azure.html) for x86_64 and AArch64 VMs
  - [Google Cloud](https://wiki.almalinux.org/cloud/Google.html)
  - [Generic Cloud/Cloud-init](https://wiki.almalinux.org/cloud/Generic-cloud-on-local.html) for all supported architectures including x86-64-v2
  - [OpenNebula](https://wiki.almalinux.org/cloud/OpenNebula.html) for x86_64 and AArch64 architectures
  - [Oracle Cloud Infrastructure](https://wiki.almalinux.org/cloud/OCI.html) for x86_64 and AArch64 Instances
- [Vagrant Boxes](https://app.vagrantup.com/almalinux):
  - Libvirt
  - VirtualBox
  - Hyper-V
  - VMWare
- [Raspberry Pi](https://wiki.almalinux.org/documentation/raspberry-pi.html)
- [Windows Subsystem for Linux](https://wiki.almalinux.org/documentation/wsl.html) for x86_64 and AArch64

## Btrfs Support

AlmaLinux 10.1 also [includes support for the Btrfs filesystem](/blog/2025-10-21-announcing-btrfs-support-in-almalinux-10-1), which has already been available in AlmaLinux OS Kitten since early September. Btrfs support encompasses both kernel and userspace enablement, and it is now possible to install AlmaLinux OS on a Btrfs filesystem from the very beginning. Initial enablement was scoped to the installer and storage management stack, and broader support within the AlmaLinux software collection for Btrfs features is forthcoming.

## Other Improvements 

In addition to Btrfs support, AlmaLinux OS 10.1 includes numerous other improvements to serve our community. We have continued to extend hardware support both by [adding drivers](https://wiki.almalinux.org/release-notes/10.1.html#extended-hardware-support) and by adding a secondary version of AlmaLinux OS and [EPEL](/blog/2025-06-26-epel-v2-now-covers-almalinux-10-stable/) to extend support of x86_64_v2 processors. 

We have also re-enabled SPICE support and Re-enabled frame pointers by default. We have continued our enablement of KVM for IBM POWER in the virtualization stack, and are [enabling the CRB repository](https://almalinux.org/blog/2025-09-08-enabling-crb-by-default-for-almalinux10/) by default for new AlmaLinux OS installations.

The full list of improvements. can be found in the [AlmaLinux OS 10.1 Release Notes](https://wiki.almalinux.org/release-notes/10.1.html). 

## Release Notes and More Information

AlmaLinux 10.1 introduces performance enhancements, updated development tools, and improved security. This release delivers new compiler toolsets and updated module streams, along with improvements to debugging and networking tools. Container and virtualization support is enhanced with the latest versions of Podman and Buildah. Security is improved with updated SELinux policies, OpenSSL featuring post-quantum cryptography support, and newer versions of SSSD and Keylime.

You can read the full release notes for this version on the wiki: [AlmaLinux OS 10.1 Release Notes](https://wiki.almalinux.org/release-notes/10.1.html).

## What can you do to help?

Your input into testing and feedback is crucial and essential for successful production releases.
Please, report any bugs you may see on the [Bug Tracker](https://bugs.almalinux.org/). Also, pop into the [AlmaLinux Community Chat](https://chat.almalinux.org) and join our Testing Channel, post a question on our [10.1 Forum](https://forums.almalinux.org/), on our AlmaLinux Community on [Reddit](https://reddit.com/r/almalinux) or catch us on [X](https://x.com/almalinux).

Please report any bugs you may see on the [Bug Tracker](https://bugs.almalinux.org/).

**Enjoy the release and have fun!**
