---
title: "Announcing ELevate -- Migration between Major Versions (7.x to 8x) of RHEL Derivative Distributions"
type: blog
author: 
 name: "theMayor"
 bio: "-"
 image: /images/profile.png
date: '2021-10-19'
post:
    title: "ELevate is a project to develop the tools and data set to enable migrations between major versions of RHEL derivative distributions."
    image: /blog-images/elevatelogo.png
---

Hey, all! We'd like to share a very cool project/initiative that we've been working on with the community.

We are extremely happy to announce our migration project for major version of RHEL-derivative distributions. We like to call it [ELevate](/elevate). Get it? EL evate? Yeah, anyway...

Before we get started, let's be smart. We HIGHLY recommend that you follow system administration best practices and make sure you have backups and/or snapshots of your system before you proceed. It is recommended to do a trial run in a sandbox to verify that migration worked as expected before you attempt to migrate any production system.

If you want to get started quickly, check out the [ELevate Quick Start Guide](https://wiki.almalinux.org/elevate/ELevate-quickstart-guide.html).

Let's take a little peak behind the scenes at how all this works. First, We've put together some patches to Red Hat's [Leapp utility](https://leapp.readthedocs.io/) (which you can find [here](https://github.com/AlmaLinux/leapp-repository/commits/almalinux)) to support migration from CentOS. Work has already begun to get those merged upstream too since we like to avoid forking as much as possible.

Second, Leapp needs several configuration files, the biggest of them is some metdata called the package evolution data file pes-events.json. This metadata is what describes the steps required for a package to "evolve" from one release to the next. Oracle have been gracious enough to contribute an initial data set which we have built upon and we've also put together the [Package Evolution Service](https://pes.almalinux.org/) to allow the community to contribute and collaborate on additional metadata. This way maintainers and application vendors can contribute metadata to the library and users can customize the metdata set they download.

If you are keen on more details about the migration process and how to contribute, please, visit the [ELevate site](/elevate) and the [AlmaLinux Migration wiki page](https://wiki.almalinux.org/sigs/Migration.html).

We've taken steps to make sure that this works for the whole communtiy, not just AlmaLinux. These are the migrations that are currently available:

- CentOS 7 - AlmaLinux 8
- CentOS 7 - Oracle Linux 8
- CentOS 7 - Rocky Linux 8
- CentOS 7 - CentOS Stream 8

We’re often asked if there are any plans for collaboration between the various downstream RHEL projects and this is a great example of something where everyone -- AlmaLinux, CentOS, RHEL, Oracle and Rocky communities and developers can all contribute and collaborate. We'd love to see that happen.

Join us on the [AlmaLinux Community Chat](https://chat.almalinux.org/almalinux/channels/migration) for help and assistance.

All your contributions, feedback and bug reports matter to AlmaLinux. You can also reach out to us on [Twitter](https://twitter.com/almalinux) and [Reddit](https://reddit.com/r/AlmaLinux).