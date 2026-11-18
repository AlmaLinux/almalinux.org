---
title: "NGINX2Shell: Patched nginx packages released"
type: blog
author:
  name: "Jonathan Wright"
  bio: "Infrastructure SIG Lead & ALESCo Member"
  image: /users/jonathan.jpg
date: "2026-11-18T22:35:22Z"
post:
  title: "NGINX2Shell is a set of five critical nginx vulnerabilities that can let an unauthenticated attacker crash nginx, and potentially run code on the server. Patched nginx packages for AlmaLinux 8, 9, and 10 are now in the production repositories. Update now."
header:
  template: vulnerability
  title: "nginx patches: released"
  subtitle: "NGINX2Shell: five critical\nnginx vulnerabilities"
---

Five vulnerabilities in nginx, nicknamed **NGINX2Shell**, were [disclosed by nginx today](https://nginx.org/en/security_advisories.html): [CVE-2026-123633](https://www.cve.org/CVERecord?id=CVE-2026-123633), [CVE-2026-123007](https://www.cve.org/CVERecord?id=CVE-2026-123007), [CVE-2026-123634](https://www.cve.org/CVERecord?id=CVE-2026-123634), [CVE-2026-113425](https://www.cve.org/CVERecord?id=CVE-2026-113425), and [CVE-2026-121810](https://www.cve.org/CVERecord?id=CVE-2026-121810). Each one can let an unauthenticated attacker crash an nginx worker process, and potentially run code on the server as the `nginx` user. F5, which maintains nginx, rates all five **9.2 (Critical)** on CVSS v4.0 and 8.1 (High) on CVSS v3.1. **AlmaLinux 8, 9, and 10 all ship affected nginx versions.** The two most widely exposed flaws are in HTTP/2, so any nginx with HTTP/2 turned on is at risk.

Our Core SIG has backported the fixes and built patched packages for every nginx stream still in its RHEL life cycle, and for Kitten 10. Older, retired streams, including the AlmaLinux 8 default `nginx:1.14`, are not getting these patches (see [retired streams](#retired-streams)).

Given the severity, these patches went straight to the production repositories, without a stop in the testing repository first. The [patched versions](#patched-package-versions) are listed below. Until you can update, [turning off HTTP/2](#mitigations-until-you-can-update) closes the two HTTP/2 flaws.

More information about the vulnerabilities:

- nginx security advisories: <https://nginx.org/en/security_advisories.html>
- nginx 1.30.7 changes: <https://nginx.org/en/CHANGES-1.30>
- CVE-2026-123633 F5 advisory (use-after-free in HTTP/2): <https://my.f5.com/manage/s/article/K000163928>
- CVE-2026-123007 F5 advisory (memory corruption in HTTP/2 flow control): <https://my.f5.com/manage/s/article/K000163926>
- CVE-2026-123634 F5 advisory (use-after-free in the resolver): <https://my.f5.com/manage/s/article/K000163925>
- CVE-2026-113425 F5 advisory (use-after-free in the mail proxy): <https://my.f5.com/manage/s/article/K000163931>
- CVE-2026-121810 F5 advisory (use-after-free in HTTP/3): <https://my.f5.com/manage/s/article/K000163927>
- Red Hat CVE page for CVE-2026-123007: <https://access.redhat.com/security/cve/CVE-2026-123007>
- Wiz Research write-up on the HTTP/2 flaws: <https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities>

## Summary

NGINX2Shell is the nickname this set of vulnerabilities has picked up. nginx's advisories refer to them by CVE number. nginx shipped the fixes on 2026-11-18 in nginx 1.30.7 (stable) and 1.31.9 (mainline). All five are memory corruption bugs in nginx's worker processes. F5 says each one can crash a worker, and that code execution is possible on systems where Address Space Layout Randomization (ASLR), a standard memory protection, is disabled or bypassed.

### CVE-2026-123633: use-after-free in HTTP/2

Each nginx worker process can hold a limited number of connections, set by `worker_connections`. When a worker runs low on free connection slots, nginx makes room by closing idle connections that it has marked as reusable. An HTTP/2 connection could stay marked as reusable even after a request had started on it. If the worker then ran short of connection slots while handling that request, for example while connecting to a backend server, nginx could close the client connection and free its memory while the request was still using it (a use-after-free).

nginx rates it **medium**. The flaw affects nginx 1.19.7 and later.

### CVE-2026-123007: memory corruption in HTTP/2 flow control

HTTP/2 flow control limits how much data the server may send before the client asks for more. nginx tracks this allowance (the "window") for each connection, and the protocol caps it at a maximum size. When a request is cancelled, nginx gives the part of its allowance that was never sent back to the connection. That refund was not checked against the maximum, so a client could push the window past the limit. nginx's buffer size calculations then went wrong when sending data, corrupting memory.

nginx rates it **major**. Wiz Research reports that it achieved remote code execution through this flaw, including an ASLR bypass, against official nginx builds that were doing nothing more than serving static files over HTTPS. The flaw goes back to nginx 1.9.5, the first release with HTTP/2 support.

### CVE-2026-123634: use-after-free in the resolver

When nginx proxies to a server name that contains variables, it looks the name up while handling the request, using its built-in resolver. If a Server Side Includes (SSI) or `mirror` subrequest resolves the same name at the same time, a crafted request can make nginx use memory it has already freed.

nginx rates it **medium**. The flaw goes back to nginx 0.6.18, so it affects every nginx version AlmaLinux ships.

### CVE-2026-113425: use-after-free in the mail proxy

nginx can also work as a proxy for email (IMAP, POP3, and SMTP). Traffic that F5 has not described publicly can trigger a use-after-free in a worker process running the mail proxy.

nginx rates it **major**. The flaw goes back to nginx 0.5.33, so it affects every nginx version AlmaLinux ships.

### CVE-2026-121810: use-after-free in HTTP/3

This is a close relative of CVE-2026-123633, in nginx's HTTP/3 support. When a worker ran low on connection slots while opening a new HTTP/3 request stream, nginx could mark the client connection as idle and later close it while it was still in use. F5 notes that exploitation also depends on conditions outside the attacker's control.

nginx rates it **medium**. The flaw affects nginx 1.25.0 and later.

## Impact

AlmaLinux 8, 9, and 10 all ship nginx versions in the affected range. Each flaw can only be reached if nginx uses the feature it is in:

- **CVE-2026-123007 (HTTP/2):** every nginx version AlmaLinux ships, when HTTP/2 is turned on.
- **CVE-2026-123633 (HTTP/2):** nginx 1.19.7 and later, when HTTP/2 is turned on. That is everything AlmaLinux ships except the `nginx:1.14` (the AlmaLinux 8 default), `nginx:1.16`, and `nginx:1.18` streams on AlmaLinux 8.
- **CVE-2026-123634 (resolver):** every nginx version AlmaLinux ships, when it proxies to server names that contain variables and uses SSI or `mirror` subrequests.
- **CVE-2026-113425 (mail proxy):** every nginx version AlmaLinux ships, when it runs as a mail proxy. On AlmaLinux, that needs the optional `nginx-mod-mail` module.
- **CVE-2026-121810 (HTTP/3):** only the nginx 1.26 builds (the `nginx:1.26` stream on AlmaLinux 9, AlmaLinux 10, and Kitten 10), when HTTP/3 is turned on.

HTTP/2 is the feature most sites have turned on. The default `nginx.conf` on AlmaLinux 8, 9, and 10 does not turn it on: its only HTTP/2 example is in a commented-out HTTPS server block. Most sites that serve HTTPS do turn it on, though, so if your nginx serves HTTPS, check. This lists every place in your configuration that turns on HTTP/2:

```bash
sudo grep -RnE '^\s*(listen\s.*\bhttp2\b|http2\s+on)' /etc/nginx
```

If it prints nothing, HTTP/2 is off and neither HTTP/2 flaw can be reached. If it prints anything, that system is exposed. Whatever your configuration, we recommend updating every system that runs nginx.

Our packages only update nginx installed from AlmaLinux's own repositories. If you get nginx from somewhere else, such as nginx.org's own repository, a web hosting control panel, or a third-party repository, check with that vendor for their fixes and timeline.

## Patching ahead of our upstream

Security is a top priority at AlmaLinux. At the time of writing, Red Hat has not released fixed nginx packages. Our Core SIG has backported the upstream fixes first to every nginx stream that is still supported under the [RHEL Application Streams life cycle](https://access.redhat.com/support/policy/updates/rhel-app-streams-life-cycle):

- **AlmaLinux 8:** the `nginx:1.24` stream
- **AlmaLinux 9:** the default nginx 1.20, and the `nginx:1.24` and `nginx:1.26` streams
- **AlmaLinux 10:** the default nginx 1.26
- **AlmaLinux Kitten 10:** the default nginx 1.26

The decision to ship these ahead of a CentOS Stream / RHEL update was made by our technical steering committee, [ALESCo](https://almalinux.org/blog/2024-05-21-introducing-alesco/).

### Retired streams

On AlmaLinux 8, `nginx:1.14`, `nginx:1.16`, `nginx:1.18`, `nginx:1.20`, and `nginx:1.22`, and on AlmaLinux 9, `nginx:1.22`, have reached the end of their [RHEL life cycle](https://access.redhat.com/support/policy/updates/rhel-app-streams-life-cycle), so they are not getting these patches. If you are on one of them, the safest path is to move to a supported stream, and to [turn off HTTP/2](#mitigations-until-you-can-update) until you can.

`nginx:1.14` is still the default stream on AlmaLinux 8, so if you installed nginx there without choosing a stream, that is what you have. Check which stream is enabled (marked `[e]`) with:

```bash
dnf module list nginx
```

To move to a supported stream, for example `nginx:1.24`, after checking that your configuration works with that nginx version:

```bash
sudo dnf module reset nginx
sudo dnf module enable nginx:1.24
sudo dnf distro-sync 'nginx*'
sudo systemctl restart nginx
```

## Patched package versions

Install the version listed for your release and stream, or higher.

**AlmaLinux 8**

- `nginx:1.24` stream: `nginx-1.24.0-3.module_el8.10.0+4373+4291aaad.6.alma.4`

**AlmaLinux 9**

- Default (nginx 1.20): `nginx-1.20.1-32.el9_9.1.alma.4`
- `nginx:1.24` stream: `nginx-1.24.0-9.module_el9.9.0+356+d723c317.1.alma.4`
- `nginx:1.26` stream: `nginx-1.26.3-10.module_el9.9.0+357+ccfac862.1.alma.2`

**AlmaLinux 10**

- Default (nginx 1.26): `nginx-1.26.3-16.el10_3.1.alma.3`

**AlmaLinux Kitten 10**

- Default (nginx 1.26): `nginx-1.26.3-17.el10.alma.2`

## Updating

Update nginx and restart it. A reload is not enough, because it does not load the new nginx binary:

```bash
sudo dnf clean metadata && sudo dnf upgrade 'nginx*'
sudo systemctl restart nginx
```

Most mirrors sync every few hours, so if the update is not available to you yet, try again a little later. Confirm with `rpm -q nginx` against the versions above. Don't rely on `nginx -v`: our fixes are backported, so the upstream nginx version number doesn't change.

## Mitigations until you can update

The two HTTP/2 flaws are the ones most sites are exposed to, and turning HTTP/2 off for client connections closes both of them. It does not help with the other three, so install the update as soon as you can. Browsers and most other clients fall back to HTTP/1.1 on their own. gRPC clients need HTTP/2, so if you proxy gRPC through nginx, this mitigation will break it.

1. Find every place HTTP/2 is turned on, with the same command as above:

   ```bash
   sudo grep -RnE '^\s*(listen\s.*\bhttp2\b|http2\s+on)' /etc/nginx
   ```

2. In each file it lists, remove `http2` from the `listen` lines, for example change `listen 443 ssl http2;` to `listen 443 ssl;`. On AlmaLinux 10, Kitten 10, and the `nginx:1.26` stream on AlmaLinux 9, change any `http2 on;` to `http2 off;`. Do this for every match: if any server block on an address and port still has `http2` on its `listen` line, HTTP/2 stays on for every site on that address and port.

3. Check the configuration and restart nginx, so that no worker keeps serving existing HTTP/2 connections:

   ```bash
   sudo nginx -t && sudo systemctl restart nginx
   ```

4. Confirm that your site now answers over HTTP/1.1 (replace the address with your own). This should print `1.1`:

   ```bash
   curl -so /dev/null --http2 -w '%{http_version}\n' https://www.example.com/
   ```

Once you have installed the patched packages, you can turn HTTP/2 back on by reversing these changes.

## Thanks

Thanks to the researchers who found and reported these flaws, as credited by nginx: **Xint.io** (CVE-2026-123007, CVE-2026-123634, CVE-2026-113425, and CVE-2026-121810), **Albert of Vexera AI** (CVE-2026-123633), and **Maxim Dounin** (CVE-2026-113425). Thanks also to **Roman Arutyunyan**, **Vadim Zhestikov**, and **Maxim Dounin** for writing the fixes.

Thanks to the AlmaLinux Core SIG for backporting the fixes to every supported nginx stream, and to ALESCo for moving quickly to approve shipping ahead of upstream.

And thank you to the [sponsors of the AlmaLinux OS Foundation](/foundation/), whose support makes this work possible, especially our platinum sponsors: [CloudLinux](https://www.cloudlinux.com), [Cybertrust Japan](https://www.cybertrust.co.jp/almalinux/), and [TuxCare](https://tuxcare.com/).

## Stay informed

Remaining aware of these vulnerabilities and acting quickly can keep your systems and data safe. Follow the AlmaLinux Blog, join the [Mattermost Community Chat](https://chat.almalinux.org/), and subscribe to the [Announce](https://lists.almalinux.org/mailman3/lists/announce.lists.almalinux.org/) and [Security](https://lists.almalinux.org/mailman3/lists/security.lists.almalinux.org/) mailing lists to stay informed.

## Changelog

- **2026-11-18 22:35 UTC:** Initial post published. Patched packages fixing all five NGINX2Shell vulnerabilities released straight to the production repositories for every supported nginx stream on AlmaLinux 8, 9, and 10, and for Kitten 10.
