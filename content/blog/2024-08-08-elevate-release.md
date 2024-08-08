---
title: "ELevate gets a huge update, plus 2 more OSes and hardware detection"
type: blog
author: 
 name: "Andrew Lukoshko"
 bio: "Release Engineering Lead"
 image: /users/alukoshko.jpg
date: 2024-08-08
images:
  - /blog-images/2024/2024-08-elevate-updates.png
post: 
    title: "ELevate gets a huge update, plus 2 more OSes and hardware detection"
    image: /blog-images/2024/2024-08-elevate-updates.png
---

We're happy to announce that [ELevate](https://almalinux.org/elevate/) just received the biggest update since 2021 when the project was first announced.

## How did we get here

For anyone new, ELevate allows you to upgrade in-place from older Enterprise Linux distributions to supported versions. It uses the [Leapp utility](https://leapp.readthedocs.io/) with a few patches and a data library called leapp-data.

Last month we announced that ELevateNG would get promoted to stable this week, and after tons of community-contributed feedback, the time is here! Let's dive into what has been updated. 

## Upgrades for both leapp and leapp-repository

This update includes a rebase on version [0.19.0](https://github.com/oamg/leapp-repository/releases) of the leapp-repository and all the upstream features and bug fixes. Additionally, the Package Evolution file `pes-events.json` is now based on Red Hat's, because it's now [available](https://raw.githubusercontent.com/oamg/leapp-repository/master/etc/leapp/files/pes-events.json) under an Open Source license.

Changelog entries:

* leapp is updated to version 0.16.0
* leapp-repository is updated to version 0.19.0

## Automatic hardware support detection

Historically it was left to the user to ensure that the destination OS would support the hardware the OS was being installed on. With this release, we now automatically detect supported hardware and warn users before they upgrade.

This is even more important because versions [8.10](https://wiki.almalinux.org/release-notes/8.10.html) and [9.4](https://wiki.almalinux.org/release-notes/9.4.html) of AlmaLinux included expanded hardware support, adding more than 150 storage and network devices that were disabled in Red Hat and those promising to duplicate RHEL exactly.

Changelog entry:

* ELevate now scans for hardware and checks to ensure that it will be supported in the target OS. 

## Repo support improved

Updating your OS with ELevate has historically had one hitch for users of 3rd party repos. Without proper care, packages from non-OS-default repos weren't updated, and might even be deleted during the upgrade. With this release, we have added support for some of the repos we've seen people ask about most frequently.

EPEL is one of the most common third-party repos used in Enterprise Linux, and users upgrading to AlmaLinux can now upgrade with confidence even with packages installed through EPEL.

In addition to EPEL, ELevate now supports other popular repositories: [Imunify](https://imunify360.com/), [KernelCare](https://tuxcare.com/), [MariaDB](https://mariadb.org/), [Nginx](https://www.f5.com/go/product/welcome-to-nginx), [PostgreSQL](https://www.postgresql.org/). Please join the development of ELevate in the places described below to contribute more 3rd party repos support.

Changelog entries:

* EPEL is now supported for both 7 to 8 and 8 to 9 upgrades when upgrading to AlmaLinux
* Now supports other popular repositories: MariaDB, Nginx, PostgreSQL, Imunify, KernelCare. 

## Additional OS support: Scientific Linux 7, and CentOS Stream 8 to CentOS 9

In addition to our expansion earlier this year to [include CentOS 6 support in ELevate](https://almalinux.org/blog/2024-04-25-elevate-supports-centos-6-to-centos-7/), we are happy to share two more OSes that we support!

<img loading="lazy" class="d-block mx-lg-auto img-fluid" width="624" height="430" src="/images/elevate-white-letters-no-background.png" alt="The migration paths when using ELevate">

With this release of ELevate, users can safely upgrade orphaned Scientific Linux 7 devices as well. Enterprise Linux is a common choice in the science community, and Scientific Linux has been widely used all over the world. With Scientific Linux 7 now also reaching end of life, it is important for us to help those in the Scientific community to get to a supported operating system as well. 

We're happy to share that ELevate now also supports CentOS Stream 8 to CentOS Stream 9 support. The first version of ELevate supported upgrading to CentOS Stream 8, but with CentOS Stream 8 also now being end of life, it was even more important for users to be able to upgrade to CentOS Stream 9.

## Where to Join Us

Join the [Migration Chat Channel](https://chat.almalinux.org/almalinux/channels/migration) to let us know how it goes or if you need any assistance. You can also file the bugs or issues to the [AlmaLinux leapp repository](https://github.com/AlmaLinux/leapp-repository).

We are so, so happy to be able to shepherd this project, and deeply appreciate your support. It means the world to us.