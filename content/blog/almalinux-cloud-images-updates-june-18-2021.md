---
title: "AlmaLinux Cloud Images Updates - June 18 2021"
type: blog
author: 
 name: "theMayor"
 bio: "-"
 image: /images/profile.png
date: '2021-06-18'
post:
    title: "Hello Community! Here is a quick update on the various cloud images we have available as it's one of the top things we're asked about. The good news..."
    image: /blog-images/YiMUiop.gif
---

Hello Community! Here is a quick update on the various cloud images we have available as it's one of the top things we're asked about. The good news is we now have 150002657% more COW! That's right! We now have generic cloud images (cloud-init/qcow) available for your clouding adventures.

Your one stop shop for all cloud images, sources and scripts is https://github.com/AlmaLinux/cloud-images. We keep that pretty updated and there is a table right at the top with quick links to all of items listed below. Here's a quick summary of what we have and where, right now.

- **Generic Cloud Images (cloud-init):** One of the most highly requested. All generic cloud images are available in QCOW format on the mirrors and from the main repo: https://repo.almalinux.org/almalinux/8/cloud/x86_64/images/. **The username is "almalinux"**. We've done quite a bit of testing here to ensure that you have a great experience with this. We know that there lots of different cloud configs out there and we'd like to make sure we cover any possible edge cases. **So, if you are a hosting company and would like to help sponsor testing infrastructure for cloud-init images please reach out to us on the [AlmaLinux Community Chat](https://chat.almalinux.org/).**
- **LXC/LXD:** Our official LXC and LXD container images are now available as well for x86_64 and aarch64 as well. You can check out any of the public image servers (https://images.linuxcontainers.org) for more information. **Special shout out to community members Security Team Lead Justin Coffman (https://github.com/jcoffm) for the initial patch to Distrobuilder, the amazing Elkhan Mammadli (https://github.com/LKHN) as well for all his efforts, and to all the community members who helped out with testing.**
- **Official Docker Images:** You can find the official Docker image for AlmaLinux on [Docker Hub](https://hub.docker.com/_/almalinux). The kind folks over at docker were nice enough to save you a few keystrokes too, so just `docker pull almalinux` and you're good to go.
- **Quay.io:** If quay is your thing, we've got you covered. Check out https://quay.io/repository/almalinux/almalinux.
- **Vagrant:** Vagrant boxes are available with support for VirtualBox, VMWare, Hyper-V and Libvirt. Check out https://app.vagrantup.com/almalinux and `vagrant init almalinux/8` and `vagrant up` your way to some good times. **We're also looking for someone who would like to help implement a Parallels provider for Vagrant as well. If you'd like to help please reach out to us on the [AlmaLinux Community Chat](https://chat.almalinux.org/).**
- **AWS:** Thanks to our awesome Sponsors at [Amazon Web Services](https://aws.amazon.com/) we have both [AWS Marketplace](https://aws.amazon.com/marketplace/pp/B094C8ZZ8J) and [Community AMIs](https://wiki.almalinux.org/cloud/AWS.html) available. Check out that last link to the AWS page on our wiki for a listing of all Community AMI IDs for reach region. AARCH64/Graviton Images are coming soon as well, so bookmark that page and make sure you follow us for the latest updates.
- **Google Cloud:** Last but certainly not least, Google Cloud images are now available as well. All the info you need is right here: https://cloud.google.com/compute/docs/images#almalinux

## There's more to come. Join Us!

AlmaLinux is more than just software, there's a whole community of dedicated people making the magic happen. None of this would be possible without our AWESOME community. Join us on our [AlmaLinux Community Chat](https://chat.almalinux.org/), sponsored by our good friends at Mattermost, to get involved, ask for help or just meet fellow community members. Send us your Pull Requests on [GitHub](https://github.com/almalinux). Report any bugs that you might stumble upon on the [Bug Tracker](https://bugs.almalinux.org/). You can also ask a question on our [Cloud SIG Forum](https://almalinux.discourse.group/c/sigs/cloud-sig/10) or post something on our [AlmaLinux Community on Reddit](https://reddit.com/r/almalinux).