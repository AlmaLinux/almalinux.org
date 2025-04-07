---
title: "Spring 2025 Raspberry Pi Updates"
type: blog
author:
  name: "Koichiro Iwao"
  bio: "Engineer at Cybertrust Japan"
  image: /users/koichiroiwao.jpg
date: '2025-04-07'
#images:
post:
  title: "Spring 2025 Raspberry Pi Updates"
---

Hello, Community! I'm pleased to share the latest updates on Raspberry Pi with you. Have fun on the Pi!

## AlmaLinux OS Kitten 10 is now available for Raspberry Pi

As you might have already noticed, AlmaLinux OS Kitten 10 is now available for Raspberry Pi! Visit [AlmaLinux OS Kitten 10 page](https://wiki.almalinux.org/development/almalinux-os-kitten-10.html#raspberry-pi) for details.

Both the console image and the GNOME image are available, along with previous versions; however, the MBR version has been omitted to reduce development effort. Therefore, only images with a GUID partition table are available in AlmaLinux OS Kitten 10, which means that the Raspberry Pi 3+ is no longer supported.

If you have feedback, join AlmaLinux Community Chat in the [SIG/AltArch](https://chat.almalinux.org/almalinux/channels/sigaltarch) channel or file an issue at AlmaLinux Raspberry Pi [repository](https://github.com/AlmaLinux/raspberry-pi).

## Updated Raspberry Pi images

All Raspberry Pi images including Kitten 10 have been updated to the latest packages as of the end of March 2025.

Please check out the following links for the updated images.

- [AlmaLinux 8](https://repo.almalinux.org/almalinux/8/raspberrypi/images/)
- [AlmaLinux 9](https://repo.almalinux.org/almalinux/9/raspberrypi/images/)
- [AlmaLinux Kitten 10](https://kitten.repo.almalinux.org/10-kitten/raspberrypi/images/)

## Boot order can now be changed using only AlmaLinux

A new package `rpi-eeprom` is now available on AlmaLinux. It is a tool to update Raspberry Pi 4 / 5 bootloader EEPROM and configuration.

Previously, to change the boot order of Raspberry Pi, the `rpi-eeprom-config` tool included in the official [Raspberry Pi OS](https://www.raspberrypi.com/software/) was required. However, it is now possible to change the bootloader config such as boot order using only AlmaLinux! The tool is available on all AlmaLinux versions, 8, 9 and Kitten 10.

For detailed instructions, please refer to the [Raspberry Pi page on AlmaLinux wiki](https://wiki.almalinux.org/documentation/raspberry-pi.html#configure-boot-order).

## A graphics issue with Raspberry Pi 5

[A graphics issue](https://bugs.almalinux.org/view.php?id=497) has been reported on Raspberry Pi 5. The issue was initially reported on the 16GB RAM model but is actually related to Pi 5 revision 1.1 (also called D0 stepping). Raspberry Pi 5 was initially released with two memory options: 4GB and 8GB. These models are rev 1.0, and the later-added 2GB and 16GB models were rev 1.1. Subsequently, the 4GB and 8GB models were also updated to rev 1.1 in late 2024. Therefore, if you purchase a Raspberry Pi 5 now, it is likely to be rev 1.1 and affected by this issue.

We, the development team, have obtained the latest Raspberry Pi 5 rev 1.1 and have just begun investigating the issue. Please bear with us as we work towards a solution.

See `/proc/cpuinfo` to check your Raspberry Pi 5 revision.


```bash
$ grep ^Model /proc/cpuinfo
Model           : Raspberry Pi 5 Model B Rev 1.0
```

For more information on the D0 stepping, please refer to this article by Jeff Geerling:
- [New 2GB Pi 5 has 33% smaller die, 30% idle power savings](https://www.jeffgeerling.com/blog/2024/new-2gb-pi-5-has-33-smaller-die-30-idle-power-savings)
