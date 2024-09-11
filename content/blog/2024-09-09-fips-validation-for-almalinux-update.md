---
title: "FIPS Validation for AlmaLinux OS - update"
type: blog
author:
 name: "Noam Alum"
 bio: "Automation Specialist at JetBackup"
 image: /users/noam.jpeg
date: 2024-09-09
images:
  - /blog-images/2024/benny-we-need-an-image.png
post:
    title: "FIPS Validation for AlmaLinux OS - update"
    image: /blog-images/2024/benny-we-need-an-image.png
---

After a long wait ([view the previous blog post](https://almalinux.org/blog/2023-09-19-fips-validation-for-almalinux/)), the AlmaLinux 9.2 kernel received FIPS validation making, it the first software implementation to receive a FIPS 140-3 ESV certificate using SHA3-256 as a conditioner. It's actually the first EL9 distribution to receive a FIPS 140-3 certificate for the kernel. View the certificate [here](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4750).

## What is FIPx?

When it comes to securing sensitive data, cryptographic standards play a crucial role. One of the most influential standards in this realm is **FIPS**, or **F**ederal **I**nformation **P**rocessing **S**tandards.

FIPS 140-3 is not just a Federal benchmark, it's recognized and respected worldwide, for instance, the European Union's [NIS 2 Directive](https://eur-lex.europa.eu/eli/dir/2022/2555) which focuses on network and information security mandates the use of *up-to-date encryption and cryptography leveraging established standards.* FIPS standards undergo extensive evaluations to ensure that cryptographic algorithms and implementations meet the highest security requirements, making it the gold standard for secure cryptographic practices across the globe.

Anyone who uses [AlmaLinux 9.2](https://almalinux.org/blog/almalinux-92-now-available/) can achieve FIPS compliance for FREE, the only thing you need to do is download the packages from the TuxCare repo [(docs)](https://docs.tuxcare.com/enterprise-support-for-almalinux/fips) and enable FIPS mode:

```bash
dnf -y install https://repo.tuxcare.com/fips/tuxcare-fips-release-latest-9.noarch.rpm
dnf -y install openssl-3.0.7-20.el9_2.tuxcare.1 kernel-5.14.0-284.11.1.el9_2.tuxcare.5
fips-mode-setup --enable
reboot
```

This allows people with less knowledge about cryptography to configure a strong baseline for implementing secure systems.

_Note: AlmaLinux is no longer supported by the Foundation, and has been out of support since AlmaLinux 9.3 was released in [November of 2023](https://wiki.almalinux.org/release-notes/). Backporting security fixes to older versions it out of scope for the foundation, but [Tuxcare](https://tuxcare.com/) does provide that service to their customers. Since FIPS is primarily required by institutions that like support contracts, we strongly recommend anyone who's looking for it, talk to them._

### Testing

To test this, we can setup an HTTP server, for example [Apache](https://httpd.apache.org) - if you're interested, we have a comprehensive guide on [setting up a LAMP server](https://wiki.almalinux.org/series/LAMP-server.html) on AlmaLinux, but for now we can just run:

```bash
dnf -y install httpd mod_ssl
systemctl start httpd
```

If you were to scan the server using nmap, you would see something like this:

![nmap scan in fips mode](/blog-images/2024/nmap-fips.png)

For reference, with FIPS mode disabled you get the weaker TLSv1.2 and non-compliant ciphersuites using Edwards curves, SHA1 hashes and ChaCha20-Poly1305 ciphers:

![nmap scan in non-fips mode](/blog-images/2024/nmap-nonfips.png)

Another way to check your ciphers strength is to look them up on the [Ciphersuite Info](https://ciphersuite.info) website or using the [sslscan](https://github.com/rbsec/sslscan) tool.

### Whats next?

Simon John, the Security Certification Manager at [CloudLinux](https://cloudlinux.com/) has let me know that after AlmaLinux 9.5 gets released he is going to start working on the 9.6 validation, which hopefully will materialize faster than 9.2 due to improvements in the CMVP process aimed at reducing the backlog.
