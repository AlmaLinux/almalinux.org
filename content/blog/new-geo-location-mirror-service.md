---
title: "New Geo-Location Mirror Service"
type: blog
author: 
 name: "theMayor"
 bio: "-"
 image: /users/jack.jpg
date: '2021-06-08'
post:
    title: "Hi all, we’ve developed a new geo-location mirror service which should make things a lot faster, simpler and easier when installing packages, update..."
    image: 
---

Hi all, we’ve developed a new geo-location mirror service which should make things a lot faster, simpler and easier when installing packages, updates and downloading ISOs.

When hitting https://mirrors.almalinux.org It will allow you to:

- List the mirrors nearest to you when fetching a mirrorlist (https://images2.imgbox.com/b2/55/i0aCscHk_o.png)

- Give you a list of the nearest servers to you with ISO images (https://images2.imgbox.com/37/b1/oJHASQ4w_o.png)

You can help test it out. Add the following record in /etc/hosts on your server:

136.243.31.169 mirrors.almalinux.org

Now `dnf` will get the ten nearest mirrors from https://mirrors.almalinux.org/mirrorlist/8/

Please discuss any feedback on the [AlmaLinux Community Chat](https://chat.almalinux.org/), the [AlmaLinux Forums](https://almalinux.discourse.group/t/new-geo-location-mirror-service/279) or on [Reddit](https://www.reddit.com/r/AlmaLinux/comments/nvhk2e/new_geolocation_mirror_service/).
