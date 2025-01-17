---
title: "Multiple rsync Vulnerabilities Discovered - Mitigation Status"
type: blog
author: 
    name: "Jonathan Wright"
    bio: "Infra SIG team lead & ALESCo member"
    image: /users/jonathan.jpg
date: '2025-01-17'
post:
    title: "Multiple rsync Vulnerabilities Discovered - Mitigation Status"
    image: /blog-images/2025/2025-01-17-rsync-vulnerabilities.png
---
Security researchers at Google, namely Pedro Gallegos, Simon Scannell, and Jasiel Spelman, identified vulnerabilities in both the rsync server and client. These vulnerabilities range from extremely concerning to just annoying, and are at different stages of being patched. This blog post will be updated as patches are released by us.

## The Announcement
The server vulnerabilities ([CVE-2024-12084](https://access.redhat.com/security/cve/CVE-2024-12084) and [CVE-2024-12085](https://access.redhat.com/security/cve/CVE-2024-12085)) can lead to remote code execution (RCE). On the client side, vulnerabilities allow a malicious server to read arbitrary files ([CVE-2024-12086](https://access.redhat.com/security/cve/CVE-2024-12086)), create unsafe symlinks ([CVE-2024-12087](https://access.redhat.com/security/cve/CVE-2024-12087)), and, under certain conditions, overwrite arbitrary files ([CVE-2024-12088](https://access.redhat.com/security/cve/CVE-2024-12088)). Additionally, during the coordinated response to these issues, Aleksei Gorban reported a sixth vulnerability ([CVE-2024-12747](https://access.redhat.com/security/cve/CVE-2024-12747)) related to how the rsync server manages symlinks.

These vulnerabilities were responsibly disclosed to us through the CERT/CC Vulnerability Notes Database, ahead of the [public disclosure](https://www.kb.cert.org/vuls/id/952657) on January 14, 2025.

# Impact and Mitigation:

## AlmaLinux OS 8 & AlmaLinux OS  9
AlmaLinux 8 and AlmaLinux 9 are vulnerable only to 5 of the 6 CVEs (CVE-2024-12085, CVE-2024-12086, CVE-2024-12087, CVE-2024-12088, and CVE-2024-12747). Red Hat has released patches addressing only CVE-2024-12085. That was promptly released for [AlmaLinux 8](https://errata.almalinux.org/8/ALSA-2025-0325.html) and [AlmaLinux 9](https://errata.almalinux.org/9/ALSA-2025-0324.html) as part of our normal patch and release workflow.

We have also prepared packages with patches for the remaining vulnerabilities from upstream Rsync, but ALESCo is still discussing releasing those patches if Red Hat does not patch them. If these patches are important to you and your rsync use-cases please [let ALESCo know in the ALESCo room on the AlmaLinux community chat](https://chat.almalinux.org/almalinux/channels/alesco)!

#### Vulnerabilitiy Status
* CVE-2024-12084 - Not Affected on AlmaLinux 8 or 9
* CVE-2024-12085 - Patched on AlmaLinux 8 and 9
* CVE-2024-12086 - Vulnerable on AlmaLinux 8 and 9
* CVE-2024-12087 - Vulnerable on AlmaLinux 8 and 9
* CVE-2024-12088 - Vulnerable on AlmaLinux 8 and 9
* CVE-2024-12747 - Vulnerable on AlmaLinux 8 and 9

#### Patched Packages (CVE-2024-12085)
* rsync-3.1.3-20.el8_10.x86_64.rpm
* rsync-3.1.3-20.el8_10.aarch64.rpm
* rsync-3.1.3-20.el8_10.ppc64le.rpm
* rsync-3.1.3-20.el8_10.s390x.rpm
* rsync-daemon-3.1.3-20.el8_10.x86_64.rpm
* rsync-daemon-3.1.3-20.el8_10.aarch64.rpm
* rsync-daemon-3.1.3-20.el8_10.ppc64le.rpm
* rsync-daemon-3.1.3-20.el8_10.s390x.rpm
* rsync-3.2.3-20.el9_5.1.x86_64.rpm
* rsync-3.2.3-20.el9_5.1.aarch64.rpm
* rsync-3.2.3-20.el9_5.1.ppc64le.rpm
* rsync-3.2.3-20.el9_5.1.s390x.rpm
* rsync-daemon-3.2.3-20.el9_5.1.x86_64.rpm
* rsync-daemon-3.2.3-20.el9_5.1.aarch64.rpm
* rsync-daemon-3.2.3-20.el9_5.1.ppc64le.rpm
* rsync-daemon-3.2.3-20.el9_5.1.s390x.rpm

## AlmaLinux OS Kitten 10
On January 14, 2025 we released an updated package for AlmaLinux OS Kitten 10 addressing all six vulnerabilities without waiting for patches to be included in CentOS Stream 10. If Red Hat chooses to only patch some of the vulnerabilities we will carry patches for all of the vulnerabilities within AlmaLinux Kitten 10 (which would be a deviation from Red Hat).

#### Vulnerabilitiy Status
* CVE-2024-12084 - Patched on AlmaLinux OS Kitten 10
* CVE-2024-12085 - Patched on AlmaLinux OS Kitten 10
* CVE-2024-12086 - Patched on AlmaLinux OS Kitten 10
* CVE-2024-12087 - Patched on AlmaLinux OS Kitten 10
* CVE-2024-12088 - Patched on AlmaLinux OS Kitten 10
* CVE-2024-12747 - Patched on AlmaLinux OS Kitten 10

#### Patched Packages
* rsync-3.3.0-6.el10.alma.1.x86_64.rpm
* rsync-3.3.0-6.el10.alma.1.x86_64_v2.rpm
* rsync-3.3.0-6.el10.alma.1.aarch64.rpm
* rsync-3.3.0-6.el10.alma.1.ppc64le.rpm
* rsync-3.3.0-6.el10.alma.1.s390x.rpm

## AlmaLinx rsync Backport Package

AlmaLinux maintains an optional Rsync package that is primarily used by AlmaLinux Mirror maintainers to allow for additional functionality [needed by our mirrors](https://lists.almalinux.org/hyperkitty/list/mirror-announce@lists.almalinux.org/thread/6QKFWQZV2XHDIZ4O4DUOHFFEWLJP47V3/). 

On January 14  we released updates for these backported rsync RPMs. rsync from this backport repo was at version 3.3.0, and we updated the repo to 3.4.0 and subsequently 3.4.1, as the updates were released upstream. 

#### Vulnerabilitiy Status
* CVE-2024-12084 - Patched in rsync Backport Package
* CVE-2024-12085 - Patched in rsync Backport Package
* CVE-2024-12086 - Patched in rsync Backport Package
* CVE-2024-12087 - Patched in rsync Backport Package
* CVE-2024-12088 - Patched in rsync Backport Package
* CVE-2024-12747 - Patched in rsync Backport Package

#### Patched Packages
* rsync-3.4.0-1.el8.x86_64.rpm (regressions fixed in rsync-3.4.1-1.el8.x86_64.rpm)
* rsync-3.4.0-1.el9.x86_64.rpm (regressions fixed in rsync-3.4.1-1.el9.x86_64.rpm)
* rsync-3.4.0-1.el8.aarch64.rpm (regressions fixed in rsync-3.4.1-1.el8.aarch64.rpm)
* rsync-3.4.0-1.el9.aarch64.rpm (regressions fixed in rsync-3.4.1-1.el9.aarch64.rpm)

## Further updates

We will update this blog post as future updates are available. Please also sign up for the AlmaLinux Announce mailing list to make sure you don't miss any updates. If you have any questions or concerns, feel free to reach out in our [community chat](https://chat.almalinux.org)! 

