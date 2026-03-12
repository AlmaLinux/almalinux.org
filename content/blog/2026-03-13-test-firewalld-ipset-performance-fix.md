---
title: "Call for testing - firewalld ipset performance fix for AlmaLinux 8"
type: blog
author:
  name: "Andrew Lukoshko"
  bio: "AlmaLinux Lead Architect"
  image: /users/alukoshko.jpg
date: 2026-03-13
images:
  - /blog-images/2026/2026-03-13-firewalld-ipset-fix.png
post:
  title: "We've fixed a long-standing firewalld performance issue that caused ipset reloads with nftables to take minutes instead of seconds. The fix is already merged upstream. Help us test the patched package for AlmaLinux 8!"
  image: /blog-images/2026/2026-03-13-firewalld-ipset-fix.png
---

For years, firewalld users across multiple Linux distributions have been hitting a painful performance issue: reloading the firewall with large ipsets (10,000+ entries) and the nftables backend takes minutes instead of seconds, often causing network disruption. The problem has been [reported upstream](https://github.com/firewalld/firewalld/issues/933) as well as in [Debian](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=1006544), [Red Hat Bugzilla](https://bugzilla.redhat.com/show_bug.cgi?id=1908127), and by [our community](https://github.com/AlmaLinux/almalinux-deploy/issues/186). We've investigated the root cause, developed a fix, and submitted it upstream where it has already been [merged](https://github.com/firewalld/firewalld/pull/1544). Now we need your help testing the patched package for AlmaLinux 8 before releasing it to production.

## The problem

Users running firewalld with the nftables backend and large ipsets (e.g. blocklists with 10,000+ entries) experience `firewall-cmd --reload` taking anywhere from 80 seconds to over 15 minutes — depending on set size and hardware. During this time, network connectivity is often disrupted. Switching to the iptables backend works around the issue, but that's not a real solution.

The problem is most severe on systems running older nftables/kernel combinations (such as nftables 1.0.4 / kernel 4.18 in EL 8), but has been reported across distributions including Debian, RHEL and AlmaLinux. Newer systems (EL 9, EL10) are significantly less affected but still benefit from the fix.

## Root cause

We instrumented firewalld's nftables backend and identified two compounding issues:

1. **firewalld 0.9.x adds each ipset entry to 3 nftables families** (`inet`, `ip`, `ip6`) instead of 1, resulting in 36,000 nft operations for a 12k ipset.
2. **nftables 1.0.4 / kernel 4.18 has O(n) per-element insertion cost for interval sets**, so each successive chunk takes progressively longer as the set grows — classic O(n²) behavior.

The fix batches all element fragments into a single `"add element"` operation per chunk of 1000 elements (instead of one operation per entry), letting nftables handle bulk insertion natively.

## Benchmark

Using a 12,000-entry ipset with the nftables backend and `firewall-cmd --reload`:

| System | Before | After |
|---|---:|---:|
| EL 8 (nftables 1.0.4, kernel 4.18) | ~82,600 ms | ~2,600 ms |
| EL 9 (nftables 1.0.9, kernel 5.14) | ~1,560 ms | ~1,240 ms |


On EL 8 that's a **~32x improvement** — from over a minute down to under 3 seconds.

## Upstream

We submitted the fix upstream and it has already been merged: [firewalld/firewalld#1544](https://github.com/firewalld/firewalld/pull/1544), closing the long-standing upstream [issue #933](https://github.com/firewalld/firewalld/issues/933). The firewalld maintainer also pushed the fix to the `stable-0.9` branch for easier backporting to older distributions.

## How to test

We encourage anyone using large ipsets with firewalld on AlmaLinux 8 to test the patched package.

**Install the testing repo**

```bash
sudo dnf install -y almalinux-release-testing
```

**Update firewalld**

```bash
sudo dnf update firewalld firewalld-filesystem python3-firewall
```

**Confirm you have the patched version**

```bash
rpm -q firewalld
```

You should see `firewalld-0.9.11-10.el8_10.alma.1` or higher.

**Restart firewalld and verify**

```bash
sudo systemctl restart firewalld
time firewall-cmd --reload
```

_**Note**: We don't recommend that you keep the testing repo enabled after you've updated the packages, unless you've done this on a truly non-production environment. If this is a production environment, you can disable the repo with this command:_

```bash
sudo dnf config-manager --disable almalinux-testing
```

## Share your results!

If you encounter problems or want to share your testing results, please let us know as soon as you can, either in the [Development](https://chat.almalinux.org/almalinux/channels/development) channel on our Mattermost chat, on [bugs.almalinux.org](https://bugs.almalinux.org), or by emailing [packager@almalinux.org](mailto:packager@almalinux.org). It's just as important to report if everything works fine as it is to report bugs, so let us know either way!
