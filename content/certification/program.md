---
title: "The AlmaLinux Certification Program"
type: p
aliases:
  - /certification/hardware-certification/hardware-certification-program/
---

###### last updated - September 2026

The AlmaLinux Certification Program, run by the [AlmaLinux Certification SIG](https://wiki.almalinux.org/sigs/Certification.html) (Special Interest Group), certifies that hardware and software work correctly on AlmaLinux OS. Certification is free, the suite is open source, and you run it yourself. Before 2026 you had to file a form, wait for a scheduled slot, sometimes ship hardware to us, and then wait days for the test run.

Certification here is a statement about compatibility. It says that AlmaLinux runs correctly on a piece of hardware, or that a piece of software runs correctly on AlmaLinux. This is not a regulatory or security certification. AlmaLinux OS 9.2 has those separately: [FIPS 140-3 validated cryptographic modules](/security/fips-certification/) and a [Common Criteria certification](/security/cc-certification/).

This document is for hardware and software vendors, and for anyone who wants to certify equipment or software they use. Certified hardware and software are listed in the [AlmaLinux Catalog](https://catalog.almalinux.org). If you have questions about anything here, ask in the [~SIG/Certification](https://chat.almalinux.org/almalinux/channels/sigcertification) room on [chat.almalinux.org](https://chat.almalinux.org).

## Validation levels

Every entry in the catalog includes the level of validation, which tells you who ran the test. Community validated means our users have confirmed the functionality, which is just as valuable to us and our community as a vendor listing.

Validations are cumulative. A vendor, the AlmaLinux OS Foundation, and any number of community members can all add their own attestation to the same listing, and each one adds to the confidence in that certification. A listing with more than one leads with the vendor's validation, and the others stay on the page.

- **Community validated:** submitted by a community member. For hardware it is backed by certification suite data, the same suite vendors and the Foundation run. For software it is a confirmation that the product works on a given release, counted one per person per release.
- **AlmaLinux validated:** tested and certified directly by the AlmaLinux OS Foundation.
- **Vendor validated:** published by the vendor under their own account and backed by their own testing data. This is the path for hardware and software vendors who want to state compatibility officially and list AlmaLinux as a supported operating system.

Validation is recorded for each AlmaLinux major version separately, and the catalog shows whether a release was proven by a run or only stated as supported. A product certified on AlmaLinux 9 and then left alone shows an empty row for AlmaLinux 10 until someone validates it there, so plan to revalidate when a new major version lands.

## How hardware certification works

You run the suite and publish the results. We review what arrives.

### Run the suite

Boot our regular [live media](/get-almalinux/#Live_Media-x86_64-10) on the system you want to certify, or run the suite on an existing AlmaLinux installation. Nothing needs to be wiped or reinstalled, so you can certify hardware that is already in service.

The suite is packaged as an RPM in the [`extras` repository](https://wiki.almalinux.org/repos/AlmaLinux.html), so installing it is `dnf install alma-certify`. Nearly all hardware completes a certification run in under 10 minutes. Benchmarks do not run by default, and they take longer than that when you ask for them, because some of them do real work such as building CPython from source.

Live media cannot certify a GPU that needs a proprietary driver, because installing the NVIDIA driver requires a reboot and a live root does not survive one. Those cards need an installed system with the driver already working. Everything else, including cards on in-tree drivers, certifies from live media normally.

`alma-certify` is open source and lives in the [alma-certify](https://github.com/AlmaLinux/alma-certify) repository, along with its documentation and issue tracker.

`alma-certify` is a full rewrite. It replaces the earlier Ansible-based Hardware Certification Suite, and it runs directly on the machine being certified instead of driving it remotely. If you have automation built against the old suite, read through the repository before your first run: the invocation and the output format are both different.

### What can be certified

A run on another distribution warns you and continues if you say so, but it cannot certify anything. It stays local, `alma-certify submit` declines it, and a bundle that reaches the catalog another way is held for a reviewer. The check reads the report itself, so uploading from an AlmaLinux machine does not change the outcome.

The same is true of a whole machine certified inside a virtual machine or a container, where the firmware, storage controller, and network device under test all belong to the hypervisor. A GPU passed through to a guest is the real device, so a GPU-scoped run is the one claim a virtual machine can make, and it submits normally.

You keep the results either way, and `alma-certify bundle` still produces a shareable archive.

### Publish your results

Running the suite does not require an account. Publishing what you found needs a free [AlmaLinux Account](https://accounts.almalinux.org), the same account system the [catalog](https://catalog.almalinux.org) authenticates against. Vendors publishing under a vendor account produce a vendor validated listing, and everyone else produces a community validated listing.

You start the run, the machine shows you a code, and you approve it from your own browser or by scanning a QR code with your phone.

### Review

Every submission goes into a review queue before it appears in the catalog, whether it comes from a vendor, from a community member, or from us.

The catalog checks each result bundle as it arrives. The report has to match the schema the suite publishes, the files have to match their checksums, and a run made on something other than AlmaLinux is held for a person. A reviewer then looks at the submission itself, including whether it duplicates a listing that already exists, and sets the validation level it is published at. Vendor accounts are verified separately, before anything can be published on a vendor's behalf.

Bring a failure you do not understand, or a test you want added, to the SIG chat room.

## What the suite tests

`alma-certify` runs directly on the machine being certified and produces a machine-readable report that the catalog ingests. It supports AlmaLinux 8, 9, and 10 on x86_64 and aarch64, and it needs root on the machine under test. ppc64le and s390x are not supported, because the suite reads SMBIOS to identify the machine and the tool it uses for that is not built for either architecture.

**Collect** takes a normalized hardware inventory, covering CPUs, memory, disks, network cards, GPUs, firmware, and driver versions. **Validate** answers whether AlmaLinux works correctly on the hardware, and these are the tests that decide certification. **Benchmark** measures performance, and those results feed the public leaderboards in the catalog. Benchmarking is optional and off by default, so a certification run never waits on it.

The validation checks are short functional runs that confirm the hardware behaves correctly. They cover:

- CPU and memory: verified computation and memory error counters.
- Storage: SMART health, NVMe error logs, and a write-and-read-back pass confirming that every block survives the round trip.
- Networking: every PCI network controller has a driver bound and produced an interface, with an optional throughput check against a peer machine.
- Kernel and platform: taint bits that indicate a real fault, kernel error messages, PCIe AER errors, the real-time clock, thermal trip points, watchdogs, Secure Boot state, and firmware versions.
- Baseboard management controllers, where the machine has one, including chassis health as the controller reports it.
- Virtualization, by loading the KVM modules and booting a minimal guest.
- GPUs: NVIDIA driver and CUDA checks that confirm the card computes correct answers.
- Power management and peripherals: frequency governors, display backlight, suspend and resume, and USB hotplug.

Tests are required, conditional, or informational. A required test failing fails the certification. A conditional test skips with a reason when it does not apply, and fails certification if it runs and fails. An informational test is recorded for the reviewer and never gates the result. A few checks need somebody at the machine, such as a reboot, a suspend and resume, or plugging a USB device in and out, and those only run when you ask for them.

Benchmarks cover CPU, memory bandwidth and latency, network throughput, cryptography, compression, compilation, scheduling, and GPU compute. Each result records its metric and unit, and captures the tuned profile, CPU governor, SMT state, and mitigation status, so you can compare two machines fairly.

For the current catalog of tests on any machine, run `alma-certify list`.

## How software certification works

There is no suite to run against an application the way there is against a machine, so software certification works differently. A software certification covers a whole major version of AlmaLinux, so one listing applies across its minor releases.

Publishers list their product in the catalog, cite the AlmaLinux releases it supports, and submit their own testing data for a vendor validated listing. A publisher that is not in the catalog yet can be added as part of the same submission.

Anyone running the software can confirm that it works on the release they are using. Those confirmations are counted one per person per release, and they sit alongside the publisher's certification. If you are running a product on a release its publisher has not cited, you can report that too, and it appears on the listing once a reviewer accepts it. We want to get those reports back to publishers as the catalog grows.

Software listings do not record licensing. Check the publisher's site for whether a product is open source or commercial.

## Certification lifecycle

The SIG certifies against major versions of AlmaLinux, on the expectation that minor versions carry forward. Hardware certified for AlmaLinux 9 does not need to be recertified until AlmaLinux 10.

Because a run now takes minutes, we encourage community checkups on minor version updates and re-confirmation of existing listings. You do not need to coordinate those with us.

## For vendors

Vendors who want a vendor validated listing should start by joining the [~SIG/Certification](https://chat.almalinux.org/almalinux/channels/sigcertification) room and setting up a vendor account on the catalog.

Hardware can be certified before it is announced. Mark the submission as pre-release and set the date its results become public. Until that date the run is not listed anywhere.

If you need your interaction with the SIG to be private, for example because you are working under a non-disclosure agreement, the Certification SIG maintains a private mailing list at [certification-sig@lists.almalinux.org](mailto:certification-sig@lists.almalinux.org).

Once a certification is published, we ask that you list AlmaLinux as a supported operating system for the tested hardware. If your organization joins the Foundation as a sponsor member, the Marketing SIG will work with you on publicity around the certification.

If you need the Foundation to host hardware for ongoing testing, or you want to donate hardware, reach out through the SIG chat room or the mailing list and we will make arrangements.

## Where to reach us

- [Mattermost chat, SIGs/Certification](https://chat.almalinux.org/almalinux/channels/sigcertification), the primary place the community engages with the SIG, on both certifications and the suite itself. It is bridged to Matrix at [#sig-certification:almalinux.im](https://app.almalinux.im/#/room/#sig-certification:almalinux.im).
- [AlmaLinux/alma-certify](https://github.com/AlmaLinux/alma-certify) for the suite, its documentation, and issue tracking.
- [The Certification SIG board](https://github.com/orgs/AlmaLinux/projects/6) for asynchronous planning.
- [certification-sig@lists.almalinux.org](mailto:certification-sig@lists.almalinux.org) for conversations that need to stay private.
