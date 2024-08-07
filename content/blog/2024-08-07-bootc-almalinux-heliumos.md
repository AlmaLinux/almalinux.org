---
title: "Bringing bootc to AlmaLinux"
type: blog
author: 
 name: "Isaac Beverly"
 bio: "Developer, HeliumOS"
 image: /users/imbev.jpg
date: 2024-08-07
images:
  - /blog-images/2024/
post: 
    title: "Bringing bootc to AlmaLinux"
    image: /blog-images/2024/
---

bootc is a new deployment method that powers [Image mode for RHEL](https://www.redhat.com/en/about/press-releases/red-hat-reimagines-enterprise-linux-ai-future-image-mode-red-hat-enterprise-linux) and [HeliumOS](https://www.heliumos.org/), a new Linux distribution. We are excited to announce that AlmaLinux now offers [bootc images for Intel/AMD(x86_64)](https://quay.io/repository/almalinuxorg/almalinux-bootc?tab=tags).

## How did this start?
My goal as developer of HeliumOS is to produce a Linux-based desktop operating system that is user-friendly, stable, and reliable. The first foray towards this goal used a Debian base, however this had some issues:

- Debian has 3-5 years of support. Though stable relative to most Linux distributions, I wanted more stability.
- An unexpected interruption during a traditional Linux package manager update can render the system un-bootable or otherwise broken.

2 months ago, I learned of Image mode for RHEL, a new method of deploying RHEL that used OCI images for updates. Rebasing on Enterprise Linux and using bootc, the technology behind Image mode for RHEL would solve both of the issues that I found with Debian. After various experiments, HeliumOS [announced](https://www.heliumos.org/blog/post/heliumos-v9-alpha-is-available-for-downlaod/) an Alpha release based on CentOS Stream.

Despite solving several issues, rebasing on CentOS Stream introduced new problems:

- CentOS Stream has a minor-rolling release schedule. This meant that Nvidia drivers and other software that require a specific version of the Linux kernel would be more difficult to distribute.
- CentOS Stream only has 5 years of support. This may be acceptable for some usage, but limits HeliumOS usage in other environments with longer lifecycle requirements.

A small hop to a minor-stable Enterprise Linux distribution such as AlmaLinux would resolve both issues.

Through collaboration with the AlmaLinux [Virt and Container SIG](https://chat.almalinux.org/almalinux/channels/sigvirtcontainer), and with help from the [Fedora bootc chat](https://matrix.to/#/#bootc:fedoraproject.org), we have setup workflows to produce AlmaLinux bootc images. Updates and new releases to HeliumOS going forward will be delivered through bootc images derived from AlmaLinux.

## What are OCI containers and images?

[OCI](https://opencontainers.org/) containers provide an isolated environment running on a container runtime such as Podman or containerd(Docker). Software deployed via a typical OCI container will use the host system's kernel and a portable environment delivered via an OCI image.

Deployment of software via OCI images is especially useful because application dependencies are resolved during image build. OCI containers can be built and deployed to any system with an OCI container runtime without the deployed system needing to be concerned with dependency resolution.

## What are atomic Linux distributions?

Atomic operations execute as a single unit. When applied to Linux distributions, updates either successfully update the system, or completely fail, with no intermediate state. There are many implementations of this system: Fedora Silverblue using rpm-ostree, VanillaOS using ABRoot, openSUSE MicroOS using BTRFS snapshots, even Android using GKI+Modules.

## What is bootc?

[bootc](https://containers.github.io/bootc/) is a tool that uses bootc-compatible OCI images and OSTree to deploy updates to a Linux system in an atomic fashion. By bundling the Linux kernel and other essential components within an OCI image with the proper SELinux configuration, the image's root file system becomes more suitable for booting. On the deployment system, bootc maps the OCI image to a format compatible with OSTree. OSTree then treats the image as any other OSTree commit. After a reboot, the system automatically reboots into the new update. The bootloader also offers an option to rollback to a previous image. Distributions can use bootc to provide atomic updates with the convenience of existing OCI infrastructure and tooling.

## What's next?

HeliumOS development continues, from Nvidia Driver support in HeliumOS, to distribution-agnostic tools such as [bootc-gtk](https://codeberg.org/HeliumOS/bootc-gtk). We're hoping for a stable release based on AlmaLinux 10 in 2025. If you have any questions or would like to contact me for other reasons, you can find me in the HeliumOS [Matrix Space](https://matrix.to/#/#heliumos:matrix.org), AlmaLinux [Mattermost Server](https://chat.almalinux.org), or Fedora bootc [Matrix Room](https://matrix.to/#/#bootc:fedoraproject.org).
