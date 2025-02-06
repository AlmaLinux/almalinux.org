---
title: "Introducing AlmaLinux OS Kitten"
type: blog
author: 
 name: "benny Vasquez & Neal Gompa"
 bio: "Chair of the Board, and ALESCo member"
 image: /users/bennyandneal.png
date: '2024-10-22'
images:
  - /blog-images/2024/introducingkitten.png
post:
    title: "Introducing AlmaLinux OS Kitten"
    image: /blog-images/2024/introducingkitten.png
---

Since the beginning of the AlmaLinux project, we have constantly been thinking about what comes next. Preparation has always been a cornerstone of AlmaLinux's release agility and speed has been our hallmark. Today, we're sharing another peak behind the curtain and showing off another cool thing we're doing to prepare for the next step.

## <u>AlmaLinux OS Kitten 10</u>

Since we started building AlmaLinux directly from the sources that Red Hat uses for Red Hat Enterprise Linux (RHEL), we have been able to deliver bug fixes and security patches faster than ever before for our community. We still keep our promise of compatibility with RHEL, and every deviation from RHEL is [recorded in our release notes](https://wiki.almalinux.org/development/Modified-packages.html), but our build and infrastructure teams have been embracing that freedom even more.

CentOS Stream 10, which will eventually be the source for RHEL10, has already started being built and is available for use today. Because we anticipated many changes in 10, we wanted to get a head start on building AlmaLinux OS 10. Earlier this year we started setting up infrastructure and the build pipeline for AlmaLinux OS 10, and started testing using CentOS Stream 10's code. Based on this preparation work, we are excited to share that we have successfully built a preview of AlmaLinux OS 10 that we are calling AlmaLinux OS Kitten 10. 

<small>Note: Our kitten is not related to [this one](https://www.sandia.gov/ccr/software/kitten-lightweight-kernel/) :D</small>

{{< figure src="/blog-images/2024/kitten10-screenshot.png" link="/blog-images/2024/kitten10-screenshot.png" caption="A screenshot of AlmaLinux OS Kitten 10" width="60%">}}


## <u>Why share this version of AlmaLinux with the world?</u>

Simply put, supporting our community with transparency and engagement. Earlier this year [Red Hat shared](https://www.redhat.com/en/blog/upcoming-improvements-red-hat-enterprise-linux-minor-release-betas) that they would no longer be releasing traditional betas for minor versions of RHEL. That automatically required that we shift our approach to building AlmaLinux for 10, and impacted our thought processes around AlmaLinux 9.5 (note: [the beta release of 9.5 dropped last week](/blog/2024-10-15-announcing-95-beta/)).

Releasing this version of AlmaLinux allows anyone who is building from or extending AlmaLinux (like the folks at [Cybertrust Japan with MIRACLE LINUX](/blog/2024-07-02-ctj-sponsorship/)) to engage in our release process sooner than they previously could, and gives our community even deeper insights into our build process.

## <u>How is AlmaLinux OS Kitten different from CentOS Stream?</u>

First, this is not "AlmaLinux Stream." CentOS Stream is a product of the CentOS community--it's the ultimate destination of the CentOS community's work. AlmaLinux OS Kitten is not a product at all, it is meant as a vehicle along the journey of development of the next version of AlmaLinux.

We are using our freedom here to do a bunch of work in preparation for AlmaLinux OS 10. Below you will find a list of the big differences, and on our wiki you can find the full [AlmaLinux OS Kitten 10 release notes](https://wiki.almalinux.org/release-notes/kitten-10).

### Re-enabling Frame Pointers

Red Hat Enterprise Linux and CentOS Stream disable [frame pointers](https://www.brendangregg.com/blog/2024-03-17/the-return-of-the-frame-pointers.html) by default, but with AlmaLinux OS Kitten 10, we are re-enabling them. This enables system-wide real-time tracing and profiling for optimizing the performance of any workload running on AlmaLinux.

### AlmaLinux OS Kitten includes an additional build using x86-64-v2

Within the [x86-64](https://en.wikipedia.org/wiki/X86-64) architecture, there are versions that represent specific CPU feature sets. Earlier this year, we noticed that RHEL was increasing the architecture version baseline to v3, which results in the loss of support for numerous older CPUs(and some newer ones). When RHEL [switched to v2 (for RHEL 9) in 2021](https://developers.redhat.com/blog/2021/01/05/building-red-hat-enterprise-linux-9-for-the-x86-64-v2-microarchitecture-level#), most people didn't notice. It was far less impactful because the v2 specification had existed much longer (relative to RHEL's switch) and most mainstream CPUs had included the necessary features for quite some time.

Both in AlmaLinux Kitten 10, and when we release AlmaLinux OS 10, we will follow Red Hat's decision to ship x86-64-v3 optimized binaries by default, but we will also provide additional x86-64-v2 architecture ONLY for older hardware that doesn't support modern CPU feature sets.

Please note: all 3rd party packages for RHEL10 will be built for x86-64-v3, so AlmaLinux OS Kitten 10 built for x86-64-v2 will only be appropriate in workloads where the default OS package set is enough, or where users will be able to rebuild any additional packages they require for x86-64-v2 architecture themselves. ALESCo is currently weighing the option of [rebuilding EPEL](https://docs.fedoraproject.org/en-US/epel/) for x86-64-v2 users. If you use this version, please let us know by [commenting on the RFC](https://github.com/AlmaLinux/ALESCo/pull/2), so we can make informed decisions about this version in the future.

### Secure Boot

Trusted boot has long been required for bare metal devices, and is also becoming more and more popular in virtualized environments. AlmaLinux OS Kitten 10 supports Secure Boot for Intel/AMD and ARM platforms.

### Adding SPICE

Simple Protocol for Independent Computing Environments (SPICE) has been [unsupported](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/considerations_in_adopting_rhel_9/assembly_virtualization_considerations-in-adopting-rhel-9#ref_changes-to-spice_assembly_virtualization) since RHEL 9.0. Members of the AlmaLinux community have requested we add support back in, so SPICE support is fully re-enabled in AlmaLinux OS Kitten 10 for both server and client applications.

### KVM for IBM POWER

KVM for IBM POWER has also been [unsupported](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/considerations_in_adopting_rhel_9/assembly_virtualization_considerations-in-adopting-rhel-9#ref_changes-to-kvm_assembly_virtualization) since RHEL 9.0. We enable it in the AlmaLinux OS Kitten 10 virtualization stack, so it's possible to continue using KVM just like it is in AlmaLinux 8.

### More hardware supported

Starting with AlmaLinux 8.10 and 9.4 we re-enabled support for more than 150 devices that were removed upstream. We will continue that support in AlmaLinux OS Kitten 10, as well as in AlmaLinux OS 10.

### Firefox and Thunderbird in the system repositories

Our upstream decided to remove packaged versions of Firefox and Thunderbird RPM packages from CentOS Stream 10 and RHEL10 in favor of using Flatpak versions of them. To support our community of desktop users, we decided to continue shipping them in AlmaLinux OS Kitten 10 as regular RPM packages.

## <u>Where to get AlmaLinux OS Kitten 10</u>
You can get AlmaLinux OS Kitten 10 ISOs for all supported architectures from its own primary mirror: [kitten.repo.almalinux.org](https://kitten.repo.almalinux.org/10-kitten/isos/). You can also find more information and installation instructions on the AlmaLinux OS Kitten 10 [wiki page](https://wiki.almalinux.org/development/almalinux-os-kitten-10.html) and [release notes](https://wiki.almalinux.org/release-notes/kitten-10.html#installation-instructions).

*In case you are wondering, Cloud and Container options will be added there shortly!*

## <u>Where to give feedback about these changes</u>

Current and future AlmaLinux contributors can engage with us on [our developer mailing list](https://lists.almalinux.org/mailman3/lists/devel.lists.almalinux.org/). Interested users can share feedback on [our user community list](https://lists.almalinux.org/mailman3/lists/users.lists.almalinux.org/) or [our forums](https://forums.almalinux.org/).

You can also join us this Thursday for a Meetup with some of the members of ALESCo: <https://events.almalinux.org/event/107/>

## <u>Question and Answers!</u>

We have some anticipated questions with their answers below, but if you have questions that aren't answered the best place to get those answers is this Thursday at the ALESCo Meetup and Q&A! If you can't make it, feel free to submit your questions ahead of time here: <https://forms.gle/21dAedZmHvhaM8ot5>

### Why Kitten?

AlmaLinux has used [cat names](https://wiki.almalinux.org/FAQ.html#why-does-the-almalinux-codename-include-cats) in our code names for our entire existence, and this felt like a perfect extension of that. This OS is the version that will grow up to be the next AlmaLinux cat.

### How often will AlmaLinux OS Kitten 10 be updated?

Package updates will happen frequently. Images will be rebuilt every 3 months.

### But, like, what IS AlmaLinux OS Kitten?

It is the direct upstream for AlmaLinux OS and is the primary point for the AlmaLinux community to engage and influence the future of AlmaLinux OS. Fixes and features land here first and trickle down into AlmaLinux OS as appropriate. It is the integration and collaboration point for AlmaLinux to its upstreams as well, such as CentOS Stream and Fedora.

### How can I contribute to AlmaLinux OS Kitten?

Specific guidelines have not yet been defined, but if you are interested, the best place to discuss contribution at this time is in the [ALESCo channel on Mattermost](https://chat.almalinux.org/almalinux/channels/alesco).

### After AlmaLinux OS 10 is released, where will bugs be patched?

Everything starts with AlmaLinux OS Kitten 10, then if the fix is appropriate for AlmaLinux OS 10 releases, it will be cherry-picked and shipped in the release. The goal is to have a central point for everyone to work from for fixes and features.

_This version of AlmaLinux includes desktop backgrounds created by the incredible visual effects folks over at [Image Engine](https://image-engine.com/). We can't thank them enough for their work. They were awesome to work with, and we are so excited to have them as part of the AlmaLinux community._
