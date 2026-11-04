{{- $date := now | dateFormat "2006-01-02" -}}
---
title: "NAME (CVE-YYYY-NNNNN): Patched PACKAGE available in testing"
type: blog
author:
  name: "Your Name"
  bio: "Your Title or Role"
  image: /users/username.jpg
date: {{ $date }}
post:
  title: "A one- or two-sentence summary for the blog listing page: what the flaw lets an attacker do, which AlmaLinux releases are affected, and where the fix is."
header:
  template: vulnerability
  title: "NAME: patched"
  subtitle: "CVE-YYYY-NNNNN"
---

Opening paragraph: name the vulnerability and link its CVE record (https://www.cve.org/CVERecord?id=CVE-YYYY-NNNNN), say in one or two plain sentences what an attacker can do with it, give the severity ratings from the sources that have published one, say which AlmaLinux releases are affected, and say where patched packages are available.

If one group of users is most at risk (for example, virtualization hosts or shared hosting), add a short paragraph telling them so.

More information about the vulnerability:

- CVE record: <https://www.cve.org/CVERecord?id=CVE-YYYY-NNNNN>
- Red Hat CVE page: <https://access.redhat.com/security/cve/CVE-YYYY-NNNNN>
- Add the researcher's write-up, the upstream announcement, and the upstream fix commit, if they exist.

## Summary

How the bug works, in plain language for a reader who isn't a specialist in this part of the stack. Say where the flaw lives, what goes wrong, and what the researcher showed it can do. Say how long the vulnerable code has been around if that's known. Credit who found it, who wrote the fix, and when it landed upstream.

## Impact

Which AlmaLinux releases ship the vulnerable code, which systems are most at risk, and whether we recommend updating every system or only some. Say whether a workaround exists. If one does, add a "Mitigations until you can update" section after this one with the exact commands and how to undo them.

## Patching ahead of our upstream

Use this section when we ship a fix before CentOS Stream or RHEL does. Otherwise, delete it.

Security is a top priority at AlmaLinux. At the time of writing, [Red Hat lists RHEL VERSIONS as affected with no fix released yet](https://access.redhat.com/security/cve/CVE-YYYY-NNNNN). Our core team has backported the upstream fix to every affected AlmaLinux release. The decision to ship ahead of a CentOS Stream / RHEL update was made by our technical steering committee, [ALESCo](https://almalinux.org/blog/2024-05-21-introducing-alesco/).

## Patched versions

- AlmaLinux 8 is patched in `PACKAGE-VERSION.el8_N` and above
- AlmaLinux 9 is patched in `PACKAGE-VERSION.el9_N` and above
- AlmaLinux 10 is patched in `PACKAGE-VERSION.el10_N` and above
- AlmaLinux Kitten 10: give the version, or say the fix will arrive in the next regular update

## Help us test

Patched packages are in the testing repository so the community can verify them before they go to production. Replace `PACKAGE` below with the package name (for the kernel, use `'kernel*'`).

**Install the testing repo**

```bash
sudo dnf install -y almalinux-release-testing
```

**Update the package**

```bash
sudo dnf update PACKAGE --enablerepo=almalinux-testing
```

**Restart what uses it**

For a kernel update, reboot. On a virtualization host, migrate or shut down your guests first. For other packages, restart the services that use the package.

```bash
sudo reboot
```

**Confirm you are running a patched version**

Compare the output against the versions listed above (for the kernel, use `uname -r`).

```bash
rpm -q PACKAGE
```

We don't recommend keeping the testing repo enabled after you've updated, unless you've done this on a truly non-production environment. If this is a production environment, you can disable the repo with this command:

```bash
sudo dnf config-manager --disable almalinux-testing
```

If you encounter problems, please let us know as soon as you can, either in [AlmaLinux chat](https://chat.almalinux.org) or on [bugs.almalinux.org](https://bugs.almalinux.org).

## Thanks

Thank the people who found, reported, and fixed the vulnerability upstream, by name. Then thank the AlmaLinux core team for the patched builds, ALESCo if it approved shipping ahead of upstream, and the community members who help test.

## Stay informed

Remaining aware of these vulnerabilities and acting quickly can keep your systems and data safe. Follow the AlmaLinux Blog, join the [Mattermost Community Chat](https://chat.almalinux.org/), and subscribe to the [Announce](https://lists.almalinux.org/mailman3/lists/announce.lists.almalinux.org/) and [Security](https://lists.almalinux.org/mailman3/lists/security.lists.almalinux.org/) mailing lists to stay informed.

## Changelog

- **{{ $date }} HH:MM UTC:** Initial post published. Patched PACKAGE available in `almalinux-testing` for AlmaLinux 8, 9, and 10.
