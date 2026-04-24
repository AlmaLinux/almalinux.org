---
title: "Linux Kernel 6.18 is in testing for Raspberry Pi"
type: blog
author:
  name: "Koichiro Iwao"
  bio: "AltArch SIG Lead for Raspberry Pi Builds, Cybertrust Japan"
  image: /users/koichiroiwao.jpg
date: "2026-04-30"
---

As announced in the [Raspberry Pi Forum](https://forums.raspberrypi.com/viewtopic.php?t=394580), the kernel of Raspberry Pi OS is planned move to 6.18, the next upstream LTS, in the near future.

We are also considering migrating our AlmaLinux images for Raspberry Pi to the 6.18 kernel, and we now offer a pre-release Raspberry Pi kernel for users interested in cutting-edge updates.

The testing kernel is available for AlmaLinux 9 and 10 (and will be for Kitten 10). To use it, need to enable an additional repo:

```bash
dnf copr --hub build.almalinux.org enable metalefty/raspberrypi-testing
dnf update
```

and reboot.

Please note that the testing kernel may be unstable and is not intended for production environments.

## Share your results!

We welcome your feedback.
If you encounter any issues with the testing kernel, or even if you don't, please let us know at
[bugtracker](https://bugs.almalinux.org)
or
[SIG/AltArch](https://chat.almalinux.org/almalinux/channels/sigaltarch)
channel on Mattermost.

Reports confirming that no issues were encountered are equally important when validating the new kernel.
