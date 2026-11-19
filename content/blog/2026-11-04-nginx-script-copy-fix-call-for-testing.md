---
title: 'Call for testing - nginx fix for "no buffer space in script copy" errors'
type: blog
author:
  name: "Andrew Lukoshko"
  bio: "AlmaLinux Lead Architect"
  image: /users/alukoshko.jpg
date: 2026-11-04
images:
  - /blog-images/2026/2026-11-04-nginx-script-copy-fix.png
post:
  title: 'After the CVE-2026-42533 security update, some nginx configurations started failing with intermittent HTTP 500 errors and "no buffer space in script copy" alerts. We''ve found the cause and built a fix that keeps the CVE protection in place. Help us test it on AlmaLinux 8, 9 and 10!'
  image: /blog-images/2026/2026-11-04-nginx-script-copy-fix.png
---

The recent nginx security update for CVE-2026-42533 introduced a regression: on some configurations, nginx randomly answers a small share of requests with HTTP 500 and logs `[alert] ... no buffer space in script copy`. Users reported it to us after updating, and we were able to reproduce it on every AlmaLinux release that received the update. We've found the root cause and built fixed nginx packages that remove the regression while keeping the CVE-2026-42533 fix fully in place. The packages are now in the AlmaLinux testing repository, and we need your help testing them before they go to production.

## The problem

After updating to the nginx packages that fix CVE-2026-42533, some users started seeing errors like this in `/var/log/nginx/error.log`:

```text
[alert] 12345#0: *678 no buffer space in script copy, client: 192.0.2.10, server: example.com, request: "GET /some/path HTTP/1.1"
```

Each of these alerts means the request failed with HTTP 500. The failures are intermittent: the same URL can work on one request and fail on the next. On one affected site, between a third and a half of the requests to a single location failed.

The problem shows up when a `set` or `rewrite` directive uses a variable from a `map` marked `volatile`, and the map value itself contains other variables. For example:

```nginx
map $uri $cache_key {
    volatile;
    default "$scheme://$host$uri$is_args$args";
}

server {
    location /purge/ {
        set $key $cache_key;
        ...
    }
}
```

Configurations like this worked fine before the CVE-2026-42533 update.

## What went wrong

CVE-2026-42533 is a buffer overrun in nginx's script engine, the code that builds strings from variables for directives like `set`, `rewrite`, `return` and `proxy_pass`. The [upstream fix](https://github.com/nginx/nginx/commit/7ac6789) adds a check: before copying data into the result buffer, nginx makes sure it doesn't write past the end of that buffer. To do that, upstream stores the buffer end in each script engine instance.

Adding a field to the script engine structure changes nginx's ABI, which would break third-party dynamic modules built against the current packages. To avoid that, the backported fix shipped in the CentOS Stream and RHEL packages (and therefore in AlmaLinux) keeps the buffer end in a single global variable instead. That works as long as only one script runs at a time.

But scripts can be nested. When `set $key $cache_key` copies the value of a volatile map variable, nginx evaluates the map right then, and the map runs its own script to build `"$scheme://$host$uri..."`. That inner script overwrites the global buffer end with the end of _its own_ buffer. When control returns to the outer `set`, its bounds check compares against the wrong buffer. Whether that check fails depends on where the two buffers happen to land in memory, which is why the errors are random.

Without `volatile`, the map value is computed once and cached before the outer script starts, so there's no nesting and no error.

## What the fix does

The fix is small. Every function that runs a script (`ngx_http_complex_value()`, `ngx_http_script_run()`, and their `stream` module equivalents) now saves the current global buffer end before it starts and restores it when it finishes. A nested script can still use the global for its own buffer, but the outer script gets its correct value back as soon as the inner one returns. This gives the same result as upstream's per-engine buffer end:

- **The CVE-2026-42533 protection stays fully in place.** Every bounds check added by the security fix is still there and still checks against the right buffer. We confirmed that a request that triggers the original overflow is still rejected with HTTP 500 and the same alert.
- **The ABI doesn't change**, so existing third-party dynamic modules keep working.
- **Nested scripts work again**, so configurations like the one above stop producing errors.

Here are our results from 2000 requests against the example configuration above:

| Package                          | Before the fix | With the fix |
| -------------------------------- | -------------: | -----------: |
| AlmaLinux 9, nginx 1.20          |       26 × 500 |            0 |
| AlmaLinux 9, `nginx:1.24` stream |       20 × 500 |            0 |
| AlmaLinux 10, nginx 1.26         |       19 × 500 |            0 |

We've also reported the issue and the fix to Red Hat as [RHEL-300689](https://redhat.atlassian.net/browse/RHEL-300689), so that it can be fixed in CentOS Stream and RHEL as well.

## Packages in testing

| Release      | nginx                      | Package                                                 |
| ------------ | -------------------------- | ------------------------------------------------------- |
| AlmaLinux 8  | `nginx:1.24` module stream | `nginx-1.24.0-3.module_el8.10.0+4351+6f6e4e3e.5.alma.2` |
| AlmaLinux 9  | default package            | `nginx-1.20.1-28.el9_8.6.alma.2`                        |
| AlmaLinux 9  | `nginx:1.24` module stream | `nginx-1.24.0-7.module_el9.8.0+335+c30a9238.5.alma.2`   |
| AlmaLinux 10 | default package            | `nginx-1.26.3-6.el10_2.7.alma.1`                        |

If you use a module stream, the testing repository will offer you the update only for the stream you have enabled. You can check which stream that is with `dnf module list nginx`.

## How to test

We especially welcome testing from anyone who has seen the `no buffer space in script copy` alert, but every report helps, including "everything still works".

**Install the testing repo**

```bash
sudo dnf install -y almalinux-release-testing
```

**Update nginx and any installed nginx modules**

```bash
sudo dnf upgrade 'nginx*' --enablerepo=almalinux-testing
```

**Confirm you have the patched version**

```bash
rpm -q nginx
```

The result should match the package for your release in the table above.

**Check your configuration and restart nginx**

The package update doesn't restart nginx, so restart it to load the new binary:

```bash
sudo nginx -t && sudo systemctl restart nginx
```

**Check the error log**

After running for a while with your usual traffic, this should not find any new alerts:

```bash
sudo grep 'no buffer space in script copy' /var/log/nginx/error.log
```

_**Note**: We don't recommend that you keep the testing repo enabled after you've updated the packages, unless you've done this on a truly non-production environment. If this is a production environment, you can disable the repo with this command:_

```bash
sudo dnf config-manager --disable almalinux-testing
```

## Share your results!

If you encounter problems or want to share your testing results, please let us know as soon as you can, either in the [Development](https://chat.almalinux.org/almalinux/channels/development) channel on our Mattermost chat, on [bugs.almalinux.org](https://bugs.almalinux.org), or by emailing [packager@almalinux.org](mailto:packager@almalinux.org). It's just as important to report if everything works fine as it is to report bugs, so let us know either way!
