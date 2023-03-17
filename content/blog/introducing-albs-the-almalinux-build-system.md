---
title: "Introducing ALBS: The AlmaLinux Build System"
type: blog
author: 
 name: "themayor"
 bio: "-"
 image: /images/profile.png
date: '2022-07-08'
post:
    title: "The AlmaLinux Build System is now available. Read more to learn about the current features and roadmap."
    image: /blog-images/ALBS_Cover_Image.png
---

# ALBS: Announcing Our New AlmaLinux Build System - Achieving Transparency & Future Roadmap
We here at the AlmaLinux OS Foundation believe that making it easy for community members to build packages and images is a fundamental part of growing and ensuring a healthy enterprise Linux ecosystem. AlmaLinux is fully open source and supported by a growing list of members helping to improve each version. To that end, we started work long ago to make sure that our build system is also transparent and open for use by any organization that is interested in building a better Linux distribution.

Today we are glad to announce the first fruits of our efforts, ALBS, The AlmaLinux Build System. Our build system is available at: https://build.almalinux.org/.

It has been quite some time since we released the source for the AlmaLinux Build System by releasing it under GPLv3 license: https://github.com/AlmaLinux/build-system. However, code will only take you so far.

Since then, it has been bootstrapped, deployed, and used to build AlmaLinux OS 8.6 as well as AlmaLinux OS 9.0 for all four platforms: x86_64, Arm aarch64, PowerPC ppc64le & s390x. This system is also used to generate & publish errata and sign packages.

Today we are adding the next stage of transparency for our build processes by releasing anonymous, read-only access to our build system. This allows anyone to see what packages are being built right now, when a particular package was built, when a package build fails, and all the logs associated with the build process for each and every package.



The User Guide for the new version of the build system can be found on the github site: https://github.com/AlmaLinux/build-system/wiki/AlmaLinux-Build-System-User-Guide

In addition to this initial read-only access, we’ve begun building updates delivering fully functional OVAL files for use by OpenSCAP as well as any other security software. The OVAL files have all the errata information, as well as mitigation recommendations and support for modules too.

Information on OVAL Streams and files can be accessed in the wiki at https://wiki.almalinux.org/documentation/oval-streams.html.

## Future Roadmap

By the end of July, we plan to:

- Introduce a robust RBAC system to enable and grant access to maintainers and contributors from different organizations to build packages
- Add SBOM support for builds by integrating with CodeNotary ensuring package provenance and constitution is well documents and transparent
In the future, we are looking into:

- Implement Organization/SIG namespaces within the build system
- Add [COPR](https://copr.fedorainfracloud.org/) support
- Automate VM & container image building & publishing
The AlmaLinux OS Foundation wants to make it easy for people to build packages and images for the “Enterprise Linux” ecosystem for any organization that is interested in doing so.

## Help Us Build the Future

If you would like to participate - join us at on the AlmaLinux Community Chat at https://chat.almalinux.org, the AlmaLinux Community on [Reddit](https://reddit.com/r/almalinux) or catch us on [Twitter](https://twitter.com/almalinux).