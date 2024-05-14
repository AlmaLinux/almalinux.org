---
title: "How ELevate supports business needs"
type: blog
author: 
 name: "David der Nederlanden"
 bio: "Linux Cloud Architect at Bizway"
 image: /users/ddernederlanden.jpg
date: '2024-05-22'
images:
  - /blog-images/2024/2024-04-23-centos6-to-centos7.png
post:
    title: "How ELevate supports business needs"
    image: /blog-images/2024/2024-04-23-centos6-to-centos7.png
---

# How Elevate supports business needs
While we've been busy upgrading all our CentOS 7 servers to AlmaLinux 8 and higher, the ELevate Project now has the abillity to upgrade CentOS 6 servers too!

## whoami and a bit about our systems

I'm David from the Netherlands and I try to spread the feeling I experience myself while working within the hosting industry whenever I can, it really is something magical!
My employer Bizway, a Dutch Managed Service Provider (MSP from now on) gives me the chance to explore all the different aspects that are on the table when providing services to customers.

Things that interest me a lot are automation, mostly anything opensource, networking and infrastructure.

The first Linux I ever used was actually Debian, which I luckily still use a lot too, as it is the base for [Proxmox Virtual Environment](https://www.proxmox.com).
While for the past 4 years CentOS and AlmaLinux took most of my time, Debian always kept a special place because of one simple reason, Debian provides in-place OS upgrades.

Even though servers can, and one can discuss, maybe even should be configured in state so you can destroy and replace it easily, that is not always the case.

So when AlmaLinux came around and further down the road ELevate popped up offering in-place upgrades from CentOS 7 systems to for example AlmaLinux 8 and higher, it also entered that special place!

## Why there can be (and are!) still CentOS 6 servers alive and kicking
We always used CentOS as our main operating system for our webhosting platforms, while we were eventually forced to look elsewhere, we still had a lot of CentOS 7 and a couple of CentOS 6 systems around,
since ELevate came around we started upgrading our whole fleet to AlmaLinux 8 as we started using that for our new deployments too, we're almost done doing so.

Upgrading is most of the time the less painfull way to get your customer to use a new OS,
as with migrating to a new server there's always something that takes some debugging where in-place upgrades keep it mostly intact,
which is important, because as a techie we tend to forget that customers mostly want the servers to just work to support their business needs.

That still doesn't make up for the CentOS 6 servers currently around, which in all honesty should've been gone a long time ago already,
in which as a MSP you can only do so much for your customer,
if in the end they use an application for their business that for some reason only runs on CentOS 6,
or their developer left a long time ago, well, good luck with replacing that server...

It gives however a great reason to have some fun with the new release of [ELevate](https://almalinux.org/blog/2024-04-25-elevate-supports-centos-6-to-centos-7/), as it now supports ELevating CentOS 6 too!

Nowadays there are less and less excuses to make, as [DirectAdmin](https://www.directadmin.com) for example made it even possible to run php 5.6 code on AlmaLinux 9,
which is a great way of offering your customer a up-to-date operating system if they're really dependent on php 5.6, which gives us one less thing to worry about.

So when CloudFest and AlmaLinux day came around great things happened at the hackathon and the idea for ELevating CentOS 6 servers to CentOS 7 was born, which is really exciting news.

Once benny posted that ELevate was available for CentOS 6 I was really excited to try it on one of our servers, so after a bit of cloning and snapshotting off we went!

## Practical tips from a real life ELevate user
While after all the ELevate process itself is quite painless, it can be quite hard to get there.
I really recommend following/reading the detailed [wiki](https://wiki.almalinux.org/elevate) for the different available migrations.

ELevate is really good at identifying (potential) issues which you must resolve beforehand, below you can read some of those.

### /boot
One that bothered us the most was that the /boot partition is almost always in need of more space,
while in more recent installations it was a matter of cleaning up old kernels, in our CentOS 6 servers that really wasn't happening as most servers had a 128Mb /boot partition.

So I had to move the /boot partition to a new partition which was bigger, again, something to keep in mind,
while ELevate is a great tool to help deprecating those last CentOS 6 servers, it still might be cleaner to do it from scratch some day.

While moving the partition is quite an easy way, it can be quite dirty if you put it directly behind your data partition,
you might want to consider moving that further back and just expanding the current /boot partition itself,
or even simpler, move it to a seperate disk, for which the steps are as follows:

```bash
# add a new disk of 1Gb to your VM
# add it to the boot order in your hypervisor of choice

# create a new partition on the new disk with fdisk /dev/sdb as primary and type Linux.

# reload the partitions and create a ext4 filesystem on the new partition
partx -v -a /dev/sdb
mkfs.ext4 /dev/sdb1

# copy your original /boot partition to the new partition with dd
dd if=/dev/sda1 of=/dev/sdb1 bs=1M

# extend the new partition as the old size is inherited while using dd
e2fsck -fy /dev/sdb1
resize2fs /dev/sdb1
e2fsck -fy /dev/sdb1

# unmount the old boot partition and mount the new one
umount /dev/sda1
mount /dev/sdb1 /boot

# install grub on the new disk and scramble uuid of original /boot so it doesn't get mounted accidentally
grub-install --recheck /dev/sdb
tune2fs /dev/sda1 -U random

# check the UUID's and grub
blkid
cat /etc/fstab
cat /boot/grub/grub.conf

# delete old partition so it can't be used again accidentally
fdisk /dev/sda

# reboot the machine to actually boot from the new /boot partition
reboot now
```

### grub to grub2!
When upgrading to CentOS 7 my test server switches from grub to grub2, when I wanted to try ELevating it to AlmaLinux 8 it complained about some grub issues,
I had to create a /boot/grub2/grub.cfg file and create /etc/default/grub.

For /etc/default/grub I created it by using the booted system and put the following there:
```bash
GRUB_TIMEOUT=5
GRUB_DISTRIBUTOR="$(sed 's, release .*$,,g' /etc/system-release)"
GRUB_DEFAULT=saved
GRUB_DISABLE_SUBMENU=true
#GRUB_TERMINAL_OUTPUT="console"
GRUB_CMDLINE_LINUX=< put the output of cat /proc/cmdline here! >
GRUB_DISABLE_RECOVERY="true"
GRUB_THEME="/boot/grub2/themes/system/theme.txt"
```

And generate /boot/grub2/grub.cfg with:
```bash
grub2-mkconfig -o /boot/grub2/grub.cfg
```

### DirectAdmin specific tips
After every leapp upgrade we rebuild all packages that DirectAdmin brings, sometimes this can go wrong with for example some older local libraries, the following commands might help you out sometime.
```bash
# remove and list old local items
da build list_removals
da build remove_items
da build remove_old_local libiconv
# restore old local item in case it was actually necessary
da build restore_old_local libnghttp2

# build everything (keep resolving upcoming issues untill this runs succesfully)
da build all

# this one specifically helped me after the CentOS 6 upgrade as DirectAdmin kept complaining about local libraries.
da build doMigrateToSystemCurl
```

Something to keep in mind is in general on CentOS 6 you're running older software versions, as you must for example update MySQL too from 5.6 to 5.7 in the process, you will run into changed or removed configuration parameters,
change or comment as needed in /etc/my.cnf to get you running again.

In short you want to check at least the following parameters before building all packages.
```bash
# For /usr/local/directadmin/custombuild/options.conf:
mod_ruid2=no # as mod_ruid2 isn't supported anymore
mysql=5.7 # or higher if your application supports it
phpX_mode=php-fpm # as mod_php is deprecated

# Within /etc/my.cnf disable deprecated parameters like:
thread_concurrency=8
```

### Test, test and... test.
Something easily forgotten, and to be really honest, we've all done it at one point or another by thinking: "easy, I've done that so many times, no way it goes wrong!",
is to always define some testing points and write down / share the results before and after the change, in this case upgrading.

It also gives a really good starting point when cleaning up older packages afterwards, sometimes the server has lived quite long and not every package installed is still needed,
when you know what to expect from the services your customer provides on their server you can actually clean up packages and test afterwards if all customer critical services are still working.


## AlmaLinux and ELevate helps us sleep at night
Overall AlmaLinux offers us a really stable platform which is exactly what we want and need,
one of their slogans is "No drama, just Linux", which is true if you follow the different developments in Linux Land,
the way they adapted to the several changes Red Hat brought us was really comforting and I think a great way forward.

The fact that they are able to patch CVE's themselves now as they see fit and even share their own [Errata](https://errata.almalinux.org/) is awesome!

ELevate helps us keeping servers up-to-date and secure for another decade while providing the least impact for our customers,
which in the end is what counts and makes ourselves and our customers really happy.

If you have any questions after reading the above story feel free contact me at any possible way, one of them is via [AlmaLinux Chat](https://chat.almalinux.org), thanks for reading!
