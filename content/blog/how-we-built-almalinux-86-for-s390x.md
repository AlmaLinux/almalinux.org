---
title: "How We Built AlmaLinux 8.6 for s390x"
type: blog
author:
  name: "Jack Aboutboul"
  bio: "-"
  image: /users/jack.jpg
date: "2022-11-07"
post:
  title: "A Legendary Release for a Legendary Platform. It was a lot of work, but someone had to do it!"
  image: /blog-images/Mainframe_Post_Cover.png
---

The AlmaLinux OS Foundation [announced support for the IBM z (s390x) platform](https://www.hpcwire.com/off-the-wire/almalinux-foundation-builds-almalinux-os-8-for-s390x/) thanks to a collaboration with Gold Partner, Sine Nomine Associates (SNA).

The Almalinux OS Foundation continues a long history of Linux and open source software support on mainframes, which was kickstarted at the end of the last century. In this blog, we wanted to highlight some of SNA’s involvement as we open a new chapter for Linux on the mainframe.

Back in 2000, SNA was winning awards at key industry conferences for evangelizing Linux on the IBM mainframe environment, since then it has continued supporting Linux and open source software. The engineering firm has worked tirelessly to bring open source to the platform and recently worked with IBM and Microsoft to bring .NET 6 to IBM z https://community.ibm.com/community/user/ibmz-and-linuxone/blogs/elizabeth-k-joseph1/2021/11/10/net-6-comes-to-ibm-z-and-linuxone.

SNA also created its first Linux distribution for mainframes in 2012. Their distribution was based on CentOS 6.2 and, for trademark reasons, called ClefOS. In the early days, the hardware investment was significant. They had to use a server farm of PCs running a mainframe emulator called Hercules, on which Linux ran to build ClefOS. “It worked,” says Neale Ferguson, Chief Scientist at SNA, “but it was slow and took six weeks to create a new distribution when a new CentOS release came out.”

The process was reduced by several orders of magnitude because of IBM z resources made available as part of the Linux Community system based at [Marist College](https://www.marist.edu/), which provides ongoing support. In fact, as Linux on mainframe sees a new chapter with AlmaLinux, SNA would like to express its gratitude to the Open Mainframe project and the resources that the Marist College, Poughkeepsie, NY, has generously provided to projects for many decades.

Since SNA wasn’t in a position to bootstrap a distribution itself when it came time to find an alternative to CentOS. AlmaLinux “was the most aligned with the open source philosophy,” says Ferguson, and the approach has been a collaborative effort from the start, sharing knowledge and resources.

But what’s involved in bootstrapping the AlmaLinux distribution for a completely different architecture? Ferguson says it involves building a “starter kit” for your first chroot test environment. The process involves digging out appropriate packages (RPMs) in the x86_64 distribution that need to be added, excluding those that aren’t, such as those relating to BIOS and other firmware, and modifying others that would be useful for z. Fortunately, the number of RPMs that need attention is small: “We have around 14,000 binary RPMs built and there’s around 10 to 15 RPMs that need any intervention to build in the environment,” says Ferguson.

For example, SNA found that FreeType, the library used for rendering fonts, didn’t build on z. Ferguson discovered that GNU Binutils had a new program called windres for manipulating Windows resources: “Creating Windows resources on z didn’t make much sense, so we had to add some code into the build to ignore it,” says Ferguson. SNA found small issues like this but Ferguson says “99 percent of the time, you can build straight from packages.”

Essentially, the main challenge has been inferring what settings there are for certain RPMs. This inference has an element of trial and error, discovering what is and isn’t needed in a package, for instance, you may need to pre-install packages before building an RPM or you may build an RPM and discover other dependent packages are needed. “But you’ll find there’s a switch that can be utilized to remove the dependency,” says Fergusom. But in the scheme of thousands of RPMs the number of problematic ones account for a small number

Compiling AlmaLinux 9 for z was also made easier to bootstrap as there is a CentOS 9 Stream available for z. However, AlmaLinux 8 was more complicated. As there was no CentOS 8 for z, it meant using Fedora 28 and building a chroot tarball in Mock for the test chroot environment.

For AlmaLinux 8, Ferguson says they have had to build on top of Fedora They had to replace the required packages (RPMs) in the tarball with AlmaLinux RPMs and assets from the Git repositories for a bootstrapping environment for AlmaLinux.

SNA uses a three-pass approach to building a new distribution: “Build once, build a second time using what you’ve just built and build a third time based on what you built the second time around,” Ferguson explains. “By the time you reach the third build, it's pristine; there are no artifacts from anything except your AlmaLinux environment.” And future releases will only get easier. “The first build is always the hardest,” admits Ferguson

Looking to the future, Ferguson says they have ten builders, previously used for ClefOs, that can be put to work. The team is looking at the project’s build node code to see if it could act as a proxy to farm out builds to other builders: “We were building a ClefOS distribution within two or three days, once everything was automated, and that includes building every package three times,” and Ferguson says they’d like to match the success the main distribution has had with the speed of their releases.

“We want to ensure that this version of Almalinux looks like any other endpoint you want to use and behaves like all the others that AlmaLinux offers to the community,” says Ferguson. The goal is for users to be able to simply select it from the build factory and be able to use the AlmaLinux mirrors to make it easy for users to download the latest mainframe edition.

If you’d like to learn more, join the conversation on the [Almalinux Mattermost server](https://chat.almalinux.org/).
