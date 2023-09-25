---
title: "Welcome new repositories for AlmaLinux OS: Testing and Synergy"
type: blog
author: 
 name: "Andrew Lukoshko"
 bio: "Release Engineering Lead"
 image: /users/alukoshko.jpg
date: '2023-08-24'
post:
    title: "Welcome new repositories for AlmaLinux OS: Testing and Synergy"
    image: /blog-images/new-repos-announcement.png
---

Hello, Community! Since [AlmaLinux OS has shifted its direction to RHEL compatibility](https://almalinux.org/blog/future-of-almalinux/), we can now provide additional content for our community. For that reason, two additional repositories have been added - **Testing** and **Synergy**. Today, we are announcing that both repositories are available for AlmaLinux OS 8 and AlmaLinux OS 9. 

## Testing Repository

As we [mentioned last week](https://almalinux.org/blog/testers-needed-for-updated-packages-intel-and-amd-cpus-affected/), the Testing repository contains security updates that AlmaLinux OS is now able to release without waiting for the patches to be released upstream. As these packages require additional testing before being released, we invite the community to help test them and provide feedback. 

**Note:** The Testing repository is recommended only for non-production machines.

To enable the Testing repository on AlmaLinux machines, run the following command:

```bash
dnf install -y almalinux-release-testing
``` 

Users also can check available updates on [repo.almalinux.org](https://repo.almalinux.org/):
* [AlmaLinux OS 8](https://repo.almalinux.org/vault/8/testing/)
* [AlmaLinux OS 9](https://repo.almalinux.org/vault/9/testing/)

Grab the package you'd like to test and tell us how it works for you on [Bug Tracker](https://bugs.almalinux.org). 

## Synergy Repository

The Synergy repository is designed for any possible package that is not present in RHEL or EPEL yet, but has been requested by a member of the AlmaLinux community, for the community. While we do encourage and welcome contributions, as soon as the package appears to be in EPEL it will be removed from the Synergy repository. 

Moreover, this repository can be enabled for other distros in the Enterprise Linux Ecosystem like RHEL, CentOS, etc.

To enable the Synergy repository on AlmaLinux machines, run the following command:

```bash
dnf install -y almalinux-release-synergy
```

To enable the Synergy repository on other RHEL-compatible distributions run the following command:

```bash
dnf install -y https://repo.almalinux.org/almalinux/almalinux-release-synergy-latest-$(rpm -E %rhel).noarch.rpm
```

**Note:** Enabling the Synergy repository will also automatically enable EPEL and PowerTools/CRB repositories.

Available packages can also be found on [repo.almalinux.org](https://repo.almalinux.org/):
* [AlmaLinux OS 8](https://repo.almalinux.org/almalinux/8/synergy/)
* [AlmaLinux OS 9](https://repo.almalinux.org/almalinux/9/synergy/)

You can use the closest [mirror](https://mirrors.almalinux.org/isos.html) for faster access.

Currently, the repository contains packages for [Pantheon Desktop Environment](https://almalinux.org/blog/building-pantheon-for-almalinux-9/) and [Warpinator app](https://almalinux.org/blog/building-warpinator-for-almalinux/).

## Contribute and Get Help

These repos are managed by the [Core SIG](https://wiki.almalinux.org/sigs/Core.html), and you can find more information about all of the AlmaLinux OS available repositories on the [Repositories Wiki Page](https://wiki.almalinux.org/repos/), including the requirements for packages to be considered for adding to Synergy. 

Responsible persons for repositories:
* Testing Repository - [Eduard Abdullin](https://chat.almalinux.org/almalinux/messages/@eabdullin)
* Synergy Repository - [Sonia Boldyreva](https://chat.almalinux.org/almalinux/messages/@sonyasulu)

Join [Packaging chat channel](https://chat.almalinux.org/almalinux/channels/engineeringpackaging) to request packages, discuss anything, or ask for assistance.

We are grateful for all contributions from our community and are still encouraging everyone to contribute not only to AlmaLinux, but to the full EL ecosystem.
