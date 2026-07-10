---
title: "GhostLock (CVE-2026-43499) kernel privilege escalation: Patch released"
type: blog
author:
  name: "Andrew Lukoshko"
  bio: "AlmaLinux Lead Architect"
  image: /users/alukoshko.jpg
date: "2026-07-09"
images:
  - /blog-images/2026/2026-07-09-ghostlock.png
post:
  title: "GhostLock (CVE-2026-43499) is a use-after-free in the kernel's real-time mutex code that lets an unprivileged local user escalate to root and escape containers. It has been present since 2011 and affects every supported AlmaLinux release. Patched kernels are in the testing repository now — please help us verify them."
  image: /blog-images/2026/2026-07-09-ghostlock.png
---

## Update: The fix is now in production

**The patched kernel for GhostLock (CVE-2026-43499) has been released to the production repositories for every affected AlmaLinux release — 8, 9, and 10.** You no longer need to enable the testing repo. Just run:

```bash
sudo dnf clean metadata && sudo dnf upgrade
sudo reboot
```

The fixed versions released to production are **`kernel-4.18.0-553.141.2.el8_10`** (AlmaLinux 8), **`kernel-5.14.0-687.24.1.el9_8`** (AlmaLinux 9), and **`kernel-6.12.0-211.32.1.el10_2`** (AlmaLinux 10), or higher. Confirm you are running the patched version with `uname -r` after rebooting. Most mirrors sync every few hours, so if the update is not available to you yet, try again a little later.

The testing-repo instructions further down in this post remain for reference but are no longer the recommended path. Thanks to everyone who helped verify this patch — community testing got it into production faster than we could have managed alone.

---

A new Linux kernel local-privilege-escalation flaw has been disclosed, and we are shipping patched kernels for it. **GhostLock** ([CVE-2026-43499](https://www.cve.org/CVERecord?id=CVE-2026-43499)) is a use-after-free in the kernel's real-time mutex (rtmutex) priority-inheritance code. An unprivileged local user can exploit it to gain root, and it works from inside a container to escape to the host. No special capabilities are required. **Every supported AlmaLinux release (8, 9, and 10) is affected.** Patched kernels are available in the testing repository today, and we would like your help verifying them before we push them to production.

## What the bug is

GhostLock lives in the kernel's real-time mutex code (`kernel/locking/rtmutex.c`), on the futex priority-inheritance (PI) path. The helper `remove_waiter()` assumes the waiter it is cleaning up always belongs to the currently running task. In the `FUTEX_CMP_REQUEUE_PI` requeue path, however, the kernel has to unwind on behalf of a _different_, sleeping thread when it detects a deadlock cycle and rolls back with `-EDEADLK`. During that rollback it clears `pi_blocked_on` on the wrong task, leaving a **dangling pointer into freed kernel stack memory** — a stack use-after-free.

An attacker triggers it by arranging three futexes and a set of coordinated threads into a priority-inversion deadlock, then reclaiming the freed stack frame with a forged waiter structure. From there the public write-up chains the constrained write into arbitrary kernel read/write, control-flow hijack, and finally root — a reliable, unprivileged local privilege escalation and container escape.

Like several recent kernel flaws, GhostLock is remarkably old: it was introduced back in **2011** (Linux 2.6.39) and sat unnoticed for roughly 15 years. Because it only depends on `CONFIG_FUTEX_PI`, which is enabled on essentially every distribution kernel, the exposure is broad. It was reported to security@kernel.org by **Nebula Security** — who found it with their automated analysis tool, VEGA — and is now fixed in mainline (commit `3bfdc63936dd`, Linux 7.1).

## Patching ahead of our upstream

Security is a top priority at AlmaLinux. A reliable, capability-free local root that also breaks container isolation, present in the kernel for well over a decade, is exactly the kind of flaw we do not want to sit on. Our core team has backported the upstream `rtmutex` fix to every affected AlmaLinux branch. The decision to ship ahead of a CentOS Stream / RHEL update was made by our technical steering committee, [ALESCo](https://almalinux.org/blog/2024-05-21-introducing-alesco/).

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

You should see the version listed for your release below (or higher).

We don't recommend keeping the testing repo enabled after you've updated, unless you've done this on a truly non-production environment. If this is a production environment, you can disable the repo with this command:

```bash
sudo dnf config-manager --disable almalinux-testing
```

If you encounter problems, please let us know as soon as you can, either in [AlmaLinux chat](https://chat.almalinux.org) or on [bugs.almalinux.org](https://bugs.almalinux.org).

## Affected versions and patched kernels

All supported AlmaLinux releases are affected:

- **AlmaLinux 8** is patched in `kernel-4.18.0-553.141.2.el8_10` and above.
- **AlmaLinux 9** is patched in `kernel-5.14.0-687.24.1.el9_8` and above.
- **AlmaLinux 10** is patched in `kernel-6.12.0-211.32.1.el10_2` and above.

Install the version listed for your release, or higher.

## Thanks

Thanks to **Nebula Security** for finding, analyzing, and reporting this vulnerability upstream, and for the public write-up that made it possible to understand and verify the fix.

Thanks as well to the AlmaLinux core team for turning around patched builds for every affected release, and to ALESCo for moving quickly to approve shipping ahead of upstream. And thank you in advance to everyone in the community who helps us test these kernels — that's the part that gets them safely into production.

## Stay informed

Remaining aware of these vulnerabilities and acting quickly can keep your systems and data safe. Follow the AlmaLinux Blog, join the [Mattermost Community Chat](https://chat.almalinux.org/), and subscribe to the [Announce](https://lists.almalinux.org/mailman3/lists/announce.lists.almalinux.org/) and [Security](https://lists.almalinux.org/mailman3/lists/security.lists.almalinux.org/) mailing lists to stay informed. We will update this post when the patched kernels move from testing to production.
