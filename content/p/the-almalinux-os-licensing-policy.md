---
title: "The AlmaLinux OS licensing policy"
type: p
---


## AlmaLinux Licensing guidelines

Licensing in open source can be complicated, so we've put together these guidelines to simplify the AlmaLinux approach for our community. The definitions below these guidelines expand on this information but simply stated, this is how we approach licensing:

0. **Use existing license -** If what we're shipping is based on something else, we use the underlying license that already exists.

1. **CC BY-SA 4.0 for most content -** CC BY-SA 4.0 is best for anything that cannot be subject to patents, but that we also don't want to see duplicated without attribution. This includes things like wiki and website content. Anything patentable should be under a software license with a patent clause, using the guidelines below.

1. **CC0 for some content -** CC0 is best for anything that cannot be subject to patents, but where attribution would cause undue burdens. For example, SBOMs. Anything patentable should be under a software license with a patent clause, using the guidelines below.

2. **GPLv2 for unique OS software -** Anything that is unique to AlmaLinux and ships with the OS should be GPLv2 since GPLv2 and GPLv3 cannot be mixed in the same distribution.

3. **GPLv3 for unique non-OS software -** it's ideal for anything we make that does not have to be shipped with AlmaLinux OS.

4. **MIT for unique libraries -** any libraries that we're shipping should likely be shipped using an MIT license unless there's a specific reason not to (ie: preventing weaponization by bad actors).

**Note:** Licensing with an open source license does not relinquish ownership, only a copyright assignment would do that and we do not use copyright assignments. We believe it is healthy for a real community to have distributed copyright ownership, and will not decline code based solely on copyright ownership, as long as it is shared under an open source license.

## Definitions

A **“Contribution”** is any contribution to the AlmaLinux OS Foundation that does not include (a) already-existing upstream software or content that merely is packaged, or is intended to be packaged, in AlmaLinux OS, or changes or additions to such already-existing software or content, or (b) material intended to be used for AlmaLinux OS Foundation logos.

Your Contribution is **“Explicitly Licensed”** if you specifically attach a license notice to it.

**“Default License”** describes the license you grant under this policy for a Contribution that is not Explicitly Licensed.

**“Code”** refers to software code, RPM spec files, or any functional material whose principal purpose is to control or facilitate the building of packages.

## Distributions

The AlmaLinux OS distribution is a compilation of software packages. Each package is governed by its own license. Like Red Hat Enterprise Linux, the AlmaLinux OS compilation copyright is licensed under GPLv2. To the extent you hold any copyright in the selection, coordination, or arrangement of packages making up the AlmaLinux OS distribution, you license that copyright under GPLv2.

The compilation license does not supersede the licenses of code and content contained in the distributions, including anything you may have contributed to that pre-existing material. The complete licensing terms applicable to a given package can be found in the source code of the package.

## Explicitly Licensed Contributions

Explicitly Licensed Contributions can be under any of the open source or open content licenses considered acceptable for the Fedora Project.
AlmaLinux.org Content

As of 2021-05-01, new content published on [www.almalinux.org](https://www.almalinux.org), [wiki.almalinux.org](https://wiki.almalinux.org) and [blog.almalinux.org](https://blog.almalinux.org) is licensed under the Creative Commons Attribution-ShareAlike 4.0 International Public License (CC BY-SA 4.0), except as otherwise indicated in this document or the content itself. Accordingly, the Default License for Contributions to such content is CC BY-SA 4.0, with attribution solely to the AlmaLinux OS Foundation.

## Licensed Repositories

The Default License for Contributions to an AlmaLinux OS repository that contains notice of a license is that same license.

## Code Contributions

The Default License for Contributions of Code is the **MIT license**, as follows:

Copyright Contributors to the AlmaLinux OS Foundation.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Other Contributions

The Default License for Contributions not otherwise addressed in this policy, including mailing list postings, forum posts, website design elements, and content in issues and comments submitted to the AlmaLinux Bug Tracker, is the CC0 1.0 Universal Public Domain Dedication (CC0).
AlmaLinux OS Logos

AlmaLinux OS logos are covered by the AlmaLinux Trademark Guidelines and not within the scope of this policy. If you want to contribute to the development of AlmaLinux OS logos, please contact the AlmaLinux OS Foundation Governing Board. 

Last updated: August 23, 2023
Updated and adapted from the [CentOS Project Licensing Policy](https://www.centos.org/legal/licensing-policy/)