---
title: "DISA STIG Automation for AlmaLinux OS 9"
type: blog
author:
  name: "Artem Karasev"
  bio: "Head of Brand & Product Marketing, TuxCare"
  image: /users/akarasev.png
date: "2026-10-26"
images:
  - /blog-images/2026/2026-10-26-disa-stig-automation-almalinux-os-9.png
post:
  title: "TuxCare has contributed free DISA STIG automation for AlmaLinux OS 9 to the ComplianceAsCode project, so you can now check a system against the STIG with OpenSCAP. Here's how to try it today."
  image: /blog-images/2026/2026-10-26-disa-stig-automation-almalinux-os-9.png
---

Hello AlmaLinux community! At TuxCare, we've contributed free DISA STIG automation for AlmaLinux OS 9 to the ComplianceAsCode project, and the maintainers [merged it](https://github.com/ComplianceAsCode/content/pull/15208) on October 20, 2026. That means you can now point OpenSCAP at an AlmaLinux OS 9 system and get a report of which STIG requirements it meets, rather than working through a few hundred of them by hand.

## So what is a STIG?

STIG stands for Security Technical Implementation Guide. It's a set of secure configuration standards that DISA (the US Defense Information Systems Agency) publishes for products used in Department of Defense networks, and each requirement has a severity category, from CAT I for the most serious findings down to CAT III. STIGs are very similar to CIS benchmarks, with additional requirements focused on national security. You don't have to work for the US government to use one either: they're freely available, so anyone can use them as a hardening baseline.

We spent more than a year working with DISA on the STIG for AlmaLinux OS 9, which DISA published as the "[Cloud Linux AlmaLinux OS 9 STIG](https://ncp.nist.gov/checklist/1264)" and first released in December 2024. Like a CIS benchmark, though, a STIG on its own is just a document, so you need something to check your systems against it. Commercial scanners such as Tenable Nessus already support this one, and we wanted the community to have a free, open source option as well, like the STIG content ComplianceAsCode already ships for RHEL 9.

## What have we contributed?

ComplianceAsCode is the upstream project that converts standards such as STIGs and CIS benchmarks into automated checks and fixes. It's where the SCAP Security Guide comes from, and it's the content OpenSCAP reads when you run a scan (AlmaLinux already has an [OpenSCAP guide](https://wiki.almalinux.org/documentation/openscap-guide.html) on the wiki if you're new to it). Our colleague Simon John, whom you may know from his posts here on [FIPS validation](/blog/2023-09-19-fips-validation-for-almalinux/) and [CIS benchmarks](/blog/2023-11-28-cis-benchmarks-update/), wrote the AlmaLinux OS 9 STIG profile and submitted it upstream as [pull request #15208](https://github.com/ComplianceAsCode/content/pull/15208).

The profile covers STIG version V1R8. Its [controls file](https://github.com/ComplianceAsCode/content/blob/master/products/almalinux9/controls/stig_almalinux9.yml) lists 439 requirements, and 434 of them have automated checks. Of the other five, two need a human to review them, one check is still pending, and two cover packages (quagga and ypserv) that don't exist on AlmaLinux OS 9, so they don't apply.

Here's an example. ALMA-09-009590 is a CAT I requirement stating that the system must verify GPG signatures on packages from external repositories. If you read Simon's CIS post, you'll recognize the check: it looks for `gpgcheck=1` in the `[main]` section of `/etc/dnf/dnf.conf`. Now imagine doing that by hand for every requirement, on every server.

ComplianceAsCode also generates Bash scripts and Ansible playbooks for its profiles, including fixes we wrote for our new rules, such as enabling the TuxCare Extended Security Updates (ESU) repository on licensed systems. Once you've read the report, you can fix whatever failed and scan again. A word of warning, though: read the remediation before you run it. Some STIG settings, such as SmartCard authentication and the SSH and login restrictions, can lock you out of a box if you apply them before you have another way in, so try it on a test VM first.

## How can I try it?

The profile is already in ComplianceAsCode's main branch and assigned to the [0.1.83 release](https://github.com/ComplianceAsCode/content/milestone/83), scheduled for November 26, 2026. If you'd rather not wait, you can build it from source on an AlmaLinux OS 9 system:

```bash
sudo dnf install git cmake make openscap-utils openscap-scanner python3 python3-setuptools python3-pip
git clone https://github.com/ComplianceAsCode/content.git
cd content
pip3 install -r requirements.txt
./build_product almalinux9
sudo oscap xccdf eval --profile xccdf_org.ssgproject.content_profile_stig --results results.xml --report report.html build/ssg-almalinux9-ds.xml
```

If the system can reach the internet, add `--fetch-remote-resources` so OpenSCAP can download AlmaLinux's security advisory data and check whether patches are up to date. Without it, that check shows as "notchecked."

Open `report.html` in your browser, and you'll see every check in the profile with its result. If you spot a false positive, a rule that doesn't quite fit AlmaLinux, or even just a typo, please open an issue or a pull request on the [ComplianceAsCode GitHub project](https://github.com/ComplianceAsCode/content). The weeks before 0.1.83 ships are the best time to catch those.

## Can I pass the full STIG with this?

You can use the profile to scan and harden any AlmaLinux OS 9 system for free. Passing the complete STIG is a different matter because the STIG itself names specific components. Specifically because AlmaLinux 9.2 and 9.6 are no longer supported by the AlmaLinux OS Foundation, a system only passes when it runs TuxCare ESU for AlmaLinux 9.2 or 9.6 with our FIPS 140-3 validated packages. We're starting FIPS validation work for AlmaLinux 9.10 in November 2026.

FIPS cryptography is mandatory under the STIG, and ALMA-09-004310, another CAT I requirement, says the system must use the TuxCare ESU repository. A community AlmaLinux OS 9 install will fail that check, and the report will tell you so.

## Going further in regulated environments

For those of you who need a passing result for an audit, our [FIPS for AlmaLinux page](https://tuxcare.com/fips-for-almalinux/) explains how ESU and the FIPS packages work. If you'd like the hardening Ansible scripts and kickstarts updated more often than the open source release, plus direct access to TuxCare engineers, that's what our Security Hardening Support is for.

For anything about ESU, the FIPS packages, or Security Hardening Support, email our sales team at [sales@tuxcare.com](mailto:sales@tuxcare.com).

Questions about the profile are welcome at [chat.almalinux.org](https://chat.almalinux.org), where you'll find us hanging out with the rest of the community.
