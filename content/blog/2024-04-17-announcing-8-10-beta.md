---
title: "Announcing AlmaLinux 8.10 Beta!"
type: blog
author:
 name: "Eduard Abdullin"
 bio: "The Release and Automation Engineer."
 image: /users/eduard-abdullin.jpg
date: '2024-04-17'
images:
  - /blog-images/2024-04-17-810-beta.png
post:
    title: "Announcing AlmaLinux 8.10 Beta!"
    image: /blog-images/2024-04-17-810-beta.png

---

# AlmaLinux 8.10 Beta Now Available 

Hello Community! The AlmaLinux OS Foundation is announcing the availability of AlmaLinux 8.10 Beta "Cerulean Leopard" for all supported architectures:
* Intel/AMD (x86_64)
* ARM64 (aarch64)
* IBM PowerPC (ppc64le)
* IBM Z (s390x)

Beta ISOs are available at [repo.almalinux.org](https://repo.almalinux.org/almalinux/8.10-beta/isos/). 

A usual reminder: this is a **BETA** release. It should not be used for production installations. The provided upgrade instructions should not be used on production machines unless you have backups and a recovery option. Now if you want to test this release to see how things will work in 8.10 stable, you're on the right track!

## Release Notes and More Information

The AlmaLinux 8.10 Beta brings updates to security and data protection, improvements in web-console and system roles to automate operations and ensure consistency in intricate IT settings. The release continues to enhance system availability, reliability, and recovery processes, alongside improving virtual machine snapshot functions in hybrid cloud scenarios. New system roles have been introduced to streamline the creation and administration of logical volume manager (LVM) snapshots for better data backup and recovery processes. Performance, scalability, and reliability continue to be the focus of updates in the 8.10 Beta version to aid developers in application development and management.

You can read the full release notes for this version on the wiki: [AlmaLinux OS 8.10 Release Notes](https://wiki.almalinux.org/release-notes/8.10-beta.html).

## Renewing support for upstream disabled hardware

With AlmaLinux 8.10 we have also differentiated ourselves in another way. Our community has asked us to help them stay on updated operating systems by providing support for older hardware. 

* The following device drivers were modified to re-add PCI IDs for hardware disabled in upstream:
    * **aacraid** -  Dell PERC2, 2/Si, 3/Si, 3/Di, Adaptec Advanced Raid Products, HP NetRAID-4M, IBM ServeRAID & ICP SCSI 
    * **be2iscsi** - Emulex OneConnect Open-iSCSI for BladeEngine 2 and 3 adapters 
    * **hpsa** - HP Smart Array Controller 
    * **lpfc** - Emulex LightPulse Fibre Channel SCSI 
    * **megaraid_sas** - Broadcom MegaRAID SAS 
    * **mlx4_core** - Mellanox Gen2 and ConnectX-2 adapters 
    * **mpt3sas** - LSI MPT Fusion SAS 3.0 
    * **mptsas** - Fusion MPT SAS Host 
    * **qla2xxx** - QLogic Fibre Channel HBA 
    * **qla4xxx** - QLogic iSCSI HBA 

For a complete list of hardware support for which was added in this release, see the  [Extended hardware support - fix for WIKI link](https://wiki.almalinux.org/release-notes/8.10-beta.html#extended-hardware-support) section.
  
While this list is quite comprehensive, we also want to hear more from a wider base of users! If you use older hardware, does this list cover everything you need it to? If not, please share more here on the AlmaLinux Forums: [Re-adding support for older hardware](https://almalinux.discourse.group/t/re-adding-support-for-older-hardware/3851).

## What you can do to help?

Your input into testing and feedback is crucial and essential for successful production releases. 
Please, report any bugs you may see on the [Bug Tracker](https://bugs.almalinux.org/). Also, pop into the [AlmaLinux Community Chat](https://chat.almalinux.org) and join our Testing Channel, post a question on our [8.10 Beta Forum](https://almalinux.discourse.group/c/devel/8-10-beta/29), on our AlmaLinux Community on [Reddit](https://reddit.com/r/almalinux) or catch us on [Twitter](https://twitter.com/almalinux). 

Enjoy this Beta release, let us know what you think and stay tuned. 

**Happy Testing!**
