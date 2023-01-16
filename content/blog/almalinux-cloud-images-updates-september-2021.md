---
title: "AlmaLinux Cloud Images Updates - September 2021"
type: blog
author: 
 name: "theMayor"
 bio: "-"
 image: /images/profile.png
date: '2021-09-20'
post:
    title: "Bug fixes, AWS, Azure, aarch64 support, OpenNebula and more!"
    image: 
---

Hello, Community! Lots going on here in AlmaLinux land as we continue our journey through the clouds. Today we're pleased to share the latest updates about [AlmaLinux Cloud Images](https://github.com/AlmaLinux/cloud-images). Those include aarch64 support for our AWS AMIs, support for OpenNebula x86_64 and aarch64, and aarch64 support for our Generic (cloud-init) Cloud images/OpenStack.

Links for downloads: https://wiki.almalinux.org/cloud/Generic-cloud.html

Some general fixes and updates that were made across all cloud images:

- Added IPv6 support: https://github.com/AlmaLinux/cloud-images/issues/20
- Fixed Ansible leftover files and directories: https://github.com/AlmaLinux/cloud-images/issues/24

## AWS AMIs

We've added ARM64/Graviton support to our AMIs. As always, AMIs are available both via the [AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-zgsymdwitnxmm) as well as [Community AMIs](https://wiki.almalinux.org/cloud/AWS.html#community-amis).

Additionally the following issues were addressed as well for AWS AMIs:

- Fixed incorrect SELinux type on interface files and other system files after vmimport. https://github.com/AlmaLinux/cloud-images/issues/23
- Fixed Machine ID duplication
- Added QEMU support for image builder
- Added Installed and configured AWS Systems Manager Agent

We would sincerely like to thank AWS for their generous sponsorship of the AlmaLinux Foundation.

## Microsoft Azure

AlmaLinux images are now available on Mircrosoft Azure including a global in-network set of mirrors. You can read the announcement [here](https://almalinux.org/blog/almalinux-now-available-on-microsoft-azure-azure-sponsors-almalinux/) and get more information on the [wiki](https://wiki.almalinux.org/cloud/Azure.html).

We would sincerely like to thank Microsoft Azure for their generous sponsorship of the AlmaLinux Foundation.

## Generic (cloud-init) Cloud Image/OpenStack

We've updated our [generic cloud/OpenStack images](https://wiki.almalinux.org/cloud/Generic-cloud.html) to include support for aarch64 as well. You can read more about those, and how to download and verify those images, on the wiki linked above too.

You can also find information on how to [run the generic cloud image on your local machine](https://wiki.almalinux.org/cloud/Generic-cloud-on-local.html).

## OpenNebula

By popular demand, we've added support for the [OpenNebula](https://opennebula.io/) cloud platform for both x86_64 and aarch64. See the [OpenNebula page](https://wiki.almalinux.org/cloud/OpenNebula.html) on the wiki for info.

## Join the fun!

You can follow along, submit issues and pull requests ti to our [Cloud Images Repository on GitHub](https://github.com/AlmaLinux/cloud-images). To read more about AlmaLinux, our Cloud images, and how to contribute, please, visit the [AlmaLinux wiki](https://wiki.almalinux.org/) and join us on the [AlmaLinux Community Chat](https://chat.almalinux.org/).

We'd like to give a big thanks to the Community, for the contributions, feedback and bug reports, that are so valuable to making AlmaLinux better.

You can ask any questions on the [AlmaLinux Community Forums](https://forums.almalinux.org/) for any help and assistance. You can also follow us on [Twitter](https://twitter.com/almalinux) and [Reddit](https://reddit.com/r/AlmaLinux).

Stay tuned, because some more great announcements are coming right down the pipe!