---
title: "How ELevate supports business needs"
type: blog
author: 
 name: "David der Nederlanden"
 bio: "Linux Cloud Architect at Bizway"
 image: /users/ddernederlanden.jpg
date: '2024-05-02'
images:
  - /blog-images/
post:
	title: "How ELevate supports business needs"
	image: /blog-images/
---

## whoami and a bit about our systems
I'm David, from the Netherlands and I try to spread the feeling I experience myself while working within the hosting industry whenever I can, it really is something magical!
My employer Bizway, a Dutch Managed Service Provider (MSP from now on) gives me the chance to explore all the different aspects that are on the table when providing services to customers.

Things that interest me a lot are automation, mostly anything opensource, networking and infrastructure.

The first Linux I ever used was actually Debian, which luckily I still use a lot too, as it is the base for [Proxmox Virtual Environment](https://www.proxmox.com).
While for the past 4 years CentOS and AlmaLinux took most of my time, Debian always kept a special place because of one simple reason, because Debian provided in-place OS upgrades.

Even though servers can, and one can discuss, maybe even should be configured in state so one can destroy and replace one easily, that is not always the case.

So when AlmaLinux came around and further down the road ELevate popped up offering in-place upgrades from CentOS 7 systems to for example AlmaLinux 8 and higher, it also entered that special place!

## Why there can be (and are!) still CentOS 6 servers alive and kicking
We always used CentOS as our main operating system for our webhosting platforms, while we were eventually forced to look elsewhere, we still had a lot of CentOS 7 and a couple of CentOS 6 systems around,
since ELevate came around we started upgrading our whole fleet to AlmaLinux 8 as we started using that for our new deployments too, we're almost done doing so.

Upgrading is most of the time the less painfull way to get your customer to use a new OS,
as in migrations to a new server there's always something that takes some debugging while with in-place upgrades it mostly stays intact.

That still doesn't make up for the CentOS 6 servers still around, which in all honesty should've been gone a long time ago already,
which as a MSP you can only do so much for your customer,
if they in the end use an application for their business that for some reason only runs on CentOS 6,
or their developer left a long time ago, well, good luck with that replacing that server...

Nowadays there are less and less excuses to make, as [DirectAdmin](https://www.directadmin.com) for example made it even possible to run php 5.6 code on AlmaLinux 8.

So when CloudFest and AlmaLinux day came around great things happened at the hackathon and the idea for ELevating CentOS 6 servers to CentOS 7 was born, which is really exciting news.

Once benny posted that ELevate was available for CentOS 6 I really was excited to try it on one of our servers, so after a bit of cloning and snapshotting off we went!

## Practical tips from a real life ELevate user
While after all the process itself is quite painless, it can be quite hard to get there.
ELevate is really good at identifying (potential) issues which you must resolve beforehand.

One that bothered us the most was that the /boot partition was almost always in need of more space,
while in more recent installations it was a matter of cleaning up old kernels, in our CentOS 6 server that really wasn't happening.
I had to move the /boot partition to a new partition which was bigger, which again, is something to keep in mind,
while it is a great tool to help deprecating those last CentOS 6 servers, it still might be cleaner to do it from scratch some day.

Test, test and... test. Something easily forgotten to be really honest, we've all done it at one point or another "easy, I've done that so many times, no way it goes wrong!",
just take from me to always define some testing points and write down / share the results before and after the change, in this case upgrading.

## AlmaLinux and ELevate helps us sleep at night
Overall AlmaLinux offers us a really stable platform which is exactly what we want and need,
one of their slogans is "No drama, just Linux", which is true if you follow the different developments in Linux Land,
the way they adapted to the several changes Red Hat brought us was really comforting and I think a great way forward.

The fact that they are able to patch CVE's themselves now as they see fit and even share their own Errata is awesome!


ELevate helps us keeping servers up-to-date and secure for another decade while providing the least impact for our customers,
which in the end is what counts and makes ourselves and our customers really happy.

If you have any questions after reading the above story feel free contact me at any possible way, one of them is via [AlmaLinux Chat](https://chat.almalinux.org), thanks for reading!
