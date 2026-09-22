---
title: "Software certification is here, and hardware certification takes under 10 minutes"
type: blog
author:
  name: "Jonathan Wright"
  bio: "Infrastructure SIG Lead & ALESCo Member"
  image: /users/jonathan.jpg
date: "2026-09-22"
images:
  - /blog-images/2026/2026-09-22-certification-in-minutes.png
post:
  title: "Software certification is live, a hardware certification run now takes under 10 minutes, and we're proud to announce our brand new AlmaLinux Certification Catalog at catalog.almalinux.org."
  image: /blog-images/2026/2026-09-22-certification-in-minutes.png
---

Two years ago we [announced the AlmaLinux Certification SIG](/blog/2024-09-10-announcing-new-certification-sig/) and the Hardware Certification Program. That post ended with three things we wanted and didn't have yet: software certification, toolkits so that vendors and community members could certify things easily themselves, and a way to certify a machine without installing AlmaLinux on it first. We have all three today, plus a new place to share the results.

The old program worked, but it asked too much time of you and of us, and this is how we fixed it!

## Software certification is here

You can now certify software for AlmaLinux, not just hardware. Software certification is something worthwhile for our users, because so many people want to know if the software they use daily works on AlmaLinux before they switch. We invite community members and software publishers alike to help us fill this out!

As software providers, you just list your product, cite the releases it supports, and submit. If your company isn't in the catalog yet, you can create it at the same time.

As a community member or AlmaLinux user, helping us certify software is easy. Just sign in to [catalog.almalinux.org](https://catalog.almalinux.org) and confirm that a product works on the release you're running.

## Hardware certification in under 10 minutes

The [suite](https://github.com/AlmaLinux/alma-certify) is rewritten, and for the overwhelming majority of systems a certification run now finishes in under 10 minutes. It ships as an RPM in the [`extras` repository](https://wiki.almalinux.org/repos/AlmaLinux.html):

```bash
dnf install alma-certify
```

You don't need AlmaLinux installed on the machine you want to certify. Our [live media](/get-almalinux/) is enough, so you can reboot a machine that's already doing a job, certify it, and put it back without touching what's on it.

If you're not sure what to run, run `alma-certify` with no arguments. It walks you through the options, builds the correct command using your answers, and runs it with your approval!

Registering a machine is easy, too! You start the run, the machine shows you a code, and you approve it from your own browser or by scanning a QR code with your phone.

Note: do you run a datacenter? If you happen to be deploying new servers, making this part of your deploy using the QR code to register would be a huge help to us, and shouldn't take much of your time at all!

The suite also takes a normalized inventory of a machine, covering CPUs, memory, disks, network cards, GPUs, firmware, and driver versions.

Benchmarking is still included in the suite as an option, but no longer runs by default. It still covers CPU, memory bandwidth and latency, network throughput, cryptography, compression, compilation, scheduling, and GPU compute, and those results feed public leaderboards in the catalog so you can see how a machine compares to others like it.

## The catalog

All of this work ends up in the brand new [catalog.almalinux.org](https://catalog.almalinux.org). It shows information for systems, components, software, benchmarks, and validations.

Every listing says who did the testing: the vendor, the AlmaLinux OS Foundation, or a community member. Those validations stack and complement each other, and they're tracked per AlmaLinux major version. The [certification page](/certification/) has the details.

Publishing your results requires an [AlmaLinux Account](https://accounts.almalinux.org), and every submission goes through review before it appears, whether it comes from a vendor, from a community member, or from us. Everything in the catalog is also available through a public, read-only API, so pull this data into your own tooling if it's useful to you.

One clarification, because the word gets used loosely: our certification is a statement about compatibility. It says that AlmaLinux runs correctly on this hardware, or that this software runs correctly on AlmaLinux. It isn't a regulatory or security certification. We do also have those separately ([FIPS 140-3 validated cryptographic modules](/security/fips-certification/) and a [Common Criteria certification](/security/cc-certification/) at EAL1), but this is separate.

## For vendors

Vendors had some of the hardest times getting us information: from the amount of time required for the tests, to the amount of work it took to get things listed on the website. It's now much, much easier.

`alma-certify` is a full rewrite of the suite. It replaces the Ansible-based suite that we used to provide, runs directly on the machine being certified, and produces a report the catalog can ingest. As always, it's fully [open source](https://github.com/AlmaLinux/alma-certify).

You can also submit results for hardware you haven't announced yet and set the date they become public. The [program page](/certification/program/) covers the rest of the process. Reach out to the [~SIG/Certification](https://chat.almalinux.org/almalinux/channels/sigcertification) room directly if you have questions.

## Go try it

Two things would make all of this worth it. A lot of people and organizations want proof that AlmaLinux runs on the hardware they already own before they'll give it a try, and now they can get that proof themselves. Every result that gets submitted makes the case to hardware and software vendors that supporting AlmaLinux officially is a low-effort thing to do.

So if you have hardware sitting in front of you, or software you rely on every day, go tell us that it works. The [Certification SIG](https://wiki.almalinux.org/sigs/Certification.html) wiki page has the chat room and meeting details if you want to help shape where this goes next.
