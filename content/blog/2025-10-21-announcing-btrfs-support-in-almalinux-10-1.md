---
title: "Announcing Btrfs support in AlmaLinux OS 10.1"
type: blog
author:
  name: "Davide Cavalca"
  bio: "Production Engineer, Linux Userspace at Meta"
  image: /users/davidecavalca.png
date: "2025-10-21"
images:
  - /blog-images/2025/btrfs_almalinux101.png
post:
  title: "Announcing Btrfs support in AlmaLinux OS 10.1"
  image: /blog-images/2025/btrfs_almalinux101.png
---

# Announcing Btrfs support in AlmaLinux OS 10.1

AlmaLinux OS 10.1 will support the Btrfs filesystem, which has already been available in AlmaLinux OS Kitten since early September.

## What is Btrfs?

[Btrfs](https://btrfs.readthedocs.io/) is a modern Copy-on-Write (CoW) filesystem implementing advanced features while also focusing on fault tolerance, repair and easy administration. Among other things, it provides snapshotting, built-in volume management, checksumming for data and metadata, transparent compression and efficient copying via reflinks. These features lead to better performance for most common workloads and stronger resistance against bitrot and other potential issues with the underlying storage medium. Btrfs is already supported by a variety of Linux distributions, and is the default filesystem for several of them, notably Fedora Linux and openSUSE.

## What does making it available mean?

Btrfs support encompasses both kernel and userspace enablement, and it is now possible to install AlmaLinux OS with a Btrfs filesystem from the very beginning. Initial enablement was scoped to the installer and storage management stack, and broader support within the AlmaLinux software collection for Btrfs features is forthcoming.

Btrfs support in AlmaLinux OS did not happen in isolation. This was proposed and scoped in [RFC 0005](https://github.com/AlmaLinux/ALESCo/blob/master/rfcs/0005-enable-btrfs-as-tech-preview.md), and has been built upon prior efforts by the [Fedora Btrfs SIG](https://fedoraproject.org/wiki/SIGs/Btrfs) in Fedora Linux and the [CentOS Hyperscale SIG](https://sigs.centos.org/hyperscale/) in CentOS Stream.

## How can I use it?

To use Btrfs for your AlmaLinux OS deployment, simply go through the AlmaLinux OS installation process with AlmaLinux OS Kitten or AlmaLinux OS 10.1 and select custom partitioning. In the custom partitioning panel, you will be able to select a Btrfs partitioning scheme instead.

{{< figure src="/blog-images/2025/alma-btrfs-install.jpg" width="45%" alt="Installing AlmaLinux with the Btrfs filesystem" >}}
{{< figure src="/blog-images/2025/alma-btrfs-install-mountpoints.jpg" width="45%" alt="Customizing Btrfs filesystem mountpoints during the AlmaLinux installation" >}}

After that, AlmaLinux OS will be installed on a Btrfs volume instead of the default XFS+LVM configuration.

## What can you do to help?

We'd appreciate any feedback on this -- please let us know if you hit any issues or have questions. You can report any bugs on the [Bug Tracker](https://bugs.almalinux.org/), and connect with us in the [AlmaLinux Community Chat](https://chat.almalinux.org/), the [AlmaLinux Community Forums](https://forums.almalinux.org/), our AlmaLinux Community on [Reddit](https://reddit.com/r/almalinux), or on [Bluesky](https://bsky.app/profile/almalinux.org).
