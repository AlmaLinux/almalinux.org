---
title: "Azure Marketplace Updates"
type: blog
author:
  name: "Elkhan Mammadli"
  bio: "AlmaLinux OS Cloud engineer"
  image: /users/elkhan.jpg
date: "2024-10-09"
images:
  - /blog-images/2024/azure-marketplace-updates.png
post:
  title: "Azure Marketplace Updates"
  image: /blog-images/2024/azure-marketplace-updates.png
---

Hello Community! We'd like to share a quick update for our AlmaLinux Azure users.

If you've been using the original AlmaLinux Azure image for **x86_64** architecture (VM Image URN: `almalinux:almalinux:*`), you may have gotten an email like this:

> _Your Workloads are running on images that will be deprecated soon_
>
> _You're receiving this email because you have virtual machine and/or virtual machine scale set deployments that are running on images scheduled for deprecation._
>
> _One or more offers from the publisher, almalinux, have been scheduled for deprecation. You currently have workloads that are running on images within these offers._
>
> **_Impact_**
>
> • _Following the scheduled deprecation date, you won't be able to deploy any additional virtual machine (VM) or virtual machine scale set (VMSS) instances using any images within these offers._
>
> • _Your active VM instances won't be affected following the deprecation date._
>
> • _Your existing VMSS deployments will continue to be operational but can't be scaled out following deprecation._

That notice is being sent because we have set that image to be **deprecated and removed from the Azure Marketplace on 30 Dec 2024**. It is important to note, however:

- Your active VM instances **won’t be affected** following the deprecation date, and **will still receive regular updates**.

This change comes as part of our improved processes and partnership with Microsoft, which now allows us to provide enhanced AlmaLinux Core VM offer (VM Image URN: `almalinux:almalinux-x86_64:*`) on the Azure Marketplace. Providing an upgrade path of the existing offer wasn’t possible. Instead, we've decided to use this opportunity to create a new improved offer.

You can get current and up-to-date AlmaLinux Azure images on the Azure Marketplace:

- [AlmaLinux OS (x86_64/AMD64)](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/almalinux.almalinux-x86_64?tab=Overview)
- [AlmaLinux OS (AArch64/ARM64)](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/almalinux.almalinux-arm?tab=Overview)
- [AlmaLinux OS (x86_64/AMD64) HPC](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/almalinux.almalinux-hpc?tab=Overview)

For more details and guidelines, please, check the [Azure Wiki Page](https://wiki.almalinux.org/cloud/Azure.html).

## Get Help

For any help or assistance, please, join us at the _[SIG/Cloud & Virtualization](https://chat.almalinux.org/almalinux/channels/sigcloud)_ channel on [chat.almalinux.org](https://chat.almalinux.org/).
