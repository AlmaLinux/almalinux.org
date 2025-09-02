---
title: "Expanding ELevate support: CentOS 6 to CentOS 7 migrations"
type: blog
author:
  name: "Yuriy Kohut"
  bio: "ELevate Project Engineer @ CloudLinux"
  image: /users/yuriy-kohut.jpg
date: "2024-04-25"
images:
  - /blog-images/2024/2024-04-23-centos6-to-centos7.png
post:
  title: "Expanding ELevate support: CentOS 6 to CentOS 7 migrations"
  image: /blog-images/2024/2024-04-23-centos6-to-centos7.png
---

Last month we [highlighted](https://almalinux.org/blog/2024-03-26-almalinux-march-events-roundup/) our achievements from the CloudFest Hackathon, including our work on a significant improvement for the ELevate project. The Hackathon Team started working on enabling the migration of CentOS 6 machines to CentOS 7 within the [ELevate Project](https://wiki.almalinux.org/elevate/).

Today, we are proud to announce that CentOS 6 to CentOS 7 migrations are now a reality in ELevate, making this migration available to users.

### The reasons behind

One of the ways that CloudLinux gives back to the open source community is to contribute to and enhance the enterprise linux ecosystem beyond just the AlmaLinux Community. Alongside the community, we do our best to cover AlmaLinux users' needs.

The security of infrastructure globally is always at risk. Upgrading between major versions of an operating system in the Enterprise Linux ecosystem has always required downtime and migrating your data in some way. This barrier to keeping operating systems up to date is something we wanted to be able to help out with.

### How we did it

In case you aren't familiar, [ELevate](https://almalinux.org/elevate/) uses the [Leapp utility](https://leapp.readthedocs.io/) and [a few patches](https://github.com/AlmaLinux/leapp-repository/commits/almalinux) to perform upgrades from CentOS 7 to one of the supported operating systems. That doesn't help anyone who is still using CentOS 6, however.

The Leapp utility isn't suitable for this use case, so we had to find another way. Our Hackathon Team's research found another migration tool - Red Hat's open source [Red Hat Upgrade Tool](https://github.com/upgrades-migrations/redhat-upgrade-tool.git). While the work at the Hackathon didn't get beyond that research, we continued the work after the Hackathon, and were able to modify that tool to perform the CentOS 6 to CentOS 7 upgrade.

In the process of adapting that tool from initially supporting only Red Hat OS, we made a lot of changes, including disabling the Red Hat management system and related code, and patches to add CentOS branding.

The ELevate project now [provides](https://repo.almalinux.org/elevate/el6/) the tool, packages, and the CentOS 6 Vault repository file for simplicity and user's convenience. In the [AlmaLinux Wiki](https://wiki.almalinux.org/elevate/ELevating-CentOS6-to-CentOS7.html) you can find a guide that covers this migration.

### Limitations and a warning

In its current form, the CentOS 6 to CentOS 7 migration is only available for x86_64 architecture machines. If you need to see it expanded, come talk to us to see how you can contribute!

The most successful migration approach we found is divided into 2 stages:<br> 1. Migration from CentOS 6 to CentOS version 7.2.1511 (this is the last CentOS version that supports the Red Hat Upgrade Tool and is necessary for migration data).<br> 2. Updating the system to the CentOS version 7.9.2009.

As always, **The most important thing you can do is take system backups or snapshots.** We also **HIGHLY** recommend doing a trial run in a sandbox to verify that migration worked as expected before you attempt to migrate any production system.

## Contribute and Get Help

We welcome any feedback on the CentOS 6 to CentOS 7 migration. Share it in the [SIG/Migration](https://chat.almalinux.org/almalinux/channels/migration) chat channel, and join it for any help, assistance or a discussion ;)

For those interested in getting involved and sharing your knowledge, we welcome you to contribute to the [Migration SIG](https://wiki.almalinux.org/sigs/Migration.html#how-to-join) projects, [documentation](https://wiki.almalinux.org/Contribute-to-Documentation.html), write a [blog post](https://github.com/AlmaLinux/almalinux.org/blob/master/contributing-blog-posts.md) or participate in [Q&A videos](https://almalinux.org/blog/2024-01-16-video-contributions/).
