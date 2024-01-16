---
title: "AlmaLinux OS 8.3 RC Release Notes"
type: blog
author: 
 name: "Jack Aboutboul"
 bio: "-"
 image: /users/jack.jpg
date: '2021-02-22'
post:
    title: "Thanks to the community feedback, we worked on the bugs and fixed most of them. By all accounts, the beta release was pretty stable already, so the Release Candidate was the likely choice (instead of another beta). Thank you to everyone who tested and reported issues at bugs.almalinux.org, or sent suggestions/mirror offers to hello@almalinux.org. Right now we have 24 mirrors, so there should be one close to you, wherever you live."
    image: 
---

Thanks to the community feedback, we worked on the bugs and fixed most of them. By all accounts, the beta release was pretty stable already, so the Release Candidate was the likely choice (instead of another beta).

Thank you to everyone who tested and reported issues at [bugs.almalinux.org](https://bugs.almalinux.org/), or sent suggestions/mirror offers to [hello@almalinux.org](mailto:hello@almalinux.org). Right now we have 24 mirrors, so there should be one close to you, wherever you live.

## Installation instructions

- There are three installation ISO images available:AlmaLinux-8.3-rc-1-x86_64-boot.iso - a single network installation CD image that downloads packages over the Internet.
- AlmaLinux-8.3-rc-1-x86_64-minimal.iso - a minimal self-containing DVD image that makes possible offline installation.
- AlmaLinux-8.3-rc-1-x86_64-dvd1.iso - a full installation DVD image that contains mostly all AlmaLinux OS packages.

Select a mirror listed on the [mirrors.almalinux.org](https://mirrors.almalinux.org/) website (please, don't use repo.almalinux.org host directly) and download a suitable ISO image from the 8.3-rc/isos/x86\_64/ directory, for example:$ wget https://mirror.interserver.net/almalinux/8.3-rc/isos/x86\_64/AlmaLinux-8.3-rc-1-x86\_64-boot.iso
Download and import the AlmaLinux public key:$ wget https://repo.almalinux.org/almalinux/RPM-GPG-KEY-AlmaLinux $ gpg --import RPM-GPG-KEY-AlmaLinux
Download and verify a checksums list:$ wget https://repo.almalinux.org/almalinux/8.3-rc/isos/x86\_64/CHECKSUM # we are looking for “Good signature”  $ gpg --verify CHECKSUM   gpg: Signature made Fri 19 Feb 2021 03:04:44 PM MSK  gpg: using RSA key 51D6647EC21AD6EA  gpg: Good signature from "AlmaLinux <packager@almalinux.org>" [unknown]  gpg: WARNING: This key is not certified with a trusted signature!  gpg: There is no indication that the signature belongs to the owner.  Primary key fingerprint: 5E9B 8F56 17B5 066C E920 57C3 488F CF7C 3ABB 34F8  Subkey fingerprint: E53C F5EF 91CE B0AD 1812 ECB8 51D6 647E C21A D6EA
Verify the downloaded ISO image checksum:# calculate the downloaded ISO SHA256 checksum $ sha256sum AlmaLinux-8.3-rc-1-x86\_64-boot.iso  1bf9bff6af3413f8f273e54c11fb45f7da63afea670eafc50dde22c45582be7a AlmaLinux-8.3-rc-1-x86\_64-boot.iso # compare it with expected checksum, it should be the same $ cat CHECKSUM | grep -E 'SHA256.*AlmaLinux-8.3-rc-1-x86\_64-boot.iso' SHA256 (AlmaLinux-8.3-rc-1-x86\_64-boot.iso) = 1bf9bff6af3413f8f273e54c11fb45f7da63afea670eafc50dde22c45582be7a

### If you decided to use the AlmaLinux-8.3-rc-1-x86_64-boot.iso image, you will need to provide the 8.3-rc/BaseOS/x86_64/kickstart/ repository from the selected mirror as the Installation Source.There are no extra Installation Sources required if you decided to go with either minimal or dvd ISO images.Upgrade instructions

Upgrade the almalinux-release package to the 8.3-3.el8 version from the beta repositories:$ dnf clean all && dnf upgrade -y almalinux-release
the new package contains updated repository URLs so that you can just run:$ dnf upgrade -y

## to update the rest of the packages.Changelog

1. The dnf package manager now uses AlmaLinux OS public mirrors by default. The current list of public mirrors can be found on the mirrors.almalinux.org website.

    The HighAvailability repo is added. It’s disabled by default and can be enabled by dnf config-manager --set-enabled ha

1. command ([ambz#16](https://bugs.almalinux.org/view.php?id=16))
2. The subscription-manager package and its dependencies added ([almbz#5](https://bugs.almalinux.org/view.php?id=5)).
3. The satellite-5-client module moved from the BaseOS to the AppStream repository ([almbz#4](https://bugs.almalinux.org/view.php?id=4)).
4. Fixed issues with the php:7.4 and nodejs:12 modules installation ([almbz#9](https://bugs.almalinux.org/view.php?id=9)).
5. Added maven:3.6 and jmc:rhel8 modules.
6. Completed the perl:5.30 module build.
7. The /usr/lib/rpm/redhat/dist.sh utility is now aware of AlmaLinux OS ([almbz#17](https://bugs.almalinux.org/view.php?id=17))
8. Added the almalinux RPM macros ([almbz#22](https://bugs.almalinux.org/view.php?id=22)).
9. The libreport-almalinux package is added to support automatic bug reporting to [bugs.almalinux.org](https://bugs.almalinux.org/) ([almbz#2](https://bugs.almalinux.org/view.php?id=2))
10. All installation environments are now available during network install ([almbz#14](https://bugs.almalinux.org/view.php?id=14))
11. The debuginfo repositories are now populated

## Known Issues

1. There is no SecureBoot support in this release (almbz#3). We are doing our best to have it in a stable release.
2. The Minimal ISO proposes to install Server environment with GNOME but actually can only install Minimal Install environment (almbz#14).
3. The mirrors support implemented with help of the DNF fastestmirror plugin that is known to be a bit "quirky". We are going to switch to geo-location-based mirror selection in the stable version.

Please send us your feedback after testing! Do report any unexpected behavior at [bugs.almalinux.org](https://bugs.almalinux.org/). Especially, anything that worked on CentOS and is different/broken now.

Sincerely,

The AlmaLinux OS Team hello@almalinux.org