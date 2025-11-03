---
title: "1 Million Docker pulls and more container updates"
type: blog
author:
  name: "Jack Aboutboul"
  bio: "-"
  image: /users/jack.jpg
date: "2022-03-15"
post:
  title: "A mythical distribution with no upstream equivalent. Why did we do it? Because we can!"
  image: /blog-images/Screen_Shot_2022-03-08_at_10.47.39.png
---

Wouldya take a look at that? A million! A million pulls of our [Docker Library Official Image](https://hub.docker.com/_/almalinux). What a huge milestone, WOW! We're seriously humbled and we'd like to thank the community, for all the contribution and support. AlmaLinux keeps getting better each day thanks to the efforts of our amazing community.

We've also officially release containers for ppc64le available on all the major registries and we've also gone ahead and updated our containers to 8.5.4 and patched against the latest security updates where applicable. 18 packages have been updated and you can [see that work here](https://github.com/docker-library/official-images/pull/12003).

Community members are also doing great work to further streamline our container development process. We're working on using a single working branch to support all the different arch images for each release, instead of a separate branch for each arch. This will greatly help with automation and cut down on development and release times. This will also allow us to maintain repeatable builds and the community to track build history better. This approach will also finally setup staging/weekly/monthly builds so that we can more frequently push out images when there are critical updates.

Finally, we really need to shout out our awesome community members [Bala](https://github.com/srbala) and [LKHN](https://github.com/LKHN) for all their amazing work. All this was made possible by their efforts.

You too can be a container hero like Bala and LKHN. Join the AlmaLinux team. If you're looking for more information and details on containers, join our [Containers and Cloud SIG](https://chat.almalinux.org/almalinux/channels/sigcloud) on the AlmaLinux Community Chat. We're waiting for you.
