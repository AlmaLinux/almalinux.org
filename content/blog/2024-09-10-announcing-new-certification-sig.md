---
title: "Announcing the AlmaLinux Certification SIG"
type: blog
author: 
 name: "Jonathan Wright"
 bio: "Infra & Certification SIG Leaders"
 image: /users/jonathan.jpg
date: '2024-09-09'
images:
  - /blog-images/2024/2024.09.certification.sig.png
post:
    title: ""
    image: /blog-images/2024/2024.09.certification.sig.png
---

After months of work, we are happy to announce the [AlmaLinux Certification Special Interest Group](https://wiki.almalinux.org/sigs/Certification.html) (SIG), along with our [Hardware Certification Program](http://almalinux.org/certification/hardware-certification/hardware-certification-program/)! This SIG has tangible goals and immediate benefits for all users of AlmaLinux, and tons of ways to get involved.

## The Certification SIG

This SIG was born out of a desire to prove that AlmaLinux works in all places that our community needs it to. The members already helping are from all over the world, and have gotten engagement from some of the most respected hardware providers in the world. Our most active engagement has been with SuperMicro, and we are so grateful to them for helping us improve and expand the Hardware Certification Program.

One of our biggest supporters, Srini Bala, sent us this to share:

> _Our customers are looking for a trusted Enterprise Linux ecosystem, and AlmaLinux has positioned itself as one of the most secure of the no-cost options out there," said Srini Bala, GM of Solution Engineering at Super Micro Computer, Inc. "Supermicro's 2U server was recently certified with the Hardware Certification Program, giving our customers more open-source Linux options for Compute intensive applications."_

## The Hardware Certification Program

The first success of the Certification SIG is the Hardware Certification Program. This program creates a bridge between the community of AlmaLinux users, and enterprises who want to prove their hardware is a good fit for their environment.

{{< figure src="/images/certificationimages/certificationprocess.svg" link="/images/certificationimages/certificationprocess.svg" caption="The Hardware Certification Process" width="40%">}}

Hardware vendors start by engaging the SIG to certify their hardware by rewviewing the program and then submitting a request for the certification. , using our open source [Hardware-Certification-Suite](https://github.com/AlmaLinux/Hardware-Certification-Suite). The guidelines were developed in the open by the Certification SIG, and then the Certification reports are submitted for inclusion. They will are always available for community review on GitHub: <https://github.com/AlmaLinux/certifications>

## Community-validated hardware certifications

One of the things this certification program allows for us community-validation of hardware, using the same certification suite that we use for the IHV-Facilitated certification testing. That helps the community feel more confident in their hardware choices without having to wait for hardware vendors to work through their red tape to start the Certification processes.

If you are a current or potential AlmaLinux user and want to see AlmaLinux validated on a specific piece of hardware but you aren't able to complete that testing yourself, you can request it by opening an issue on the [Certification GitHub repo](https://github.com/AlmaLinux/certifications). If you have access to hardware, take a look at the list and see if someone has requested a something you have! 

## This is only the beginning...(or how you can help)

We have so much room for growth with this process, and have more ideas that we want to see added. In addition to helping with community-validated hardware requests, there are a bunch of other specific ways you can help today!

Community checkups (especially on minor version updates, since the SIG only validates on major version changes) and confirmations for already validated hardware will always be welcome. We want to build a Live USB image of AlmaLinux with the hardware certification suite on it, so that users can certify hardware without having to start with a freshly-installed device.

Even more exciting, we'll be working on spinning up a Software Certification Program over the coming months to provide software validation and certification that our users can trust.

Eventually, we'd love to be able to provide Toolkits for easy self-certification by ISVs and IHVs and repeatable community validation, streamlining this process for everyone involved. 

## The Value of Certification

Hardware and Software Certification hold different values for users and vendors. For users of AlmaLinux, the value of the having a path for certification allows AlmaLinux users to feel confident in their hardware and software choices. For IHVs and ISVs, it shows their commitment to open source, and helps make them the right choice for the massive community of AlmaLinux users.

We are so excited to be able to share this with the world. If you'd like to get involved, please join the [~SIG/Certification](https://chat.almalinux.org/almalinux/channels/sigcertification) room on [chat.almalinux.org](http://chat.almalinux.org), take a look at the work we have stacked up on our [project board](https://github.com/orgs/AlmaLinux/projects/6/), and then join us at the [next SIG meeting (Sept 10th!)](https://events.almalinux.org/category/6/).