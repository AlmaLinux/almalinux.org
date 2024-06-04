---
title: "General Availability of AlmaLinux 8.10 Stable!"
type: blog
author:
 name: "Eduard Abdullin"
 bio: "Release and Automation Engineer."
 image: /users/eduard-abdullin.jpg
date: '2024-05-28'
images:
  - /blog-images/2024/2024-05-28-almalinux-8-10-stable.png
post:
    title: "AlmaLinux 8.10 Stable Now Available!"
    image: /blog-images/2024/2024-05-28-almalinux-8-10-stable.png

---

# AlmaLinux 8.10 Stable Now Available 

Hello Community! The AlmaLinux OS Foundation is announcing the general availability of [AlmaLinux OS 8.10](https://mirrors.almalinux.org/isos.html) codenamed "Cerulean Leopard"!

Installation ISOs are available on the mirrors now for all 4 architectures:
* [Intel/AMD (x86_64)](https://mirrors.almalinux.org/isos/x86_64/8.10.html)
* [ARM64 (aarch64)](https://mirrors.almalinux.org/isos/aarch64/8.10.html)
* [IBM PowerPC (ppc64le)](https://mirrors.almalinux.org/isos/ppc64le/8.10.html)
* [IBM Z (s390x)](https://mirrors.almalinux.org/isos/s390x/8.10.html)

Torrents are available as well at:
* [Intel/AMD (x86_64)](https://repo.almalinux.org/almalinux/8.10/isos/x86_64/AlmaLinux-8.10-x86_64.torrent)
* [ARM64 (aarch64)](https://repo.almalinux.org/almalinux/8.10/isos/aarch64/AlmaLinux-8.10-aarch64.torrent)
* [IBM PowerPC (ppc64le)](https://repo.almalinux.org/almalinux/8.10/isos/ppc64le/AlmaLinux-8.10-ppc64le.torrent)
* [IBM Z (s390x)](https://repo.almalinux.org/almalinux/8.10/isos/s390x/AlmaLinux-8.10-s390x.torrent)

## How we build

AlmaLinux matches release and software versions with Red Hat Enterprise Linux (RHEL) and builds from the same sources as RHEL, ensuring complete compatibility with RHEL, and does so from freely available open source code. If you are looking for a deeper understanding of how AlmaLinux is built, watch this 23-minute video of our Lead Architect explaining in detail at [AlmaLinux Day: Germany](https://almalinux.org/almalinux-day-germany-2024/), earlier this year:

{{< youtube id="aMvI5E9-LYI" width="45%" height="25%" autoplay="false" controls="true" mute="false" title="AlmaLinux Day Germany 2024: Building without following" >}}

## ISOs, Live Images, Cloud and Containers

AlmaLinux also offers a variety of Cloud, Container and Live Images. The builds for these get kicked off as soon as the public repository was ready. 

**The following images are expected to be available shortly.** 

* [Container](https://wiki.almalinux.org/containers/) images including Platform and UBIs alternatives. We provide a wide variety of containers for your use. 
* [LXC/LXD](https://images.linuxcontainers.org/images/almalinux/) 
* [Live Media](https://wiki.almalinux.org/LiveMedia.html) for GNOME, GNOME-mini, KDE, XFCE, MATE and more.
* Cloud Images 
    * [AWS](https://wiki.almalinux.org/cloud/AWS.html) for x86_64 and AArch64 EC2 Instances
    * [Azure](https://wiki.almalinux.org/cloud/Azure.html) for x86_64 and AArch64 VMs
    * [Google Cloud](https://wiki.almalinux.org/cloud/Google.html)
    * [Generic Cloud/Cloud-init](https://wiki.almalinux.org/cloud/Generic-cloud-on-local.html) for all 4 architectures
    * [OpenNebula](https://wiki.almalinux.org/cloud/OpenNebula.html) for x86_64 and AArch64 architectures
    * [Oracle Cloud Infrastructure](https://wiki.almalinux.org/cloud/OCI.html) for x86_64 and AArch64 Instances
* [Vagrant Boxes](https://app.vagrantup.com/almalinux):
    * Libvirt
    * VirtualBox
    * Hyper-V
    * VMWare for x86_64 and AArch64
    * Parallels for AArch64
* [Raspberry Pi](https://wiki.almalinux.org/documentation/raspberry-pi.html)
* [Windows Subsystem for Linux](https://wiki.almalinux.org/documentation/wsl.html) for x86_64 and AArch64

## Release Notes and More Information

AlmaLinux 8.10 brings updates to security and data protection, and improvements in web-console and system roles to automate operations and ensure consistency in intricate IT settings. The release continues to enhance system availability, reliability, and recovery processes, alongside improving virtual machine snapshot functions in hybrid cloud scenarios. New system roles have been introduced to streamline the creation and administration of logical volume manager (LVM) snapshots for better data backup and recovery processes. Performance, scalability, and reliability continue to be the focus of updates in the 8.10 version to aid developers in application development and management.

You can read the full release notes for this version on the wiki: [AlmaLinux OS 8.10 Release Notes](https://wiki.almalinux.org/release-notes/8.10.html).

## Renewing support for upstream deprecated hardware

With AlmaLinux 8.10 we have also differentiated ourselves by meeting another request from our community for support with older hardware to help them stay on updated operating systems.

The following device drivers were modified to re-add PCI IDs for hardware disabled in upstream:
* The following device drivers were modified to re-add PCI IDs for hardware disabled in upstream:
    * **aacraid** -  Dell PERC2, 2/Si, 3/Si, 3/Di, Adaptec Advanced Raid Products, HP NetRAID-4M, IBM ServeRAID & ICP SCSI 
    * **be2iscsi** - Emulex OneConnect Open-iSCSI for BladeEngine 2 and 3 adapters 
    * **be2net** - Emulex BladeEngine 2 and 3 adapters
    * **hpsa** - HP Smart Array Controller 
    * **lpfc** - Emulex LightPulse Fibre Channel SCSI 
    * **megaraid_sas** - Broadcom MegaRAID SAS 
    * **mlx4_core** - Mellanox Gen2 and ConnectX-2 adapters
    * **mpt3sas** - LSI MPT Fusion SAS 3.0 
    * **mptsas** - Fusion MPT SAS Host 
    * **qla2xxx** - QLogic Fibre Channel HBA 
    * **qla4xxx** - QLogic iSCSI HBA 

For a complete list of hardware support for which was added in this release, see the  [Extended hardware support](https://wiki.almalinux.org/release-notes/8.10.html#extended-hardware-support) section in the 8.10 release notes.
  
While this list is quite comprehensive, we also welcome feedback from all of our users! If you use older hardware, does this list cover everything you need it to? If not, please share more here on the AlmaLinux Forums: [Re-adding support for older hardware](https://forums.almalinux.org/t/re-adding-support-for-older-hardware/3851).

## Pitch In

Join us in the [AlmaLinux Community Chat](https://chat.almalinux.org) to get any assistance you need and help others. You can also post a question on our [8.10 Forum](https://forums.almalinux.org/c/devel/8-stable/36), on our AlmaLinux Community on [Reddit](https://reddit.com/r/almalinux), catch us on [Twitter/X](https://twitter.com/almalinux) and follow us on Mastodon [@almalinux@fosstodon.org](https://fosstodon.org/@almalinux)

Please report any bugs you may see on the [Bug Tracker](https://bugs.almalinux.org/). 

**Enjoy the release and have fun!**
