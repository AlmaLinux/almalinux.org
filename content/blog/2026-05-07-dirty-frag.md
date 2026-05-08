---
title: "Dirty Frag vulnerability fix is ready for testing"
type: blog
author:
  name: "Andrew Lukoshko"
  bio: "AlmaLinux Lead Architect and ALESCo Chairman"
  image: /users/alukoshko.jpg
date: "2026-05-07"
images:
  - /blog-images/2026/2026-05-07-dirty-frag.png
post:
  title: "A second high-severity local-root flaw landed in the Linux kernel a week after Copy Fail. If you run AlmaLinux on a multi-tenant host, container build farm, CI runner, or any system where untrusted users can get a shell, help us test the fix — or apply the one-line mitigation now."
  image: /blog-images/2026/2026-05-07-dirty-frag.png
---

## The Announcement

A week after [Copy Fail](/blog/2026-05-01-cve-2026-31431-copy-fail/), researcher Hyunwoo Kim disclosed a second Linux kernel flaw in the same broad area — IPsec ESP and rxrpc — that they have named _Dirty Frag_. The bug lives in the in-place decryption fast paths of `esp4`, `esp6`, and `rxrpc`: when a socket buffer carries paged fragments that are not privately owned by the kernel (e.g. pipe pages attached via `splice(2)`/`sendfile(2)`/`MSG_SPLICE_PAGES`), the receive path decrypts directly over those externally-backed pages, exposing or corrupting plaintext that an unprivileged process still holds a reference to.

Like the previous Copy Fail vulnerability, **Dirty Frag immediately yields root on all major distributions**. Every supported AlmaLinux release is affected. Per Hyunwoo Kim's [public disclosure on oss-security](https://www.openwall.com/lists/oss-security/2026/05/07/8) (2026-05-07), the responsible-disclosure embargo was broken before distributions could coordinate, so **no CVE identifiers have been allocated** for either of the two bugs that make up Dirty Frag, and a working exploit is now publicly available.

If you run AlmaLinux on a multi-tenant host, container build farm, CI runner, or any system where untrusted users can get a shell, this one matters — and with public exploit code in the wild, it matters today.

More information about the vulnerability:

- Public disclosure on oss-security: <https://www.openwall.com/lists/oss-security/2026/05/07/8>
- Researcher write-up: <https://dirtyfrag.io>
- Upstream fix for ESP: <https://git.kernel.org/pub/scm/linux/kernel/git/netdev/net.git/commit/?id=f4c50a4034e62ab75f1d5cdd191dd5f9c77fdff4>
- rxrpc fix on the netdev list: <https://lore.kernel.org/all/afKV2zGR6rrelPC7@v4bel/>

## Patching ahead of our upstream

Security is a top priority at AlmaLinux, and the severity of this flaw — combined with how trivial it is to exploit — meant we did not want to wait. Patches are not yet available from Red Hat, so our core team has built patched kernels using the upstream ESP fix (mainline commit [`f4c50a4034e6`](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=f4c50a4034e6)) backported and adapted to each supported AlmaLinux branch. The decision to ship these ahead of a CentOS Stream / RHEL update was made by our technical steering committee, [ALESCo](https://almalinux.org/blog/2024-05-21-introducing-alesco/).

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

The patched kernel versions are listed below. Use either of these commands:

```bash
uname -r
rpm -q kernel
```

We don't recommend keeping the testing repo enabled after you've updated, unless you've done this on a truly non-production environment. If this is a production environment, you can disable the repo with this command:

```bash
sudo dnf config-manager --disable almalinux-testing
```

If you encounter problems, please let us know as soon as you can, either in [AlmaLinux chat](https://chat.almalinux.org), on [bugs.almalinux.org](https://bugs.almalinux.org).

### A note for AlmaLinux Kitten 10 users

AlmaLinux Kitten 10 is itself a development release and does not have a separate testing repository. The patched kernel is shipping directly to Kitten's regular repository, so there is nothing extra to enable — just update and reboot:

```bash
sudo dnf update 'kernel*'
sudo reboot
```

Confirm with `uname -r` against the Kitten version listed below.

## Patched kernel versions

- AlmaLinux 8 is patched in `kernel-4.18.0-553.123.2.el8_10` and above
- AlmaLinux 9 is patched in `kernel-5.14.0-611.54.3.el9_7` and above
- AlmaLinux 10 is patched in `kernel-6.12.0-124.55.2.el10_1` and above
- AlmaLinux Kitten 10 will be patched in the next regular kernel build; see the Kitten repo for the current version

## Temporary mitigation if you cannot reboot yet

If updating and rebooting right now is not an option, you can neutralize the attack surface by blacklisting the affected modules. None of `esp4`, `esp6`, or `rxrpc` are loaded on a typical workload that does not use IPsec transport mode or AFS, so on most systems this is safe to apply immediately:

```bash
sudo sh -c "printf 'install esp4 /bin/false\ninstall esp6 /bin/false\ninstall rxrpc /bin/false\n' > /etc/modprobe.d/dirtyfrag.conf; rmmod esp4 esp6 rxrpc 2>/dev/null; true"
```

This writes a `modprobe` config that prevents the three modules from loading, and unloads them if they happen to be loaded already (the `rmmod` is best-effort and silent if the module isn't present). The command is safe to run unchanged on all supported releases. To revert, remove `/etc/modprobe.d/dirtyfrag.conf`.

The Dirty Frag exploit works by corrupting page-cache pages of sensitive files (such as `/etc/passwd` or `/usr/bin/su`). If you suspect the system may have already been targeted before you applied the mitigation, drop the page cache so any tampered pages are evicted and the next read comes fresh from disk:

```bash
sudo sh -c 'echo 3 > /proc/sys/vm/drop_caches'
```

This is safe to run on a live system — it only frees clean cache and dentry/inode entries — and pairs well with the blacklist above.

A note on `rxrpc.ko`: on AlmaLinux it ships only as part of the `kernel-modules-partner` subpackage, which is published exclusively in the AlmaLinux **Devel** repository. `kernel-modules-partner` is not enabled by default and **should not be installed on any production system** — it carries unsupported partner-only modules and exposes additional code paths (including `rxrpc`, the second half of Dirty Frag) that are absent on a standard install. If you have it installed, the simplest mitigation is to remove it entirely:

```bash
sudo dnf remove kernel-modules-partner
```

**Do not rely on this if you actually use IPsec ESP or AFS/rxrpc** — those workloads will break. The proper fix is to install the patched kernel and reboot.

## Thanks

Thanks to **Hyunwoo Kim** for finding, responsibly disclosing, and writing up this vulnerability, and to **Steffen Klassert** for shepherding the upstream fix through the netdev tree.

Thanks to the AlmaLinux core team for turning around patched builds for every supported release within a day of the upstream fix landing, and to ALESCo for moving quickly to approve shipping ahead of upstream. And thank you in advance to everyone in the community who helps us test these kernels — that's the part that gets them safely into production.

## Stay informed

Remaining aware of these vulnerabilities and acting quickly can keep your system and data safe. Follow the AlmaLinux Blog, join the [Mattermost Community Chat](https://chat.almalinux.org/), and subscribe to [Announce](https://lists.almalinux.org/mailman3/lists/announce.lists.almalinux.org/) and [Security Mailing List](https://lists.almalinux.org/mailman3/lists/security.lists.almalinux.org/) to stay informed and updated. We will update this post when the patched kernels move from testing to production.
