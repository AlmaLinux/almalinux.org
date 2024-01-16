---
title: "Introducing AlmaLinux Beta: A Community-Driven Replacement for CentOS"
type: blog
author: 
 name: "Jack Aboutboul"
 bio: "-"
 image: /users/jack.jpg
date: '2021-02-01'
post:
    title: "CloudLinux is proud to announce the release of AlmaLinux OS Beta. We’ve collected community feedback and built our new beta release around what you wo..."
    image: 
---

CloudLinux is proud to announce the release of AlmaLinux OS Beta. We’ve collected community feedback and built our new beta release around what you would expect from an enterprise-level Linux distribution. AlmaLinux OS is a completely free 1:1 binary compatible fork of Red Hat Enterprise Linux (RHEL) 8, inspired by the community and built by the engineers and talent behind CloudLinux. Visit [this link](https://repo.almalinux.org/almalinux/8.3-beta/isos/x86_64/) to download Beta images.With the Beta release deployed, we’d like to ask the community to be involved and provide feedback. We aim to build a Linux distribution entirely from community contributions and feedback. During AlmaLinux OS Beta, we ask for assistance in testing, documentation, support and future direction for the operating system. Together, we can build a Linux distribution that fills the gap left by the now unsupported CentOS distribution.The AlmaLinux team set up all the necessary infrastructure to make it convenient for our contributors to provide their input. The public repository on [Github](https://github.com/AlmaLinux) is where we will finalize the source code for the system, and any additional documentation will be posted on the [wiki](https://wiki.almalinux.org/). We set up the wiki and repository to make it easy for the community to provide as much information and feedback as possible. The AlmaLinux team will review every comment and request, but we ask that only registered contributors [file bug reports](https://bugs.almalinux.org/login_page.php) to filter out spam.To facilitate communication and help answer some of the common questions you might already have, we will be hosting a live QA webinar with the AlmaLinux OS team. The webinar will take place on February 10, 5 PM (UTC) / 9 AM (PST). Among the participants present will be Igor Seletskiy, CEO of CloudLinux, and Alexander Vinogradov, Head of Engineering at AlmaLinux.You can sign up for our webinar [here](https://blog.almalinux.org/webinars/almalinux-beta-qa-webinar/).If you have any questions, comments, feedback or concerns, please feel free to send us your thoughts to [hello@almalinux.org](mailto:hello@almalinux.org) or send them during the webinar on Twitter with the hashtag #AlmaLinuxBeta.CloudLinux and the AlmaLinux OS team would like to thank the community for their input. This is just the beginning for AlmaLinux OS, and we look forward to continued improvements and updates for the next generation enterprise-level Linux operating system.Thank you for your contribution, input, and support throughout launching AlmaLinux OS! The infrastructure was the first step, now we need your help to make the next one!Release Notes for AlmaLinux OS 8 betaThe release code name: Purple [Manul](https://en.wikipedia.org/wiki/Pallas%27s_cat).CloudLinux is proud to present the beta version of AlmaLinux OS. After roughly a month and a half from the announcement, here is a 1:1 RHEL binary compatible replacement for your RHEL-based systems. This is for the community and by the community, you're the soul of Linux. Thank you for your interest and suggestions so far, keep them coming.Use this version to thoroughly test your workloads and report any unintended features (ie, bugs) you may find, it will help make AlmaLinux OS better.Installation instructions

- There are three installation ISO images available:[AlmaLinux-8.3-beta-1-x86_64-boot.iso](https://repo.almalinux.org/almalinux/8.3-beta/isos/x86_64/AlmaLinux-8.3-beta-1-x86_64-boot.iso) - a single network installation CD image that downloads packages over the Internet.
- [AlmaLinux-8.3-beta-1-x86_64-minimal.iso](https://repo.almalinux.org/almalinux/8.3-beta/isos/x86_64/AlmaLinux-8.3-beta-1-x86_64-minimal.iso) - a minimal self-containing DVD image that makes possible offline installation.
- [AlmaLinux-8.3-beta-1-x86_64-dvd1.iso](https://repo.almalinux.org/almalinux/8.3-beta/isos/x86_64/AlmaLinux-8.3-beta-1-x86_64-dvd1.iso) - a full installation DVD image that contains mostly all AlmaLinux packages. We don't really recommend using it unless you need to set up and use AlmaLinux on a machine without internet access.

Download a preferable ISO image and verify its checksum. Here is an example for GNU/Linux:# download and import the AlmaLinux public key
$ wget https://repo.almalinux.org/almalinux/RPM-GPG-KEY-AlmaLinux
$ gpg --import RPM-GPG-KEY-AlmaLinux # download a checksums list
$ wget https://repo.almalinux.org/almalinux/8.3-beta/isos/x86\_64/CHECKSUM  # verify the checksums list, we are looking for “Good signature”
$ gpg --verify CHECKSUM 
gpg: Signature made Thu 28 Jan 2021 11:39:12 PM MSK
gpg: using RSA key 51D6647EC21AD6EA
gpg: Good signature from "AlmaLinux <packager@almalinux.org>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg: There is no indication that the signature belongs to the owner.
Primary key fingerprint: 5E9B 8F56 17B5 066C E920 57C3 488F CF7C 3ABB 34F8
  Subkey fingerprint: E53C F5EF 91CE B0AD 1812 ECB8 51D6 647E C21A D6EA # download the network install ISO $ wget https://repo.almalinux.org/almalinux/8.3-beta/isos/x86\_64/AlmaLinux-8.3-beta-1-x86\_64-boot.iso
\# calculate the downloaded ISO SHA256 checksum
$ sha256sum AlmaLinux-8.3-beta-1-x86\_64-boot.iso 
d15be406f417e81382b46a54d87dff01c8ca770c847c18703f19146587b61a1f AlmaLinux-8.3-beta-1-x86\_64-boot.iso # compare it with expected checksum, it should be the same
$ cat CHECKSUM | grep -E 'SHA256.*AlmaLinux-8.3-beta-1-x86\_64-boot.iso'
SHA256 (AlmaLinux-8.3-beta-1-x86\_64-boot.iso) = d15be406f417e81382b46a54d87dff01c8ca770c847c18703f19146587b61a1f

### If you decided to use the AlmaLinux-8.3-beta-1-x86_64-boot.iso image, you will need to provide this https://repo.almalinux.org/almalinux/8.3-beta/BaseOS/x86_64/kickstart/repository as the Installation Source:If you are going to install a non-minimal environment, you will need to add the AppStream repository to the additional repositories: https://repo.almalinux.org/almalinux/8.3-beta/AppStream/x86_64/os/.There are no extra Installation Sources required if you decided to go with AlmaLinux-8.3-beta-1-x86_64-minimal.iso or AlmaLinux-8.3-beta-1-x86_64-dvd1.iso images.How to set up a usb key to install AlmaLinux OS

> dd if=AlmaLinux-8.3-beta-1-x86\_64-boot.iso of=/dev/sdX

## Where sdX is your usb deviceKnown issues

- Our libreport/abrt packages aren’t integrated with the bugs.almalinux.org bug-tracker yet, so a user will have to submit a crash report manually. Issue: [almbz#2](https://bugs.almalinux.org/view.php?id=2).
- The “perl:5.30” module support is incomplete in the beta release, it will be finished in the stable.
- We don’t have the latest “jmc” and “maven” module versions. They will be updated later.
- The “satellite-5-client” module is located in the BaseOS repository instead of the AppStream. Issue: [almbz#4](https://bugs.almalinux.org/view.php?id=4).
- There is no support for Secure Boot in the beta release. Issue: [almbz#3](https://bugs.almalinux.org/view.php?id=3).
- The debuginfo repositories are empty and will be populated in a couple of days after the beta release.