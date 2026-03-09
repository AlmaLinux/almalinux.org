---
title: "AlmaLinux and NVIDIA Streamline Driver and CUDA Updates"
type: blog
author:
  name: "Jonathan Wright"
  bio: "Infrastructure SIG lead & ALESCo member"
  image: /users/jonathan.jpg
date: 2026-03-09
images:
  - /blog-images/2026/2026-02-26-nvidia-cuda-updates.png
post:
  title: "AlmaLinux and NVIDIA Streamline Driver and CUDA Updates"
  image: /blog-images/2026/2026-02-26-nvidia-cuda-updates.png
---

[Last August](https://almalinux.org/blog/2025-08-06-announcing-native-nvidia-suport/) we started shipping NVIDIA's open GPU kernel modules, and saw incredible amounts of adoption and excitement about that announcement!

Today we are excited to share that with the release of version 13.2, NVIDIA has added official support for enterprise Linux compatible distributions, including AlmaLinux, to CUDA. That means that users of NVIDIA hardware can receive support for NVIDIA drivers and CUDA on AlmaLinux within NVIDIA's supported configurations.

We are also excited to be able to ship NVIDIA's CUDA drivers in an official AlmaLinux repository - streamlining updates and uses of NVIDIA for AlmaLinux users worldwide.

## What changed?

NVIDIA has added official support for enterprise Linux compatible distributions, including AlmaLinux, ensuring that our users can get support from NVIDIA when using NVIDIA infrastructure.

We also now have an agreement with NVIDIA that allows us to distribute NVIDIA's packages directly from our repositories, rather than users getting the drivers separately from us.

## Why the change?

Right now, when NVIDIA releases a new driver, there is a very slight delay in our release of the updates, which can result in brief version mismatches for users of NVIDIA hardware and AlmaLinux. Shipping the open source drivers along with the userspace and CUDA components ourselves means that all the packages are updated in tandem. There won't be any delay between the release of the two package sets, ensuring the versions are always in sync.

You will notice that the userspace and CUDA component RPMs are signed by NVIDIA, and are being distributed from nvidia.repo.almalinux.org instead of being distributed through the [AlmaLinux Mirror System](https://mirrors.almalinux.org/). We are only redistributing those packages that NVIDIA builds, not building them ourselves. The open source drivers will continue to be built and signed by us.

## How to see what version of the NVIDIA packages you are using right now

For anyone that was already using our release of the open source NVIDIA drivers on AlmaLinux, the changes will be completely transparent. The next time you update, the packages will be updated to point to the correct versions without you having to make any changes at all.

If you are curious, you can confirm you are using the packages from AlmaLinux by running the following commands in your terminal application:

`rpm -q almalinux-release-nvidia-driver`

For example, for AlmaLinux 9 and 10:

### AlmaLinux OS 9

[root@alma9-nvidia ~]# rpm -q almalinux-release-nvidia-driver
almalinux-release-nvidia-driver-9-4.el9.x86_64

### AlmaLinux OS 10

```
[root@alma10-nvidia ~]# rpm -q almalinux-release-nvidia-driver
almalinux-release-nvidia-driver-10-4.el10.x86_64
```

If you see DNF errors, it may mean that you have installed NVIDIA packages directly or have other conflicts. We can help on [chat.almalinux.org](http://chat.almalinux.org)!

## How you can give help, or get it!

We would love to hear feedback from anyone who gets a chance to use these new packages in testing or production. If you have any questions or would like some community support, please join us in [chat.almalinux.org](http://chat.almalinux.org).
