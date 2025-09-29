---
title: "ALESCo - Updates and requests!"
type: blog
author:
  name: "Cody Robertson"
  bio: "CTO, Hawk Host"
  image: /users/cody.jpeg
date: "2025-03-05"
images:
  - /blog-images/2025/mar-alesco-updates.png
post:
  title: "Come read what ALESCo has been up to, and the new process for taking requests!"
  image: /blog-images/2025/mar-alesco-updates.png
---

In case you missed it ALESCo ([The AlmaLinux Engineering Steering Committee](https://almalinux.org/blog/2024-05-21-introducing-alesco/)) that we announced in May of 2024 has been hard at work setting up processes and stretching our legs. It's been a bit since we've done this kind of update, so let's get to it! 

## ALESCo's Mission

As a reminder: [ALESCo](https://almalinux.org/alesco/) is a group of engineers heavily involved in using and developing AlmaLinux, formed into a committee that generally guides the technical progression and growth of AlmaLinux as an operating system.

Our mission statement reads as follows:

_The AlmaLinux Engineering Steering Committee (ALESCo) is dedicated to guiding the technical direction of the AlmaLinux distribution on a day-to-day basis within the guidelines set forth by the board, ensuring its robustness, reliability, sustainability, and relevance in the open-source ecosystem. ALESCo will work collaboratively with, and oversee relevant technical-focused Special Interest Groups (SIGs) to achieve these goals. It is "air traffic control" for engineering matters._

## Recent ALESCo Activity

Last summer, there was a [vulnerability in OpenSSH's server (sshd)](https://openwall.com/lists/oss-security/2024/07/01/3) in glibc-based Linux systems: CVE-2024-6387 or "regreSSHion." ALESCo came together on the day regreSSHion was published to decide to [incorporate upstream patches](https://almalinux.org/blog/2024-07-01-almalinux-9-cve-2024-6387/), independent of CentOS Stream/RHEL. We also [submitted this patch to CentOS Stream 9](https://gitlab.com/redhat/centos-stream/rpms/openssh/-/merge_requests/77) to benefit the whole ecosystem because we are committed to working upstream.

That pattern has happened a number of times since ALESCo was formed, most recently with [CVE-2025-26465](https://almalinux.org/blog/2025-02-20-test-patches-for-cve-2025-26465/), which we anticipate releasing this week.

We have bi-weekly meetings (which you can find on [events.almalinux.org](http://events.almalinux.org), and that we announce in the ~ALESCo channel on [chat.almalinux.org](http://chat.almalinux.org)), the minutes of which are recorded in the wiki.

## What we need from you - feedback on hardware support and other requests

One of the things we did in 2024 was set up a process to accept requests from the community, and to accept feedback from our users about ideas that we have. We decided to use a GitHub repository, and ask people to submit [their requests in the form of an RFC](https://github.com/AlmaLinux/ALESCo/pulls).

_For anyone not familiar with GitHub in general - [The front page of pull request](https://github.com/AlmaLinux/ALESCo/pull/2) shows the general discussion about the proposal. If you click [Files changed](https://github.com/AlmaLinux/ALESCo/pull/2/files) you'll see the current version of the proposal, including any accepted updates or suggestions. You can leave your own feedback in the form of a comment or a reaction to the first comment._

### RFC - Build Fedora EPEL for AlmaLinux and AlmaLinux Kitten x86_64_v2

The first RFC submitted for this process is to discuss a [potential rebuild of the Extra Packages for Enterprise Linux](https://github.com/AlmaLinux/ALESCo/pull/2) (or [EPEL](https://docs.fedoraproject.org/en-US/epel/)) to be used alongside the \_v2 version of AlmaLinux that we are including with AlmaLinux 10.

### RFC0003 - Enable KVM on AlmaLinux 9 on ppc64le

There's a second RFC that's been submitted by the folks at Oregon State University's Open Source Lab to [Enable KVM on AlmaLinux 9 on ppc64le](https://github.com/AlmaLinux/ALESCo/pull/3/files). KVM is something we enabled on AlmaLinux Kitten and AlmaLinux 10 beta already, and they're looking to see it added to AlmaLinux 9 as well.

If you want to see all of the RFCs as they get submitted, you can "watch" the GitHub repo and select custom - then chose to get notifications of pull requests being created. 

## What's Next?

As will always be the case with AlmaLinux, if you want to help, we're happy to have you! ALESCo is still quite new, and anything new will have room for improvement. The immediate way to help us is by making sure you provide feedback on all of the things we're discussing. If you want to be more involved, or want some more information about what this is all about, please reach out to us.

Over the coming months we'll also be working to expand the number of people on ALESCo, to make sure we have as many diverse perspectives as possible. If you are interested in joining in that capacity, the best way to show your interest is by being active in the community, attending the meetings, and making sure you're helping out your fellow community members! We'll have a formal way of accepting expressions of interest soon.

For now, the best and simplest way to get involved is to[ join the mattermost channel](https://chat.almalinux.org/almalinux/channels/alesco).
