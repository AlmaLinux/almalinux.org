---
title: "Testers needed: Zenbleed patch for AlmaLinux 8 and 9"
type: blog
author: 
 name: "Andrew Lukoshko"
 bio: "Release Engineering Lead"
 image: /users/alukoshko.jpg
date: '2023-07-24'
post:
    title: "Testers needed: Zenbleed patch for AlmaLinux 8 and 9"
    image: /blog-images/23.07.24.zenbleed.png
---

EDIT, July 27th: as of 12 hours after the release we have still seen no reports of any errors from users who have applied this update. If you see any problems, feel free to report them to us: [bugs.almalinux.org](https://bugs.almalinux.org)

EDIT, July 26: We will be releasing this patch on July 27th at 7am US Eastern time. Read more on the [forums](https://almalinux.discourse.group/t/zenbleed-patch-release-7am-eastern-us-time-7-27-23/2802).

Edit, July 25: AMD has put out an [official security bulletin](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7008.html) that lists all of the impacted hardware and anticipated release dates of patches for older CPUs. 

Earlier today our community pointed out a new, trivially exploitable flaw in [AMD systems called Zenbleed](https://lwn.net/Articles/939099/). Due to an accident on the AMD side, the patch was released ahead of responsible disclosure, and unpatched systems are at great risk. We were able to pull in the patch, get through our normal testing, and we are now ready for wider testing for both AlmaLinux 8 and 9.


## How did AlmaLinux get the patch?

The fix was released by AMD, so we were able to pull that directly in, similar to what all other distributions are currently having to do. We pulled in three patches from linux-firmware upstream:

[https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/amd-ucode?id=69143e8eca62a80b9791b8d358d1cc4c90e373c9](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/amd-ucode?id=69143e8eca62a80b9791b8d358d1cc4c90e373c9)

[https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/amd-ucode?id=b250b32ab1d044953af2dc5e790819a7703b7ee6](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/amd-ucode?id=b250b32ab1d044953af2dc5e790819a7703b7ee6)

[https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/amd-ucode?id=0bc3126c9cfa0b8c761483215c25382f831a7c6f](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/amd-ucode?id=0bc3126c9cfa0b8c761483215c25382f831a7c6f)

You can see the diff of the changes on [git.almalinux.org](https://git.almalinux.org/rpms/linux-firmware/commit/b908df53b1c732aa18435a947f8e3c6a45ebc72c). 


## How do I install the updated packages?

Due to the risks involved in these patches, these packages are not yet in production and need testing! If you are willing to help provide us feedback, and have access to a **bare metal AMD system**, you can manually install them by pulling them from the AlmaLinux Build System.  

**To install the new RPM on AlmaLinux 8:**

```bash
dnf update https://build.almalinux.org/pulp/content/builds/AlmaLinux-8-x86_64-7032-br/Packages/l/linux-firmware-20230404-114.git2e92a49f.el8_8.alma.noarch.rpm
```


**For AlmaLinux 9:**

```bash
dnf update https://build.almalinux.org/pulp/content/builds/AlmaLinux-9-x86_64-7033-br/Packages/l/linux-firmware-20230310-134.el9_2.alma.noarch.rpm
```


**To check that the installation completed successfully, you can run:**

```bash
rpm -qa linux-firmware
```

**To update CPU microcode run the following:**

```bash
echo 1 > /sys/devices/system/cpu/microcode/reload
```

Once you have completed your testing, please help us by letting us know it works for you! Please share the following information (sanitized in whatever way you feel comfortable) in a comment on the issue we’ve opened to track this update on bugs.almalinux.org. We have created one specific to [AlmaLinux 8](https://bugs.almalinux.org/view.php?id=412) and one for [AlmaLinux 9](https://bugs.almalinux.org/view.php?id=413). Please include the output of the two commands from the test server and whether it worked for you.

```bash
lscpu
journalctl -k --grep=microcode
```


## Why call for testing now?

The depth of this exploit is motivation for moving fast, in our opinion. Our users are looking for a patch to come quickly, and this is one more opportunity that we have as a result of our decision to aim for [ABI compatibility](https://almalinux.org/blog/future-of-almalinux/). We will be looking for more opportunities for testing and early/beta adopters as we expand. In fact, we have a kernel update in testing right now, that was shared in [chat.almalinux.org](https://chat.almalinux.org/almalinux/pl/5o5ffzjc53djtrifnuqdeb1ser) earlier today. If you have interest in helping us with testing, please do join us there!


## Come help!

Joining the AlmaLinux community is easy! For anyone that has time to offer: the Release Engineering SIG (~Engineering/RelEng on [chat.almalinux.org](https://chat.almalinux.org)) could use help for testing and building our pipelines, but the Infra, Cloud, and Marketing SIGs are always looking as well. You can also convince your company to become a sponsor or just back us as an individual [on GitHub](https://github.com/sponsors/AlmaLinux) or [OpenCollective](https://opencollective.com/almalinux-os-foundation). 

Thank you to everyone who helps make AlmaLinux happen. Our individual sponsors and backers in addition to our corporate sponsors are the biggest reason we can continue to provide AlmaLinux OS free forever.
