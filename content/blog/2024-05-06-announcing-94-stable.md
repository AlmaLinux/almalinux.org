---
title: "General Availability of AlmaLinux 9.4 Stable!"
type: blog
author:
 name: "Eduard Abdullin"
 bio: "The Release and Automation Engineer."
 image: /users/eduard-abdullin.jpg
date: '2024-05-06'
images:
  - /blog-images/2024/2024-05-06-almalinux-9-4-stable.png
post:
    title: "General Availability of AlmaLinux 9.4 Stable!"
    image: /blog-images/2024/2024-05-06-almalinux-9-4-stable.png

---

# AlmaLinux 9.4 Stable Now Available 

Hello Community! The AlmaLinux OS Foundation is announcing the general availability of [AlmaLinux OS 9.4](https://mirrors.almalinux.org/isos.html) codenamed "Seafoam Ocelot"!

Installation ISOs are available on the mirrors now for all 4 architectures:
* [Intel/AMD (x86_64)](https://mirrors.almalinux.org/isos/x86_64/9.4.html)
* [ARM64 (aarch64)](https://mirrors.almalinux.org/isos/aarch64/9.4.html)
* [IBM PowerPC (ppc64le)](https://mirrors.almalinux.org/isos/ppc64le/9.4.html)
* [IBM Z (s390x)](https://mirrors.almalinux.org/isos/s390x/9.4.html)

Torrents are available as well at:
* [Intel/AMD (x86_64)](https://repo.almalinux.org/almalinux/9.4/isos/x86_64/AlmaLinux-9.4-x86_64.torrent)
* [ARM64 (aarch64)](https://repo.almalinux.org/almalinux/9.4/isos/aarch64/AlmaLinux-9.4-aarch64.torrent)
* [IBM PowerPC (ppc64le)](https://repo.almalinux.org/almalinux/9.4/isos/ppc64le/AlmaLinux-9.4-ppc64le.torrent)
* [IBM Z (s390x)](https://repo.almalinux.org/almalinux/9.4/isos/s390x/AlmaLinux-9.4-s390x.torrent)

## How we build

Matching release and software versions with Red Hat Enterprise Linux(RHEL), AlmaLinux builds from the same sources as RHEL, promises complete compatibility with RHEL, and does so from freely available open source code. This makes it the only choice for anyone looking for a truly open source Enterprise Linux. If you are looking for a deeper undertanding of how AlmaLinux is built, watch this 23 minute video of our Lead Architect explaining in detail at [AlmaLinux Day: Germany](https://almalinux.org/almalinux-day-germany-2024/), earlier this year.

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

The AlmaLinux 9.4 introduces updates to enhance machine security and data protection. Enhancements in web-console and system roles automate additional operations and promote consistency in complex IT environments. The new release's features aim to improve system availability and reliability, facilitate easier recovery operations, and enhance virtual machine snapshot capabilities in hybrid cloud environments. The new system roles introduced enable the creation and management of logical volume manager (LVM) snapshots for improved data backup and recovery processes. Additionaly, updates in the 9.4 release continues to improve performance, scalability, and reliability for developers in building and managing applications.

You can read the full release notes for this version on the wiki: [AlmaLinux OS 9.4 Release Notes](https://wiki.almalinux.org/release-notes/9.4.html).

## Renewing support for upstream deprecated hardware

With AlmaLinux 9.4 we have also differentiated ourselves by meeting another request from our community for support with older hardware to help them stay on updated operating systems.

The following device drivers were modified to re-add PCI IDs for hardware disabled in upstream:
  * **aacraid** -  Dell PERC2, 2/Si, 3/Si, 3/Di, Adaptec Advanced Raid Products, HP NetRAID-4M, IBM ServeRAID & ICP SCSI 
  * **be2iscsi** - Emulex OneConnectOpen-iSCSI for BladeEngine 2 and 3 adapters 
  * **hpsa** - HP Smart Array Controller 
  * **lpfc** - Emulex LightPulse Fibre Channel SCSI 
  * **megaraid_sas** - Broadcom MegaRAID SAS 
  * **mlx4_core** - Mellanox Gen2 and ConnectX-2 adapters 
  * **mpt3sas** - LSI MPT Fusion SAS 3.0 
  * **mptsas** - Fusion MPT SAS Host 
  * **qla2xxx** - QLogic Fibre Channel HBA 
  * **qla4xxx** - QLogic iSCSI HBA 

For a complete list of hardware support for which was added in this release, see the  [Extended hardware support](https://wiki.almalinux.org/release-notes/9.4.html#extended-hardware-support) section in the 9.4 release notes.
  
While this list is quite comprehensive, we also welcome feedback from all of our users! If you use older hardware, does this list cover everything you need it to? If not, please share more here on the AlmaLinux Forums: [Re-adding support for older hardware](https://forums.almalinux.org/t/re-adding-support-for-older-hardware/3851).

## Pitch In

Join us in the [AlmaLinux Community Chat](https://chat.almalinux.org) to get any assistance you need and help others. You can also post a question on our [9.4 Forum](https://forums.almalinux.org/c/devel/9-stable/36), on our AlmaLinux Community on [Reddit](https://reddit.com/r/almalinux), catch us on [Twitter/X](https://twitter.com/almalinux) and follow us on Mastodon [@almalinux@fosstodon.org](https://fosstodon.org/@almalinux)

Please report any bugs you may see on the [Bug Tracker](https://bugs.almalinux.org/). 

**Enjoy the release and have fun!**
