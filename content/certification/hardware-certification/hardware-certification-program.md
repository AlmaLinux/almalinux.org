---
title: "AlmaLinux Certification SIG's Hardware Certification Program"
type: p
---

###### last updated - Sept 8th, 2024

### Abstract

The AlmaLinux OS Foundation (ALOSF) Hardware Certification Program, managed by the [AlmaLinux Certification SIG](https://wiki.almalinux.org/sigs/Certification.html), aims to establish a streamlined, collaborative framework for Independent Hardware Vendors (IHVs) and ALOSF to certify hardware compatibility with AlmaLinux OS. The program leverages an open-source certification toolkit developed and curated by ALOSF, which is built upon various open-source hardware and software testing projects and tools. This toolkit is tailored for the purpose of hardware certification with AlmaLinux OS. The program presents two easy-to-use certification variants, facilitated either by IHVs or ALOSF, to accommodate the global support threshold challenges and foster a broader adoption of AlmaLinux OS. The Certification SIG (Special Interest Group) invites interested parties to partake in shaping the certification standards and procedures, ensuring a transparent, community-driven approach towards global hardware certification.

The SIG invites experts, IHVs, and community members to participate in shaping the certification standards and procedures. Interested parties can join by participating in a meeting, or joining the SIG's chat room. Details for both can be found in the [wiki](https://wiki.almalinux.org/sigs/Certification.html).

<div class="d-grid d-md-flex justify-content-md-start">
   <a class="btn al-cta-blue" href="/certification/ecosystem-catalog/"><i class="bi bi-check-all"> </i>See Currently Certified Hardware</a>  <a class="btn al-cta-green" href="https://forms.gle/wuCSDisQwR5nFz3d8"><i class="bi bi-people-fill"></i> Get Certified</a>
</div>
<div>
	<p>Once you review the below, if you have feedback or ideas to improve the AlmaLinux Certification Program, we'd love to hear from you!</p>
<a class="btn al-cta-yellow" href="https://wiki.almalinux.org/sigs/Certification.html"><i class="bi bi-people-fill"></i> Get involved</a>
</div>

## Table of Contents

- [Introduction](#uintroductionu)
  - [Background](#background)
  - [Scope](#scope)
- [Objectives and benefits](#uobjectives-and-benefitsu)
- [Certification types](#ucertification-typesu)
- [Collaboration Spaces and Tools](#ucollaboration-spaces-and-toolsu)
- [Certification Process](#ucertification-processu)
  - [Initiating the process](#initiating-the-process)
  - [Pre-certification](#pre-certification)
  - [Certification Testing](#certification-testing)
  - [Post-Certification](#post-certification)
  - [Certification Locations](#certification-locations)
- [Certification Testing Areas](#ucertification-testing-areasu)
- [Certification Lifecycle](#ucertification-lifecycleu)
- [Contribute to testing: “Community Validated”](#ucontribute-to-testing-community-validatedu)
- [Appendix: Glossary of terms](#uappendix-glossary-of-termsu)

## <u>Introduction</u>

### Background

The AlmaLinux OS Foundation (ALOSF) is committed to delivering an open source, community-owned and governed, forever-free enterprise Linux distribution that is focused on long-term stability and production-grade robustness. In alignment with these objectives, the Hardware Certification Program is engineered to rigorously test and certify hardware for seamless compatibility and optimal performance with AlmaLinux OS.

### Scope

This document outlines the certification process, objectives, testing areas, and collaboration mechanisms. It aims to serve as a comprehensive guide for Independent Hardware Vendors (IHVs) and other stakeholders interested in hardware certification for AlmaLinux OS. If there are any questions about this process or document, the best place to ask is in the [~SIG/Certification](https://chat.almalinux.org/almalinux/channels/sigcertification) room on [chat.almalinux.org](http://chat.almalinux.org).

## <u>Objectives and benefits</u>

Hardware certification for IHVs provides a verified, trusted foundation for enterprise deployments, ensuring optimal compatibility and performance while accelerating market adoption of both hardware and AlmaLinux OS. To achieve this, the program aims to:

1.  Establish a streamlined, collaborative framework for hardware certification.
1.  Leverage open-source certification toolkits for transparent and robust testing.
1.  Encourage community participation through the Special Interest Group (SIG).
1.  Provide two certification types to accommodate support threshold challenges

While hardware certification has challenges both for IHVs and for AlmaLinux, the benefits to the AlmaLinux community far outweigh the work that will be put in.

- Ensuring Workload Compatibility: Verifies hardware meets workload needs.
- Promoting Interoperability: Encourages best practices for wide-ranging compatibility.
- Maximizing Test Efficiency: Utilizes a holistic, needs-based approach to optimize resources.
- Offering Free Resources: Including a no-cost certification suite & support improves the ecosystem overall.

## <u>Certification types</u>

Achieving widespread, global support for hardware compatibility with AlmaLinux OS presents a complex array of challenges, including but not limited to regional standards, legal frameworks, and varying hardware configurations. To navigate these challenges and lower the barriers to entry for IHVs, the Hardware Certification Program offers three certification types:

1.  **IHV-Facilitated Certification:** The certification is conducted by the IHVs themselves, adhering to guidelines and testing procedures provided by ALOSF. This option offers greater flexibility for IHVs who have the necessary resources to conduct tests in-house. It is especially preferred when the vendor needs to account for specific local requirements, legal considerations, or a variety of hardware configurations. This type of certification will be identified as "Certified" in the AlmaLinux ecosystem catalog.
1.  **ALOSF-Facilitated Certification:** The testing is conducted by ALOSF, with or without significant participation from the IHV, to ensure an accurate representation of the hardware's capabilities. This type of certification will be identified as "Certified" in the AlmaLinux ecosystem catalog.
1.  **Community-Facilitated Certification without IHV Support:** Hardware certified solely by ALOSF without active IHV participation. This type of certification will be identified as "Community Validated" in the AlmaLinux ecosystem catalog.  

Each of these certification types is designed to accommodate the diverse needs and resources of IHVs, thereby aiding in the broader adoption and support of AlmaLinux OS on a global scale.

## <u>Collaboration Spaces and Tools</u>

The majority of this work is done in an asynchronous manner, so we rely on a collection of tools and applications to manage the workload at any given point.

GitHub Board & Repositories, and other: 

- [AlmaLinux/Certifications](https://github.com/AlmaLinux/certifications)
  - This repo is the primary point of contact for the SIG, acts as the holder of certification results, and is the location for certification requests that are not initiated by the foundation or the IHV. It is also the source for the Hardware Certification Program documentation.
- [AlmaLinux/Hardware-Certification-Suite](https://github.com/AlmaLinux/Hardware-Certification-Suite)
  - This repo houses the certification suite itself, and documentation, issues tracking, and related code snippets.
- [Certification SIG Board](https://github.com/orgs/AlmaLinux/projects/6)
  - This board provides an asynchronous method of communication, allowing for more flexible timelines, especially for international participants. Additionally, the GitHub platform serves as a mechanism for organizations to collaborate with the SIG on making certification requests from Independent Software Vendors (ISVs) and Independent Hardware Vendors (IHVs).
- [Mattermost chat - SIGs/Certifcation](https://chat.almalinux.org/almalinux/channels/sigcertification)
  - This acts as the primary way for the community to engage with each other (including the SIG members) for work on certifications or the certification suite. The most collaborative place for the SIG is this chat room. This room is also bridged to matrix on [#sig-certification:almalinux.im](https://app.almalinux.im/#/room/#sig-certification:almalinux.im)
- Private certification mailing list
  - The ([certification-sig\@lists.almalinux.org](mailto:certification-sig@lists.almalinux.org?subject=updateme)) mailing list acts as a private place for the Certification SIG to communicate with IHVs and ISVs. If you require your interaction with the SIG to be private (for example, if you are working with the SIG under NDA), you may reach out here.

## <u>Certification Process</u>

The certification process is intentionally simple.

{{< figure src="/images/certificationimages/certificationprocess.svg" link="/images/certificationimages/certificationprocess.svg" caption="The Hardware Certification Process" width="40%">}}

### Initiating the process

For IHVs, initiating the process is as simple as filling out this [google form](https://forms.gle/wuCSDisQwR5nFz3d8). If you have questions that you would like answered ahead of time, reaching out via one of the methods detailed in the [Collaboration Tools](#ucollaboration-spaces-and-toolsu) section is best.

<div class="d-grid d-md-flex justify-content-md-start">
<a class="btn al-cta-green" href="https://forms.gle/wuCSDisQwR5nFz3d8"><i class="bi bi-people-fill"></i> Get Certified</a>
</div>

We strongly recommend you join the [Mattermost chat - SIGs/Certifcation](https://chat.almalinux.org/almalinux/channels/sigcertification), if you have not already done so, after submitting your form to help facilitate collaboration throughout the process and engagement with the community.

### Pre-certification

Before starting the certification testing phase, some preliminary steps will be taken to ensure that the hardware and related documentation are prepared correctly. The pre-certification process might include any or all of the following:

1.  Initial Review: After the request is submitted, the SIG will confirm that the request is valid and can be acted on. For example:
    1.  Does the hardware in question have architecture support in AlmaLinux?
    1.  Does the accompanying documentation match what was submitted for certification?
1.  Hardware housing: If hardware is to be shipped to ALOSF, the SIG will reach out to facilitate that.
1.  Test Environment Prep: For IHVs submitting their own test results, ALOSF may also want to perform a validation of the testing environment based on the submitted test logs, ensuring it meets the requirements.
1.  Timeline and Milestones: A tentative timeline, along with key milestones for the certification process, is shared with the IHV.
1.  Legal Agreements: Any necessary legal agreements, such as Non-Disclosure Agreements (NDAs) or Memorandums of Understanding (MOUs), are finalized.

Completion of the pre-certification phase ensures that both the IHV and ALOSF have a clear understanding of the steps involved in the certification process, what to expect, and how to proceed.

### Certification Testing

Testing, whether done by the Certification SIG or by the IHV, will look largely the same. The host is prepared, and then the tests are run. Running the tests can take between 2 and 5 days, depending on the resources of the device. The image below provides slightly more detail.

The SIG will provide ad-hoc support for IHV-facilitated certification testing including helping the IHV as they implement any IHV-specific tests (if desired or required), and can help diagnose any problems that come up within the certification process.

Note: ALOSF Platinum Sponsor Member, Tuxcare, has offered 2 years of free technical support for IHVs who certify at least 2 pieces of hardware. If the IHV also joins the foundation as a sponsor member, Tuxcare will extend that support window to 5 years.

{{< figure src="/images/certificationimages/certificationtestingprocess.svg" link="/images/certificationimages/certificationtestingprocess.svg" caption="Hardware Certification Testing Process" width="30%">}}

### Post Certification

Once the certification has been completed successfully, the results and certification status will be listed on the AlmaLinux website (almalinux.org), and the IHV will be asked to list AlmaLinux as a supported operating system for the hardware that was tested.

If the IHV joins the foundation as a member, then the Marketing SIG will work with the IHV on the publicity around the certification and joining the foundation. 

### Certification Locations

If the IHV is not able to provide hosting for the hardware that is being tested, the ALOSF will provide three certification locations:

- EU -- Poland, @Atman data center - staffed by CloudLinux
- Asia -- TBD
- USA -- Various, based on need and timing

If the hardware being tested is also being donated to the ALOSF, then it will need to be sent to the USA location in Atlanta for hosting. 

## <u>Certification Testing Areas</u>

The suite has a broad set of tests, balancing the needs of the community across many different uses for AlmaLinux and the hardware we support. In general, these are the areas that the certification suite touches on:

1.  Hardware Detection
1.  CPU Stress Testing
1.  Containerization
1.  KVM Functionality
1.  Network Performance
1.  Linux Kernel Testing through LTP ([Linux Test Project](https://github.com/linux-test-project/ltp))
1.  USB Port Functionality (Optional - requires hands-on coordination with the hardware host)
1.  PXE Device Booting
1.  OS Feature Benchmarking via PTS ([Phoronix Test Suite](http://phoronix-test-suite.com))

## <u>Certification Lifecycle</u>

The Certification SIG will certify for major versions of AlmaLinux, expecting that minor versions will carry forward. For example, if hardware is certified for AlmaLinux 9.3, the hardware will not need to be re-certified until AlmaLinux 10 is released.

The Certification SIG will engage the IHVs for another round of certification when it's time. If the IHV has donated the hardware to ALOSF, then the SIG will maintain the certification ourselves, and alert the IHV to update their website when the updated certification is confirmed. 

## <u>Contribute to testing: "Community Validated"</u>

In addition to the certification processes with IHVs managed by the AlmaLinux OS Foundation (ALOSF), we encourage community involvement in hardware testing. Individuals with access to hardware that we have yet to certify are encouraged and invited to participate. This not only amplifies the scope of our hardware compatibility and validates the strength of the certification suite, but also shows IHVs the types and scope of the AlmaLinux user base.

Hardware that has been certified without input from the IHV will be described on the AlmaLinux website with a "Community Certified" status. This serves as a first confirmation of compatibility until a relationship with the IHV can be confirmed, and provides users with confidence in hardware compatibility.

Once the certification suite has been run, results should be shared through a pull request to the [Certifications](https://github.com/AlmaLinux/certification-test-results) repo.

#### Benefits

- Increased Coverage: With community support, we can vastly increase the range of hardware tested, providing more options for end-users.
- Quick Feedback: Engaged community members running these tests can provide rapid feedback on compatibility, aiding in engagement with IHVs for the SIG.
- Community Trust: Hardware that is "Community Certified" has been vetted by the very users who rely on it, creating a sense of trust and reliability.

If you have a specific certification request, or have hardware in reserve, take a look at the Community Requested Certifications list. We'd love to have you!

<div class="btn-row">
<a class="btn btn-primary btn-block p-2" href="https://github.com/AlmaLinux/certifications"><i class="bi bi-people-fill"></i> Request Certification</a>
</div>

## <u>Appendix: Glossary of terms</u>

**ALOSF:** AlmaLinux OS Foundation - The organization responsible for maintaining and governing AlmaLinux OS.

**IHV:** Independent Hardware Vendor - Companies that produce hardware to be used with various operating systems including AlmaLinux OS.

**ISV:** Independent Software Vendor - Companies that produce software that runs on various operating systems including AlmaLinux OS.

**LTP:** Linux Test Project - A project included in the certification suite aimed at delivering test suites to the open-source community to validate the reliability and stability of Linux.

**MOU:** Memorandum of Understanding - A formal agreement between two or more parties.

**NDA:** Non-Disclosure Agreement - A legal contract between at least two parties outlining confidential material.

**PTS:** Phoronix Test Suite - An open-source benchmark software for Linux.

**PXE:** Preboot Execution Environment - A technology that allows computers to load a software assembly from a network.

**SIG:** Special Interest Group - A community within ALOSF with a shared interest in advancing a specific area of AlmaLinux OS, such as hardware certification.

**SSH:** Secure Shell - A cryptographic network protocol for operating network services securely over an unsecured network.
