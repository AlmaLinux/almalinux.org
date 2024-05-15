---
title: "Minimal Container Images now Available on Docker Hub and Quay.io"
type: blog
author: 
 name: "Jack Aboutboul"
 bio: "-"
 image: /users/jack.jpg
date: '2021-06-28'
post:
    title: "We've had a number of requests for minimal container images and we are glad to announce that those are now available on Docker Hub and Quay.io!"
    image: 
---

Hello All,

We've had a number of requests for minimal container images and we are glad to announce that those are now available on:

- Docker Hub: https://hub.docker.com/_/almalinux
- Quay.io: https://quay.io/repository/almalinux/almalinux

**Minimal Image**

The minimal image is a stripped-down image that uses the microdnf package manager and contains a very limited package set. It is designed for applications that come with their own dependencies bundled (e.g. NodeJS, Python). The almalinux:minimal tag always points to the most recent version of the minimal image. Tags for major (e.g. almalinux:8-minimal) and minor (e.g. almalinux:8.4-minimal) releases are also available.

**Platform Image**

The default (platform) image is a general-purpose image with a full DNF stack and basic tools like find, tar, vi, etc. The almalinux:latest tag will always point to the latest stable release of the default image. Major releases and minor releases are also tagged with their version (e.g. almalinux:8 or almalinux:8.4).

The AlmaLinux community would like to personally thank community contributor [Bala Raman](https://github.com/srbala) for of his hard work and dedication to the Cloud and Containers SIG. If containers are your thing and you'd like to contribute, please join us on [AlmaLinux Community Chat](https://chat.almalinux.org/almalinux/channels/sigcloud) or on our [Containers](https://forums.almalinux.org/c/sigs/containers/23) forum.
