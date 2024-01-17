---
title: "Announcing CentOS SIG Repository Availability in AlmaLinux"
type: blog
author: 
 name: "Jack Aboutboul"
 bio: "-"
 image: /users/jack.jpg
date: '2021-09-01'
post:
    title: "Enabling Use of Native CentOS SIGs in AlmaLinux"
    image: 
---

Hello Community. One of the top requests our team gets and many of the support inquiries that come our way are related to enabling, installing, or working with software from the [CentOS SIGs](https://wiki.centos.org/SpecialInterestGroup). For those who are unfamiliar with SIGs, they are Special Interest Groups (SIG) within the CentOS community that focus on a small set of issues, in order to either create awareness or to focus on development along a specific topic. Some of the more popular SIGs are the [Storage SIG](https://wiki.centos.org/SpecialInterestGroup/Storage), [Virtualization SIG](https://wiki.centos.org/SpecialInterestGroup/Virtualization) and the [Hyperscale SIG](https://wiki.centos.org/SpecialInterestGroup/Hyperscale).

SIGs release their own repositories which contain the packages from their work. Previously, in order to use SIGs you would need to manually find the correct repository, download and then install the relevant `centos-release-*` packages in order to enable that repository. This is problematic and not very user-friendly to say the least. Some in the community have even asked us if we’re planning to rebuild the SIG packages and offer them as our own (more on that below).

We thought of a better solution.

## What is AlmaLinux doing with CentOS SIGs?

Today we are announcing that upstream CentOS Special Interest Groups’ release packages are now available in AlmaLinux’s repository, making it easy to enable SIG repositories via `dnf`. You can find more details about each of the available SIGs and how to enable them on the [AlmaLinux Wiki CentOS SIGs Repositories Page](https://wiki.almalinux.org/repos/CentOS.html).

Some of the SIG repositories you can easily enable right now in AlmaLinux:

- [Cloud SIG](https://wiki.centos.org/SpecialInterestGroup/Cloud)

OpenStack Train/Ussuri/Victoria

- [Config Management SIG](https://wiki.centos.org/SpecialInterestGroup/ConfigManagementSIG)

Ansible 2.9

- [Messaging SIG](https://wiki.centos.org/SpecialInterestGroup/Messaging)

Qpid Proton 0.30

Rabbit 3.8

- [Network Functions Virtualization SIG](https://wiki.centos.org/SpecialInterestGroup/NFV)

HAProxy 2.2

Openvswitch 2.13

OVN 20.12.0

- [Ops Tools SIG](https://wiki.centos.org/SpecialInterestGroup/OpsTools)

collectd 5

- [Storage SIG](https://wiki.centos.org/SpecialInterestGroup/Storage)

Ceph 14 (Nautilus) / 15 (Octopus) / 16 (Pacific)

GlusterFS 6/7/8/9

NFS Ganesha 2.8/3

Samba 4.11/4.12/4.13/4.14

- [Virtualization SIG](https://wiki.centos.org/SpecialInterestGroup/Virtualization)

Kata Containers 2.0

Libguestfs 1.44

Libvirt 7.0

QEMU-KVM 5.2

## Our motivation

In a word, community. Couldn’t we just rebuild the CentOS SIG repositories? Yes, but the CentOS ecosystem already has many great people working on a variety of initiatives. Rather than distract from those efforts by rebuilding, offering and eventually maintaining (post CentOS 8 EOL) the SIG packages for ourselves, we’d like to support the community’s existing work, participate in, and help improve the SIG process. Let’s keep building–together.

By encouraging developers/contributors interested in the various SIG development to work upstream and submit contributions there (and submit bugs there: https://wiki.centos.org/ReportBugs), we can ensure this work remains centralized and continues to be part of the long-term stability, success, health and vitality of the community.

There are also many changes underway now that the shift to CentOS Stream has begun which will affect how SIGs are built moving forward, with most of them focusing on Stream.

## What about the upcoming CentOS 8 EOL and the Stream Transition?

CentOS SIGs currently can build their packages against CentOS 8 and CentOS Stream 8. The upcoming CentOS 8 EOL presumably means that in the future SIGs would only be able to build against CentOS Stream 8. One might expect that the CentOS 8 repositories from the SIGs would become EOL along with the CentOS 8 distribution. However, we’ve proposed a solution to that problem.

Instead of building against CentOS 8 and CentOS Stream 8, SIGs should build against RHEL 8 and CentOS Stream 8! This would ensure that the SIGs’ output is consumable by the entire RHEL family of distributions, including rebuilds like AlmaLinux. While this is not currently possible today, we have [officially requested](https://pagure.io/centos-infra/issue/400) RHEL build targets in the CentOS Community Build Service. We hope this will be approved and implemented. The feedback in favor of this method has been overwhelmingly positive from SIG maintainers so far, as well as from RHEL business leaders (see video linked in the issue above).

We’d like to thank the community for their contributions, questions and comments on these issues. Your feedback and bug reports are so important to making AlmaLinux better. Please join us on the [AlmaLinux Community Chat](https://chat.almalinux.org/) and on the [AlmaLinux Community Forums](https://forums.almalinux.org/) for any help and assistance or to discuss anything announced here. You can also follow us on [Twitter](https://twitter.com/almalinux) and [Reddit](https://reddit.com/r/AlmaLinux).
