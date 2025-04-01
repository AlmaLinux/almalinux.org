---
title: "ELevate Project Updates"
type: blog
author: 
 name: "Yuriy Kohut"
 bio: "ELevate Project Engineer @ CloudLinux"
 image: /users/yuriy-kohut.jpg
date: 2025-04-01
images:
  - /blog-images/2025/2025-04-01-elevate-updates.png
post: 
    title: "ELevate Project Updates"
    image: /blog-images/2025/2025-04-01-elevate-updates.png
---

Hello everyone! We’ve got ELevate Project updates to share.

The ELevate Project currently follows 3 stages for delivering updates:

* New upgrade paths, features, bug fixes, and new versions of leapp-repository and leapp-data are first introduced in **ELevate NG**. The AlmaLinux Team, along with the community, tests these enhancements.
* ELevate NG then moves to general **Testing**, during which it gathers additional data, features, and improvements.
* Once these updates are thoroughly tested and approved, the AlmaLinux Team releases them to **ELevate Stable**.

Today's changes are available in **ELevate NG** and **ELevate Testing**. We expect them to be released to Stable after the general availability of AlmaLinux OS 10 Stable.

### ELevate Testing Changes

Previously we've announced new upgrade paths available as a part of ELevate NG: 
* AlmaLinux OS 9 to AlmaLinux 10.0 beta.
* CentOS Stream 9 to CentOS Stream 10.

**Please note: These upgrades are for testing purposes only and are not intended for production environments.**

These paths are now available as a part of ELevate Testing. This means that when AlmaLinux 10.0 Stable is released, these paths will be updated for ELevate Stable.

### ELevate NG Changes

Based on our community requests, we've added an upgrade path to ELevate NG - to AlmaLinux Kitten 10.

Additionally, we have updated ELevate NG to include leapp-repository upstream version [0.22.0](https://github.com/AlmaLinux/leapp-repository/pull/139) with the latest fixes and EL 10 support.

### Call for Testers

We welcome the community to help us test these new upgrade paths and share their experiences. Your input will directly contribute to the quality and development of the final release. 

Detailed instructions for testing this migration can be found:
* [ELevate Testing](https://wiki.almalinux.org/elevate/ELevate-testing-guide.html)
* [ELevate NG](https://wiki.almalinux.org/elevate/ELevate-NG-testing-guide.html)

Please, report any bugs you may see to the [ELevate leapp repository](https://github.com/AlmaLinux/leapp-repository).

### Will I be able to use ELevate to upgrade from 10 beta to 10 stable when it's released?

When 10 stable is released, ELevate will support upgrades from version 9 to 10 stable. However, ELevate will not support upgrades from 10 beta to 10 stable. You can update systems running 10 beta using the regular update process with detailed instructions that will be provided in the release notes. 

### Contribute and Get Help

We thank you for your continued support and contributions to the ELevate Project and AlmaLinux OS. 

Have feedback, questions, or just want to join the discussion? Join us in the ~migration channel on the [AlmaLinux Community Chat](https://chat.almalinux.org/almalinux/channels/migration).

**Happy testing!**
