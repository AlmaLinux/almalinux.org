---
title: "CIFSwitch (CVE-2026-46243) Patches Released"
type: blog
author:
  name: "Andrew Lukoshko"
  bio: "AlmaLinux Lead Architect"
  image: /users/alukoshko.jpg
date: "2026-05-28"
images:
  - /blog-images/2026/2026-05-28-cifswitch.png
post:
  title: "A local-root flaw, dubbed CIFSwitch and now tracked as CVE-2026-46243, lets an unprivileged user become root through the cifs.spnego request-key helper on any system with cifs-utils installed and unprivileged user namespaces enabled. The patched kernels have now been released to the production repositories — update and reboot."
  image: /blog-images/2026/2026-05-28-cifswitch.png
---

> **Update: CVE assigned and patched kernels are now in production**
>
> **2026-06-02 15:31 UTC:** The vulnerability has been assigned **CVE-2026-46243**, and the patched kernels have been released to the **production** repositories/mirrors. You no longer need to enable the testing repo to get them. Just run:
>
> ```bash
> sudo dnf clean metadata && sudo dnf upgrade
> sudo reboot
> ```
>
> Thanks to everyone in the community who helped verify these builds. The kernels released to production are bit for bit identical to those that were in testing. The rest of this post is preserved as originally published.

A new Linux local-root vulnerability, nicknamed **CIFSwitch** by its discoverer Asim Manizada, was [disclosed today on oss-security](https://www.openwall.com/lists/oss-security/2026/05/28/2) after the linux-distros embargo expired. A CVE has been requested but is not yet assigned at the time of writing. The flaw chains a userspace `request-key` helper from `cifs-utils` with a missing input check in the kernel's CIFS client. Any unprivileged user on a system that has `cifs-utils` installed, the CIFS kernel module loadable, and unprivileged user namespaces enabled (the default on every supported AlmaLinux release) can pivot to root.

If you run AlmaLinux on a multi-tenant host, a container build farm, a CI runner, or anywhere a user with shell access might want more than they should have, this matters today.

More information about the vulnerability:

- Discoverer write-up: <https://heyitsas.im/posts/cifswitch>
- Proof of concept: <https://github.com/manizada/CIFSwitch>
- Disclosure on oss-security: <https://www.openwall.com/lists/oss-security/2026/05/28/2>
- Upstream kernel fix: `smb: client: reject userspace cifs.spnego descriptions` (commit [`3da1fdf4efbc`](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=3da1fdf4efbc))

## The bug, briefly

When the kernel's CIFS client needs a Kerberos/SPNEGO ticket to authenticate a mount, it asks userspace for one via the `request-key` mechanism, calling out to `/usr/sbin/cifs.spnego` (from `cifs-utils`). The "description" string passed to that helper is supposed to be constructed by the kernel and is meant to describe a target server, UID, credential type, and so on.

The flaw is that an unprivileged user could also request a key with a `cifs.spnego` type and supply their own forged description. The kernel client did not reject userspace-originated descriptions, so the attacker controlled what `cifs.spnego` saw. By placing the call inside a freshly crafted user/mount namespace, the attacker controls the NSS lookups that `cifs.spnego` performs while it is still running with the caller's privileges, then leverages the resulting state transitions back in the parent namespace to execute code as root.

The upstream fix is small: the kernel now rejects `cifs.spnego` descriptions that did not originate from the kernel itself, which closes the entire attack class without needing matching changes in `cifs-utils`.

## Affected releases

The underlying logic is present in the CIFS client on every supported AlmaLinux release, and `cifs-utils` is in the default repositories on all of them. **AlmaLinux 8, 9, 10, and Kitten 10 are all affected** if `cifs-utils` is installed.

**Good news for most installs:** `cifs-utils` is **not** part of the AlmaLinux default installation on any supported release. If nothing on the system has explicitly pulled it in (directly or as a dependency of a tool that mounts SMB/CIFS shares), the exploit cannot run. Check with `rpm -q cifs-utils`. A `package cifs-utils is not installed` response means you are not exposed via the public PoC — though we still recommend installing the patched kernel to close the underlying bug.

**A note on AlmaLinux 10 and SELinux:** the public CIFSwitch exploit is **blocked by SELinux in enforcing mode** on AlmaLinux 10 and Kitten 10. The default policy denies the namespace and NSS-lookup transitions the exploit relies on, so an unprivileged user cannot turn the bug into root on a stock AlmaLinux 10 system. This is defense in depth, not a fix — the underlying kernel flaw is still present, the kernel still accepts attacker-controlled `cifs.spnego` descriptions, and any future variant of the exploit that takes a different code path could bypass the current SELinux denials. Install the patched kernel anyway. If you have SELinux disabled or set to permissive on AlmaLinux 10, treat the system as fully exploitable.

## Patched kernel versions

These kernels are available **in the testing repository** today. Once the community has helped verify them, they will be released to the production repositories. This post will be updated when that happens.

- AlmaLinux 8: `kernel-4.18.0-553.126.2.el8_10`
- AlmaLinux 9: `kernel-5.14.0-687.5.4.el9_8`
- AlmaLinux 10: `kernel-6.12.0-211.7.4.el10_2`
- AlmaLinux Kitten 10: the fix will ride along in the next regular kernel update; no separate emergency build is being cut

## Help us test

```bash
sudo dnf install -y almalinux-release-testing
sudo dnf update 'kernel*' --enablerepo=almalinux-testing
sudo reboot
```

Confirm with `uname -r` or `rpm -q kernel` against the versions above.

If you do not want the testing repo enabled afterwards (and on a production box you almost certainly do not), disable it once you have rebooted:

```bash
sudo dnf config-manager --disable almalinux-testing
```

If you run into anything, please let us know in [AlmaLinux chat](https://chat.almalinux.org) or on [bugs.almalinux.org](https://bugs.almalinux.org).

## Temporary mitigations if you cannot reboot yet

Any one of the following blocks every public CIFSwitch exploit we are aware of. **Only apply these on systems that do not mount SMB/CIFS shares** — each of them breaks CIFS mounting in some way, and the third one specifically breaks Kerberos/SPNEGO authentication for CIFS mounts. If you actively use CIFS, the right answer is to install the patched kernel and reboot.

**Option 1 — remove `cifs-utils` entirely.** The exploit needs the `cifs.spnego` userspace helper to be present. If nothing on the box mounts CIFS, removing the package is the cleanest mitigation:

```bash
sudo dnf remove cifs-utils
```

**Option 2 — prevent the CIFS kernel module from loading.**

```bash
sudo sh -c "printf 'install cifs /bin/false\n' > /etc/modprobe.d/cifswitch.conf; rmmod cifs 2>/dev/null; true"
```

This writes a `modprobe` config that prevents the module from loading and unloads it if it happens to already be loaded (the `rmmod` is best-effort and silent if the module isn't present). To revert, remove `/etc/modprobe.d/cifswitch.conf`.

**Option 3 — neutralize the `cifs.spnego` request-key handler.** Point it at `/bin/false` so any attempt to invoke it (including the exploit path) fails immediately:

```bash
sudo sh -c 'echo "create cifs.spnego * * /bin/false" > /etc/request-key.d/cifs.spnego.conf'
```

This leaves the kernel module and `cifs-utils` in place but breaks Kerberos/SPNEGO authentication for any CIFS mounts. To revert, remove `/etc/request-key.d/cifs.spnego.conf`.

These are workarounds, not fixes. Install the patched kernel and reboot when you can.

## Thanks

Thanks to **Asim Manizada** for finding, writing up, and responsibly disclosing this vulnerability through the linux-distros coordination process, and to the upstream kernel maintainers for landing the fix promptly.

Thanks again to the AlmaLinux core team for turning around patched builds for every supported release on disclosure day. And thank you in advance to everyone in the community who helps us test these kernels — that's the part that gets them safely into production.

## Stay informed

Remaining aware of these vulnerabilities and acting quickly can keep your system and data safe. Follow the AlmaLinux Blog, join the [Mattermost Community Chat](https://chat.almalinux.org/), and subscribe to [Announce](https://lists.almalinux.org/mailman3/lists/announce.lists.almalinux.org/) and [Security](https://lists.almalinux.org/mailman3/lists/security.lists.almalinux.org/) mailing lists to stay informed and updated. We will update this post when the patched kernels move from testing to production.
