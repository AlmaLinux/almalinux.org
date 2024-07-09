---
title: "How to get updates after CentOS 7 end of life"
type: blog
author: 
 name: "benny Vasquez"
 bio: "Chair, board of directors"
 image: /users/benny.jpeg
date: 2024-07-09
images:
  - /blog-images/2024/2024-07-centosEOL.png
post: 
    title: "How to get updates after CentOS 7 end of life"
    image: /blog-images/2024/2024-07-centosEOL.png
---

On June 30th CentOS 7 hit end of life, ending the long-loved and widely used CentOS Linux era. While the CentOS Project continues on with CentOS Stream, much of the world still needs another option for updates or upgrading with CentOS 7. The AlmaLinux community has a few options for you. (if you are seeing this post after July of 2024, check the [AlmaLinux Wiki](https://wiki.almalinux.org/elevate/ELevate-quickstart-guide.html) for the Always Up To Date directions)

## CentOS 7 End of Life - What's next? 

If you were using CentOS 7 still, you have likely been seeing this error when trying to apply updates. This indicates that it is time to find another solution, as you will no longer be getting updates for your device. 

```bash 
Cannot find a valid baseurl for repo: base/7/x86_64
```
it also spits out:

```bash 
Could not retrieve mirrorlist http://mirrorlist.centos.org/?release=7&arch=x86_64&repo=os&infra=stock error was
14: curl#6 - "Could not resolve host: mirrorlist.centos.org; Unknown error"
```

When that happens, you have a few options. 

* Backup your CentOS 7 device's content, and wipe and install a supported operating system (like the new AlmaLinux 8.10 or 9.4) on the device.
* Use Project ELevate to upgrade your device in-place to a supported operating system (like the new AlmaLinux 8.10 or 9.4) on the device.
* ignore it and hope things don't go south.

If you've hit the error without knowing the CentOS 7 end of life was near (and assuming you are chosing one of the first two options above), you will likely also need a buffer of time to help 

## Convert and upgrade CentOS 7 to AlmaLinux 8

AlmaLinux 8 just entered the second part of its life, where updates are limited to security updates. Those updates will continue until 31 May 2029. You can see the security updates that are happening for both AlmaLinux 8 and 9 on our [Errata](https://errata.almalinux.org) page, and AlmaLinux 8 will continue to receive updates through 

Upgrading your CentOS 7 devices to AlmaLinux 8 will take a little planning, but your future self will thank you.

Here are the key steps you need to follow to upgrade your CentOS 7 system to AlmaLinux 8. Check out [AlmaLinux Wiki](https://wiki.almalinux.org/elevate/ELevating-CentOS7-to-AlmaLinux-9) for an in-depth step-by-step guide that covers more steps, tips and known issues you might find helpful. 
* To get started on the upgrade process, an updated system is required to get the latest updates. Don't forget to reboot the system after updating it. 
    **NOTE:** Since the CentOS 7 repositories are now offline you will need to swap to the CentOS vault, or you can use our CentOS 7 mirror that we've setup for use with ELevate:
  ```bash
  sudo curl -o /etc/yum.repos.d/CentOS-Base.repo https://el7.repo.almalinux.org/centos/CentOS-Base.repo
  sudo yum upgrade -y
  ```
  **Don't forget to reboot!**
* Next you need to install the *elevate-release* package with the project repo and GPG key:
  ```bash
  sudo yum install -y http://repo.almalinux.org/elevate/elevate-release-latest-el$(rpm --eval %rhel).noarch.rpm
  ```
* Install leapp packages and upgrade data for AlmaLinux:
  ```bash
  sudo yum install -y leapp-upgrade leapp-data-almalinux
  ```
* The next step is to run a pre-upgrade command to identify possible problems and recommended solutions. Most popular issues and fixes are listed in the [wiki](https://wiki.almalinux.org/elevate/ELevating-CentOS7-to-AlmaLinux-9.htm), so be sure to check it.
  ```bash
  sudo leapp preupgrade
  ```
* After checking the preupgrade report and applying the neccessary fixes you can start an upgrade. You'll be offered to reboot the system after it and you'll see a new entry in GRUB called ELevate-Upgrade-Initramfs will appear. The system will be automatically booted into it. See how the update process goes in the console.
  ```bash
  sudo leapp upgrade
  ```
* When you login verify that the system was successfully upgraded to AlmaLinux 8. We also recommend checking logs and packages left from the previous OS version and removing or updating them manually.

## Upgrade CentOS 7 or 8 to AlmaLinux 9

If you are still running CentOS Linux 8 (which hit the end of life in December of 2021) or CentOS Stream 8 and want to upgrade, the process is very similar to the one outlined above. Do yourself a favor, and upgrade in place to AlmaLinux 9 using these instructions, to continue to receive updates through 31 May 2032. 

If you upgraded to AlmaLinux 8 using the instructions above, you can continue with the steps to [prepare](https://wiki.almalinux.org/elevate/ELevating-CentOS7-to-AlmaLinux-9.html#prepare-the-system-for-migration-to-almalinux-9) you system for upgrading to AlmaLinux 9.

### Converting from CentOS 8
If you are running CentOS 8 you can convert it to AlmaLinux 8 first using the [AlmaLinux Migration Tool](https://wiki.almalinux.org/documentation/migration-guide.html#how-to-migrate). Note, that the minimal supported version for conversion is 8.4. The key steps are: 
* Download [almalinux-deploy.sh](https://github.com/AlmaLinux/almalinux-deploy/blob/master/almalinux-deploy.sh) script:
  ```bash
  curl -O https://raw.githubusercontent.com/AlmaLinux/almalinux-deploy/master/almalinux-deploy.sh
  ```
* Run the script and check the output for any errors. If the conversion went without any issues, you'll see that upgrading to AlmaLinux is complete in the output.
  ```bash
  sudo bash almalinux-deploy.sh
  ```
* Now reboot the system to boot with AlmaLinux kernel and check the release 

### Upgrading to AlmaLinux 9

As soon as you get your AlmaLinux 8 system ready and prepared, you can start upgrading to AlmaLinux 9 by following these key steps. Check the wiki for more tips, known issues and recommendations. 
* Install the *elevate-release* package with the project repo and GPG key:
  ```bash
  sudo yum install -y http://repo.almalinux.org/elevate/elevate-release-latest-el$(rpm --eval %rhel).noarch.rpm
  ```
* Install leapp packages and upgrade data for AlmaLinux:
  ```bash
  sudo yum install -y leapp-upgrade leapp-data-almalinux
  ```
* Start a preupgrade check that will identify possible problems and recommended solutions. Most popular issues and fixes are listed in the [wiki](https://wiki.almalinux.org/elevate/ELevating-CentOS7-to-AlmaLinux-9.htm), so be sure to check it.
  ```bash
  sudo leapp preupgrade
  ```
* After checking the preupgrade report and applying the necessary fixes you can start an upgrade. You'll be offered to reboot the system after it and see a new entry in GRUB called ELevate-Upgrade-Initramfs appear. The system will be automatically booted into it. See how the update process goes in the console.
  ```bash
  sudo leapp upgrade
  ```
* Login and verify that the system was successfully upgraded to AlmaLinux 9. We also recommend checking logs and packages left from the previous OS version and removing or updating them manually.

## Extended support for CentOS 7

If you do not yet have the ability to upgrade your CentOS 7 devices to AlmaLinux, a few of our sponsors can offer you some short term help. 

TuxCare, a Platinum Sponsor member of the AlmaLinux OS Foundation and massive contributor to AlmaLinux, offers extended CentOS 7 life through security patches and support. You can read more about that on the [TuxCare website](https://tuxcare.com/almalinux-enterprise-support/). 

Cybertrust Japan, another Platinum sponsor member and contributor, extends the life of CentOS Linux 6, 7, and 8 with security patches for their customers through the "CentOS Extension Package". You can read more about that in their [press release](https://www.softbanktech.co.jp/en/news/release/press/2024/001/) from earlier this year, or on [the Cybertrust Japan website](https://www.cybertrust.co.jp/centos/support/centos7-extend-support.html).

OpenLogic from Perforce is a Silver Sponsor member and offers support for a number of open source software options, including extended CentOS 7 support as well! Read more on [the OpenLogic website](https://www.openlogic.com/solutions/enterprise-linux-support/centos).

## What's next?

If you have chosen your path, or even started your upgrade processes, we strongly recommend you plan for the next step as you do.