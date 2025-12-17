---
title: "Major ELevate updates - AlmaLinux now supported in upstream LEAPP"
type: blog
author:
  name: "Andrew Lukoshko"
  bio: "Lead Architect"
  image: /users/alukoshko.jpg
date: "2025-12-15"
images:
  - /blog-images/2025/2025-12-elevate-updates.png
post:
  title: "Major ELevate updates - AlmaLinux now supported in upstream LEAPP"
  image: /blog-images/2025/2025-12-elevate-updates.png
---

Earlier this year at [DevConf](https://www.devconf.info/cz/), I learned of some upcoming changes that were going to impact ELevate. The work with the team at Red Hat has completed, and we are excited to say that, as of November 18th, [the newest update to ELevate](https://wiki.almalinux.org/elevate/Changelog.html) has been released.

## What is ELevate?

In case you have not yet heard of ELevate: ELevate is an AlmaLinux project that, since 2021 has provided the ability to upgrade between major versions of RHEL-based distributions.

ELevate has two components: updates to [the open source LEAPP project](https://github.com/AlmaLinux/leapp-repository/tree/almalinux), and a data library called [leapp-data](https://github.com/AlmaLinux/leapp-data). These together allow users to upgrade in-place from an unsupported operating system to a modern operating system, and then from 8 to 9 and 9 to 10 of that operating system.

In the years [since ELevate was first announced](/blog/announcing-elevate-migration-between-major-versions-7x-to-8x-of-rhel-derivative-distributions/) four years ago, we have removed support for both Oracle Linux and CentOS Stream, and added support for [upgrading from CentOS 6](/blog/2024-04-25-elevate-supports-centos-6-to-centos-7/), [Scientific Linux 7](/blog/2024-08-08-elevate-release/), and for upgrading to enterprise linux versions of all kinds to 9 and 10. This update is maybe our most disruptive yet.

## What changed?

With the release of leapp-repository 0.23.0, two big things changed. First, LEAPP now supports CentOS Stream natively, and the LEAPP team accepted a pull request to add [AlmaLinux](https://github.com/oamg/leapp-repository/pull/1391) support as well. That significantly reduces the amount of work that we have to maintain in ELevate.

Second, they updated the format of the migration data (the data the describes the package upgrade paths). That meant that all supported OSes needed to have their migration data updated to retain supporting upgrades.

## Our commitment to ELevate users

AlmaLinux and CentOS Stream will be supported upgrade paths in ELevate for the long-term, and will be maintained by us in upstream LEAPP. We would love to see contributions from any additional operating systems that would like to see support in ELevate. They will need to have that support added both to the upstream leapp-repository, and to ELevate.

## We want to hear from you!

We take feedback in the form of issues and pull requests on our own [leapp-repository](https://github.com/AlmaLinux/leapp-repository) repo, or as part of a discussion in the ~Migration channel on [chat.almalinux.org](https://chat.almalinux.org), and can't wait to hear from you!
