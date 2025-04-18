---
title: "AlmaLinux OS Now Available via WSL CLI!"
type: blog
author: 
 name: "Elkhan Mammadli"
 bio: "Cloud SIG lead & ALESCo member"
 image: /users/elkhan.jpg
date: '2025-04-17'
post:
    title: "AlmaLinux OS Now Available via WSL CLI"
    image: /blog-images/2025/2025-04-almalinux-wsl-cli.png

---

I’m excited to share some great news for users running AlmaLinux OS on Windows Subsystem for Linux (WSL).

You can now install AlmaLinux OS images directly via the **WSL CLI tool** - no extra configuration and without having to navigate the Microsoft Store interface to install it! This change also makes it possible to install AlmaLinux on Windows Server, where the Store isn't available.

## What's New?

Previously, installing AlmaLinux on WSL required Microsoft Store. With this update, you can install the needed AlmaLinux OS directly from the CLI tool using a simple command:

```
wsl --install <AlmaLinux OS version>
```

The supported versions are:

* AlmaLinux-8 - available via WSL CLI and Microsoft Store
* AlmaLinux-9 - available via WSL CLI and Microsoft Store
* AlmaLinux-Kitten-10 - available via WSL CLI only

For more information and guidance about AlmaLinux OS for WSL, please, check [AlmaLinux Wiki](https://wiki.almalinux.org/documentation/wsl.html).

### How to Get Started

* Find PowerShell, Windows Terminal or CMD in the Windows search bar. Choose Run as administrator option.
* To install AlmaLinux on WSL, make sure you have WSL enabled on your system. If not, install it with:

  ```
  wsl --install --no-distribution
  ```
* If you’re already using WSL and want to add AlmaLinux, list all the Linux distributions that are officially available for installation via the WSL CLI:
  ```
  wsl --list --online
  ```
* Install AlmaLinux OS, for example, AlmaLinux 9:
  ```
  wsl --install AlmaLinux-9
  ```
* Launch AlmaLinux after installation to start using it:
    * Open it from the Windows Terminal. Click the small arrow ▾ next to the tab or the “+” icon. You’ll see a dropdown with available WSL distros listed. Click AlmaLinux-9. It will open in a new tab, ready to use.
    * Or run the command:

      ```
      wsl -d AlmaLinux-9
      ```

## How We Build WSL Images

Our built AlmaLinux WSL images are published on the **~SIG/Cloud** channel in the [AlmaLinux Community Chat](https://chat.almalinux.org), so anyone can test them. 

For those, who'd like to build their custom AlmaLinux WSL image, they can be easily built similar to how Open Container Initiative (OCI) container images are built. Only a couple of packages are needed:
* Install `bash`, `git`, `buildah` and `jq`.
* Clone the [WSL images repo](https://github.com/AlmaLinux/wsl-images.git).
* Run one of the scripts inside the `rootfs/` directory. Each script represents each AlmaLinux image.
* Ask the community in the ~SIG/Cloud [channel](https://chat.almalinux.org/almalinux/channels/sigcloud) to help test the images.

## How Can I Contribute?

We’d love for the community to help with testing! The testing has to be done in a Windows environment - so your input is super valuable. You can refer to the [Testing guide](https://github.com/AlmaLinux/wsl-images/blob/main/docs/Testing.md).

Feel free to join us and ask questions in the **~SIG/Cloud** channel in the [AlmaLinux Community Chat](https://chat.almalinux.org). We’d love to hear your feedback!

Enjoy your AlmaLinux OS on WSL :)
