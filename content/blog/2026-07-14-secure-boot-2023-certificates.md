---
title: "Microsoft 2011 Secure Boot certificates have expired — AlmaLinux users are covered!"
type: blog
author:
  name: "Andrew Lukoshko"
  bio: "AlmaLinux Lead Architect"
  image: /users/alukoshko.jpg
date: 2026-07-14
images:
  - /blog-images/2026/2026-07-14-secure-boot-2023-certificates.png
post:
  title: "The Microsoft UEFI Secure Boot certificates from 2011 have expired. Here's why your AlmaLinux systems will keep booting, and how to prepare for future shim updates."
  image: /blog-images/2026/2026-07-14-secure-boot-2023-certificates.png
---

You may have seen news that the Microsoft UEFI Secure Boot certificates from 2011 have expired. The short version for AlmaLinux users: **everything is covered, and your systems will not stop booting.** There is nothing you have to do right now, but a quick check will make sure you are ready for future shim updates. Here is what happened and what we recommend.

## What happened?

The Microsoft certificates that have anchored UEFI Secure Boot since 2011 have reached the end of their lifecycle. The **Microsoft Corporation KEK CA 2011** expired on June 24, 2026, and the **Microsoft Corporation UEFI CA 2011** — the certificate used to sign Linux shim bootloaders — expired on June 27, 2026.

Importantly, the expiration does **not** invalidate anything that is already signed. Existing systems continue to boot exactly as before. What changed is that Microsoft now signs new boot components with the replacement **2023 certificates**, so firmware needs to trust the 2023 certificates to boot newly signed components.

## AlmaLinux has you covered

We prepared for this transition well in advance:

- **x86_64**: The current shim in AlmaLinux 8, 9, and 10 is **dual-signed** with both the 2011 and the 2023 Microsoft UEFI CA. It boots under Secure Boot regardless of whether your firmware has been updated with the 2023 certificates.
- **aarch64**: The current shim is signed with the 2023 Microsoft UEFI CA. If your ARM64 system boots with Secure Boot enabled today, it already trusts the 2023 certificate.

In other words: **no action is required right now, and your existing AlmaLinux systems will keep booting.**

## How to be prepared for future shim updates

At some point, shim builds will be signed with the 2023 certificate only. To be ready for that, we recommend checking that your firmware already carries the 2023 certificates.

First, check whether Secure Boot is enabled at all (if it is disabled, none of this affects you):

```bash
mokutil --sb-state
```

Then check for the 2023 certificates in your firmware's signature database and Key Exchange Key:

```bash
mokutil --db | grep 'UEFI CA 2023'
mokutil --kek | grep 'KEK 2K CA 2023'
```

If both commands print a matching certificate, your system is ready and you are done.

## Adding the 2023 certificate if it is missing

If the commands above return nothing, you can enroll the updated Secure Boot certificates with fwupd. On AlmaLinux 9 and 10:

```bash
sudo dnf install -y fwupd
sudo fwupdmgr refresh
sudo fwupdmgr update
sudo reboot
```

After the reboot, run the verification commands again:

```bash
mokutil --db | grep 'UEFI CA 2023'
mokutil --kek | grep 'KEK 2K CA 2023'
```

Note that AlmaLinux 8 ships an older fwupd version that cannot perform this update — for AlmaLinux 8, air-gapped systems, and virtual machines, see the manual enrollment instructions in the wiki page linked below.

## Learn more

This post is only a summary. The full documentation — including per-release details, manual certificate enrollment, guidance for virtual machines and cloud platforms, and notes on TPM-bound disk encryption — is available on our wiki: [UEFI Secure Boot: transition to 2023 certificates](https://wiki.almalinux.org/documentation/secure-boot-2023-certificates.html).

## Get involved!

If you have any questions or run into issues, join us on [chat.almalinux.org](http://chat.almalinux.org) or report bugs at [bugs.almalinux.org](https://bugs.almalinux.org).

If you want to stay up to date, follow us on [our forum](https://almalinux.discourse.group/), [Reddit](https://www.reddit.com/r/AlmaLinux/), [X](https://twitter.com/AlmaLinux), [Mastodon](https://fosstodon.org/@almalinux/), [LinkedIn](https://www.linkedin.com/company/80320905/), and [YouTube](https://www.youtube.com/channel/UCt9lpkqUPp1FUEi9uqVlPQA).
