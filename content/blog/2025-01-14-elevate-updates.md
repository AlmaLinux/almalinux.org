---
title: "ELevate Project Updates"
type: blog
author:
  name: "Yuriy Kohut"
  bio: "ELevate Project Engineer @ CloudLinux"
  image: /users/yuriy-kohut.jpg
date: 2025-01-14
images:
  - /blog-images/2025/2025-01-14-elevate-updates.png
post:
  title: "ELevate Project Updates"
  image: /blog-images/2025/2025-01-14-elevate-updates.png
---

Hello everyone! We’ve got some updates about the ELevate Project to share with you today :)

### New Upgrade Path Available

We are excited to announce that the upgrade path from AlmaLinux OS 9 to AlmaLinux 10.0 beta is now available in ELevate NG.

**Please note: This upgrade is for testing purposes only and is not intended for production environments.**

The AlmaLinux 9 to AlmaLinux 10 beta upgrade is a crucial part of our ongoing preparations for the version 10.0 stable release, expected in Q2. Early testing allows us to identify and address potential issues and before the stable release ensuring the stable upgrade for users.

We'd love the community to help us try and test this new upgrade path and share their experiences. Your input will directly contribute to the quality and development of the final release.

Detailed instructions for testing this migration can be found [here](https://wiki.almalinux.org/elevate/ELevate-NG-testing-guide.html#prepare-the-system-for-upgrade-to-almalinux-10).

Please, report any bugs you may see to the [ELevate leapp repository](https://github.com/AlmaLinux/leapp-repository).

**"Will I be able to use ELevate to upgrade from 10 beta to 10 stable when it's released?"**

When 10 stable is released, ELevate will support upgrades from version 9 to 10 stable. However, ELevate will not support upgrades from 10 beta to 10 stable. You can update systems running 10 beta using the regular update process with detailed instructions that will be provided in the release notes.

### General Updates and Changelog

We have made some adjustments to our supported distributions. As of October 23, 2024, [EuroLinux is no longer being distributed](https://docs.euro-linux.com/), and as a result the ELevate Project will no longer support upgrading to EuroLinux. This decision allows us to focus our resources on maintaining actively supported distributions.

Additionally, we have updated the project to include the latest features, fixes, and updates. See the [changelog](https://wiki.almalinux.org/elevate/Changelog.html) to stay in the loop.

### Contribute and Get Help

We thank you for your continued support and contributions to the ELevate Project and AlmaLinux OS.

Have feedback, questions, or just want to join the discussion? Join us in the ~migration channel on the [AlmaLinux Community Chat](https://chat.almalinux.org/almalinux/channels/migration).

**Happy testing!**
