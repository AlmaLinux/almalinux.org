---
title: "ELevate Project Updates"
type: blog
author: 
 name: "Andrew Lukoshko"
 bio: "Release Engineering Lead"
 image: /users/alukoshko.jpg
date: 2024-01-30
images:
  - /blog-images/2024-01-30-elevate-updates.png
post: 
    title: "ELevate Project Updates"
    image: /blog-images/2024-01-30-elevate-updates.png
---

Hello, Community! We are excited to share that we are about to release a great deal of updates for the [ELevate Project](https://almalinux.org/elevate/).

## ELevate now supports EPEL and more

ELevate, a fork of Red Hat's Leapp project, supports migrations between CentOS 7 and Enterprise Linux (EL) 8, and between EL8 and EL9 systems. It has helped more than 50,000 systems upgrade in place, allowing our global community to easily keep their infrastructure updated and more secure. The AlmaLinux community is constantly working on improving the project.

Originally, Red Hat’s Leapp only offered support for Red Hat Enterprise Linux and its official repositories. However, ELevate now offers 3rd party repository support. Specifically, we recently announced a testing version of ELevate that [included EPEL support](https://almalinux.org/blog/2023-12-05-announcing-epel-support-in-elevate/) for migrations from CentOS 7 to AlmaLinux 8. Today, this feature is available in the **stable** version of ELevate.

In addition, we have expanded beyond just EPEL support. Migration with additional repositories like Imunify, KernelCare, MariaDB, nginx, and PostgreSQL is available for all supported systems including AlmaLinux, CentOS, EuroLinux, Oracle Linux, and Rocky Linux.

## The next evolution of ELevate

Today we are also announcing the new version of ELevate -  ELevate Next Generation (NG). 

The new version of ELevate comes with some big changes that allow us to follow upstream closely, maintain the project with just a minimal subset of patches, and deliver updates and new features faster to supported operating systems.

These updates include the latest version of the leapp-repository [0.19.0](https://github.com/oamg/leapp-repository/releases) to include all the upstream features and bugfixes. Additionally, the Package Evolution file `pes-events.json` is now based on Red Hat's, as it's [available](https://raw.githubusercontent.com/oamg/leapp-repository/master/etc/leapp/files/pes-events.json) now under Open Source license.

CloudLinux OS and control panel support were removed in ELevate NG and are now only available in [CloudLinux's own ELevate fork](https://github.com/cloudlinux/leapp-repository).

## Contribute to the project 

In order to ensure ELevate NG's smooth functioning and top-notch user experience, we are seeking your help and support to join us in the testing phase. **Please, do not use it on production machines.** 

We appreciate any feedback and insights as they help us to improve the project's performance. For guidance during testing, please refer to the [Migrate with ELevate NG Guide](https://wiki.almalinux.org/elevate/ELevate-NG-testing-guide.html) available in the Wiki.

Join the [Migration Chat Channel](https://chat.almalinux.org/almalinux/channels/migration) to let us know how it goes or if you need any assistance.

We are always grateful for your support, as it means the world to us.
