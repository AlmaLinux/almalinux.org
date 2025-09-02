---
title: "Secure boot with AlmaLinux"
type: blog
author:
  name: "Sofia Boldyreva"
  bio: "Technical Writer for AlmaLinux OS Project"
  image: /users/sofia-boldyreva.png
date: 2024-04-11
images:
  - /blog-images/2024-04-08-secure-boot.png
post:
  title: "Secure boot with AlmaLinux"
  image: /blog-images/2024-04-08-secure-boot.png
---

The new AlmaLinux releases are coming shortly (expect our beta releases for 9.4 and 8.10 over the next couple of weeks!), and we'd like to talk about one of the vital components of each system - its security. It's important to keep your system secure and one of the easiest ways that is rarely talked about is by enabling Secure Boot.

AlmaLinux OS has provided Secure Boot since its [8.4 release](https://wiki.almalinux.org/release-notes/8.4.html).

### About Secure Boot

In case you are not yet familiar, [Secure Boot](https://en.wikipedia.org/wiki/UEFI#Secure_Boot) is a security feature built to ensure that only trusted software can run during the boot process. This feature helps prevent malicious software or unauthorized code from being loaded at boot time. Secure Boot verifies the signature of the operating system during boot-up, providing additional protection against malware and unauthorized access.

AlmaLinux uses the shim bootloader to support Secure Boot - an open-source bootloader that creates trust between the UEFI firmware and the operating system during the boot process. Shim ensures that the boot process remains secure by verifying the signature of the boot loader before loading the operating system.

The AlmaLinux shim is officially signed by Microsoft and currently trusts 2 certificates. You can find more details about the trusted certificates and a bunch of other AlmaLinux security features on the [Security page](https://almalinux.org/security/).

### Checking your Secure Boot state

We highly recommend enabling Secure Boot on your AlmaLinux System.

Note: before completing the steps below, ensure that your machine supports UEFI Secure Boot.

You can use the mokutil tool to check whether or not Secure Boot is enabled on your system already. Run the following command in the terminal:

```bash
mokutil --sb-state
```

The output will display whether the Secure Boot is enabled or disabled.

To enable Secure Boot on your machine, enter the BIOS/UEFI settings during the boot process (usually done by pressing a key like F2, F10, F12, or Delete during bootup). Then, look for the Secure Boot option and enable it. Save the changes and restart your system for Secure Boot to be active.

If you running AlmaLinux on a virtual machine, we recommend enabling Secure Boot in the settings at creation time. Steps to do so are outlined in a few different guides, like the [Fedora guide](https://docs.fedoraproject.org/en-US/quick-docs/uefi-with-qemu/) and [Virtuzzo guide](https://docs.virtuozzo.com/virtuozzo_hybrid_server_7_users_guide/managing-virtual-machines-and-containers/performing-virtual-machine-specific-operations.html#enabling-secure-boot-for-virtual-machines).

### More Security Features

As I mentioned earlier, we believe strongly in security and have worked to provide both the features and the guides that you might need to build a secure environment. Check out our comprehensive list of [Security Measures](https://almalinux.org/security/) to enhance your AlmaLinux system's security even more.

### Interested in sharing your knowledge?

Feel like getting involved and sharing your knowledge? We welcome you to get involved with contributing to the [documentation](https://wiki.almalinux.org/Contribute-to-Documentation.html), writing a [blog post](https://github.com/AlmaLinux/almalinux.org/blob/master/contributing-blog-posts.md) or participating in [Q&A videos](https://almalinux.org/blog/2024-01-16-video-contributions/).
