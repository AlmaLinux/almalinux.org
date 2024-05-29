---
title: "Announcing AlmaLinux 8.9 Stable!"
type: blog
author:
 name: "Jack Aboutboul"
 bio: "AlmaLinux Community Manager"
 image: /users/jack.jpg
date: '2023-11-21'
images:
  - /blog-images/23.11.21.89stable.jpg
post:
    title: "Announcing AlmaLinux 8.9 Stable!"
    image: /blog-images/23.11.21.89stable.jpg

---

# AlmaLinux 8.9 Stable Now Available 

Hello Сommunity! The AlmaLinux OS Foundation is proud to announce the general availability of [AlmaLinux OS 8.9](https://mirrors.almalinux.org/isos.html) codenamed "Midnight Oncilla"! 

Installation ISOs are available on the mirrors now for all 4 architectures:
* [Intel/AMD (x86_64)](https://mirrors.almalinux.org/isos/x86_64/8.9.html)
* [ARM64 (aarch64)](https://mirrors.almalinux.org/isos/aarch64/8.9.html)
* [IBM PowerPC (ppc64le)](https://mirrors.almalinux.org/isos/ppc64le/8.9.html)
* [IBM Z (s390x)](https://mirrors.almalinux.org/isos/s390x/8.9.html)

Torrents are available as well at:
* [Intel/AMD (x86_64)](https://repo.almalinux.org/almalinux/8.9/isos/x86_64/AlmaLinux-8.9-x86_64.torrent)
* [ARM64 (aarch64)](https://repo.almalinux.org/almalinux/8.9/isos/aarch64/AlmaLinux-8.9-aarch64.torrent)
* [IBM PowerPC (ppc64le)](https://repo.almalinux.org/almalinux/8.9/isos/ppc64le/AlmaLinux-8.9-ppc64le.torrent)
* [IBM Z (s390x)](https://repo.almalinux.org/almalinux/8.9/isos/s390x/AlmaLinux-8.9-s390x.torrent)

## Update from Other AlmaLinux 8.x, ELevate from CentOS 7
Users of earlier versions of AlmaLinux 8.x can update to the latest version via `dnf update` or from graphical desktop tools.

Still on CentOS 7.x? Looking for a new home? [AlmaLinux's ELevate](https://almalinux.org/elevate/) enables migration between major versions of RHEL® derivatives. Move from CentOS 7.x to AlmaLinux 8.x or 9.x, or another derivative.

Running another 8.x? Move to AlmaLinux using [almalinux-deploy](https://github.com/AlmaLinux/almalinux-deploy).


## Live Images, Cloud and Containers

AlmaLinux also offers a variety of Cloud, Container and Live Images. The builds for these get kicked off as soon as the public repository is ready. **The following images are expected to be available shortly.** 

We will post a separate "Images Update" announcement soon, to keep the community informed.

* [Docker](https://wiki.almalinux.org/containers/docker-images.html#about-almalinux-docker-images) images including Platform and UBIs alternatives. We provide a wide variety of containers for your use. Please see our [Docker Official Image](https://hub.docker.com/_/almalinux) as well as [all AlmaLinux images](https://hub.docker.com/u/almalinux). 

**IMPORTANT!** The `latest` and `minimal` tags now point to the latest AlmLinux 9 version. If you're using these tags and want to stay on AlmaLinux 8 please update your Dockefiles.

* [LXC/LXD](https://images.linuxcontainers.org/images/almalinux/) 

* [Live Media](https://wiki.almalinux.org/LiveMedia.html) for GNOME, GNOME-mini, KDE, XFCE, MATE and more.
* Cloud Images 
    * [AWS AMIs](https://wiki.almalinux.org/cloud/AWS.html) for x86_64 and Graviton Instances
    * [Azure](https://wiki.almalinux.org/cloud/Azure.html) Images for the standard and HPC flavors for x86_64 and aarch64 
    * [Google Cloud](https://wiki.almalinux.org/cloud/Google.html) 
    * [Generic Cloud/Cloud-init](https://wiki.almalinux.org/cloud/Generic-cloud-on-local.html) for all 4 architectures
    * [Open Nebula](https://wiki.almalinux.org/cloud/OpenNebula.html) for all 4 architectures
    * [Oracle Cloud Infrastructure](https://wiki.almalinux.org/cloud/OCI.html) for x86_64 and aarch64
* [Vagrant Boxes](https://app.vagrantup.com/almalinux):
    * Libvirt
    * VirtualBox
    * Hyper-V
    * VMWare
    * Parallels 

* [Raspberry Pi](https://wiki.almalinux.org/documentation/raspberry-pi.html)
* [Windows Subsystem for Linux](https://wiki.almalinux.org/documentation/wsl.html)

## Release Notes and More Information

AlmaLinux 8.9 continues to deliver enhanced security, better performance, and improved management capabilities. This release also introduces updates to container management and automation processes along with enhancements to the web console that make management tasks easier. Moreover, users now can configure health check actions, allowing for better monitoring and maintenance of the system.

You can read more about this release by checking out the [Release Notes](https://wiki.almalinux.org/release-notes/8.9.html).

## Join us on Mastodon!
Have you jumped on Mastodon yet? Follow us! [@almalinux@fosstodon.org](https://fosstodon.org/@almalinux)

## Pitch In

Join us in the [AlmaLinux Community Chat](https://chat.almalinux.org) to get any assistance you need and help others. You can also post a question on our [8.9 Forum](https://forums.almalinux.org/c/devel/8-9-stable/41) or on our AlmaLinux Community on [Reddit](https://reddit.com/r/almalinux). Catch us on [Twitter](https://twitter.com/almalinux) and follow us on Mastodon [@almalinux@fosstodon.org](https://fosstodon.org/@almalinux)

Please report any bugs you may see on the [Bug Tracker](https://bugs.almalinux.org/). 

As always, an extra special thank you to the Fedora and RHEL teams at Red Hat, in the community and beyond. We stand on the shoulders of giants.

Enjoy the release and have fun! 
