---
title: "Linux Kernel 6.18 testing for Raspberry Pi"
type: blog
author:
  name: "Koichiro Iwao"
  bio: "AltArch SIG Lead for Raspberry Pi Builds, AlmaLinux OS Foundation"
  image: /users/koichiroiwao.jpg
date: "2026-04-29T13:00:00Z"
images:
  - /blog-images/2026/2026-04-29-pi-testing.png
post:
  title: "Linux Kernel 6.18 for Raspberry Pi is now available for testing in AlmaLinux OS! Try it out and let us know your feedback."
  image: /blog-images/2026/2026-04-29-pi-testing.png
---

As announced in the [Raspberry Pi Forum](https://forums.raspberrypi.com/viewtopic.php?t=394580), the kernel of Raspberry Pi OS is planning a move to 6.18, the next upstream LTS kernel version, in the near future.

We are also considering migrating our AlmaLinux images for Raspberry Pi to the 6.18 kernel, and we now offer a pre-release Raspberry Pi kernel for users interested in these cutting-edge updates.

The testing kernel is available for AlmaLinux OS 9 and 10 (and will be available for Kitten 10 as well). To use it, need to enable an additional repo, and reboot.

### To enable the testing repo

```bash
dnf copr --hub build.almalinux.org enable metalefty/raspberrypi-testing
dnf update
reboot
```

Please note that the testing kernel may be unstable and is not intended for production environments.

## Share your results!

We welcome your feedback, and are always interested in what you find. Please remember that reports confirming that no issues were encountered are equally important when validating the new kernel.

If you encounter any issues with the testing kernel, or even if you don't, please let us know! Bugs are best reported in our [bugtracker](https://bugs.almalinux.org)
or, you can share them with us in the
[SIG/AltArch](https://chat.almalinux.org/almalinux/channels/sigaltarch)
channel on Mattermost.
