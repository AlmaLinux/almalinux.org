---
title: "AlmaLinux 8 GPG key change"
type: blog
author: 
 name: "Andrew Lukoshko"
 bio: "Release Engineering Lead"
 image: /users/alukoshko.jpg
date: 2023-12-19
images:
  - /blog-images/2023-12-almalinux8keychange.png
post: 
    title: "AlmaLinux 8 GPG key change"
    image: /blog-images/2023-12-almalinux8keychange.png
---

Earlier this year we realized that the GPG key we use to sign packages for AlmaLinux 8 is set to expire in January of 2024. If you keep your system up to date, you don't need to take any further action.

If your device is running a little behind in updates for AlmaLinux 8, please read more below to identify the actions you need to take.


## Getting ready for AlmaLinux 8 GPG key change

On January 12, 2024 we will start signing RPM packages and repodata for AlmaLinux 8 with the updated GPG key. Taking the steps below will allow you  to continue to recieve updates without problems when we make the switch. 

### Fast track
If you want to make sure your system already includes and trusts new AlmaLinux 8 GPG key you can just import it:

```
rpm --import https://repo.almalinux.org/almalinux/RPM-GPG-KEY-AlmaLinux
```

This command imports new AlmaLinux 8 GPG key to rpm database if it's not there yet, or does nothing if it's already trusted. No more action required.

### How to check your system and import new key
The new GPG key is included in the `almalinux-release` package version `8.8-3.el8` (released Oct 16, 2023) or higher. To see if your system already trusts the new AlmaLinux 8 GPG key you can run the following:
```
rpm -q gpg-pubkey-ced7258b-6525146f
```
If the new GPG key is already trusted, you will see the following message, and no further action is necessary:
```
gpg-pubkey-ced7258b-6525146f
```
If the GPG key is not trusted, you will see the following error:
```
package gpg-pubkey-ced7258b-6525146f is not installed
```
In this case we recommended that you import the new AlmaLinux 8 GPG key to the rpm database:
```
rpm --import https://repo.almalinux.org/almalinux/RPM-GPG-KEY-AlmaLinux
```
If your device is running in an airgapped environment, or does not have an external network connection, as long as the `almalinux-release` package version `8.8-3.el8` or higher is installed you can also import key directly from the file:
```
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-AlmaLinux
```
### What will happen if none of the above is done?
If your system is recent enough and you install updates on regular basis, nothing bad will happen. The new AlmaLinux 8 GPG key is included in `almalinux-release` package version `8.8-3.el8` or higher (released Oct 16, 2023). 

In this case when trying to install package signed with the new key `dnf` may ask you to trust new key (this is exactly what happens when you install updates on clean just installed OS). If you use `dnf` with `-y` argument this will happen automatically.

**BUT**, if your system has not received updates for a long time and `almalinux-release` package version is lower than `8.8-3.el8` you will not be able to install packages signed with the new key until you manually import new GPG key as trusted. 

## Get or give help!

As the number of AlmaLinux users grows the number of people asking questions and needing help is growing, too! If you have questions about this or anything else AlmaLinux-related, you can ask on our forums or in our [AlmaLinux Community Chat](https://chat.almalinux.org/). While you're there, take a second to see if there are any unanswered questions that you can help with! 

You can also keep up to date with all things AlmaLinux by subscribing to our [announce](https://lists.almalinux.org/postorius/lists/announce.lists.almalinux.org/) mailing list, or our signing up for our [monthly newsletter](https://lists.almalinux.org/postorius/lists/newsletters.lists.almalinux.org/). Catch us on [Reddit](https://reddit.com/r/almalinux), and follow us on Mastodon [@almalinux@fosstodon.org](https://fosstodon.org/@almalinux) or [X](https://twitter.com/almalinux).