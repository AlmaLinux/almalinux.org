---
title: "AlmaLinux with Raspberry Pi 5 Support!"
type: blog
author:
  name: "Koichiro Iwao"
  bio: "Engineer at Cybertrust Japan"
  image: /users/koichiroiwao.jpg
date: 2024-06-11
images:
  - /blog-images/2024/2024-06-11-almalinux-support-for-raspberry-pi-5.png
post:
  title: "AlmaLinux with Raspberry Pi 5 Support!"
  image: /blog-images/2024/2024-06-11-almalinux-support-for-raspberry-pi-5.png
---

Raspberry Pi 5 support has been much anticipated in the AlmaLinux community, and today we are very excited to share great news. AlmaLinux now has support for Raspberry Pi 5!

## How it all started

When I joined the AlmaLinux Community, I had a keen interest in Raspberry Pi images. Raspberry Pi is widely known for its role in teaching computing and programming and is also a favorite among DIY enthusiasts. Living in Japan, where the [Raspberry Pi community](https://www.raspi.jp/) is exceptionally active, I felt inspired to have a hand in boosting the popularity of AlmaLinux OS.

There were already existing Raspberry Pi images, so I began contributing by updating them. The release of Raspberry Pi 5 in October 2023, with its significant upgrades and improvements, brought even more interest in AlmaLinux for Raspberry Pi. As requests for updated images started to appear, I felt motivated to continue my contributions. AlmaLinux's commitment to providing top-notch software support and user experience only fueled my enthusiasm further. This is what drives me to remain actively involved in the AlmaLinux Raspberry Pi community.

## Working Process

Typically, the kernels used to build AlmaLinux Raspberry Pi images were created by [Pablo Greco](https://github.com/psgreco) from CentOS. However, the process is quite challenging and, like any open-source project, it benefits from contributions. This challenge intrigued me, so I decided to get involved.

My first step was to learn the Raspberry Pi boot process to build AlmaLinux's kernel package based on the [Raspberry Pi kernel](https://github.com/raspberrypi/linux), which is a fork of the Linux kernel. Although I had previously contributed to AlmaLinux Raspberry Pi images, I didn't know much about the boot process. It took considerable time and effort to successfully build a kernel on my ARM environment, overcoming failed builds and boot issues along the way. These attempts allowed me to understand the Raspberry Pi boot process more deeply and identify what was going wrong.

Another challenge was understanding the differences between Pi 4 and Pi 5. Gathering all this information helped me [rebase](https://git.almalinux.org/rpms/raspberrypi2/commit/1168a780efe6f8d86e678019ee7dcb487ea774cd) the kernel to [Raspberry Pi OS sources](https://github.com/raspberrypi/linux/tags), resulting in a successfully working kernel for Raspberry Pi 5.

The final step involved updating the Raspberry Pi [firmware](https://git.almalinux.org/rpms/linux-firmware-raspberrypi/commit/e043d6736dc9b886f4904a5a5a5af9ce1289137b) package. With everything in place, the [build scripts](https://github.com/AlmaLinux/raspberry-pi) were ready to create images with Raspberry Pi 5 support.

### Special Thanks

I would like to express my gratitude to a fellow Japanese Raspberry Pi enthusiast whose invaluable assistance with testing helped with polishing and improving AlmaLinux Raspberry Pi images. Thank you, [Akkie](https://magpi.raspberrypi.com/articles/interview-akkie) for your support!

## Get AlmaLinux for Raspberry Pi

AlmaLinux provides standard Raspberry Pi images and with GNOME desktop environment. You can get the images from the [AlmaLinux website](https://almalinux.org/get-almalinux). The installation [guide](https://wiki.almalinux.org/documentation/raspberry-pi.html) is available on the Wiki.

## Contribute

If you're passionate about Raspberry Pi and would like to contribute, join AlmaLinux Community Chat in the [SIG/AltArch](https://chat.almalinux.org/almalinux/channels/sigaltarch) channel and explore AlmaLinux Raspberry Pi [repository](https://github.com/AlmaLinux/raspberry-pi). We look forward to welcoming you!
