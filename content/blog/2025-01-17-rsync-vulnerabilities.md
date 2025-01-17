---
title: "Multiple rsync Vulnerabilities Discovered - Mitigation Status"
type: blog
author: 
    name: "Jonathan Wright"
    bio: "-"
    image: /users/jonathan.jpg
date: '2025-01-17'
post:
    title: "Multiple rsync Vulnerabilities Discovered - Mitigation Status"
    image: 
---
Security researchers at Google, namely Pedro Gallegos, Simon Scannell, and Jasiel Spelman, identified vulnerabilities in both the rsync server and client. The server vulnerabilities ([CVE-2024-12084](https://access.redhat.com/security/cve/CVE-2024-12084) and [CVE-2024-12085](https://access.redhat.com/security/cve/CVE-2024-12085)) can lead to remote code execution (RCE). On the client side, vulnerabilities allow a malicious server to read arbitrary files ([CVE-2024-12086](https://access.redhat.com/security/cve/CVE-2024-12086)), create unsafe symlinks ([CVE-2024-12087](https://access.redhat.com/security/cve/CVE-2024-12087)), and, under certain conditions, overwrite arbitrary files ([CVE-2024-12088](https://access.redhat.com/security/cve/CVE-2024-12088)). Additionally, during the coordinated response to these issues, Aleksei Gorban reported a sixth vulnerability ([CVE-2024-12747](https://access.redhat.com/security/cve/CVE-2024-12747)) related to how the rsync server manages symlinks.

These vulnerabilities were responsibly disclosed to us through the CERT/CC Vulnerability Notes Database, ahead of the [public disclosure](https://www.kb.cert.org/vuls/id/952657) on January 14, 2025.

# Impact and Mitigation:

## AlmaLinx rsync Backport Packages
On January 14, 2025 we released updates for our [backported rsync RPMs](https://wiki.almalinux.org/Mirrors.html) - mainly tailored to mirror owners.  rsync from this backport repo was at version 3.3.0, which was vulnerable to all 6 CVEs.  rsync 3.4.0 was released to address them all, and subsequently 3.4.1 to address regressions discovered in 3.4.0.  We updated the repo to 3.4.0 and subsequently 3.4.1.

#### Vulnerabilitiy Status
CVE-2024-12084 - Patched
CVE-2024-12085 - Patched
CVE-2024-12086 - Patched
CVE-2024-12087 - Patched
CVE-2024-12088 - Patched
CVE-2024-12747 - Patched

#### Patched Packages
rsync-3.4.0-1.el8.x86_64.rpm (regressions fixed in rsync-3.4.1-1.el8.x86_64.rpm)
rsync-3.4.0-1.el9.x86_64.rpm (regressions fixed in rsync-3.4.1-1.el9.x86_64.rpm)
rsync-3.4.0-1.el8.aarch64.rpm (regressions fixed in rsync-3.4.1-1.el8.aarch64.rpm)
rsync-3.4.0-1.el9.aarch64.rpm (regressions fixed in rsync-3.4.1-1.el9.aarch64.rpm)

## AlmaLinux Kitten 10
On January 14, 2025 we released updated package for AlmaLinux Kitten 10 addressing all six vulnerabilities.  At the time of this posting, Red Hat has not patched CentOS Stream 9 or CentOS Stream 10.  If Red Hat chooses to only patch some of the vulnerabilities we will continue to carry patches for all of them within AlmaLinux Kitten 10 - a potential deviation from Red Hat.

#### Vulnerabilitiy Status
CVE-2024-12084 - Patched
CVE-2024-12085 - Patched
CVE-2024-12086 - Patched
CVE-2024-12087 - Patched
CVE-2024-12088 - Patched
CVE-2024-12747 - Patched

#### Patched Packages
rsync-3.3.0-6.el10.alma.1.x86_64.rpm
rsync-3.3.0-6.el10.alma.1.x86_64_v2.rpm
rsync-3.3.0-6.el10.alma.1.aarch64.rpm
rsync-3.3.0-6.el10.alma.1.ppc64le.rpm
rsync-3.3.0-6.el10.alma.1.s390x.rpm

## AlmaLinux 8 & AlmaLinux 9
AlmaLinux 8 and AlmaLinux 9 are vulnerable only to 5 of the 6 CVEs - CVE-2024-12085, CVE-2024-12086, CVE-2024-12087, CVE-2024-12088, and CVE-2024-12747.  On January 14, 2025 we prepared packages for AlmaLinux 8 and AlmaLinux 9 with plans to release them on January 15, 2025.  Red Hat released updates on January 15, 2025 addressing only CVE-2024-12085 which we promptly released for [AlmaLinux 8](https://errata.almalinux.org/8/ALSA-2025-0325.html) and [AlmaLinux 9](https://errata.almalinux.org/9/ALSA-2025-0324.html) as well.  Our builds that patch all five vulnerabilities have not been released as of this posting.

We have patched builds to address all five CVEs but have not released them as of yet.  ALESCo is working to decide if we will release these patched builds and carry the patches moving forward if Red Hat does not also patch them.  This would be a deviation from Red Hat.  If these patches are important to you and your rsync use-cases please [let ALESCo know](https://chat.almalinux.org/almalinux/channels/alesco)!

#### Vulnerabilitiy Status
CVE-2024-12084 - Not Affected
CVE-2024-12085 - Patched
CVE-2024-12086 - Vulnerable
CVE-2024-12087 - Vulnerable
CVE-2024-12088 - Vulnerable
CVE-2024-12747 - Vulnerable

#### Patched Packages (CVE-2024-12085)
rsync-3.1.3-20.el8_10.x86_64.rpm
rsync-3.1.3-20.el8_10.aarch64.rpm
rsync-3.1.3-20.el8_10.ppc64le.rpm
rsync-3.1.3-20.el8_10.s390x.rpm
rsync-daemon-3.1.3-20.el8_10.x86_64.rpm
rsync-daemon-3.1.3-20.el8_10.aarch64.rpm
rsync-daemon-3.1.3-20.el8_10.ppc64le.rpm
rsync-daemon-3.1.3-20.el8_10.s390x.rpm
rsync-3.2.3-20.el9_5.1.x86_64.rpm
rsync-3.2.3-20.el9_5.1.aarch64.rpm
rsync-3.2.3-20.el9_5.1.ppc64le.rpm
rsync-3.2.3-20.el9_5.1.s390x.rpm
rsync-daemon-3.2.3-20.el9_5.1.x86_64.rpm
rsync-daemon-3.2.3-20.el9_5.1.aarch64.rpm
rsync-daemon-3.2.3-20.el9_5.1.ppc64le.rpm
rsync-daemon-3.2.3-20.el9_5.1.s390x.rpm
