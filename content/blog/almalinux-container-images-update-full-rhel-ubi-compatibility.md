---
title: "AlmaLinux Container Images Update - Full RHEL UBI Compatibility!"
type: blog
author: 
 name: "Jack Aboutboul"
 bio: "-"
 image: /users/jack.jpg
date: '2021-09-23'
post:
    title: "A Full Set of UBI Compatible Containers, Updates, New Registries and More."
    image: 
---

Hello, Community, container and DevOps fans everywhere. Our [Cloud and Containers SIG](https://wiki.almalinux.org/sigs/Cloud.html) have been hard at work lately on a little bit of a project for you. Today we have some news to share about some container updates, new images, new registries and distribution so stick with us for all the info. Now, it's time to announce some goodness!

FYI: All container images are available for both the x86_64 and arm64/v8 architectures too!

## Full UBI Compatible Container Set

We are thrilled to announce that as of today, [AlmaLinux now provides fully compatible alternatives](https://wiki.almalinux.org/containers/docker-images.html) for Red Hat Universal Base Images (UBI)! What are UBI you may ask? UBI are meant to be OCI-compliant container base operating system images with complementary runtime languages and packages included. Prior to UBI, developers would need to package their containerized app depending on the deployment target--this essentially made those containers not really all that portable. UBIs allow you to essentially have a standard, repeatable build and deployment for your code and application, regardless of deployment target.

Our new UBI compatible images come in four variants: Minimal, Base, Micro, and Init. Here is a quick summary of what they offer:

*FYI*: Our *Default* container image isn’t going away! It’s been updated. Read more below!

[**Minimal**](https://wiki.almalinux.org/containers/docker-images.html#almalinux-minimal): A minimal, compacted image that contains a limited package set and uses the microdnf package manager as a replacement for DNF. A minimal DNF uses libdnf and therefore doesn't require Python. This image is 52% smaller in size (37MB download, 102MB expanded). It is designed for applications that come with their dependencies bundled like GO, NodeJS, Java.

Container image tag for Minimal (Platform): `almalinux:minimal`

Container image tag for Minimal (UBI alternative): `almalinux/8-minimal`

[**Base**](https://wiki.almalinux.org/containers/docker-images.html#almalinux-base): An image designed to be a base for your containerized applications, middleware and utilities. The Base image includes some helpful OS tools like find, tar, vi, etc., and a full DNF stack. The systemd initialization system and access to free dnf repositories are fully available.

Container image tag: `almalinux/8-base`

[**Micro**](https://wiki.almalinux.org/containers/docker-images.html#almalinux-micro): An even more minimized image. It is distributed without any package manager. The Micro image uses the package manager on the underlying host to install packages, typically using Buildah or Multi-stage builds with Podman. The Micro image is 82% smaller than the Base image and 68% smaller than the Minimal image. Since this image has only very few packages, it is more secure compared to other images.

Container image tag: `almalinux/8-micro`

[**Init**](https://wiki.almalinux.org/containers/docker-images.html#almalinux-init): For running multiple applications with an init system. As a default, systemd is enabled for use.

Container image tag: `almalinux/8-init`

## Container Security/Package Updates, New Registries and Distribution

In addition to all of the above, two of our images are available as [Official Docker Hub](https://hub.docker.com/_/almalinux) images: **Default** and **Minimal**. Both of those have now been updated with the latest security fixes and package updates.

[**Default**](https://wiki.almalinux.org/containers/docker-images.html#almalinux-default-platform): Is a general purpose (platform) container image that contains default packages and can be used as a drop-in replacement for the CentOS 8 image.

Container image tag: `almalinux:latest`

[**Minimal**](https://wiki.almalinux.org/containers/docker-images.html#almalinux-minimal): A minimal, compacted image that contains a limited package set and uses the microdnf package manager as a replacement for DNF. A minimal DNF uses libdnf and therefore doesn't require Python. This image is 52% smaller in size (37MB download, 102MB expanded). It is designed for applications that come with their dependencies bundled like GO, NodeJS, Java.

Container image tag for Minimal (Platform): `almalinux:minimal`

Container image tag for Minimal (UBI alternative): `almalinux/8-minimal`

All images are available at AlmaLinux's [Docker Hub](https://hub.docker.com/_/almalinux) and [quay.io](https://quay.io/repository/almalinux/almalinux).

We'd also like to welcome AWS' [ECR Container Registry](https://gallery.ecr.aws/?searchTerm=almalinux) Service. All AlmaLinux images will be published there as well in the future. If you're running container-based workloads on [AWS](https://aws.amazon.com/) on either ECS, EKS or anywhere else really, AlmaLinux containers are now available to you locally on AWS.

AlmaLinux would like to thank AWS for their gracious sponsorship of the AlmaLinux Foundation.

Stay tuned for more information about additional container registries and application specific images like Java JDK, NodeJS and more.

If you'd like to read more about AlmaLinux container images, you can check out the containers section of the [AlmaLinux Wiki](https://wiki.almalinux.org/containers/docker-images.html). There you can find helpful information, details about each container, container tags and links for the repositories for each image.

Containers are a lightweight version of the OS with an essential base for you to build upon. AlmaLinux container images are a good method to build a containerized application and push it to the registry server to share and collaborate with others. Containers also provide some additional advantages for users like high reliability, security, and performance.

## Call for Contributors

Are you a DevOps DOer? Are containers your A-game? Do you live in k8s? Wanna have a lot of fun building more containers, kubernetes operators and a whole lot more? Our [Cloud and Container](https://chat.almalinux.org/almalinux/channels/sigvirtcontainer) SIG is looking for YOU! Join Us by clicking the link above!

## Thanks!

As always, we’d like to thank our incredible Community for their contributions, questions and comments on these issues. We’d especially like to shout out immortal community heroes [Bala Raman](https://github.com/srbala) and [Elkhan Mammadli](https://github.com/LKHN) for all their efforts.

Your feedback and bug reports are so valuable to making AlmaLinux better. Please join us on the [AlmaLinux Community Chat](https://chat.almalinux.org/) and the [AlmaLinux Community Forums](https://forums.almalinux.org/) for any help and assistance or to discuss anything announced here. You can also follow us on [Twitter](https://twitter.com/almalinux) and [Reddit](https://reddit.com/r/AlmaLinux).