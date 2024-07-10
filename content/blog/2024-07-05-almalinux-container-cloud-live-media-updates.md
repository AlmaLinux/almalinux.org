---
title: "AlmaLinux Cloud, Container and Live Media Images Updates"
type: blog
author: 
 name: "Andrew Lukoshko"
 bio: "Release Engineering Lead"
 image: /users/alukoshko.jpg
date: 2024-07-05
images:
  - /blog-images/2024/2024-07-05-images-updates.png
post: 
    title: "Delivering news on both AlmaLinux 9.4 and 8.10 images updates."
    image: /blog-images/2024/2024-07-05-images-updates.png
---

Hey Community! We have been doing a ton of work to automate our image creation, so we don't need to announce our image updates anymore; They come out so close to when we release the new versions that a separate announcement isn't necessary. However, we have heard from some of you that you have come to rely on this announcement, so here it is for AlmaLinux 9.4 and 8.10.

## Cloud and Container Images Updates and Changes

AlmaLinux OS provides a variety of cloud images that have been updated to 9.4 and 8.10 including: 
* [Amazon AWS](https://wiki.almalinux.org/cloud/AWS.html) 
* [Generic Cloud](https://wiki.almalinux.org/cloud/Generic-cloud.html)
    * Impacted architectures: **x86_64, AArch64, ppc64le, s390x**. The size of the boot partition (`/boot`) increased from `512 MiB` to `1024 MiB / 1GiB`. This means that three and more kernels can be installed and enables larger initramfs (initial ram file system) and kernel related development.
* [OpenNebula](https://wiki.almalinux.org/cloud/OpenNebula.html)
    * Impacted architecture: **x86_64**. AlmaLinux OpenNebula images now have unified - BIOS and UEFI - boot support. The download URLs of the UEFI images are symlinked to the current image for compatibility.
* [Microsoft Azure](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/almalinux.almalinux-x86_64)

You can also find the Cloud Images Changelog in the [AlmaLinux Wiki](https://wiki.almalinux.org/cloud/cloud-changelog.html).

Container images have been updated as well. 
* You can get official [Docker](https://hub.docker.com/_/almalinux) images and [OCI Images from Quay.io](https://quay.io/organization/almalinuxorg), and starting with AlmaLinux versions 9.4 and 8.10 you can also get the container images from [GitHub packages](https://github.com/orgs/AlmaLinux/packages).
* We've updated scripts and workflows to build AlmaLinux container images. They are now based on [GitHub Actions](https://github.com/AlmaLinux/container-images/actions). We welcome contributors and interested ones to the new GitHub repo - [container-images](https://github.com/AlmaLinux/container-images).

If you want to contribute to Cloud or Container images or have any questions, please join the [Cloud SIG](https://wiki.almalinux.org/sigs/Cloud.html).

## Live Media Images 

All Live Media images were also updated to versions [AlmaLinux 9.4](https://repo.almalinux.org/almalinux/9/live/x86_64/) and [AlmaLinux 8.10](https://repo.almalinux.org/almalinux/8/live/x86_64) which includes the following variants:
* GNOME
* GNOME-Mini
* KDE - `kdepim-addons` package for additional plugins for KDE PIM applications has been added back.
* MATE
* XFCE 

OpenVPN tools for integrating VPN into NetworkManager including desktop-specific packages are now pre-installed in all Live Media images. 

## More Options 

The following options have also been updated to the latest versions:
* LXD/LXC to [AlmaLinux 9.4](https://images.linuxcontainers.org/images/almalinux/9/amd64/) and [AlmaLinux 8.10](https://images.linuxcontainers.org/images/almalinux/8/amd64/)
* [Raspberry Pi](https://wiki.almalinux.org/documentation/raspberry-pi.html) images to [AlmaLinux 9.4](https://repo.almalinux.org/almalinux/9.4/raspberrypi/images/) and [AlmaLinux 8.10](https://repo.almalinux.org/rpi/images/) including **Raspberry Pi 5** support.
* [Vagrant Box](https://wiki.almalinux.org/installation/vagrant-boxes.html) images to [AlmaLinux 9.4](https://app.vagrantup.com/almalinux/boxes/9) and [AlmaLinux 8.10](https://app.vagrantup.com/almalinux/boxes/8)

You can check the [AlmaLinux website](https://almalinux.org/get-almalinux/) for a full list of images AlmaLinux provides.

## How to Help and Contribute 

All your contributions, feedback, and bug reports help us improve AlmaLinux.

Please, check the [Help and Support](https://wiki.almalinux.org/Help-and-Support.html) wiki page, and join us on the [AlmaLinux Community Chat](https://chat.almalinux.org) for any help, assistance, or to discuss anything. Reach out to us on [Reddit](https://reddit.com/r/almalinux), Mastodon at [@almalinux@fosstodon.org](https://fosstodon.org/@almalinux), and follow us on [X (formerly known as Twitter)](https://twitter.com/almalinux).
