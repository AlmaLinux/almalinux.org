---
title: "x86_64_v2 EPEL Now Covers AlmaLinux 10 Stable"
type: blog
author:
 name: "Eduard Abdullin"
 bio: "The Release and Automation Engineer."
 image: /users/eduard-abdullin.jpg
date: '2025-06-10'
images:
  - /blog-images/2025/2025-06-10-epel-v2-for-almalinux-10-available.png
post:
    title: "x86_64_v2 EPEL Now Covers AlmaLinux 10 Stable"
    image: /blog-images/2025/2025-06-10-epel-v2-for-almalinux-10-available.png

---

In March, [ALESCo approved a proposal](https://github.com/AlmaLinux/ALESCo/blob/master/rfcs/0001-build-fedora-epel-for-almalinux-and-almalinux-kitten-x86_64_v2.md) to build EPEL packages from Fedora’s source RPMs (SRPMs) to maintain long-term feature parity for our x86_64_v2 support initiative. [Last month these packages became available for AlmaLinux Kitten 10](https://almalinux.org/blog/2025-05-13-epel-10-kitten-v2/), and today we are happy to announce **x86_64_v2 EPEL support is now available for AlmaLinux 10 Stable** as well.

The EPEL package builds for AlmaLinux OS 10 stable are now complete and ready for use!

## How It Works

We monitor the [EPEL repository](https://dl.fedoraproject.org/pub/epel/10/Everything/source/tree/) for the latest stable packages, grab their SRPMs, and rebuild them using the [AlmaLinux Build System](https://build.almalinux.org/). These rebuilt packages are signed with a dedicated GPG key and then released to a [dedicated repository](https://epel.repo.almalinux.org). 

We also ensured that our EPEL packages have the `.alma_altarch` suffix for easy identification. 

## How To Use

EPEL support on x86_64_v2 works just like it [does](https://wiki.almalinux.org/repos/Extras.html#epel) on any other AlmaLinux system:

```
dnf install epel-release
```

Run the command in the terminal and you are good to go! 

## How To Report Bugs

If the RPM you're using has the `.alma_altarch` suffix and you face a bug, please, report it on the [AlmaLinux Bug Tracker](https://bugs.almalinux.org/). However, if the bug is reproducible on a non-_v2 system, using upstream EPEL, then the bug can be [reported to the EPEL packager](https://fedoraproject.org/wiki/EPEL/FAQ#Where_can_I_find_help_or_report_issues?) like normal. 

## Contribute and Get Help

Let us know how EPEL support for x86_64_v2 works for you! Join us on the [AlmaLinux Community Chat](https://chat.almalinux.org), [Reddit](https://reddit.com/r/almalinux), in the [Fediverse](https://fosstodon.org/@almalinux), or on [X](https://x.com/almalinux).

If you'd like to contribute to AlmaLinux and packaging, or have a question to discuss, check the [Core SIG](https://wiki.almalinux.org/sigs/Core.html).