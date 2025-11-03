---
title: "AlmaLinux OS brings openQA to RHEL ecosystem"
type: blog
author:
  name: "Elkhan Mammadli"
  bio: "AlmaLinux OS Cloud and OpenQA engineer"
  image: /users/elkhan.jpg
date: "2023-07-20"
post:
  title: "AlmaLinux OS brings openQA to RHEL ecosystem"
  image: /blog-images/openqa.png
---

Hello! I'm [Elkhan Mammadli](https://chat.almalinux.org/almalinux/messages/@lkhn) and you may know me as an avid AlmaLinux contributor and the head of AlmaLinux Cloud Images SIG. Today I'd like to share an absolutely awesome story about collaboration–the open source way.

AlmaLinux OS has come a long way in a very short time. We’ve been fully committed to delivering the best possible experience for the community, no matter where or what you run. A big part of ensuring the quality of our releases is testing; lots and lots of testing. A while ago we went looking for a good testing automation framework to build into our release process.

Thanks to a [fortuitous session at FOSDEM](https://fosdem.org/2023/schedule/event/openqa_for_gnome/), we decided to use [openQA](https://open.qa/), which is used by a few other distros, including openSUSE, Fedora and Debian. There were a couple of problems before we could get started though. openQA didn’t have support for any enterprise linux derivatives, didn’t support the RHEL virt stack, and it also didn’t have support for s390x. So we added them!

## What is openQA and how does it work?

Simply put, openQA is an automated test tool for operating systems. It simplifies automated testing of the whole installation process of an operating system in a wide combination of software and hardware configurations. The openQA tool uses virtual machines to reproduce predefined processes and check the output against what it expects. You can check out the [openQA](https://open.qa/) site or our [openQA User Guide](https://wiki.almalinux.org/development/openQA.html) for more details.

## How did we do it?

As I have been leading the openQA efforts, I rolled up my sleeves and got to work.
First and foremost, while openQA worked well with Fedora, it did not yet work with RHEL. So the first order of business was submitting pull requests to make sure that openQA could identify RHEL and any other EL-derivative.
During our work to implement openQA for AlmaLinux, we implemented virtualization support for s390x architecture in openQA. We also adapted it to work on the RHEL virtualization stack, bringing back KVM support in ppc64le architecture for AlmaLinux 9. KVM support was removed from RHEL, and as part of our 1:1 RHEL clone promise, KVM support has not been part of the “official” AlmaLinux 9 for ppc64le; it has only been implemented for openQA and corresponds with the Kernel and QEMU-KVM packages in the openQA repo.

With the recent shift in our goals from 1:1 to RHEL compatible, adding KVM support to our ppc64le images is something we might consider adding back in, afterall!

Stay tuned for more in-depth insights into the development process and the challenges overcome by the AlmaLinux Team, as I will be sharing them soon.

Although currently AlmaLinux openQA only has what we consider the bare minimal set of tests, we will be continuing to expand the testing we provide to meet the needs of the community. We expect experienced users will add the tests they need to see as well!

## Where is it?

The AlmaLinux openQA testing system is available at [openqa.almalinux.org](https://openqa.almalinux.org/).

## Special Thanks

I would also like to include a shout out to openQA developers for such a cool project, the Fedora project for the tests and inspiration, and “The GNOME guy”, Sam Thursfield, whose presentation on the FOSDEM played a big role for me."

## Contribute and Get Help

We invite you to contribute to the AlmaLinux testing suite by helping us define a test suite tailored to your needs. By getting involved, you are playing a vital role in ensuring that we test user-specific scenarios, improving AlmaLinux for all. Join the [Mattermost Chat](https://chat.almalinux.org/almalinux/channels/engineeringqa) if you need help or have any questions, and explore the openQA repositories to start making a difference. We look forward to collaborating with you, offering assistance, and together creating a lasting impact in the AlmaLinux community.
