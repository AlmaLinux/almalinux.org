---
title: "Spring 2025 Raspberry Pi Updates"
type: blog
author:
  name: "Koichiro Iwao"
  bio: "Engineer at Cybertrust Japan"
  image: /users/koichiroiwao.jpg
date: '2025-03-19'
#images:
post:
  title: "Spring 2025 Raspberry Pi Updates"
---

Hello, Community! I'm excited to share the latest updates on Raspberry Pi with you.

## AlmaLinux OS Kitten 10 is now available for Raspberry Pi

As you might have already noticed, AlmaLinux OS Kitten 10 is now available for Raspberry Pi! Visit [AlmaLinux OS Kitten 10 page](https://wiki.almalinux.org/development/almalinux-os-kitten-10.html#raspberry-pi) for details.

Both the console image and the GNOME image are available, along with previous versions; however, the MBR version has been omitted to reduce development effort. Therefore, only images with a GUID partition table are available in AlmaLinux OS Kitten 10, which means that the Raspberry Pi 3+ is no longer supported.

If you have feedback, join AlmaLinux Community Chat in the [SIG/AltArch](https://chat.almalinux.org/almalinux/channels/sigaltarch) channel or file an issue at AlmaLinux Raspberry Pi [repository](https://github.com/AlmaLinux/raspberry-pi). 

## Boot order can now be changed using only AlmaLinux 

A new package `rpi-eeprom` is now available on AlmaLinux.  It is a tool to update Raspberry Pi 4 / 5 bootloader EEPROM and configuration.

Previously, to change the boot order of Raspberry Pi, the `rpi-eeprom-config` tool included in the official [Raspberry Pi OS](https://www.raspberrypi.com/software/) was required.  However, it is now possible to change the bootloader config such as boot order using only AlmaLinux!  The tool is available on all AlmaLinux versions, 8, 9 and Kitten 10.

For detailed instructions, please refer to the [Raspberry Pi page on AlmaLinux wiki](https://wiki.almalinux.org/documentation/raspberry-pi.html#configure-boot-order).