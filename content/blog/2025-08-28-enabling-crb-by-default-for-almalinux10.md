---
title: "Enabling CRB by default for AlmaLinux 10"
type: blog
author:
 name: "Neal Gompa"
 bio: "Principal Consultant, Velocity Limitless; AlmaLinux Engineering Steering Committee member"
 image: /users/nealgompa.png
date: '2025-08-28'
images:
  - /blog-images/2025/crb_enabled_almalinux10.png
post:
    title: "Enabling CRB by default for AlmaLinux 10"
    image: /blog-images/2025/crb_enabled_almalinux10.png

---

AlmaLinux OS 10 and AlmaLinux OS Kitten 10 will have the CRB repository enabled by default.

As part of our efforts to continue improving the experience for AlmaLinux users, we are enabling the CRB repository by default.
This reduces the friction in using software from Fedora Extra Packages from Enterprise Linux (EPEL).

## What is the CRB repository?

The CRB repository is an extra collection of packages that have not been historically made available by default.
A lot of the packages are primiarly useful for developing software,
but it also includes software that is used by a number of popular packages (such as the KDE Plasma Desktop, among others)
that are not needed for the core Enterprise Linux solution set.

## Why are we enabling it by default?

Have you ever seen errors like this one?

```
Error: 
 Problem: package plasma-discover-6.3.6-1.el10_0.aarch64 from epel requires libDiscoverCommon.so()(64bit), but none of the providers can be installed
  - package plasma-discover-6.3.6-1.el10_0.aarch64 from epel requires plasma-discover-libs(aarch-64) = 6.3.6-1.el10_0, but none of the providers can be installed
  - conflicting requests
  - nothing provides libAppStreamQt.so.3()(64bit) needed by plasma-discover-libs-6.3.6-1.el10_0.aarch64 from epel
(try to add '--skip-broken' to skip uninstallable packages or '--nobest' to use not only best candidate packages)
```

This is the result of trying to install packages from EPEL that depend on packages that are in the CRB repository and the repository is not enabled on the system.
Many users trip up on this and it results in a lot of bug reports about broken dependencies to EPEL maintainers.

Speaking of EPEL, the forthcoming AlmaLinux OS 10.1 release will introduce a new `selinux-policy-extra` package in the CRB repository,
which will be necessary for software from EPEL to work properly with SELinux.
For systems upgrading after AlmaLinux OS 10.1 releases, `selinux-policy-extra` will get installed during the upgrade if the CRB repository is enabled.

As part of preparing for this change and resolving the larger usability issues with leveraging packages from EPEL,
the AlmaLinux Engineering Steering Committee (ALESCo) has approved [a change to AlmaLinux that enables the CRB repository by default](https://github.com/AlmaLinux/ALESCo/blob/master/rfcs/0006-enable-crb-on-almalinux-10.md).
This will apply to all installs so that the `selinux-policy-extra` package will be available and installed when `epel-release` is installed.
