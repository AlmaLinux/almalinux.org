---
title: "Announcing AlmaLinux 9.4 Beta!"
type: blog
author:
 name: "Eduard Abdullin"
 bio: "The Release and Automation Engineer."
 image: /users/eduard-abdullin.jpg
date: '2024-04-15'
images:
  - /blog-images/2024-04-15-94-beta.png
post:
    title: "Announcing AlmaLinux 9.4 Beta!"
    image: /blog-images/2024-04-15-94-beta.png

---

# AlmaLinux 9.4 Beta Now Available 

Hello Community! The AlmaLinux OS Foundation is announcing the availability of AlmaLinux 9.4 Beta "Seafoam Ocelot" for all supported architectures:
* Intel/AMD (x86_64)
* ARM64 (aarch64)
* IBM PowerPC (ppc64le)
* IBM Z (s390x)

Beta ISOs are available at [repo.almalinux.org](https://repo.almalinux.org/almalinux/9.4-beta/isos/). 

A usual reminder: this is a **BETA** release. It should not be used for production installations. The provided upgrade instructions should not be used on production machines unless you don't mind if something breaks. Now if you wanna test this somehow, somewhere to see how things will work in 9.4 stable, you're on the right track.

## Release Notes and More Information

The AlmaLinux 9.4 Beta introduces updates to enhance machine security and data protection. Enhancements in web-console and system roles automate additional operations and promote consistency in complex IT environments. The new release's features aim to improve system availability and reliability, facilitate easier recovery operations, and enhance virtual machine snapshot capabilities in hybrid cloud environments. The new system roles introduced enable the creation and management of logical volume manager (LVM) snapshots for improved data backup and recovery processes. Additionally, updates in the 9.4 Beta release continue to improve performance, scalability, and reliability for developers in building and managing applications.

You can read the full release notes for this version on the wiki: [AlmaLinux OS 9.4 Release Notes](https://wiki.almalinux.org/release-notes/9.4-beta.html).

## Renewing support for upstream deprecated hardware

With AlmaLinux 9.4 we have also differentiated ourselves in another way. Our community has asked us to help them stay on updated operating systems by providing support for older hardware. 

* The following device drivers were modified to re-add PCI IDs for hardware disabled in upstream:
    * **aacraid** -  Dell PERC2, 2/Si, 3/Si, 3/Di, Adaptec Advanced Raid Products, HP NetRAID-4M, IBM ServeRAID & ICP SCSI 
    * **be2iscsi** - Emulex OneConnectOpen-iSCSI for BladeEngine 2 and 3 adapters 
    * **hpsa** - HP Smart Array Controller 
    * **lpfc** - Emulex LightPulse Fibre Channel SCSI 
    * **megaraid_sas** - Broadcom MegaRAID SAS 
    * **mpt3sas** - LSI MPT Fusion SAS 3.0 
    * **mptsas** - Fusion MPT SAS Host 
    * **qla2xxx** - QLogic Fibre Channel HBA 
    * **qla4xxx** - QLogic iSCSI HBA 

For a complete list of hardware support for which was added in this release, see the  [Extended hardware support](https://wiki.almalinux.org/release-notes/9.4-beta.html#extended-hardware-support) section.
  
While this list is quite comprehensive, we also want to hear more from a wider base of users! If you use older hardware, does this list cover everything you need it to? If not, please share more here on the AlmaLinux Forums: [Re-adding support for older hardware](https://forums.almalinux.org/t/re-adding-support-for-older-hardware/3851)

## What you can do to help?

Your input into testing and feedback is crucial and essential for successful production releases. 
Please, report any bugs you may see on the [Bug Tracker](https://bugs.almalinux.org/). Also, pop into the [AlmaLinux Community Chat](https://chat.almalinux.org) and join our Testing Channel, post a question on our [9.4 Beta Forum](https://forums.almalinux.org/c/devel/9-4-beta/29), on our AlmaLinux Community on [Reddit](https://reddit.com/r/almalinux) or catch us on [Twitter](https://twitter.com/almalinux). 

Enjoy this Beta release, let us know what you think and stay tuned. We expect the production release of AlmaLinux OS 9.4 to follow the production release of RHEL 9.4 by about a week, and RHEL 9.4 is currently anticipated sometime in mid-May.

**Happy Testing!**
