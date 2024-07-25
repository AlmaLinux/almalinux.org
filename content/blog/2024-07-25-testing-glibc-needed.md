---
title: "Testers needed: glibc regression in 9.4"
type: blog
author: 
 name: "Andrew Lukoshko"
 bio: "Release Engineering Lead"
 image: /users/alukoshko.jpg
date: 2024-07-25
images:
  - /blog-images/2024/2024-07.glibcblog.png
post: 
    title: "Testers needed: glibc regression in 9.4"
    image: /blog-images/2024/2024-07.glibcblog.png
---

# Testers needed: glibc regression in 9.4

Recently, the VFX community was faced with a regression in [glibc](https://en.wikipedia.org/wiki/Glibc) causing instabiltiy for very common some software in RHEL 9.4 and distributions based on it. The fix has been available upstream, but has not yet been released. We need your help testing the fix before we consider releasing it ourselves.

## The backstory

In May, VFX users in the AlmaLinux community were attemping to upgrade their devices to AlmaLinux 9.4 and found that, after the upgrade, SideFX's Houdini software was crashing when performing random operations. It was confirmed that this was true upstream, and was therefore reported correctly there (more details: https://issues.redhat.com/browse/RHEL-39415).

The fix has been available since the end of June, is already in glibc upstream, and has been merged into CentOS Stream 9, but has not yet been released in CentOS Stream 9 or in RHEL 9.4. This blocks the VFX community, and anyone else anyone running an Enterprise Linux distribution based on RHEL 9, stuck on version 9.3 and not getting security updates. 

While this is not a bug we would normally fix before it is merged into RHEL, we see the needs of our community and are strongly considering it. These users remain unpatched for all security and bug updates that are already a part of 9.4, including the recently patched [regreSSHion](https://almalinux.org/blog/2024-07-01-almalinux-9-cve-2024-6387/) bug.

However, due to the importance of the glibc library we know that very careful testing by both the AlmaLinux team and our users is necessary.

## Where did AlmaLinux get the patch?
This is a constant source of confusion for people who aren't familiar with the development process, so we want to be very clear: our patch is taken from the same place that RHEL's patch will come from: the CentOS Stream 9 [merge request](https://gitlab.com/redhat/centos-stream/rpms/glibc/-/merge_requests/176).

## How do I install the updated packages?
We encourage users both in the VFX community and in other places to participate in testing the fix by doing the following:
```bash
dnf install almalinux-release-testing --refresh
dnf update glibc*
```
Then use your system as usual, run services and applications, etc.

## How can I leave my feedback?
Join the [Development](https://chat.almalinux.org/almalinux/channels/development) channel in our Mattermost chat and share your hardware specs, experience with the update. If everything works just fine let us know as well.

