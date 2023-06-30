---
title: "Our Value Is Our Values"
type: blog
author: 
 name: "Jack Aboutboul"
 bio: "AlmaLinux Community Manager"
 image: /users/jack.jpg
date: '2023-06-30'
post:
    title: "Updates for the AlmaLinux OS Community around the current post-RHEL news status."
    image: /blog-images/23.06.30.values.png
---

As we [discussed last week](https://almalinux.org/blog/impact-of-rhel-changes/), on June 21 Red Hat [announced](https://www.redhat.com/en/blog/furthering-evolution-centos-stream) that RHEL source code will only be available via the Red Hat Customer Portal.

## What is the status of security updates?

Prior to Red Hat's policy change, when RHEL published a package update of any sort (security or bugfix), they published the corresponding source code into a [repository](http://git.centos.org). Then AlmaLinux integrated the update into our own build and test system, produced a new RPM, and published it to our repositories.

The first part of that chain is now broken. Only Red Hat customer accounts can access Red Hat Software, and it is a violation of the Red Hat Subscription Agreement to re-distribute Red Hat Software, which includes using it in a downstream rebuild.

From a security and update perspective, this makes our job more difficult, but by no means impossible. Let's use OpenSSL as an example since it's a crucial package that (like all packages) occasionally issues security updates. The following timeline may be instructive, and demonstrates our ability to provide security updates to our users.

-   RHEL 9.2 shipped with OpenSSL 3.0.7 on May 10. That source code was published [here](https://git.centos.org/rpms/openssl/tree/f856de47f51f8c949c41527034be360d859d5489).
-   AlmaLinux 9.2 also shipped with OpenSSL 3.0.7 on May 10.
-   Upstream OpenSSL published [CVE-2023-2650](https://www.openssl.org/news/secadv/20230530.txt) on May 30, with a fix available in OpenSSL 3.0.9.
-   RHEL 9.2 [published](https://access.redhat.com/errata/RHSA-2023:3722) a patched OpenSSL 3.0.9 on June 21.
-   AlmaLinux [published](https://errata.almalinux.org/9/ALSA-2023-3722.html) OpenSSL 3.0.9 on June 23.

We've been evaluating several ways to build updates. As we outlined in our previous post, "[Impact of RHEL changes to AlmaLinux](https://almalinux.org/blog/impact-of-rhel-changes/)", we will continue to put out updates as quickly as we can produce them. The process is more labor intensive as we require gathering data and patches from several sources, comparing them, testing them, and then building them for release. But rest assured, updates will continue flowing just as they have been.

## Our Value is our Values

When executed properly, downstream rebuilds provide tremendous value and are a tremendous asset to upstream projects. AlmaLinux aims to deliver the best possible outcomes; for the broader open-source community, for our upstream, and the Enterprise Linux ecosystem as a whole.

In the interests of communal ownership and transparency within the broader open-source community, we set up a non-profit to steer clear of any semblance of a corporate motive. We publish our bank statements. We invest significant time and effort to ensure ground rules exist so that anyone coming from the CentOS community has a place to go and feel safe to contribute. Some may write that off, but the rage that pervaded the community at the time AlmaLinux began made it clear that there was a void that needed to be filled with something positive.

For the Enterprise Linux ecosystem, we prevented fragmentation by [enabling use of the CentOS SIGs](https://almalinux.org/blog/announcing-centos-sig-repository-availability-in-almalinux/) within AlmaLinux, a move that other downstreams emulated. We advocated for [RHEL build roots in the CentOS Build system](https://pagure.io/centos-infra/issue/400) for this purpose as well. This ensured that work and effort would stay centralized and keep code flowing upstream. We expanded platform support to a new architecture -- Raspberry Pi -- and helped the ELRepo project secure a sponsorship for aarch64 hardware, to build for it. We currently have close to 80,000 aarch64 systems running AlmaLinux. We also made monetary contributions and participated in Fedora Flock, Nest, CentOS Connect and Dojos, and even openSuse Conf. Part of the draw of a product or distribution is the community around it, and we've enriched the community around RHEL and CentOS Stream.

We have also enriched the upstream community. AlmaLinux community members have submitted PRs to projects such as RPM, AWX, and VirtualBox. Our community has sent over 50 PRs to GlusterFS and also extended [openQA](https://news.opensuse.org/2023/05/30/almalinux-contributes-to-openqa-addes-support-features/). A Red Hat employee even thanked us for enabling Fedora tests to run on [ELN](https://docs.fedoraproject.org/en-US/eln/) and RHEL. An AlmaLinux contributor (who was formerly an ArchLinux user) was so fired up by our community that he now maintains over 600 Fedora and [Extra Packages for Enterprise Linux](https://docs.fedoraproject.org/en-US/epel/) (EPEL) packages, including some widely-used ones like certbot, brotli, iperf3, imapsync, and countless Python libraries, many of them as the primary contributor maintaining them for the greater Fedora and Enterprise Linux ecosystem. [EPEL](https://docs.fedoraproject.org/en-US/epel/) is tremendously important to both Red Hat and RHEL users.

AlmaLinux, as a downstream of RHEL and as a community, has demonstrated our value both to Red Hat and to the open-source community at large. We're strongly committed to the principles upon which open-source was founded and which the community expects -- trust, transparency, honesty, integrity, and mutual respect. In short, our value is our values.