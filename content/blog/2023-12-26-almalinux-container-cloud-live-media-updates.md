---
title: "AlmaLinux Cloud, Container and Live Media Images Updates"
type: blog
author: 
 name: "Andrew Lukoshko"
 bio: "Release Engineering Lead"
 image: /users/alukoshko.jpg
date: 2023-12-26
images:
  - /blog-images/2023-12-21-images-updates.jpg
post: 
    title: "AlmaLinux Cloud, Container and Live Media Images Updates"
    image: /blog-images/2023-12-21-images-updates.jpg
---

Hey Community! We're just sharing some news on both AlmaLinux 9.3 and 8.9 images updates. 


## Cloud and Container Images Updates and Changes

AlmaLinux OS provides a variety of cloud images, so we've been updating them to 9.3 and 8.9 versions including: 
* [Amazon AWS](https://wiki.almalinux.org/cloud/AWS.html)
    * Starting AlmaLinux OS versions 8.9 and 9.3 Amazon Machine images have UEFI boot support. Thus boot mode was changed to the `uefi-preferred` meaning that UEFI will be chosen on the supported instance types. We are planning to publish separate AMIs with enabled Secure Boot and NitroTPM(vTPM) support.
* [Generic Cloud](https://wiki.almalinux.org/cloud/Generic-cloud.html)
    * Starting AlmaLinux OS 8.9 Generic Cloud images have hybrid - BIOS and UEFI - boot support. The download URLs of the UEFI images are symlinked to the current image for compatibility.
* [OpenNebula](https://wiki.almalinux.org/cloud/OpenNebula.html)
    * Starting AlmaLinux OS 8.9 Generic Cloud images have hybrid - BIOS and UEFI - boot support.
* Microsoft Azure images for [x86_64](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/almalinux.almalinux-x86_64) and [AArch64](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/almalinux.almalinux-arm) architectures
* [Oracle Cloud Infrastructure](https://wiki.almalinux.org/cloud/OCI.html)

Container images have been updated as well. You can get official [Docker](https://hub.docker.com/_/almalinux) images and [OCI Images from Quay.io](https://quay.io/organization/almalinuxorg).

If you wish to contribute or have any questions, please check with the [Cloud SIG](https://wiki.almalinux.org/sigs/Cloud.html).

## Live Media Images 

All Live Media images were also updated to versions [AlmaLinux 9.3](https://repo.almalinux.org/almalinux/9/live/x86_64/) and [AlmaLinux 8.9](https://repo.almalinux.org/almalinux/8/live/x86_64/) which include the following variants:
* GNOME
* GNOME-Mini
* KDE
* MATE
* XFCE 

## More options 

The following options have also been updated
* LXD/LXC to [AlmaLinux 9.3](https://images.linuxcontainers.org/images/almalinux/9/amd64/) and [AlmaLinux 8.9](https://images.linuxcontainers.org/images/almalinux/8/amd64/)
* [Vagrant Box](https://app.vagrantup.com/almalinux) images to AlmaLinux 9.3 and 8.9
* Raspberry Pi images to [AlmaLinux 9.3](https://repo.almalinux.org/almalinux/9.3/raspberrypi/images/) and [AlmaLinux 8.9](https://repo.almalinux.org/almalinux/8.9/raspberrypi/images/)

You can check the [AlmaLinux website](https://almalinux.org/get-almalinux/) for a full list of images AlmaLinux provides.

## How to help and contribute 

All your contributions, feedback and bug reports help us improve AlmaLinux. Please join us on the [AlmaLinux Community Chat](https://chat.almalinux.org) for any help, assistance, or to discuss anything. Reach out to us on [Reddit](https://reddit.com/r/almalinux), Mastodon  at [@almalinux@fosstodon.org](https://fosstodon.org/@almalinux), and follow us on [X (formerly known as twitter)](https://twitter.com/almalinux).
