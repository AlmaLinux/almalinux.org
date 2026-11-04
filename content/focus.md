---
title: "AlmaLinux Focus Guide"
type: focus
images:
  - /images/og/focus.png
description: "Links to everything in the AlmaLinux Focus Guide from ADMIN and Linux New Media: download the guide, explore the AlmaLinux pages behind each article, and find out how to run and shape AlmaLinux."
---

<!--
  Target of the QR code on page 2 of the 2026 AlmaLinux Focus Guide ("Scan for links to everything in this guide").
  Article list and page numbers match the final PDF (AlmaLinux_Focus_Guide_2026.pdf).
  Images in static/landingpages/focus/ are fanned page spreads rendered from that PDF.
  The hero line and the chair's note come from our own ad on page 2. Don't reuse the guide's cover illustration as page art: it's licensed stock art (credited on page 3).
  Styles live in assets/scss/focus.scss.
-->

<div class="al-event-band al-focus-hero">
  <div class="row g-5 align-items-center">
    <div class="col-lg-7">
      <p class="al-focus-kicker">The AlmaLinux Focus Guide from ADMIN</p>
      <h1>Enterprise Linux, for and by the people who use it.</h1>
      <p class="al-focus-lead mb-3">Thanks for picking up the AlmaLinux Focus Guide from <a href="https://www.admin-it.io/">ADMIN IT Infrastructure &amp; Operations</a>, published by Linux New Media. This page collects the links from every article in the guide, so you can pick up wherever you left off.</p>
      <p class="al-focus-lead">If you don't have a copy yet, you can get it free from ADMIN with your email address.</p>
      <a href="https://mailchi.mp/admin-magazine.com/almalinux-focusguide" class="btn btn-lg px-4 al-cta-blue"><i class="bi bi-download" aria-hidden="true"></i> Get the Focus Guide</a>
    </div>
    <div class="col-lg-5">
      <img src="/landingpages/focus/cover.webp" alt="The cover of the 2026 AlmaLinux Focus Guide, with the table of contents and the AlmaLinux ad behind it" class="img-fluid" width="800" height="616" />
    </div>
  </div>
</div>

<h2 id="articles">What's in the guide</h2>

The articles themselves are in the guide. Each card below has a summary of one article, followed by links to the AlmaLinux projects, pages, and posts that article mentions.

<div class="row g-4 al-focus-articles">
  <div class="col-md-6" id="intro">
    <div class="al-focus-article">
      <img src="/landingpages/focus/intro.webp" width="800" height="803" alt="Introducing AlmaLinux article pages from the Focus Guide" class="img-fluid" loading="lazy" />
      <span class="al-focus-page-badge">Page 4 · A community-owned enterprise Linux solution</span>
      <h3>Introducing AlmaLinux</h3>
      <p>If you're new to AlmaLinux, start here. Amy Pettle tells the story of how AlmaLinux OS got going when CentOS Linux ended, and why CloudLinux handed it to the nonprofit AlmaLinux OS Foundation shortly after the first release. You'll also learn how our board gets elected under the 2026 bylaws, and where to download AlmaLinux OS 10, 9, or 8.</p>
      <div class="al-focus-related">
        <p class="al-focus-related-label">Related links</p>
        <ul>
          <li><a href="/get-almalinux/"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> Download AlmaLinux OS</a></li>
          <li><a href="/foundation/"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> The AlmaLinux OS Foundation</a></li>
          <li><a href="/blog/2026-06-10-new-bylaws-and-2026-election/"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> Our 2026 bylaws and election</a></li>
          <li><a href="/blog/2026-02-25-almalinux-2025-recap/"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> 2025 AlmaLinux year in review</a></li>
          <li><a href="https://chat.almalinux.org"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> AlmaLinux chat</a></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="col-md-6" id="rhel-compatibility">
    <div class="al-focus-article">
      <img src="/landingpages/focus/rhel-compatibility.webp" width="800" height="803" alt="Friendly Fork article pages from the Focus Guide" class="img-fluid" loading="lazy" />
      <span class="al-focus-page-badge">Page 6 · RHEL compatibility</span>
      <h3>Friendly Fork</h3>
      <p>In June 2023, Red Hat restricted access to RHEL source code, and we had to decide what AlmaLinux would be next. We picked application binary interface (ABI) compatibility over 1:1, and this article explains what that means and where our code comes from now. It also covers what we've been able to do since, like shipping some security fixes before RHEL does. Our 2023 interview with benny Vasquez about the decision is in there too.</p>
      <div class="al-focus-related">
        <p class="al-focus-related-label">Related links</p>
        <ul>
          <li><a href="/blog/future-of-almalinux/"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> Our 2023 announcement</a></li>
          <li><a href="/blog/new-repositories-for-almalinux-os-synergy-and-testing/"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> The Testing and Synergy repositories</a></li>
          <li><a href="https://www.youtube.com/watch?v=Jjda39dIu7I"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> benny's talk at All Things Open 2023</a></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="col-md-6" id="media-entertainment">
    <div class="al-focus-article">
      <img src="/landingpages/focus/media-entertainment.webp" width="800" height="803" alt="That's Entertainment article pages from the Focus Guide" class="img-fluid" loading="lazy" />
      <span class="al-focus-page-badge">Page 8 · The AlmaLinux M&amp;E SIG</span>
      <h3>That's Entertainment</h3>
      <p>For almost 20 years, Media &amp; Entertainment (M&amp;E) studios ran their pipelines on CentOS. When CentOS 7 reached end of life, they needed somewhere to go, and some of them came to us. People from NOX and SHED talk about why, including the glibc bug that caused problems for Houdini, which we fixed before RHEL did. The M&amp;E SIG that grew out of it is now building an M&amp;E ISO and a Creative Installer for smaller studios.</p>
      <div class="al-focus-related">
        <p class="al-focus-related-label">Related links</p>
        <ul>
          <li><a href="https://wiki.almalinux.org/sigs/MediaAndEntertainmentSIG.html"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> Join the M&amp;E SIG</a></li>
          <li><a href="/blog/2025-12-02-almalinux-media-entertainment-sig/"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> Announcing the M&amp;E SIG</a></li>
          <li><a href="https://kernelchief.github.io/almalinux-creative-installer/"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> AlmaLinux Creative Installer</a></li>
          <li><a href="/blog/2024-07-25-testing-glibc-needed/"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> Our call for glibc testers</a></li>
          <li><a href="/blog/2026-07-28-aldla-recap/"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> AlmaLinux Day: LA recap</a></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="col-md-6" id="new-in-10-2">
    <div class="al-focus-article">
      <img src="/landingpages/focus/new-in-10-2.webp" width="800" height="803" alt="Alternate Route article pages from the Focus Guide" class="img-fluid" loading="lazy" />
      <span class="al-focus-page-badge">Page 10 · New in AlmaLinux OS 10.2</span>
      <h3>Alternate Route</h3>
      <p>AlmaLinux OS 10.2 came out in May 2026 with a few things RHEL 10 doesn't have. There's an x86-64-v2 build (with EPEL packages) so older hardware keeps running, 32-bit i686 packages maintained by engineers from Arista and Meta, NVIDIA drivers that work with Secure Boot, and Btrfs. Many of these started as community proposals to the AlmaLinux Engineering Steering Committee (ALESCo), and a lot of them got their start in AlmaLinux OS Kitten.</p>
      <div class="al-focus-related">
        <p class="al-focus-related-label">Related links</p>
        <ul>
          <li><a href="/alesco/"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> ALESCo</a></li>
          <li><a href="/blog/2024-10-22-introducing-almalinux-os-kitten/"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> Introducing AlmaLinux OS Kitten</a></li>
          <li><a href="/blog/2026-03-09-almalinux-and-nvidia-streamline-driver-and-cuda-updates/"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> NVIDIA drivers on AlmaLinux</a></li>
          <li><a href="https://epel.repo.almalinux.org"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> EPEL for x86-64-v2</a></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="col-md-6" id="build-system">
    <div class="al-focus-article">
      <img src="/landingpages/focus/build-system.webp" width="800" height="616" alt="Package Packer article pages from the Focus Guide" class="img-fluid" loading="lazy" />
      <span class="al-focus-page-badge">Page 12 · The AlmaLinux Build System</span>
      <h3>Package Packer</h3>
      <p>Why build your own build system when Koji exists? Joe Casad asked our developers, and then he shows how the pieces fit together, from the Master Service and Pulp to the AlmaLinux Test System (ALTS). Every package gets signed and gets its own Software Bill of Materials (SBOM). The whole thing is free software, so you can point it at your own packages too.</p>
      <div class="al-focus-related">
        <p class="al-focus-related-label">Related links</p>
        <ul>
          <li><a href="https://build.almalinux.org/"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> AlmaLinux Build System</a></li>
          <li><a href="https://github.com/AlmaLinux/build-system"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> Build System source on GitHub</a></li>
          <li><a href="https://github.com/AlmaLinux/alts"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> AlmaLinux Test System</a></li>
          <li><a href="https://github.com/AlmaLinux/alma-sbom"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> The alma-sbom utility</a></li>
          <li><a href="/blog/introducing-albs-the-almalinux-build-system/"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> How the Build System started</a></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="col-md-6" id="elevate">
    <div class="al-focus-article">
      <img src="/landingpages/focus/elevate.webp" width="800" height="616" alt="ELevate to the Future article pages from the Focus Guide" class="img-fluid" loading="lazy" />
      <span class="al-focus-page-badge">Page 16 · The ELevate migration tool</span>
      <h3>ELevate to the Future</h3>
      <p>Still have a CentOS 7 server around? Rubén Llorente upgraded one to AlmaLinux 8 with ELevate and wrote down every step, including the pre-upgrade check that will probably fail the first time (that's expected) and how to get past it. Once you're on 8, ELevate can take you to 9 and then 10.</p>
      <div class="al-focus-related">
        <p class="al-focus-related-label">Related links</p>
        <ul>
          <li><a href="/elevate/"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> About ELevate</a></li>
          <li><a href="https://wiki.almalinux.org/elevate/ELevate-quickstart-guide.html"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> ELevate quickstart guide</a></li>
          <li><a href="https://wiki.almalinux.org/elevate/ELevating-CentOS7-to-AlmaLinux-10.html"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> Step-by-step: CentOS 7 to AlmaLinux</a></li>
          <li><a href="https://wiki.almalinux.org/elevate/ELevate-frequent-issues.html"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> ELevate frequent issues</a></li>
          <li><a href="https://wiki.almalinux.org/elevate/Contribution-guide.html"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> Contribute to ELevate</a></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="col-12" id="interview">
    <div class="al-focus-article al-focus-article--wide">
      <div class="row g-4 align-items-center">
        <div class="col-md-4">
          <img src="/landingpages/focus/interview.webp" width="800" height="616" alt="Freedom Fighter interview pages from the Focus Guide" class="img-fluid" loading="lazy" />
        </div>
        <div class="col-md-8">
          <span class="al-focus-page-badge">Page 20 · An interview with AlmaLinux OS</span>
          <h3>Freedom Fighter</h3>
          <p>benny Vasquez (Chair of the AlmaLinux OS Foundation) and Andrew Lukoshko (AlmaLinux OS Lead Architect) talked with Amy Pettle about where AlmaLinux came from and where it's going. They get into why a nonprofit owns AlmaLinux, how we decide when to differ from RHEL, and how we test with openQA and Testinfra. Andrew also tells the story of a storage controller fix we carried in our kernel until RHEL included it.</p>
          <div class="al-focus-related">
            <p class="al-focus-related-label">Related links</p>
            <ul>
              <li><a href="/contribute/"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> Find your spot to contribute</a></li>
              <li><a href="https://github.com/AlmaLinux/ALESCo"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> The ALESCo request process</a></li>
              <li><a href="/blog/2026-10-14-what-should-almalinux-do-next/"><i class="bi bi-arrow-right-short" aria-hidden="true"></i> Tell us what we should do next</a></li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="al-event-band" id="community">
  <h2>The community behind AlmaLinux</h2>
  <!--
    Checked November 2, 2026. To refresh:
    mirrors: count the rows at https://mirrors.almalinux.org/ (380 then), shown rounded down;
    sponsor members: count the logos in layouts/partials/common/foundation-members.html (29 then);
    SIGs: count the SIG pages linked from https://wiki.almalinux.org/sigs/ (9 then, not counting the page on creating a SIG).
  -->
  <div class="row g-4 al-focus-stats">
    <div class="col-md-4">
      <a href="https://mirrors.almalinux.org/" class="al-focus-stat al-focus-stat--blue"><b>375+</b><span>Mirrors around the world, hosted by our community</span></a>
    </div>
    <div class="col-md-4">
      <a href="/members/" class="al-focus-stat al-focus-stat--green"><b>29</b><span>Sponsor members who fund AlmaLinux</span></a>
    </div>
    <div class="col-md-4">
      <a href="https://wiki.almalinux.org/sigs/" class="al-focus-stat al-focus-stat--yellow"><b>9</b><span>Special interest groups (SIGs) you can join</span></a>
    </div>
  </div>
</div>

<div class="row g-4 al-focus-actions" id="run-it">
  <div class="col-md-6">
    <div class="al-focus-article">
      <div class="al-focus-card-media al-focus-card-media--contain">
        <img src="/images/elevate.svg" width="1001" height="342" alt="The upgrade and migration paths ELevate supports" loading="lazy" />
      </div>
      <h3><i class="bi bi-play-circle" aria-hidden="true"></i> Run it</h3>
      <p>AlmaLinux OS is free to download and use. If you already run an Enterprise Linux system, <a href="/elevate/">ELevate</a> can upgrade it in place.</p>
      <a href="/get-almalinux/" class="btn px-4 al-cta-blue"><i class="bi bi-download" aria-hidden="true"></i> Get AlmaLinux</a>
    </div>
  </div>
  <div class="col-md-6" id="shape-it">
    <div class="al-focus-article">
      <div class="al-focus-card-media">
        <img src="/membership-images/ald-tokyo-2026.jpg" width="1024" height="683" alt="AlmaLinux community group photo at AlmaLinux Day: Tokyo" loading="lazy" />
      </div>
      <h3><i class="bi bi-people" aria-hidden="true"></i> Shape it</h3>
      <p>If you use AlmaLinux, you can join the AlmaLinux OS Foundation for free and vote for the board that guides the project. You can also come say hi in our <a href="https://chat.almalinux.org">chat</a> and on our <a href="https://forums.almalinux.org">forums</a>, or join a <a href="https://wiki.almalinux.org/sigs/">SIG</a>.</p>
      <a href="/members/#individual" class="btn px-4 al-cta-blue"><i class="bi bi-person-badge" aria-hidden="true"></i> Become a Member</a>
    </div>
  </div>
</div>

<h2 id="note">A note from our chair</h2>

<!-- The first paragraph is benny's note from page 2 of the guide, word for word. -->
<figure class="al-focus-note">
  <img src="/board/benny.jpg" width="250" height="250" alt="benny Vasquez" class="al-event-headshot" loading="lazy" />
  <div>
    <blockquote>
      <p>Thank you for picking up this guide. The projects in it, including AlmaLinux OS Kitten, ELevate, and our special interest groups (SIGs), exist because people who use AlmaLinux told us what they needed and then helped build it. I hope you find something here that's useful to you. When you do, I'd love for you to come tell us about it and help decide what we build next.</p>
      <p>This guide exists because of the team at Linux New Media, especially Brian Osborn, Lori White, and the authors and editors who wrote and updated every article. Thank you for telling our community's story so carefully. AlmaLinux is made possible by our <a href="/members/">sponsor members</a>, and by everyone who uses AlmaLinux and helps build it.</p>
      <p>Have a question about anything in the guide? Email us at <a href="mailto:hello@almalinux.org">hello@almalinux.org</a>, and we'll get back to you.</p>
    </blockquote>
    <figcaption><strong>benny Vasquez</strong>, Chair, AlmaLinux OS Foundation</figcaption>
  </div>
</figure>
