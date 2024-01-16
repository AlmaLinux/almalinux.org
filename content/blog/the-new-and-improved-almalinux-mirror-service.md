---
title: "The New and Improved AlmaLinux Mirror Service"
type: blog
author: 
 name: "Jack Aboutboul"
 bio: "-"
 image: /users/jack.jpg
date: '2021-08-04'
post:
    title: "Announcing our new and improved mirror service—making things faster for you."
    image: 
---

Great news about our mirror service! Our mirror service is what powers distribution of ISOs, packages and updates across the world. A while ago we developed and started testing a new geolocation-based mirror service which helps you get software faster and easier based on where in the world you are and what the closest source is. Thanks to all those who were involved in testing--It’s now official: our new mirror service is coming online on August 4th at 7.00 UTC.

A full list of AlmaLinux mirrors can be found at it’s usual location: https://mirrors.almalinux.org. Once released, the mirror service sources and configuration can be found in GitHub repo: http://github.com/AlmaLinux/mirrors/tree/mirrors_service .

We are extremely grateful for the community’s efforts to help make AlmaLinux better and the participation on the [AlmaLinux Community Chat](https://chat.almalinux.org/) and the [AlmaLinux Forums](https://forums.almalinux.org/). This would not be possible without you, your contributions and feedback. 

Also, we would like to give a HUGE thanks to our sponsors [AWS](https://aws.amazon.com/) for hosting our mirror service and [HiVelocity](https://hivelocity.com/) for their support of our mirror service.

For all of you who are interested in details about how things work we couldn’t resist getting you some technical details on how our mirror service works.

The mirror service uses the IP of an incoming request for detecting a country, a region, an [ASN](https://en.wikipedia.org/wiki/Autonomous_system_(Internet)) and a subnet. If you’re using anything like Tor, a proxy or VPN then you can expect it to use your current masked IP and not the actual IP at your physical location.

For detecting ASN and location by IP we’re using the GeoIP/ASN databases from https://www.maxmind.com. The mirror service returns all suitable mirrors by ASN/subnets:

- First of all, if a mirror’s ASN is the same as the IP of request, it will be added to the list. If the IP of request gets to at least one of the mirror’s subnets, it will be also added to the list.
- The initial list returned to the client will contain at least five mirrors. Any additional mirrors will be the nearest by geo data.
- As a fallback, the mirror service returns the full list of mirrors if it can't detect your location by IP.

In the case when it’s not possible to find mirrors by ASN/subnets, the list will be formed by these methods: 

- The ten mirrors which are nearest to you inside your country (e.g. inside the UK) will be included.
- The ten mirrors nearest to you inside your region (e.g. Europe) will be added. This list won’t include the previous list.
- The length of each list can be less than ten, because your country/region may not contain the required amount of mirrors. In that case, the ten mirrors nearest to you outside of your region and country will be added.
- The final list will be cut to the first ten elements and will be returned to you.

We hope that you find this useful and that this improves your overall experience. In the testing that was carried out so far, the new mirror seemed to work pretty well and improved download and update speeds. Be sure to let us know what you think on [Reddit](https://reddit.com/r/AlmaLinux), [Twitter](https://twitter.com/almalinux) or on the [Forums](https://almalinux.discourse.group/c/operations/infrastructure/15).