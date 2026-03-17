---
title: "AlmaLinux goes RISC-V: Kitten 10 now available for riscv64"
type: blog
author:
  name: "Andrew Lukoshko"
  bio: "AlmaLinux Lead Architect"
  image: /users/alukoshko.jpg
date: 2026-03-17
images:
  - /blog-images/2026/2026-03-17-almalinux-goes-riscv.png
post:
  title: "AlmaLinux OS Kitten 10 is now built for riscv64 with repos, Docker containers, and GenericCloud images available. Hardware images for VisionFive 2 and P550 are coming soon."
  image: /blog-images/2026/2026-03-17-almalinux-goes-riscv.png
---

[RISC-V](https://riscv.org/) is a free and open instruction set architecture (ISA) based on RISC principles. Unlike proprietary ISAs such as x86 or ARM, the RISC-V specification is openly available, allowing anyone to implement it without licensing fees. Hardware platforms based on RISC-V are becoming more widely available, from microcontrollers to application-class processors capable of running full Linux distributions.

We are excited to announce that AlmaLinux OS Kitten 10 is now available for the RISC-V architecture.

## AlmaLinux Kitten 10 for riscv64

AlmaLinux OS Kitten 10 is built for the riscv64 architecture targeting the [RV64GC profile](https://docs.riscv.org/reference/profiles/rva20-rvi20-rva22/_attachments/RISC-V_Profiles.pdf). Package repositories are publicly available and served by the [AlmaLinux Mirror Service](https://mirrors.almalinux.org/) as usual, so you can install and update packages with `dnf` just like on any other supported architecture.

## Docker containers

Official Docker container images for AlmaLinux OS Kitten 10 riscv64 are available now. If you're on an x86_64 or aarch64 host, you can run them using QEMU user-mode emulation:

```bash
docker run -it --rm --platform linux/riscv64 almalinux:10-kitten bash
```

Make sure you have QEMU user-static and binfmt_misc configured on your host for cross-architecture emulation. On most systems this can be set up with:

```bash
docker run --rm --privileged tonistiigi/binfmt --install riscv64
```

## GenericCloud VM image

A GenericCloud VM image with cloud-init support is also available for riscv64. This image can be used with QEMU to run AlmaLinux OS Kitten 10 RISC-V virtual machines, making it easy to test and develop for the architecture without dedicated hardware.

## Hardware images: VisionFive 2 and P550

Images for the [StarFive VisionFive 2](https://www.starfivetech.com/en/site/boards) (JH7110) and the [SiFive HiFive Premier P550](https://www.sifive.com/boards/hifive-premier-p550) (ESWIN EIC7700) will be available very soon. Support for these platforms was [recently merged](https://gitlab.com/redhat/centos-stream/src/kernel/centos-stream-10/-/merge_requests/1517) into the CentOS Stream 10 kernel, and we are working on producing ready-to-use images for both boards.

## Get involved!

RISC-V is an exciting and fast-moving ecosystem, and we'd love your help testing and improving AlmaLinux on this platform. If you have RISC-V hardware or are running riscv64 containers or QEMU VMs, please share your experience with us.

Report any bugs on [bugs.almalinux.org](https://bugs.almalinux.org), join the conversation in the [SIG/AltArch](https://chat.almalinux.org/almalinux/channels/sigaltarch) channel on our Mattermost chat, or post on our [forums](https://almalinux.discourse.group/).

Follow us on [Reddit](https://www.reddit.com/r/AlmaLinux/), [X](https://twitter.com/AlmaLinux), [Mastodon](https://fosstodon.org/@almalinux/), [LinkedIn](https://www.linkedin.com/company/80320905/), and [YouTube](https://www.youtube.com/channel/UCt9lpkqUPp1FUEi9uqVlPQA).
