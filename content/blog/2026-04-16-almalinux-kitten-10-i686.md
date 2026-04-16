---
title: "AlmaLinux OS Kitten 10 expands community support with i686 userspace"
type: blog
author:
  name: "Eduard Abdullin"
  bio: "AlmaLinux Release Engineering"
  image: /users/eduard-abdullin.jpg
date: 2026-04-16
images:
  - /blog-images/2026/2026-04-15-almalinux-kitten-10-i686.png
post:
  title: "AlmaLinux OS Kitten 10 now offers 32-bit x86 (i686) userspace to support its vendor community"
  image: /blog-images/2026/2026-04-15-almalinux-kitten-10-i686.png
---

We have added **i686** support to **AlmaLinux OS Kitten 10** — package repositories and official container images for 32-bit x86. There is no installer ISO for i686; this is only about userspace. If you have used i686 packages on AlmaLinux 8 or 9, the setup is the same.

## Why ship i686

32-bit x86 has not gone away. Software that only ships as i686, CI pipelines that need a specific 32-bit glibc, containers that should look like a normal distro but for `linux/386` — all of these still exist and still need a maintained package set behind them.

Vendors care about this too. **Arista** moved **[EOS](https://www.arista.com/en/support/toi/eos-4-32-0f)** from **CentOS 7** to **AlmaLinux 9**, and their tooling relies on i686 packages being available alongside x86_64.

## What this means for you

For the every day user, this doesn't impact your use of AlmaLinux. As our vendor relationships are continuing to expand and deepen, more things like this will arrive that will only improve the ecosystem as a whole.

## Repositories

Packages live on the Kitten vault: [kitten.vault.almalinux.org](https://kitten.vault.almalinux.org/). Look under `10-kitten/BaseOS/i686/os/` and the companion repos for that release.

## Docker

Official container image, 32-bit x86:

```bash
docker run -it --rm --platform linux/386 almalinux:10-kitten bash
```

## What's next

Kitten is where new things land first. We plan to bring the same i686 model — repos and container images — to **AlmaLinux OS 10 stable**. AlmaLinux 10 is supported through **2035**, and we intend to keep i686 userspace maintained for the full lifecycle alongside the other architectures.

## Get involved

If you use i686 and something is broken, let us know. Report issues on [bugs.almalinux.org](https://bugs.almalinux.org/), talk to us in [SIG/AltArch](https://chat.almalinux.org/almalinux/channels/sigaltarch) on Mattermost, or post on the [forums](https://almalinux.discourse.group/).

Follow us on [Reddit](https://www.reddit.com/r/AlmaLinux/), [X](https://twitter.com/AlmaLinux), [Mastodon](https://fosstodon.org/@almalinux/), [LinkedIn](https://www.linkedin.com/company/80320905/), and [YouTube](https://www.youtube.com/channel/UCt9lpkqUPp1FUEi9uqVlPQA).
