---
title: "AlmaLinux OS 10 - usability without compromising compatibility"
type: blog
author:
 name: "Eduard Abdullin"
 bio: "Release and Automation Engineer"
 image: /users/eduard-abdullin.jpg
date: '2025-05-22'
images:
  - /blog-images/2025/almalinux10.png
post:
    title: "Read more about how AlmaLinux OS 10 is the perfect marriage of maintaining compatibility and serving our community!"
    image: /blog-images/2025/almalinux10.png

---

# AlmaLinux OS 10.0 Stable Now Available 

The AlmaLinux OS Foundation is proud to announce the general availability of [AlmaLinux OS 10.0](https://mirrors.almalinux.org/isos.html) codenamed "Purple Lion"!

# AlmaLinux OS Improvements - usability without compromising compatibility

The goal of AlmaLinux OS is to support our community, and AlmaLinux OS 10 is the best example of that yet. With an unwavering eye on maintaining compatibility with Red Hat Enterprise Linux (RHEL), we have made small improvements to AlmaLinux OS 10 that target specific sections of our userbase. They are for users who require them and know how to use them. Anyone using AlmaLinux OS and anticipating RHEL compatibility is in safe hands and won't be disappointed. 

Like we discussed before, AlmaLinux OS 10.0 has been built from our brand new upstream, AlmaLinux OS Kitten. If you have been watching the discussions that ALESCo has been having, you'll know that Kitten brought with it a ton of new things that our community needs. 

## Supporting developers by enabling frame pointers
For software developers, frame pointers are critical to diagnosing and optimizing their applications. For those developers that use AlmaLinux as their base, the lack of frame pointers by default is a pain point - one that we are happy to help ease. 

With AlmaLinux OS 10 we are enabling frame pointers by default. This allows system-wide real-time tracing and profiling for optimizing the performance of any workload running on AlmaLinux. 

## Extended x86-64-v2 life
Within the [x86-64](https://en.wikipedia.org/wiki/X86-64) architecture, there are versions that represent specific CPU feature sets. With RHEL 10, Red Hat will only support x86-64-v3 and higher, which leaves numerous completely functional CPUs without support in the Enterprise Linux ecosystem. 

AlmaLinux OS 10 has followed Red Hat’s decision to ship x86-64-v3 optimized binaries by default, but we will also provide an additional x86-64-v2 architecture, allowing users on that older hardware to continue to receive security updates for another 10 years.

### Extending the life of EPEL for x86-64-v2
By default, EPEL follows Red Hat's builds, which means that all 3rd party packages for RHEL10 will be built for x86-64-v3. [As we announced last week](https://almalinux.org/blog/2025-05-13-epel-10-kitten-v2/) on our blog, we are happy to share that we are building EPEL packages to support users in their adoption of our x86-64-v2 release of AlmaLinux OS 10.  

## Secure Boot for ARM platforms
Trusted boot has long been required for bare metal devices, and is also becoming more and more popular in virtualized environments. AlmaLinux OS Kitten 10 supports Secure Boot for Intel/AMD and ARM platforms.

## Adding SPICE
Simple Protocol for Independent Computing Environments (SPICE) has been unsupported since RHEL 9.0. AlmaLinux users requested we add support back in, so SPICE support is fully re-enabled in AlmaLinux OS 10, for both server and client applications.

## Tech Preview of KVM for IBM POWER
AlmaLinux OS 10.0 also includes a tech-preview of KVM virtualization support for the IBM Power architecture. It has been unavailable upstream since version 9.0, but is fundamental for a number of AlmaLinux users. That list includes the [Oregon State University Open Source Lab](https://osuosl.org/), who submitted the [RFC to the AlmaLinux Engineering Steering Committee](https://github.com/AlmaLinux/ALESCo/blob/master/rfcs/0002-enable-kvm-on-almaLinux-9-on-ppc64le.md) for consideration in February.

### Continuing our expanded hardware support
Starting with AlmaLinux 8.10 and 9.4 we re-enabled support for more than 150 devices that were removed upstream. Those additions continue in AlmaLinux OS 10.0. You can see the full list of devices in the [AlmaLinux OS 10.0 release notes](https://wiki.almalinux.org/release-notes/).

## ISOs, Live Images, Cloud and Containers

AlmaLinux also offers a variety of Cloud, Container and Live Images. The builds for these get kicked off as soon as the public repository is ready. 

Installation ISOs are available on the mirrors now for all architectures:
* [Intel/AMD (x86-64)](https://mirrors.almalinux.org/isos/x86_64/10.0.html)
* [Intel/AMD (x86-64-v2)](https://mirrors.almalinux.org/isos/x86_64_v2/10.0.html)
* [ARM64 (aarch64)](https://mirrors.almalinux.org/isos/aarch64/10.0.html)
* [IBM PowerPC (ppc64le)](https://mirrors.almalinux.org/isos/ppc64le/10.0.html)
* [IBM Z (s390x)](https://mirrors.almalinux.org/isos/s390x/10.0.html)

Torrents are available as well at:
* [Intel/AMD (x86-64)](https://repo.almalinux.org/almalinux/10.0/isos/x86_64/AlmaLinux-10.0-x86_64.torrent)
* [Intel/AMD (x86-64-v2)](https://repo.almalinux.org/almalinux/10.0/isos/x86_64_v2/AlmaLinux-10.0-x86_64_v2.torrent)
* [ARM64 (aarch64)](https://repo.almalinux.org/almalinux/10.0/isos/aarch64/AlmaLinux-10.0-aarch64.torrent)
* [IBM PowerPC (ppc64le)](https://repo.almalinux.org/almalinux/10.0/isos/ppc64le/AlmaLinux-10.0-ppc64le.torrent)
* [IBM Z (s390x)](https://repo.almalinux.org/almalinux/10.0/isos/s390x/AlmaLinux-10.0-s390x.torrent)

**The following images are expected to be available shortly.** 

* [Container](https://wiki.almalinux.org/containers/) images including Platform and UBIs alternatives. We provide a wide variety of containers for your use. 
* [LXC/LXD](https://images.linuxcontainers.org/images/almalinux/) 
* [Live Media](https://wiki.almalinux.org/LiveMedia.html) for GNOME, GNOME-mini, KDE, XFCE, MATE.
* Cloud Images 
    * [AWS](https://wiki.almalinux.org/cloud/AWS.html) for x86_64 and AArch64 EC2 Instances
    * [Azure](https://wiki.almalinux.org/cloud/Azure.html) for x86_64 and AArch64 VMs
    * [Google Cloud](https://wiki.almalinux.org/cloud/Google.html)
    * [Generic Cloud/Cloud-init](https://wiki.almalinux.org/cloud/Generic-cloud-on-local.html) for all supported architectures including x86-64-v2
    * [OpenNebula](https://wiki.almalinux.org/cloud/OpenNebula.html) for x86_64, x86-64-v2 and AArch64 architectures
    * [Oracle Cloud Infrastructure](https://wiki.almalinux.org/cloud/OCI.html) for x86_64 and AArch64 Instances
* [Vagrant Boxes](https://app.vagrantup.com/almalinux) for x86_64 and x86-64-v2
    * Libvirt
    * VirtualBox
    * Hyper-V
    * VMWare
* [Raspberry Pi](https://wiki.almalinux.org/documentation/raspberry-pi.html)
* [Windows Subsystem for Linux](https://wiki.almalinux.org/documentation/wsl.html) for x86_64 and AArch64

# ELevate Project and Migration Tool

Support for AlmaLinux OS 10.0 Stable in the ELevate Project and Migration Tool is actively in development and will be available soon.
In the meantime, you can help us test ELevate upgrades to AlmaLinux OS 10.0 Beta and AlmaLinux OS 10 Kitten to ensure a smoother, well-tested process. Please, refer to the [ELevate Testing Guide](https://wiki.almalinux.org/elevate/ELevate-NG-testing-guide.html#upgrade-centos-7-to-almalinux-8) and join the [~migration channel on the AlmaLinux Community Chat](https://chat.almalinux.org/almalinux/channels/migration) to stay updated.

## Release Notes and More Information

AlmaLinux OS 10.0 Stable brings significant enhancements across core components enhancing development, security, and performance workflows. New versions of programming languages, toolchains, and compilers give developers access to the latest tools. Updates to control systems, servers, and databases aim to improve system performance and scalability.

As for security, this release introduces post-quantum cryptography support and updates to SELinux and OpenSSH. A new sudo system role simplifies configuration management across multiple systems, while new tools like Sequoia PGP expand encryption options.

You can read the full release notes for this version on the wiki: [AlmaLinux OS 10.0 Release Notes](https://wiki.almalinux.org/release-notes/10.0.html).

### What can you do to help?

Your input into testing and feedback is crucial and essential for successful production releases. 
Please, report any bugs you may see on the [Bug Tracker](https://bugs.almalinux.org/). Also, pop into the [AlmaLinux Community Chat](https://chat.almalinux.org) and join our Testing Channel, post a question on our [10.0 Forum](https://forums.almalinux.org/), on our AlmaLinux Community on [Reddit](https://reddit.com/r/almalinux) or catch us on [X](https://twitter.com/almalinux). 

Please report any bugs you may see on the [Bug Tracker](https://bugs.almalinux.org/). 

**Enjoy the release and have fun!**