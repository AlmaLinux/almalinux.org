---
title: "Looking Back, Leaping Forward: A look back at the first year for AlmaLinux and what the future holds"
type: blog
author: 
 name: "theMayor"
 bio: "-"
 image: /images/profile.png
date: '2022-02-02'
post:
    title: "Looking Back, Leaping Forward: A look back at the first year for AlmaLinux and what the future holds"
    image: /blog-images/almalinux-infographic.png
---

WOW! What a first year! The [AlmaLinux](https://almalinux.org/) community finds itself looking back at a successful 12 months with so many significant advancements and milestones. We’ve managed to pull together people from all over the world and unite and unify everyone while leveling-up this new CentOS ecosystem. We’ve also delivered three releases, with download counts in the millions. We recently celebrated over [500K Docker pulls](/blog/celebrating-500k-docker-pulls/) (we have almost a million now), a [beta release for AlmaLinux 8.5 for PowerPC](/blog/almalinux-85-beta-for-powerpc-now-available/), our [first Platinum sponsor Codenotary](/blog/welcome-codenotary-almalinux-os-foundations-first-platinum-member/), and, of course, the [release of AlmaLinux 8.5](/blog/almalinux-os-85-stable-now-available/) within 48 hours of the Red Hat Enterprise Linux (RHEL) release. That was all just in the last couple of months.

AlmaLinux was [officially announced to the world](https://blog.cloudlinux.com/almalinux-is-born) on the 14th of January last year. We named the distribution AlmaLinux as ‘alma’ means ‘soul’ in many Latin languages. The name both acknowledges the history of Linux—and the passion of the many diverse people that turned a personal project into a kernel underpinning many, many operating systems—and ties into our core belief that AlmaLinux’s community of individuals and organizations are the ‘soul’ that powers and drives us forward.

**Inclusion Built-In**

The word ‘alma’ is also derived from ‘almus,’ which means ‘nourishing, kind’. When Igor Seletskiy kickstarted this initiative as an alternative to CentOS, he realized that it would take a lot more than just technical know-how to build a distribution and community which would be sustainable for the long term. From the outset, we knew that would mean including a soon-to-be massive community of AlmaLinux users in governance and in every key decision that AlmaLinux makes.

To ensure the independence, transparency, and longevity of the project, the AlmaLinux OS Foundation became a US non-profit 501(c)(6) organization on March 18th, 2021. This made the Foundation, and not any one company or individual, the owner of all the assets related to AlmaLinux OS. This key fact is part of the strength of AlmaLinux. The community owns and controls its own direction. It can’t be bought or sold, traded or bartered. Forever.

CloudLinux, as an early sponsor, committed itself to supporting AlmaLinux, investing a minimum of $1 million per year in its development, but the open-source organization of the project means that the community can carry AlmaLinux forward on their own as well.

Swiftly following that announcement, we saw the first stable release of AlmaLinux, version 8.3, arrive on 30 March with [a live stream launch](https://www.youtube.com/watch?v=AmjQInMOQbM) and earned rapid approval by receiving CentOS core developer [Johnny Hughes’ endorsement](https://www.reddit.com/r/AlmaLinux/comments/mgic42/congrats_on_almalinux_release/) on release day. Since then, we’ve seen two more stable releases, each arriving more quickly than the last: AlmaLinux 8.4 was released just seven days after RHEL, and 8.5 was released 48 hours after RHEL in November. We’d absolutely like to thank our release engineering squad here, especially Eugene, Andrew, and Sonia, for all the incredible efforts around each release and more!

**Community-powered Results**

The technical milestones we achieved last year weren’t only focused on making point releases that were 1:1 binary compatible with RHEL. The true strength of AlmaLinux is in its people, and the community has been very busy.

We’ve developed images for many fields and requirements, from [AWS](https://wiki.almalinux.org/cloud/AWS.html#almalinux-os-amazon-web-services-amis) and [Azure images](https://wiki.almalinux.org/cloud/Azure.html#almalinux-os-in-azure-cloud), [Google Cloud](/blog/almalinux-images-for-google-cloud/), [generic (cloud-init) images](/blog/almalinux-cloud-images-updates-june-18-2021/), [LXC and LXD container](https://uk.lxd.images.canonical.com/) and [minimal container images](/blog/minimal-container-images-now-available-on-docker-hub-and-quay-io/) to [Raspberry Pi images](/blog/almalinux-for-raspberry-pi-updates-october-2021/) (with a [dedicated repo](https://repo.almalinux.org/almalinux/8/raspberrypi/)), [AlmaLinux WSL for Windows images](https://github.com/almalinux/wsl-images), [full RHEL UBI compatible container images](/blog/almalinux-container-images-update-full-rhel-ubi-compatibility/), [ARM and AArch64 releases](/blog/almalinux-os-8-4-for-arm-aarch64-now-available/), and even an 8.4 beta for PowerPC that we snuck out at the end of December!

As you might expect, we saw exponential demand for AlmaLinux during 2021, which meant scaling out and supplying new and improved mirrors at various stages. We have over 180 worldwide mirrors now service thousands of downloads a day. Our [geo-location-based mirror service](/blog/the-new-and-improved-almalinux-mirror-service/) came online in early August, helping users get ISOs, packages, and updates faster and even more efficiently based on where they were in the world. In addition to all of the [mirror sponsors](https://mirrors.almalinux.org/) and the [Infrastructure SIG](https://wiki.almalinux.org/sigs/Infrastructure.html) that has made this possible, we’re very grateful to the corporate sponsors. Our thanks go to AWS and Microsoft Azure for hosting our mirror service and HiVelocity for its early support of the mirrors, as well as KnownHost, which has been instrumental in its ongoing maintenance and improvement. A big shout out here to Jonathan, our team lead, Daniel, Cody, and the rest of our infrastructure team, for leading those efforts!

Putting into practice our goal of being responsive to community requests, we saw initiatives like the release of [AlmaLinux 8 as Live Media versions in July](/blog/announcing-almalinux-live-media-beta/), packaged for use with popular desktops, such as GNOME, KDE, and Xfce. To increase commercial confidence in the distribution, we saw efforts spearheaded by community contributor and Foundation member, Simon John, work with the Center for Internet Security (CIS) to release a [benchmark for AlmaLinux OS](https://www.cisecurity.org/). This enabled users to have more secure configurations and audit their systems using [OpenSCAP](https://wiki.almalinux.org/documentation/openscap-guide.html).

In August, we announced that [AlmaLinux was available on Microsoft Azure](/blog/almalinux-now-available-on-microsoft-azure-azure-sponsors-almalinux/) and Azure joined us as a sponsor. This opportunity took us a step closer to a significant goal in December: finding ways for AlmaLinux to enable scientific computing and research. In particular, High-Performance Computing (HPC) is often out of reach because of the investment costs, so it’s been satisfying to work in collaboration with the Microsoft Azure team and fulfill community requests by releasing [AlmaLinux OS for Azure HPC](/blog/almalinux-for-azure-hpc-now-available/).

**Community Owned & Governed**

In October, the board welcomed [benny Vasquez](/blog/hi-im-benny-how-can-i-help/), head of Developer Relations at Chef, as the new Chair, replacing Igor Seletskiy and expanding community control of the AlmaLinux OS Foundation. benny spent much of her early career in Windows desktop support and web hosting but moved to DevOps in recent years. With her wealth of experience, she intends to build diversity by introducing new people into the AlmaLinux community’s core and ensuring AlmaLinux meets the needs of anyone seeking an alternative to CentOS Linux.

Announcing membership options was a historic day for the EL community. As a whole, we were finally able to say, ‘we all own AlmaLinux.’ The distribution is 100% owned and governed by the members of the AlmaLinux OS Foundation through [bylaws](https://wiki.almalinux.org/Transparency.html#we-strive-to-be-transparent) and [memberships](/members/) for contributors, mirror providers, and sponsors. Individuals and organizations will be eligible to vote for and be voted into the AlmaLinux Foundation’s board of directors and participate in committees and directly steer AlmaLinux OS.

**We recently passed 140 new members. If you haven’t joined yet (it's 100% free), you can [today](/members/)!**

One of the first things benny did as our newly appointed chair was to attend the All Things Open conference. While there, she met many community members and ‘elbow bumped’ interested users while supporting Jack Aboutboul, AlmaLinux’s community manager, as he introduced the [ELevate Project](/elevate).

ELevate represents the AlmaLinux community’s commitment to making it easy for users to perform in-place migrations between RHEL-derivative distributions. Open-sourced under an Apache 2.0 license, ELevate ensures that data and config files are preserved. ELevate supports AlmaLinux along with many other RHEL derivatives as we believe that giving back to the ecosystem is vital for the health of open source software.

In December, it was exciting to see our first Platinum sponsor member, [Codenotary](https://codenotary.com/), especially as it comes from a company that has a deep commitment to open source. Codenotary’s founder, Moshe Bar, has a long history of supporting open source software as the creator of the companies behind both the KVM and Xen hypervisors. Without our sponsors generously donating funds and resources, we wouldn’t have achieved all that we have this year, so thank you!

**We ARE you**

The best open source projects reflect the belief that humans cannot exist in isolation and we all stand on the shoulders of giants. We depend on connection and community, and AlmaLinux recognizes that we can achieve so much more together. This extends to our ‘upstream first’ approach to bug fixes and commits, as we see it as the way to improve the ecosystem for everyone. We’d especially like to thank the CentOS team for all their groundbreaking work over the last almost two decades. Thanks go out to Community manager Rich Bowen, Carl George, ARM master Pablo Greco and the others who have encouraged our efforts and assisted along the way. Stream is just getting started and we’ve already contributed and are looking forward to continuing to grow the CentOS ecosystem.

We would not be where we are today without our community. We now have almost 800 people on the [AlmaLinux Mattermost](https://chat.almalinux.org/) server and a core team of 16 people, so it only seems right to mention a few names: [Simon John](https://twitter.com/sej7278), whose efforts made the CIS Benchmark for AlmaLinux possible; [Matiss Treinis](https://matisstreinis.com/), Web Team Lead, for being instrumental in providing us with a stylish new [AlmaLinux website](/); [Bala Raman](https://github.com/srbala) and [Elkhan Mammadli](https://github.com/lkhn), who have been strong advocates for AlmaLinux and contribute to [Live media](https://github.com/AlmaLinux/sig-livemedia) and container images and more since the project started.

**2022: a leap forward**

The word ‘alma’ also means ‘leap’ in Greek, which seems appropriate as we look to the future of AlmaLinux.

Our goals for the foundation itself are to hold open elections this year to foster greater diversity and expand the board. Additionally, we will continue increasing transparency by extending that to financial information. Ultimately, we intend to move to become a public charity and classified as a 501(c)(3) non-profit organization. This classification reflects our mission to serve anyone without discrimination, allowing contribution and use openly and equally. To achieve this will mean increasing the number of paid sponsors and growing our membership from across society.

Building on a strong 2021, we have high ambitions for our technical milestones for 2022. The beta for RHEL 9 was released in November, but we stand ready to release AlmaLinux 9 as quickly as possible after RHEL 9 lands. We expect this release will offer many improvements and enhancements mainly focused on automation and deployment at scale. With the ongoing security concerns across the industry, we’ll see some welcome security and compliance measures (e.g., integrated OpenSSL 3 and SSH root password login is disabled by default). We also intend to integrate software supply chain security with verifiable builds into AlmaLinux’s build system, using Codenotary’s amazing solution.

As well as matching RHEL releases, we will seek parity in the architectures we support. We will expand the container images we provide (language- and application-specific), the hardware we support (such as developer boards and ARM architecture), and alternative kernels.

The theme of transparency and independence extends to our technical milestones, and one we expect to achieve early in the year is the release of an open build system. This project automates building distributions and packages, testing packages, signing packages, and releasing them to public repositories. The intention is for the build environment to be fully open-source, and our build/test environments will use AWS, Azure, GCE & Equinix Metal, and others.

Commercial confidence in AlmaLinux will only grow in 2022, as we pursue FIPS followed by FEDRamp accreditation to comply with security requirements for US federal agencies and Common Criteria certification.

And finally, we will expand ELevate to include in-place migration support for more major version changes. The project already supports migrations from 7 to 8, and we plan to add 8 to 9, and potentially even 6 to 7. We’re also working with our sponsors, cPanel, to tightly integrate ELevate so that users running cPanel will be able to migrate between major versions as well.

We can’t ignore the pressures of the world we find ourselves in, so the AlmaLinux OS Foundation would like to thank all our amazing community members and gracious corporate sponsors. They have worked and continue to work incredibly hard to make all the new releases and announcements possible.

We still need YOU! Whether you do devops, RPM packaging, cloud, containers, security, graphic design, web/frontend work, we have lots of plans and if you’re looking to join a vibrant and welcoming open source community please [join us](https://chat.almalinux.org/).

With much to celebrate and much to be excited about for 2022 and beyond, the future of AlmaLinux is bright. Let’s work together to make it happen!

**Engage**

If you’re excited about the future of AlmaLinux, you can [apply for free to become a member](/members/) and for more sponsorship information, email us at [info@almalinux.org](mailto:info@almalinux.org) for a chat.

Keep up to date with important information and announcements, [join the AlmaLinux mailing lists](https://lists.almalinux.org/).

You can also connect with the community by joining us on our [Mattermost](https://chat.almalinux.org/almalinux/channels/town-square) server and [Reddit](https://www.reddit.com/r/AlmaLinux/) and following us on [Twitter](https://twitter.com/AlmaLinux).
