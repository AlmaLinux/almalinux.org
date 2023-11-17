---
title: "CIS Benchmarks Update"
type: blog
author:
 name: "Simon John"
 bio: "Security Standards Architect"
 image: /users/sjohn.png
date: '2023-10-20'
post:
    title: "CIS Benchmarks Update"
    image: /blog-images/cis_update.svg

---

Hello again AlmaLinux Community! We last posted about the [AlmaLinux OS 8 CIS benchmark](/blog/official-cis-benchmark-for-almalinux-and-openscap-guide-now-published/) almost two years ago. We've recently released the second update to that - [v3.0.0](https://workbench.cisecurity.org/benchmarks/15287) which was tested on AlmaLinux 8.8 and are about to start working on the first update to the [AlmaLinux OS 9 CIS benchmark](https://www.cisecurity.org/benchmark/almalinuxos_linux) for 9.2. So I thought it's about time we explained what it's all about.

## What are CIS benchmarks?

The [Center for Internet Security](https://www.cisecurity.org/), to quote their website, is a *community-driven nonprofit, responsible for the CIS Controls and CIS Benchmarks, globally recognized best practices for securing IT systems and data*.

Many organisations use the CIS benchmarks as their baseline for security hardening operating systems and applications. They can be either a starting point to build on or a goal to aspire towards - traditionally you'd have a percentage pass rate to achieve based on your organisation's policies for example "at least 70% at Level 2". Being an industry standard means that you can find plenty of tutorials, tools and experienced practitioners to help you.

The benchmarks cover topics like which SSH ciphers to use, AAA best practices like password complexity and filesystem permissions, how to best configure a host-based firewall (like firewalld/iptables) and how to setup auditd and rsyslog to ensure that you're logging enough information and have an audit trail in case of a security incident, and how to stop disabling SELinux! The DISA [STIGs](https://public.cyber.mil/stigs/) are very similar, but with some specific additions for national security and a different delivery method.

The benchmarks are just documents - you can read them as PDF's - no special software to install. You can find them on the [website](https://www.cisecurity.org/benchmark/almalinuxos_linux). They're available to all for free with no paywall.

CIS controls *map* to various security frameworks, so you can show an auditor how you're compliant to ISO 27002 by applying CIS controls in the  benchmarks, for example:

| **ISO 27002:2022**                            | **CIS Controls v8**                                                         | **AlmaLinux OS 9 Benchmark**         |
|-----------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------|
| 8.8 - Management of technical vulnerabilities | 7.3 - Perform Automated Operating System Patch Management                   | 1.2 - Configure Software Updates     |
| 8.2 - Privileged access rights                | 5.4 - Restrict Administrator Privileges to Dedicated Administrator Accounts | 5.3 - Configure privilege escalation |

## How can I test my servers for compliance?

Many vulnerability scanners have the capability to scan a host for compliance to various CIS benchmarks.

[OpenSCAP](https://wiki.almalinux.org/documentation/openscap-guide.html) is an open-source solution that we provide instructions and packages for.

CIS have their own [CIS-CAT Pro](https://www.cisecurity.org/cybersecurity-tools/cis-cat-pro) which can be run locally via the commandline or remotely via GUI. CIS-CAT is tightly linked to the benchmarks so updates are published simultaneously.

[Tenable](https://www.cisecurity.org/partner/tenable)'s Nessus Pro includes compliance audits against published standards and baselines (CIS, DISA STIGs) and across more than 15+ security frameworks (HIPAA, NIST 800-53). The dedicated compliance team comes with decades of combined experience and are an active part of industry working groups such as CIS. I recently worked with Tenable Research to improve the accuracy of the AlmaLinux OS 9 CIS audits.

[Qualys](https://www.cisecurity.org/partner/qualys) Policy Compliance assesses various CIS benchmarks - including AlmaLinux, as well as prioritises the risk of the misconfiguration by mapping them to the MITRE ATT&CK framework and threats such as ransomware, with the ability to remediate misconfigurations to reduce risk and bring servers into compliance.

## How can I security harden my servers?

On my [GitHub](https://github.com/sej7278/virt-installs) I have a few scripts for hardening various distro's including AlmaLinux, to CIS benchmarks, using some of my favourite technologies - Kickstart and libvirt, but also Ansible, cloud-init and Preseed.

With CIS [SecureSuite](https://www.cisecurity.org/cis-hardened-images) membership you can get access to pre-hardended virtual machine images for most cloud providers, build-kits for hardening existing infrastructure and the CIS-CAT Pro tool for testing.

Unlike some security frameworks which can be quite vague and high-level, the CIS benchmarks are distribution-specific and very descriptive - they tell you exactly which commands to type or what to put in a config file to remediate non-compliances and how to retest. This is what most companies I've worked with find attractive - a sysadmin can do the hardening and a SOC analyst can measure compliance without hiring a consultancy to tell you what is meant by phrases like *"use sufficient cryptographic controls for the classification of data at rest and in transit"*.

Using an example from the table above, 1.2.2 tests if `gpgcheck=1` is set globally to ensure signatures on RPM's from YUM repositories are checked - so that you can be sure they came from a trusted source:

```bash
grep gpgcheck /etc/dnf/dnf.conf
```

If it's set to 0, we can remediate the failure by running the following as root:

```bash
sed -i 's/^gpgcheck.*$/gpgcheck=1/' /etc/dnf/dnf.conf
```

Easy right? You obviously should take some care before just running all of the remediations on your host, you don't want to disable root login before you configure sudo, or disable password authentication before you install an SSH key, not that I've ever done that. Nope. Never. Moving swiftly along...

## How can I help?

Well I'm glad you asked! I've been contributing to CIS benchmarks for a few years now, I think I first dabbled with the SLES 12 benchmark, but my first major contribution was the AlmaLinux OS 8 v1.0.0 benchmark, which was based on a draft Fedora 28 family benchmark and eventually became the basis for the Rocky/Oracle 8 benchmarks.

The AlmaLinux OS 9 v1.0.0 benchmark was published in December 2022, which was actually the upstream of the RHEL 9 v1.0.0 benchmark that was published a couple of weeks *earlier!* We're currently working on the F34 family vNext benchmark which will become the next AlmaLinux OS 9 benchmark update.

It's truly a collaborative community effort, with representatives from various distro's as well as end-users and security professionals from all over the world, regularly attending the [Weekly Webex](https://workbench.cisecurity.org/communities/1) with the folks at CIS. I attend the distribution-independent Linux calls, where we also work on Debian, Ubuntu and even recently Amazon Linux. It can be a great learning experience too.

You can also help by reviewing [vNext drafts](https://workbench.cisecurity.org/benchmarks/10093) and adding a comment/ticket or even starting a discussion - maybe you don't agree with a policy or could improve upon it or have even just found a typo. It's not all Linux, there's plenty of other [communities](https://workbench.cisecurity.org/communities/public) you may be interested in too, including IoT, Apache, macOS, Cisco....

If you just want to come chat about all things AlmaLinux (and a surprising number of pet-related conversations), join us at [chat.almalinux.org](https://chat.almalinux.org)
