---
title: "Enabling CRB by default for AlmaLinux 10"
type: blog
author:
  name: "Neal Gompa"
  bio: "Principal Consultant, Velocity Limitless; AlmaLinux Engineering Steering Committee member"
  image: /users/nealgompa.png
date: "2025-09-08"
images:
  - /blog-images/2025/crb_enabled_almalinux10.png
post:
  title: "Enabling CRB by default for AlmaLinux 10"
  image: /blog-images/2025/crb_enabled_almalinux10.png
---

AlmaLinux OS 10 will have the CRB repository turned on by default via an update in AlmaLinux OS 10.0 on **2025-09-09**, while AlmaLinux OS Kitten 10 has had it enabled by default since the update on 2025-08-27 (`almalinux-kitten-repos-10.0-9.el10.0.1`).

As part of our efforts to continue improving the experience for AlmaLinux users, we are enabling the CRB repository by default. This reduces the friction in using software from Fedora Extra Packages from Enterprise Linux (EPEL).

## What is the CRB repository?

The CRB repository is an extra collection of packages that have not been historically made available by default for enterprise Linux distributions. A lot of the packages are primarily useful for developing software, but CRB also includes requirements for a number of popular packages (such as the KDE Plasma Desktop) that are not needed for the core enterprise Linux solution set.

## Why are we enabling it by default?

Have you ever seen errors like this one?

```shell
Error:
 Problem: package plasma-discover-6.3.6-1.el10_0.aarch64 from epel requires libDiscoverCommon.so()(64bit), but none of the providers can be installed
  - package plasma-discover-6.3.6-1.el10_0.aarch64 from epel requires plasma-discover-libs(aarch-64) = 6.3.6-1.el10_0, but none of the providers can be installed
  - conflicting requests
  - nothing provides libAppStreamQt.so.3()(64bit) needed by plasma-discover-libs-6.3.6-1.el10_0.aarch64 from epel
(try to add '--skip-broken' to skip uninstallable packages or '--nobest' to use not only best candidate packages)
```

This is the result of trying to install packages from [EPEL](https://docs.fedoraproject.org/en-US/epel/) that depend on packages that are in the CRB repository while the repository is not enabled on the system. Many users trip up on this, and it results in a lot of erroneous bug reports about broken dependencies being filed with EPEL maintainers.

## If I already have AlmaLinux OS 10 / AlmaLinux OS Kitten 10, what will happen?

The CRB repository will be enabled moving forward by setting `enabled=1` in `almalinux-crb.repo`. [Here](https://git.almalinux.org/rpms/almalinux-release/commit/4ad4fbd62a25032d5f11e665393d109b0f5ff9b8) is the commit with the change. This change will apply to all existing AlmaLinux OS systems shortly in order to prepare for AlmaLinux OS 10.1.

## If I don't want it enabled, how can I disable it?

There are various ways to disable the CRB repository after this change takes effect. The easiest way is to use `config-manager`, which is part of the `dnf-utils` package:

```shell
# Disable the CRB repository
dnf config-manager --disable crb
```

## New selinux-policy-extra package for AlmaLinux OS 10.1

Speaking of EPEL, the forthcoming AlmaLinux OS 10.1 release will introduce a new `selinux-policy-extra` package in the CRB repository, which will be necessary for software from EPEL to work properly with SELinux. For systems upgrading after AlmaLinux OS 10.1 is released, `selinux-policy-extra` will get installed during the upgrade if the CRB repository is enabled.

As part of preparing for this change and resolving the larger usability issues with leveraging packages from EPEL, the AlmaLinux Engineering Steering Committee (ALESCo) has approved [a change to AlmaLinux that enables the CRB repository by default](https://github.com/AlmaLinux/ALESCo/blob/master/rfcs/0006-enable-crb-on-almalinux-10.md). This will apply to all installs so that the `selinux-policy-extra` package will be available and installed when `epel-release` is installed.

## What can you do to help?

Your input into testing and feedback is crucial and essential for any change we make, so please do let us know if you encounter any problems or have any questions! You can report any bugs you may see on the [Bug Tracker](https://bugs.almalinux.org/). Also, pop into the [AlmaLinux Community Chat](https://chat.almalinux.org), post a question on the [AlmaLinux Community Forums](https://forums.almalinux.org/), on our AlmaLinux Community on [Reddit](https://reddit.com/r/almalinux), or catch us on [Bluesky](https://bsky.app/profile/almalinux.org).
