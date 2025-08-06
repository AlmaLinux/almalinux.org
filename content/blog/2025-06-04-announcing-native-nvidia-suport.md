---
title: "Native NVIDIA support for AlmaLinux OS 9 and 10"
type: blog
author: 
 name: "Neal Gompa and Jonathan Wright"
 bio: ""
 image: /users/nealandJonathan.png
date: '2025-08-06'
images:
  - /blog-images/2025/nvidia_support_announcement.png
post:
    title: "Native NVIDIA support for AlmaLinux OS 9 and 10"
    image: /blog-images/2025/nvidia_support_announcement.png

---

At long last, users of NVIDIA graphics cards can enjoy a drastically improved user experience with AlmaLinux.

## AlmaLinux's native NVIDIA support

AlmaLinux OS 9 and 10 now ship with packages enabling native NVIDIA driver support, including CUDA and Secure Boot. Thanks to ALESCo, NVIDIA, and this approved [RFC](https://github.com/AlmaLinux/ALESCo/blob/master/rfcs/0004-build-and-ship-nvidia-drivers.md), AlmaLinux 9 and 10 solves that for NVIDIA users by shipping NVIDIA's open source graphics driver as a kernel module, along with a repository config for many of the common userspace and CUDA components. With AlmaLinux 9 and 10 and the new NVIDIA packages, a few `dnf` commands are all that stand between users and a fully-integrated NVIDIA experience.

## NVIDIA's shift to open source 

When AlmaLinux started just 5 years ago, this wouldn't have been possible. With NVIDIA's open source version of their graphics drivers things have changed.  This open source version is slowly becoming the flagship driver, with new products being added exclusively to it. With the help of some incredible people in the open source ecosystem and the AlmaLinux community, we were able to do something that has yet to be done in the EL ecosystem - ship secure-boot signed, open source, NVIDIA kernel modules.

## How to take advantage of this update

Getting started is easy! You just install the release package and then the modules and you're all set.

_Full documentation is available at https://wiki.almalinux.org/documentation/nvidia.html with a quick getting started excerpt below._

### Installing NVIDIA Drivers for AlmaLinux OS 9, 10, and Kitten 10

First, install the package holding the NVIDIA driver and repository configurations:

```bash
dnf install almalinux-release-nvidia-driver -y
```

Next, install the driver package:
```bash
dnf install nvidia-open-kmod nvidia-driver
```

It’s recommended to reboot your system now, which will load the driver automatically on the next boot.  Alternatively, if you’re booted into the latest kernel, you can load the kernel module with the `modprobe` utility

```bash
modprobe nvidia_drm
```

The easiest way to confirm functionality is with the `nvidia-smi` utility.  This is provided by the `nvidia-cuda-driver` package.

```bash
dnf install nvidia-cuda-driver -y
nvidia-smi
```

You can confirm the module is loaded correctly with this command:

```bash
# nvidia-smi
Tue May 27 21:33:53 2025
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.153.02         	Driver Version: 570.153.02 	CUDA Version: 12.8 	|
|-----------------------------------------+------------------------+----------------------+
| GPU  Name             	Persistence-M | Bus-Id      	Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf      	Pwr:Usage/Cap |       	Memory-Usage | GPU-Util  Compute M. |
|                                     	|                    	|           	MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA L4                  	Off |   00000000:31:00.0 Off |                	0 |
| N/A   26C	P8         	11W /   72W |   	0MiB /  23034MiB |  	0%  	Default |
|                                     	|                    	|              	N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                          	|
|  GPU   GI   CI          	PID   Type   Process name                    	GPU Memory |
|    	ID   ID                                                           	Usage  	|
|=========================================================================================|
|  No running processes found                                                         	|
+-----------------------------------------------------------------------------------------+
```

If you also want the CUDA stack you can get that as follows:
`dnf install cuda`