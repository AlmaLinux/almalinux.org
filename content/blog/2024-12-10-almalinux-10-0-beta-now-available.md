---
title: "AlmaLinux 10.0 Beta Now Available"
type: blog
author:
 name: "Eduard Abdullin"
 bio: "The Release and Automation Engineer."
 image: /users/eduard-abdullin.jpg
date: '2024-12-10'
images:
  - /blog-images/2024/2024-12-10-10-0-beta.png
post:
    title: "AlmaLinux 10.0 Beta Now Available"
    image: /blog-images/2024/2024-12-10-10-0-beta.png

---

Hello Community! 

The AlmaLinux OS Foundation is announcing the availability of AlmaLinux 10.0 Beta "Purple Lion" for all supported architectures:
* Intel/AMD (x86_64)
* Intel/AMD (x86_64_v2)
* ARM64 (aarch64)
* IBM PowerPC (ppc64le)
* IBM Z (s390x)

Beta ISOs are available at [repo.almalinux.org](https://repo.almalinux.org/almalinux/10.0-beta/isos/). 

### Beta or Kitten?

[Newly introduced AlmaLinux OS Kitten](https://almalinux.org/blog/2024-10-22-introducing-almalinux-os-kitten/) is designed to serve for development and preparation purposes for the next AlmaLinux OS version. Kitten aims to bring more transparency, engagement, and  provide deeper insights into our build process. 

The astute AlmaLinux user will notice that some of the software versions in AlmaLinux OS Kitten 10 are newer than what you will find in the AlmaLinux 10 beta release. That is because Kitten is based on CentOS Stream, and AlmaLinux 10 follows Red Hat 10's release versions. It should not be anticipated that Kitten is or will be exactly what will be provided in the BETA version.

Beta releases continue to provide our community with early access to new features and enhancements, allowing testing and encouraging our community to provide valuable feedback before the stable launch.

A usual reminder: this is a **BETA** release. It should not be used for production installations. The provided upgrade instructions should not be used on production machines unless you don't mind if something breaks. If you are looking to see how things going to work in stable, you are on the right track.

## Release Notes, Stable Release Date, and More Information

AlmaLinux 10.0 Beta brings significant enhancements across core components enhancing development, security, and performance workflows. New versions of programming languages, toolchains, and compilers give developers access to the latest tools. Updates to control systems, servers, and databases aim to improve system performance and scalability.

As for security, this release introduces post-quantum cryptography support and updates to SELinux and OpenSSH. A new sudo system role simplifies configuration management across multiple systems, while new tools like Sequoia PGP expand encryption options.

This version of AlmaLinux also brings with it some deviations from RHEL 10.0, that are fully outlined in the release notes for AlmaLinux 10. We anticipate the stable release of AlmaLinux 10 coming in Q2 of next year.

You can read the full release notes for this version on the wiki: [AlmaLinux OS 10.0 Release Notes](https://wiki.almalinux.org/release-notes/10.0-beta.html).

## What can you do to help?

Your input into testing and feedback is crucial and essential for successful production releases. 
Please, report any bugs you may see on the [Bug Tracker](https://bugs.almalinux.org/). Also, pop into the [AlmaLinux Community Chat](https://chat.almalinux.org) and join our Testing Channel, post a question on our [10.0 Beta Forum](https://forums.almalinux.org/), on our AlmaLinux Community on [Reddit](https://reddit.com/r/almalinux) or catch us on [X](https://twitter.com/almalinux). 

Enjoy this Beta release, let us know what you think and stay tuned.

**Happy Testing!**
