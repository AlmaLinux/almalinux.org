---
title: "IPV6_FRAG_ESCAPE vulnerability: Fixed!"
type: blog
author:
  name: "Andrew Lukoshko"
  bio: "AlmaLinux Lead Architect"
  image: /users/alukoshko.jpg
date: "2026-06-30"
images:
  - /blog-images/2026/2026-06-30-ipv6-frag-escape.png
post:
  title: "A newly disclosed Linux kernel flaw in the IPv6 fragmentation path lets an unprivileged user inside a container escape to root on the host. It only affects AlmaLinux 10 and Kitten 10, and there is no CVE yet. A patched kernel for AlmaLinux 10 is in the testing repository now (Kitten's fix is coming in the next update). If you run containers or any multi-tenant workload, help us verify it."
  image: /blog-images/2026/2026-06-30-ipv6-frag-escape.png
---

## Update: The fix is now in production

**The patched AlmaLinux 10 kernel has been released to the production repositories.** You no longer need to enable the testing repo to get it. Just run:

```bash
sudo dnf clean metadata && sudo dnf upgrade
sudo reboot
```

The fixed version released to the public is **`kernel-6.12.0-211.29.1.el10_2`** (or higher). Confirm you are running it with `uname -r` after rebooting. Most mirrors sync every few hours, so if the update is not available to you yet, try again a little later.

The testing-repo instructions further down in this post remain for reference but are no longer the recommended path. Thanks to everyone who helped verify the patch — community testing got it into production faster than we could have managed alone.

---

A new Linux kernel local-privilege-escalation flaw has been disclosed in the IPv6 fragmentation code, and it is serious: an **unprivileged user inside a container can use it to escape to a root shell on the host**. There is no CVE assigned yet, so for now we are referring to it as **`IPV6_FRAG_ESCAPE`**, the name its proof-of-concept uses. Only **AlmaLinux 10 and AlmaLinux Kitten 10** are affected. A patched kernel for AlmaLinux 10 is available in the testing repository today, and we would like your help verifying it before we push it to production.

The flaw was discovered by security researcher **Massimiliano Oldani** during Google's kCTF program, and a deliberately-incomplete proof-of-concept has been [published on GitHub by sgkdev](https://github.com/sgkdev/ipv6_frag_escape). Because the upstream fix reached mainline without a coordinated CVE assignment or a stable backport, the public patch effectively serves as a roadmap for a 0-day. With exploit code already in the open, this one matters today.

## What the bug is

The bug is an arithmetic error in `__ip6_append_data()`, the function that assembles outgoing IPv6 packets. When a fragmented IPv6 datagram is built through a UDP socket using `MSG_SPLICE_PAGES`, the kernel undersizes its allocation and writes past `skb->end` into the trailing `skb_shared_info`, corrupting the `nr_frags` field. From there the public exploit chains that overflow into a page use-after-free, arbitrary kernel read/write, and finally a root shell in the host's initial namespaces — turning an unprivileged user inside a container into root on the host.

**Why only AlmaLinux 10 and Kitten 10?** The vulnerable code path lives in the 6.12 kernel. AlmaLinux 8 (kernel 4.18) and AlmaLinux 9 (kernel 5.14) do not contain it and are **not affected**. The same upstream code is what makes CentOS Stream 10 and RHEL 10 vulnerable as well.

More information about the vulnerability:

- Proof-of-concept and write-up: <https://github.com/sgkdev/ipv6_frag_escape>
- Researcher write-up (Massimiliano Oldani): <https://www.linkedin.com/pulse/ipv6fragescape-unprivileged-container-jail-escape-poc-oldani-xbewf>
- Upstream fix: commit `736b380e28d0` — "ipv6: account for fraggap on the paged allocation path" (landed in v7.2-rc1)

## Patching ahead of our upstream

Security is a top priority at AlmaLinux. The combination of how trivially this escalates to host root, the fact that working exploit code is already public, and the absence of any CVE or coordinated upstream fix for the RHEL/CentOS Stream kernel meant we did not want to wait. Our core team has backported and adapted the upstream `__ip6_append_data()` fix to the AlmaLinux 10 kernel. The decision to ship ahead of a CentOS Stream / RHEL update was made by our technical steering committee, [ALESCo](https://almalinux.org/blog/2024-05-21-introducing-alesco/).

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

You should see `kernel-6.12.0-211.28.2.el10_2` or higher.

We don't recommend keeping the testing repo enabled after you've updated, unless you've done this on a truly non-production environment. If this is a production environment, you can disable the repo with this command:

```bash
sudo dnf config-manager --disable almalinux-testing
```

If you encounter problems, please let us know as soon as you can, either in [AlmaLinux chat](https://chat.almalinux.org) or on [bugs.almalinux.org](https://bugs.almalinux.org).

### A note for AlmaLinux Kitten 10 users

AlmaLinux Kitten 10 is affected, but **a patched kernel is not available for Kitten yet**. The fix will arrive in the next Kitten kernel update. Until it ships, Kitten users should apply the temporary mitigation below. We will update this post once the patched Kitten kernel is available.

## Affected versions and patched kernels

Only the AlmaLinux 10 family is affected:

- **AlmaLinux 10** is fixed in `kernel-6.12.0-211.29.1.el10_2` and above, now available in the **production** repositories. (The earlier `kernel-6.12.0-211.28.2.el10_2` build was the testing-repo candidate; the production build supersedes it.)
- **AlmaLinux Kitten 10** is affected; a patched kernel is **not available yet** and will land in the next Kitten kernel update. Apply the temporary mitigation below in the meantime.

**AlmaLinux 8 and AlmaLinux 9 are not affected** and require no action.

## Temporary mitigation if you cannot reboot yet

The public exploit relies on an **unprivileged user namespace** to obtain the network capabilities it needs to craft the malicious IPv6 packets from inside a container. On systems that do not legitimately need unprivileged user namespaces, you can sharply reduce the attack surface by disabling them:

```bash
sudo sysctl -w user.max_user_namespaces=0
```

To make it persistent across reboots:

```bash
echo 'user.max_user_namespaces = 0' | sudo tee /etc/sysctl.d/99-ipv6-frag-escape.conf
```

**Be aware of the trade-off:** rootless containers (rootless Podman, unprivileged LXC, some sandboxing in browsers and CI runners) depend on unprivileged user namespaces and will stop working while this is set. If those workloads matter to you, do **not** apply this mitigation — install the patched kernel and reboot instead. To revert, remove `/etc/sysctl.d/99-ipv6-frag-escape.conf` and set the value back with `sudo sysctl -w user.max_user_namespaces=<previous value>` (the default is a large positive number).

The proper fix is the patched kernel. The mitigation is only a stop-gap for hosts that cannot reboot immediately.

## Thanks

Thanks to **Massimiliano Oldani** for finding and writing up this vulnerability, and to **sgkdev** for the public proof-of-concept and analysis that made it possible to understand and verify the fix.

Thanks as well to the AlmaLinux core team for turning around a patched kernel quickly, and to ALESCo for moving to approve shipping ahead of upstream. And thank you in advance to everyone in the community who helps us test these kernels — that's the part that gets them safely into production.

## Stay informed

Remaining aware of these vulnerabilities and acting quickly can keep your system and data safe. Follow the AlmaLinux Blog, join the [Mattermost Community Chat](https://chat.almalinux.org/), and subscribe to the [Announce](https://lists.almalinux.org/mailman3/lists/announce.lists.almalinux.org/) and [Security](https://lists.almalinux.org/mailman3/lists/security.lists.almalinux.org/) mailing lists to stay informed. We will update this post when the patched kernels move from testing to production.
