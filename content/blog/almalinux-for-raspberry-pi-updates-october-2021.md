---
title: "AlmaLinux For Raspberry Pi Updates - October 2021"
type: blog
author: 
 name: "theMayor"
 bio: "-"
 image: /users/jack.jpg
date: '2021-10-07'
post:
    title: "New Repo, Kernel 5.10.60, Working Wi-Fi!"
    image: /blog-images/almarpiupdate.png
---

Hello Everyone,

It's a great day for some tasty Pi! Today we're releasing some awesome Raspberry Pi updates. You can grab them from the [AlmaLinux Raspberry Pi](https://github.com/AlmaLinux/raspberry-pi/) Github Repo.

## New Raspberry Pi Repo

We've setup a new repo to host all Raspberry Pi packages at https://repo.almalinux.org/almalinux/8/raspberrypi/. This will enable super easy updates in the future and that should be syncing to all of our global mirrors.

## Kernel and (properly working!) Wi-Fi

We've bumped the `Kernel` to 5.10.60 and we've built a new `linux-firmware` package with [Matthias Brugger's RPi NVRAM](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/?id=58825f74eb0156822065c449a770644a69044d88) fix which enables the Wi-Fi to work right out of the box now.

## ` rootfs-expand`

Thanks to the the [great work](https://github.com/CentOS/sig-core-AltArch/blob/2eaa9c3ab33a7df96d0ac127c9667341c4b909db/centos-release/SPECS/centos-release.spec#L241) by [Fabian Arrotin](https://github.com/arrfab) expanding the rootfs is now as simple as running `rootfs-expand`.

Grab a copy pop it on your Pi and if you have any questions, would like to discuss anything or contribute, join us on the [AlmaLinux Community Chat](https://chat.almalinux.org/) the [Forums](https://forums.almalinux.org/) and [Reddit](https://reddit.com/r/almalinux).