---
title: "ELevate updates: upgrades to x86_64_v2 and from the installation ISO"
type: blog
author:
  name: "Yuriy Kohut"
  bio: "ELevate Project Engineer"
  image: /users/yuriy-kohut.jpg
date: 2026-11-20
images:
  - /blog-images/2026/2026-11-20-elevate-updates.png
post:
  title: "ELevate Stable now supports upgrades to AlmaLinux 10 x86_64_v2 and upgrades from the installation ISO for air-gapped systems, and is in sync with upstream leapp-repository 0.25.0."
  image: /blog-images/2026/2026-11-20-elevate-updates.png
---

Hello everyone! We are happy to share that a new release of ELevate, the AlmaLinux project for in-place upgrades between major versions of Enterprise Linux distributions, is now available in **ELevate Stable**. It brings the upgrade path to AlmaLinux OS 10 x86_64_v2, the ability to upgrade from the installation ISO on air-gapped systems, and a sync with the current upstream leapp-repository version 0.25.0.

## Upgrade to AlmaLinux 10 x86_64_v2

AlmaLinux OS 10 is built for the x86_64_v3 architecture level by default, and we also provide a parallel [x86_64_v2 build](/blog/2025-06-26-epel-v2-now-covers-almalinux-10-stable/) for older hardware. Earlier this year we [asked you to help us test](/blog/2026-04-20-elevate-ng-to-x86_64_v2/) the upgrade to that build in ELevate NG. Thank you to everyone who tried it and reported results!

The following upgrade paths are now part of ELevate Stable:

- AlmaLinux OS 9 to AlmaLinux OS 10 x86_64_v2.
- AlmaLinux OS 9 to AlmaLinux OS Kitten 10 x86_64_v2.

These paths use their own data packages, `leapp-data-almalinux-x86_64_v2` and `leapp-data-almalinux-kitten-x86_64_v2`, and an x86_64_v2 rootfs image that you download as part of the process. EPEL (Extra Packages for Enterprise Linux) is the 3rd-party repository currently supported for these paths.

Follow the [Upgrading AlmaLinux 9 to AlmaLinux 10 x86_64_v2](https://wiki.almalinux.org/elevate/ELevating-CentOS7-to-AlmaLinux-10.html#upgrading-almalinux-9-to-almalinux-10-x86-64-v2) instructions on the AlmaLinux Wiki.

## Upgrade from the installation ISO for air-gapped systems

ELevate can now perform the upgrade from a local installation DVD ISO image of the target OS instead of network repositories. Pass the image to leapp with the `--iso` option:

```bash
sudo leapp preupgrade --iso /root/AlmaLinux-10-latest-x86_64-dvd.iso
sudo leapp upgrade --iso /root/AlmaLinux-10-latest-x86_64-dvd.iso
```

The whole upgrade, including the phase that runs during the reboot, is then served from the ISO. This is available for the AlmaLinux OS 8 to 9 and AlmaLinux OS 9 to 10 upgrade paths, including AlmaLinux OS Kitten 10 and the x86_64_v2 variants.

A few things to keep in mind:

- The ISO replaces only the target OS packages source. The ELevate packages themselves still need to be installed on the system first.
- 3rd-party and CRB (CodeReady Builder) repositories are not on the installation media, so packages from them have to be handled after the upgrade.
- Serving local mirrors, as described in the [ELevate Offline Guide](https://wiki.almalinux.org/elevate/ELevate-offline-guide.html), remains available.

See [Upgrading air-gapped systems using the target OS installation ISO](https://wiki.almalinux.org/elevate/ELevating-CentOS7-to-AlmaLinux-10.html#upgrading-air-gapped-systems-using-the-target-os-installation-iso) for the details.

## In sync with upstream leapp-repository 0.25.0

ELevate is now based on the current upstream [leapp-repository 0.25.0](https://github.com/oamg/leapp-repository/releases/tag/v0.25.0), together with the leapp framework 0.21.0 and the upgrade data updated to the matching upstream state.

The release also includes a number of fixes, among them:

- The upgrade no longer ends up in the emergency shell on systems with LVM (Logical Volume Manager) on top of MD (software) RAID.
- Custom target repositories are accepted on systems managed by Foreman/Katello or private mirrors.
- For the CentOS 7 upgrade path, the upgrade to an OS of a different vendor is now stopped before the reboot when Secure Boot is enabled, instead of failing to boot afterwards.

The complete list of changes is in the [ELevate Changelog](https://wiki.almalinux.org/elevate/Changelog.html).

## Get started

The updated instructions can be found in the wiki:

- [ELevate Quickstart Guide](https://wiki.almalinux.org/elevate/ELevate-quickstart-guide.html)
- [ELevating CentOS 7 to AlmaLinux 10](https://wiki.almalinux.org/elevate/ELevating-CentOS7-to-AlmaLinux-10.html)

We highly recommend making backups and/or snapshots of your system before proceeding, and performing a trial run in a sandbox first.

## Contribute and get help

We thank you for your continued support and contributions to the ELevate Project and AlmaLinux OS.

Please report any bugs you may see to the [leapp-repository](https://github.com/AlmaLinux/leapp-repository) or [leapp-data](https://github.com/AlmaLinux/leapp-data). Do you have feedback, questions, or want to join the discussion? Join us in the ~migration channel on the [AlmaLinux Community Chat](https://chat.almalinux.org/almalinux/channels/migration).

If you want to stay up to date, follow us on [our forum](https://almalinux.discourse.group/), [Reddit](https://www.reddit.com/r/AlmaLinux/), [X](https://twitter.com/AlmaLinux), [Mastodon](https://fosstodon.org/@almalinux/), [LinkedIn](https://www.linkedin.com/company/80320905/), and [YouTube](https://www.youtube.com/channel/UCt9lpkqUPp1FUEi9uqVlPQA).

**Happy ELevating!**
