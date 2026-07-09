---
title: "Januscape and Bad Epoll: AlmaLinux 9 and 10 patches released"
type: blog
author:
  name: "Andrew Lukoshko"
  bio: "AlmaLinux Lead Architect"
  image: /users/alukoshko.jpg
date: "2026-07-06"
images:
  - /blog-images/2026/2026-07-06-januscape-bad-epoll.png
post:
  title: "We are shipping patched kernels for two serious flaws: Januscape (CVE-2026-53359), a KVM/x86 guest-to-host escape that gives an attacker root on the host, and Bad Epoll (CVE-2026-46242), a local privilege escalation. Januscape affects every AlmaLinux release; Bad Epoll affects AlmaLinux 9 and 10. Patched kernels are in the testing repository now — please help us verify them."
  image: /blog-images/2026/2026-07-06-januscape-bad-epoll.png
---

## Update: AlmaLinux 9 and 10 patches are now in production

**The patched kernels for Januscape (CVE-2026-53359) and Bad Epoll (CVE-2026-46242) have been released to the production repositories for AlmaLinux 9 and AlmaLinux 10.** On those releases you no longer need to enable the testing repo. Just run:

```bash
sudo dnf clean metadata && sudo dnf upgrade
sudo reboot
```

The fixed versions released to production are **`kernel-5.14.0-687.23.1.el9_8`** (AlmaLinux 9) and **`kernel-6.12.0-211.31.1.el10_2`** (AlmaLinux 10), or higher. Confirm you are running the patched version with `uname -r` after rebooting. Most mirrors sync every few hours, so if the update is not available to you yet, try again a little later.

**AlmaLinux 8 is still in the testing repository.** Its patched kernel has not yet moved to production; AlmaLinux 8 users should follow the testing-repo steps below (and we would still appreciate your help verifying it). We will update this post again when the AlmaLinux 8 kernel is released to production.

Thanks to everyone who helped verify these patches — community testing got them into production faster than we could have managed alone.

---

We are shipping patched kernels for **two** serious Linux kernel vulnerabilities and would like your help verifying them before they go to production. The first, **Januscape** ([CVE-2026-53359](https://www.cve.org/CVERecord?id=CVE-2026-53359)), is a flaw in KVM/x86 with several distinct impacts. In its most serious form it is a guest-to-host escape: an attacker who can start a virtual machine can break out and run commands as root on the host. The same bug can also be used from inside a guest to crash the host kernel, a denial of service against every other tenant on that machine. And on any host where the KVM modules are loaded and `/dev/kvm` is world-accessible at `0666`, as it is by default, an unprivileged local user can trigger it to gain root with no virtual machine in use at all. The second, **Bad Epoll** ([CVE-2026-46242](https://github.com/J-jaeyoung/bad-epoll)), is a use-after-free in the kernel's epoll subsystem that lets an unprivileged local user escalate to root.

**Januscape affects every supported AlmaLinux release (8, 9, and 10). Bad Epoll affects AlmaLinux 9 and 10.** Patched kernels covering both flaws are available in the testing repository today.

## Januscape (CVE-2026-53359): a KVM/x86 guest-to-host escape

Januscape is a vulnerability in KVM/x86 that allows a guest to escape to the host and execute commands there with **root privileges**. It can be triggered on both **Intel and AMD** hardware.

The practical impact is significant: an attacker can escape to the host after creating a VM instance on a multi-tenant x86 public cloud (for example AWS or GCP). On distributions where `/dev/kvm` is world-accessible with `0666` permissions — as it is on RHEL and its derivatives — the same bug can also be used as a reliable local privilege escalation for an unprivileged user to gain root, though that is a minor concern next to the host escape itself.

It is closely related to **ITScape (CVE-2026-46316)**, the KVM/arm64 escape reported previously by the same researcher. Given the market share of x86, this variant is considerably more destructive: **nearly all cloud hosts are affected.**

The flaw is remarkably old. The affected range spans from commit `2032a93d66fa` (2010-08-01) to `81ccda30b4e8` (2026-06-16) — it lay dormant for roughly **16 years**. It was reported to security@kernel.org and is now [patched in mainline](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=81ccda30b4e83d8f5cc4fd50503c44e3a33abfeb).

Januscape is tracked as [CVE-2026-53359](https://www.cve.org/CVERecord?id=CVE-2026-53359).

## Bad Epoll (CVE-2026-46242): a local privilege escalation

Bad Epoll is a race-condition use-after-free in the kernel's **epoll** subsystem. When two of epoll's close paths run concurrently, one can free an object while the other is still writing to it. The public analysis demonstrates turning that small use-after-free write into control of a file object, then into arbitrary kernel memory access and code execution — a reliable local privilege escalation from an unprivileged user to root.

Bad Epoll was reported by **Jaeyoung Chung** to Google's kernelCTF program, and a detailed write-up and proof-of-concept are [published on GitHub](https://github.com/J-jaeyoung/bad-epoll). **AlmaLinux 9 and 10 are affected; AlmaLinux 8 is not.**

## Patching ahead of our upstream

Security is a top priority at AlmaLinux. A guest-to-host cloud escape that affects nearly every x86 host, combined with a reliable local root, is exactly the kind of pairing we do not want to sit on. Our core team has backported the fixes for both flaws to every affected AlmaLinux branch. The decision to ship ahead of a CentOS Stream / RHEL update was made by our technical steering committee, [ALESCo](https://almalinux.org/blog/2024-05-21-introducing-alesco/).

These kernels are available **in the testing repository today**. After the community has helped verify them, we will release them to the production repositories. This blog post will be updated when that happens.

## Help us test

It only takes a few steps to install and test the patched kernel from the testing repo.

**Install the testing repo**

```bash
sudo dnf install -y almalinux-release-testing
```

**Update the kernel**

```bash
sudo dnf update 'kernel*' --enablerepo=almalinux-testing
```

**Reboot to load the new kernel**

```bash
sudo reboot
```

**Confirm you are running the patched kernel**

```bash
uname -r
rpm -q kernel
```

You should see one of the patched versions listed below (or higher).

We don't recommend keeping the testing repo enabled after you've updated, unless you've done this on a truly non-production environment. If this is a production environment, you can disable the repo with this command:

```bash
sudo dnf config-manager --disable almalinux-testing
```

If you encounter problems, please let us know as soon as you can, either in [AlmaLinux chat](https://chat.almalinux.org) or on [bugs.almalinux.org](https://bugs.almalinux.org).

## Affected versions and patched kernels

| Release      | Januscape | Bad Epoll | Patched kernel                   | Availability   |
| ------------ | :-------: | :-------: | -------------------------------- | -------------- |
| AlmaLinux 8  |    yes    |    no     | `kernel-4.18.0-553.139.4.el8_10` | testing        |
| AlmaLinux 9  |    yes    |    yes    | `kernel-5.14.0-687.23.1.el9_8`   | **production** |
| AlmaLinux 10 |    yes    |    yes    | `kernel-6.12.0-211.31.1.el10_2`  | **production** |

Install the version listed for your release, or higher.

## Thanks

Thanks to the security researchers who found, analyzed, and reported these vulnerabilities upstream, and to **Jaeyoung Chung** for the public Bad Epoll write-up that made it possible to understand and verify the fix.

Thanks as well to the AlmaLinux core team for turning around patched builds for every affected release, and to ALESCo for moving quickly to approve shipping ahead of upstream. And thank you in advance to everyone in the community who helps us test these kernels — that's the part that gets them safely into production.

## Stay informed

Remaining aware of these vulnerabilities and acting quickly can keep your systems and data safe. Follow the AlmaLinux Blog, join the [Mattermost Community Chat](https://chat.almalinux.org/), and subscribe to the [Announce](https://lists.almalinux.org/mailman3/lists/announce.lists.almalinux.org/) and [Security](https://lists.almalinux.org/mailman3/lists/security.lists.almalinux.org/) mailing lists to stay informed. We will update this post when the patched kernels move from testing to production.
