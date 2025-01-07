---
title: "AlmaLinux Cloud, Container and Live Media Images Updates"
type: blog
author: 
 name: "Andrew Lukoshko"
 bio: "Release Engineering Lead"
 image: /users/alukoshko.jpg
date: 2025-01-07
images:
  - /blog-images/2025/2025-01-07-images-updates.png
post: 
    title: "Delivering news on AlmaLinux 9.5 image updates."
    image: /blog-images/2025/2025-01-07-images-updates.png
---

Hey Community! Bringing the latest AlmaLinux OS 9.5 images updates.

## Cloud and Container Images Updates and Changes

AlmaLinux provides a variety of cloud images that are now updated to the AlmaLinux OS 9.5 version including: 
* [Amazon Web Services (AWS)](https://wiki.almalinux.org/cloud/AWS.html) 
    * Added `sos` and `tcpdump` packages for troubleshooting and log collection tools.
    * Added `nfs-utils` package to enable built-in support for mounting Amazon Elastic File System (EFS) or any NFS filesystems.
* [Generic Cloud](https://wiki.almalinux.org/cloud/Generic-cloud.html)
    * New `langpacks-en` package  to add  `en_US.UTF-8` setting it as a default locale. 
* [OpenNebula](https://wiki.almalinux.org/cloud/OpenNebula.html)
    * New `langpacks-en` package  to add `en_US.UTF-8` setting it as a default locale. 
* [Microsoft Azure](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/almalinux.almalinux-x86_64)
    * New `langpacks-en` package  to add  `en_US.UTF-8` setting it as a default locale. 
    * Added `sos` and `tcpdump` packages for troubleshooting and log collection tools.
    * Added `nfs-utils` and `cifs-utils` packages to support mounting NFS and SMB file shares from Azure Files or any NFS and SMB filesystems.

You can find more details in the [Cloud Images Changelog](https://wiki.almalinux.org/cloud/cloud-changelog.html) at the AlmaLinux Wiki. The complete list of installed packages for AlmaLinux Cloud images, starting with this version, is available on the [cloud-images git repository](https://github.com/AlmaLinux/cloud-images/tree/main/tests/packages)

Container images are updated as well. 
* You can get official [Docker](https://hub.docker.com/_/almalinux) images and [OCI Images from Quay.io](https://quay.io/organization/almalinuxorg). You can also get container images from [GitHub packages](https://github.com/orgs/AlmaLinux/packages).

If you want to contribute to Cloud or Container images, or have any questions, please check with the [Cloud SIG](https://wiki.almalinux.org/sigs/Cloud.html).

## Live Media Images - now including ARM! 

All Live Media images that include GNOME, GNOME-Mini, KDE, XFCE and MATE are updated to [AlmaLinux OS 9.5](https://repo.almalinux.org/almalinux/9.5/live/) version. 

Starting from AlmaLinux OS 9.5 all supported Live Media options are also available for the [ARM64(AArch64)](https://repo.almalinux.org/almalinux/9/live/aarch64/).

## More options 

The following options have also been updated to the latest versions:
* Incus and LXC to [AlmaLinux 9.5](https://images.linuxcontainers.org/images/almalinux/9/).
* Raspberry Pi images to [AlmaLinux 9.5](https://repo.almalinux.org/almalinux/9.5/raspberrypi/images/).
    *  Since AlmaLinux 9.5, images with GPT (GUID partition table) are available in addition to traditional MBR images. GPT supports larger disks over 2TB and allows up to 128 partitions, compared to MBR's limit of 4. However, booting from a GPT disk is not supported on Raspberry Pi 3. Select the appropriate image for your Raspberry Pi model.
* [Vagrant Boxes](https://portal.cloud.hashicorp.com/vagrant/discover/almalinux) to [AlmaLinux 9.5](https://portal.cloud.hashicorp.com/vagrant/discover/almalinux/9) 
    * Added `langpacks-en` package for the `en_US.UTF-8` locale support.
    * Added `cifs-utils`, `fs-utils` and `rsync` to provide all types of Vagrant synced folders.
    * Added `tcpdump` and `tuned` packages for network troubleshooting and optimizations.
    * You can find more details and provider-specific changes on the [Vagrant Boxes](https://wiki.almalinux.org/installation/vagrant-boxes.html) page.
* Windows Subsystem for Linux (WSL) to [AlmaLinux 9.5](https://apps.microsoft.com/store/detail/almalinux-9/9P5RWLM70SN9).

You can check the [AlmaLinux website](https://almalinux.org/get-almalinux/) for a full list of images AlmaLinux provides.

## How to help and contribute 

All your contributions, feedback and bug reports are greatly appreciated and help us improve AlmaLinux for everyone! 

If you would like to help support AlmaLinux, there are many ways to contribute - [testing](https://wiki.almalinux.org/Contribute-to-Testing.html), quality assurance, [documentation](https://wiki.almalinux.org/Contribute-to-Documentation.html), and [more](https://wiki.almalinux.org/Contribute.html). We’d be thrilled to have you join us!

If you need any help or you'd like to discuss anything, check the [Help and Support](https://wiki.almalinux.org/Help-and-Support.html) wiki page, and join us on the [AlmaLinux Community Chat](https://chat.almalinux.org). Engage in the AlmaLinux community on [Reddit](https://reddit.com/r/almalinux), or follow us on [Mastodon](https://fosstodon.org/@almalinux), and [X](https://twitter.com/almalinux).

