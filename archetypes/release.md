{{- $year := now | dateFormat "2006" -}}
{{- $date := now | dateFormat "2006-01-02" -}}
---
title: "AlmaLinux OS X.Y and A.B are now available"
type: blog
author:
  name: "Your Name"
  bio: "Your Title or Role"
  image: /users/username.jpg
date: {{ $date }}
description: "AlmaLinux OS X.Y \"Codename\" and A.B \"Codename\" are available now, with HEADLINE CHANGE 1 and HEADLINE CHANGE 2. Keep this under about 155 characters."
images:
  - /blog-images/{{ $year }}/image-name.png
post:
  title: "A one- or two-sentence summary for the blog listing page. Lead with the versions and codenames, then the changes people care about most."
  image: /blog-images/{{ $year }}/image-name.png
---

Hello Community! The AlmaLinux OS Foundation is announcing the general availability of [AlmaLinux OS X.Y](https://mirrors.almalinux.org/isos.html) codenamed "Codename" and [AlmaLinux OS A.B](https://mirrors.almalinux.org/isos.html) codenamed "Codename"!

Thank you to everyone who tested the [X.Y beta](/blog/YYYY-MM-DD-announcing-xy-beta) and [A.B beta](/blog/YYYY-MM-DD-announcing-ab-beta).

## Release highlights

AlmaLinux OS X.Y "Codename":

- Released: Month DD, YYYY
- Kernel: `X.Y.Z-NNN.N.N.elX_Y`
- Compatible with: Red Hat Enterprise Linux (RHEL) X.Y
- Architectures: x86_64, x86_64_v2, aarch64, ppc64le, s390x, and i686 userspace
- What's new: 3 to 5 headline changes, copied from the release notes

AlmaLinux OS A.B "Codename":

- Released: Month DD, YYYY
- Kernel: `X.Y.Z-NNN.N.N.elA_B`
- Compatible with: Red Hat Enterprise Linux (RHEL) A.B
- Architectures: x86_64, aarch64, ppc64le, s390x, and i686 userspace
- What's new: 3 to 5 headline changes, copied from the release notes

## AlmaLinux OS X.Y "Codename" {#X-Y}

Start with one sentence that stands on its own: the version, its kernel, and what's new. Then the details, in their own sections.

Installation ISOs are available on the mirrors now for all supported architectures:

- [Intel/AMD (x86_64)](https://mirrors.almalinux.org/isos/x86_64/X.Y.html)
- [Intel/AMD (x86_64_v2)](https://mirrors.almalinux.org/isos/x86_64_v2/X.Y.html)
- [ARM64 (aarch64)](https://mirrors.almalinux.org/isos/aarch64/X.Y.html)
- [IBM PowerPC (ppc64le)](https://mirrors.almalinux.org/isos/ppc64le/X.Y.html)
- [IBM Z (s390x)](https://mirrors.almalinux.org/isos/s390x/X.Y.html)

You can read the full release notes on the wiki: [AlmaLinux OS X.Y Release Notes](https://wiki.almalinux.org/release-notes/X.Y.html).

## AlmaLinux OS A.B "Codename" {#A-B}

Start with one sentence that stands on its own: the version, its kernel, and what's new.

Installation ISOs are available on the mirrors now for all supported architectures:

- [Intel/AMD (x86_64)](https://mirrors.almalinux.org/isos/x86_64/A.B.html)
- [ARM64 (aarch64)](https://mirrors.almalinux.org/isos/aarch64/A.B.html)
- [IBM PowerPC (ppc64le)](https://mirrors.almalinux.org/isos/ppc64le/A.B.html)
- [IBM Z (s390x)](https://mirrors.almalinux.org/isos/s390x/A.B.html)

You can read the full release notes on the wiki: [AlmaLinux OS A.B Release Notes](https://wiki.almalinux.org/release-notes/A.B.html).

## Changes to check before you upgrade

Anything that behaves differently after the upgrade, one short paragraph each.

## Cloud, container, and live images

List the images and where to find them. Copy this list from the previous release post and update it.

## Security fixes included

CVEs covered on the blog since the betas, and any kernel fixes AlmaLinux carries that upstream doesn't.

## Tell us how it goes

Please install it, upgrade a test machine, and tell us what you find. Report bugs on the [Bug Tracker](https://bugs.almalinux.org/), talk to us in [AlmaLinux Community Chat](https://chat.almalinux.org), or post on the [Forums](https://forums.almalinux.org/). You can also find us on [Reddit](https://reddit.com/r/almalinux) and [X](https://x.com/almalinux).
