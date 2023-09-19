---
title: "FIPS Validation for AlmaLinux OS"
type: blog
author:
 name: "Simon John"
 bio: "Security Standards Architect"
 image: /users/sjohn.png
date: '2023-09-19'
post:
    title: "FIPS Validation for AlmaLinux OS"
    image: /blog-images/fips140.png

---

*Note: We want to thank the folks at CloudLinux (one of our Platinum sponsors) for covering the nearly $400,000 in fees and costs (not to mention the time and effort that Simon put in) that it took for AlmaLinux 9.2 to achieve FIPS compliance. FIPS 140-3 will be valid for anyone using AlmaLinux OS 9.2, as long as it is supported. Once 9.3 is released, only TuxCare customers will be able to continue to receive updates for AlmaLinux 9.2 and the FIPS modules. Find more information about that at the end of the article below! -- benny.*

--

Hi, my name is Simon, you may have seen me around the [forum](https://almalinux.discourse.group/u/sej7278/), generally giving advice about kickstart (one of my favourite technologies). I also help write the [CIS benchmarks](https://www.cisecurity.org/benchmark/almalinuxos_linux) for AlmaLinux. In this post I'm going to talk about my day job at CloudLinux, which for the last nine months or so has focused on getting AlmaLinux OS 9 FIPS 140-3 validated.

## So what is FIPS?

The [Federal Information Processing Standard 140-3](https://csrc.nist.gov/pubs/fips/140-3/final) is the latest set of requirements from NIST in the US and the Canadian Centre for Cyber Security, for products that use cryptography in a system that processes "Sensitive But Unclassified" (SBU) information.

Basically to sell a security product to the US Federal government (and other regulated markets such as infrastructure, energy, telecoms, finance and healthcare) you have to prove that you're only using approved algorithms for encryption, hashing, signing and so on. You may have heard that [MD5 is deprecated](https://en.wikipedia.org/wiki/MD5) and [you shouldn't use SSLv3](https://security.googleblog.com/2014/10/this-poodle-bites-exploiting-ssl-30.html), well FIPS goes into much more detail.

FIPS 140-3 is a prerequisite for other security regulations and acts of law such as [CMMC](https://dodcio.defense.gov/CMMC/About/), [FedRAMP](https://www.fedramp.gov/), [HIPAA](https://www.hhs.gov/hipaa/index.html) and [FISMA](https://www.cisa.gov/topics/cyber-threats-and-advisories/federal-information-security-modernization-act); the certificates can also be used as evidence for complying with [Common Criteria](https://commoncriteriaportal.org/), [SOX](https://en.wikipedia.org/wiki/Sarbanes%E2%80%93Oxley_Act), [ISO27001](https://www.iso.org/standard/27001) and [PCI-DSS](https://www.pcisecuritystandards.org/) data encryption requirements. It's seen as the gold standard, so companies that aren't even required to comply will seek to, so they know they have a well-tested baseline for cryptography.

Claiming FIPS compliance just by running `update-crypto-policies --set FIPS` is not enough for these industries, you have to be formally validated to get your name on a certificate to show an auditor. Think of it like a university degree - you can put it on your resume but you won't get the job without producing your diploma.

## The validation process

The [Cryptographic Module Validation Program](https://csrc.nist.gov/projects/cryptographic-module-validation-program) is how you get your hardware, software or even firmware validated.

Once you've picked an accredited CST lab ([atsec](https://www.atsec.com/services/fips-140-2-and-fips-140-3-testing/index.html) in our case) and agreed on the hardware platforms (x86_64 and aarch64), Operating Environment (AlmaLinux 9) and modules (we picked the Kernel Crypto API and OpenSSL FIPS Provider to start with) you're going to validate, you reach **milestone 1** - the [Implementation Under Test](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/modules-in-process/IUT-List) list, which we were added to in December 2022.

Next the labs perform a code review and gap analysis to find any non-compliances. This is the painful part! You basically get a list of ways that AlmaLinux in FIPS mode doesn't meet the standards and have to go and fix them. We spent the next few months developing patches and passing them back to the labs to test. Since this is a long process, we also had to adjust to meet the updates that were released in the related standards (FIPS 186-5 got released, some DRBG caveats expired and the RNG implementation mandated the use of SHA3) and in the AlmaLinux packages - in fact we started on 9.1, so the patches were re-written and re-tested **a lot!**

Once you and the lab believe the software is ready and compliant, *functional* testing is performed by the lab, and if you pass that, you progress to **milestone 2** - the [Cryptographic Algorithm Validation Program](https://csrc.nist.gov/projects/cryptographic-algorithm-validation-program), which validates that you have *implemented the cryptography correctly*. We received our CAVP [certificates](https://csrc.nist.gov/projects/cryptographic-algorithm-validation-program/validation-search?searchMode=implementation&vendor=cloudlinux&productType=-1&ipp=100) in June 2023.

**Milestone 3** is [Entropy Source Validation](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/entropy-validations/esv), which involves sending a bunch of data to an automated server run by NIST that in basic terms tests that your random number generator is random enough - something very important in the world of cryptography. We received our ESV [certificates](https://csrc.nist.gov/projects/cryptographic-module-validation-program/entropy-validations/search?Vendor=cloudlinux&ipp=25) in September 2023 and were actually the first software implementation to receive a FIPS 140-3 ESV certificate using SHA3-256 as a conditioner (256-bits of entropy as opposed to the previous 64-bit LFSR implementation).

**Milestone 4** is the [Modules In Process](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/modules-in-process/Modules-In-Process-List) list, which is where we are currently sitting, whilst we wait for our final certificates that will be listed on the validated modules list [here](https://csrc.nist.gov/Projects/cryptographic-module-validation-program/validated-modules/search) eventually. There's usually a 6-8 month waiting list for reviews (you can count the number of organisations with FIPS 140-3 certificates on one hand) but once you're on the MIP list, it's safe to say you're going to get your certificate and most people are happy to start using your product.

Did I mention I like to write documentation? Well there's a whole bunch of it for CMVP! We had help from [jtsec](https://www.jtsec.es/fips-140-3-consulting), but I think we came close to a dozen documents plus the reports atsec produced for NIST, and now a blog post.

## What does this mean for the community?

[CloudLinux](https://www.cloudlinux.com/)'s TuxCare division has sponsored this activity - both my time and the (not inconsiderable!) costs, with the objective that we provide the FIPS-validated modules back to the AlmaLinux community.

This means that anyone can install the openssl and kernel packages from TuxCare on an AlmaLinux 9.2 system, using these [instructions](https://docs.tuxcare.com/enterprise-support-for-almalinux/fips/) and boot into a completely validated environment. You're running the exact same packages as were tested by the labs and validated by NIST. You can test if your favourite software works with the approved algorithms, or maybe you're an infosec enthusiast, sysadmin or developer and just want to try it out for learning purposes. You can get a lot of interesting info from just running commands such as these:

OpenSSL - you'll get a list of about 20 ciphersuites instead of 60 you'd get with a non-FIPS setup:

```bash
$ openssl ciphers -v
TLS_AES_256_GCM_SHA384         TLSv1.3 Kx=any      Au=any   Enc=AESGCM(256)    Mac=AEAD
TLS_AES_128_GCM_SHA256         TLSv1.3 Kx=any      Au=any   Enc=AESGCM(128)    Mac=AEAD
TLS_AES_128_CCM_SHA256         TLSv1.3 Kx=any      Au=any   Enc=AESCCM(128)    Mac=AEAD
ECDHE-ECDSA-AES256-GCM-SHA384  TLSv1.2 Kx=ECDH     Au=ECDSA Enc=AESGCM(256)    Mac=AEAD
```

Kernel self-test results on boot:

```bash
$ journalctl -k -o cat -g alg:
alg: self-tests for sha3-256-generic (sha3-256) passed
alg: self-tests for sha256-avx (sha256) passed
alg: self-tests for rsa-generic (rsa) passed
alg: sha1 (sha1-avx) is disabled due to FIPS
alg: self-tests for sha512-avx (sha512) passed
```

We aim to validate the remaining NSS, GnuTLS and Libgcrypt modules soon. In fact I've already started working on them, so watch this space!

## Going further into the Enterprise Linux ecosystem

For those of you who want to use this in a business environment, who may have regulatory or customer requirements for FIPS 140-3 and would like AlmaLinux 9.2 updates for five more years, Live Patching to avoid downtime, 24/7 tech support, and all of the features enterprises look for, feel free to message me on the [AlmaLinux chat](https://chat.almalinux.org/almalinux/messages/@sej7278) or check out the TuxCare [Enterprise Support for AlmaLinux](https://tuxcare.com/almalinux-enterprise-support/) product pages.
