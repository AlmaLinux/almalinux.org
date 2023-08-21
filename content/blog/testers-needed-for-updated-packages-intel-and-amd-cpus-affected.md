---
title: "Testers needed for security updates: Intel and AMD CPUs affected"
type: blog
author: 
 name: "Andrew Lukoshko"
 bio: "Release Engineering Lead"
 image: /users/alukoshko.jpg
date: '2023-08-14'
post:
    title: "Testers needed for security updates: Intel and AMD CPUs affected"
    image: /blog-images/testers-post.png
---

Earlier this week a few vulnerabilities were reported to affect Intel and AMD CPUs. The AlmaLinux OS Foundation calls for the community to help test the freshly updated packages for AlmaLinux OS 8 and AlmaLinux OS 9.

### How do I install updated  packages?

 As we recently changed the build process for AlmaLinux OS, and are now aiming to be [ABI compatible](https://almalinux.org/blog/future-of-almalinux/) with Red Hat Enterprise Linux, we are now able to release updates without waiting for the patches to be released upstream. To help accommodate that, a **Testing** repo has been created for packages that differ from RHEL and require additional testing by our users. 
To be able to help with testing, the **Testing** repo should be enabled on the AlmaLinux machine:

```bash
dnf install -y almalinux-release-testing
```
We highly recommend and encourage you to enable the **Testing** repo on all non-production machines to expand participation in the AlmaLinux development.

### CVE-2022-40982 aka Downfall (Intel)

The recently announced [CVE-2022-40982](https://downfall.page/) vulnerability is related to a Gather Data Sampling (GDS) transient execution side-channel vulnerability affecting Intel CPUs. This may allow an attacker to access stale data from previously used vector registers on the same physical core. Computing devices based on Intel Core processors from the 6th Skylake to (including) the 11th Tiger Lake generation are affected.

Once you enable the **Testing** repo, the vulnerability can be mitigated by updating CPU microcode - `microcode_ctl` package:
 
```bash
dnf update microcode_ctl
```

**To check that the installation is completed successfully, you can run:**

```bash
rpm -qa microcode_ctl
```

**Make sure that you've got the following version:**
* AlmaLinux OS 8 - microcode_ctl-20220809-2.20230808.1.el8_8.alma
* AlmaLinux OS 9 - microcode_ctl-20220809-2.20230808.1.el9_2.alma

**To update the CPU microcode run the following or reboot the computer:**

```bash
echo 1 > /sys/devices/system/cpu/microcode/reload
```


### CVE-2023-20569 (AMD)

The recently announced [CVE-2023-20569](https://nvd.nist.gov/vuln/detail/CVE-2023-20569) vulnerability affects "Zen 3" and "Zen 4" AMD CPUs as it may allow an attacker to influence the return address prediction. This may potentially lead to information disclosure.

Once you enable the **Testing** repo, the vulnerability can be partially mitigated by updating `linux-firmware` package:

```bash
dnf update linux-firmware
```

**To check that the installation is completed successfully, you can run:**

```bash
rpm -qa linux-firmware
```

**Make sure that you've got the following version:**
* AlmaLinux OS 8 - linux-firmware-20230404-114.git2e92a49f.el8_8.alma.1
* AlmaLinux OS 9 - linux-firmware-20230310-134.el9_2.alma.1

**To update the CPU microcode run the following or reboot the computer:**

```bash
echo 1 > /sys/devices/system/cpu/microcode/reload
```

### Share your output

Once you have completed your testing, please help us by letting us know it works for you! 

Please share the information (sanitized in whatever way you feel comfortable) in a comment on the issue that we have created specifically for AlmaLinux 8 and for AlmaLinux 9 to track on [bugs.almalinux.org](https://bugs.almalinux.org/):
* AlmaLinux OS 8
    * [CVE-2022-40982 (Intel)](https://bugs.almalinux.org/view.php?id=420)
    * [CVE-2023-20569 (AMD)](https://bugs.almalinux.org/view.php?id=419)
* AlmaLinux OS 9
    * [CVE-2022-40982 (Intel)](https://bugs.almalinux.org/view.php?id=418)
    * [CVE-2023-20569 (AMD)](https://bugs.almalinux.org/view.php?id=417)
    
Please include the output of the two commands from the test server and whether it worked for you:

```bash
lscpu
journalctl -k --grep=microcode
```

## Come Help with Testing

If you want to contribute and help with testing - join the AlmaLinux community and the Release Engineering SIG [chat channel](https://chat.almalinux.org/almalinux/channels/engineeringreleng).

We appreciate any contribution as they help us keep AlmaLinux OS free and make it better!
