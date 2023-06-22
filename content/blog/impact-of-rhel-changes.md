---
title: "Impact of RHEL changes to AlmaLinux"
type: blog
author: 
 name: "benny Vasquez"
 bio: "Chair, AlmaLinux OS Foundation Board of Directors"
 image: /users/benny.jpeg
date: '2023-06-22'
post:
    title: "Impact of RHEL changes to AlmaLinux"
    image: /blog-images/23.06.22.RHEL.changes.png
---

Earlier today RedHat announced another massive shift that impacts all rebuilds and forks of Red Hat Enterprise Linux. Going forward [Red Hat will now only be releasing the source code for RHEL RPMs behind their customer portal](https://www.redhat.com/en/blog/furthering-evolution-centos-stream). Since all RHEL clones rely on the sources being published, this is causing disruption for the entire Red Hat ecosystem, once again.

A quick summary: how we get RPM sources is being forced to change.
------------------------------------------------------------------

Late last week one of our build SIG members noticed that some updates for Red Hat 8 hadn't been published on [git.centos.org](https://git.centos.org/) like they were supposed to be. They assumed it was a bug and [opened a report appropriately](https://bugzilla.redhat.com/show_bug.cgi?id=2215299), but as the days went on with no resolution, we knew something was up. This morning we got our answer:

> Red Hat has decided to continue to use the Customer Portal to share source code with our partners and customers, while treating CentOS Stream as the venue for collaboration with the community.

This change means that we, as builders of a RHEL clone, will now be responsible for following the licensing and agreements that are in place around Red Hat's interfaces, in addition to following the licenses included in the software sources. Unfortunately the way we understand it today, Red Hat's user interface agreements indicate that re-publishing sources acquired through the customer portal would be a violation of those agreements.

That means we need a new solution.
----------------------------------

The short- and long-term solutions to this change are something we will be discussing over the coming weeks. We spent much of our time today diving deep to ensure we understood the depth of the problem, and discussing our potential options.

In the short term, we will be working with other members of the RHEL ecosystem to ensure that we continue to deliver security updates with the speed and stability that we have become known for.

In the long-term, we'll be working with those same partners and with our community to identify the best path forward for AlmaLinux as part of the enterprise linux ecosystem.

If you have any questions, you know how to find us (in [chat](https://chat.almalinux.org) or on [discourse](https://almalinux.discourse.group/)). Please also know that this is a rapidly developing situation, and that we will be adjusting and updating as quickly as we can. If you would like to have your voice considered as part of the conversation as we go forward, please [join the ongoing discussion on discourse](https://almalinux.discourse.group/t/how-is-rh-new-move-affecting-the-el-family/) or reach out to me directly.

If you have any needs that aren't being met or answered below, please don't hesitate to reach out: <benny@almalinux.org>

***

FAQs (because there are already many):
--------------------------------------

Below are a few questions we've seen already come up multiple times. We'll update this with any additional questions we see as we continue on.

### Does this mean I won't be getting security updates for my AlmaLinux OS Server?

No. In the immediate term, our plan is to pull from CentOS Stream updates and Oracle Linux updates to ensure security patches continue to be released. These updates will be carefully curated to ensure they are 1:1 compatible with RHEL, while not violating Red Hat's licensing, and will be vetted and tested just like all of our other releases.

### Who is involved in the conversations about the next steps for AlmaLinux at this time?

To date our board, our president, and all of our SIG leaders have been involved in the conversations, as well as many other members of the community. If you would like to be involved in the conversations, please [join the ongoing discussion on discourse](https://almalinux.discourse.group/t/how-is-rh-new-move-affecting-the-el-family/) or reach out to me directly.

### Can you just use CentOS Stream sources?

No, we are committed to remaining a downstream RHEL clone, and using CentOS Stream sources would make us upstream of RHEL. CentOS Stream sources, while being upstream of RHEL, do not always include all patches and updates that are included in RHEL packages. 

### Is Red Hat trying to kill downstream clones?

We cannot speak to Red Hat's intentions, and can only point to the things they have said publicly. We have had an incredible working relationship with Red Hat through the life of AlmaLinux OS and we hope to see that continue.