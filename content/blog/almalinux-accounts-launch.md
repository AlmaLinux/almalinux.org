---
title: "Introducing AlmaLinux Accounts"
type: blog
author: 
    name: "Jonathan Wright"
    bio: "-"
    image: /users/jonathan.jpg
date: '2023-05-03'
post:
    title: "Introducing AlmaLinux Accounts"
---
Over the past few months, our [infrastructure team](https://wiki.almalinux.org/sigs/Infrastructure.html) has been hard at work preparing our single sign-on system that will provide a unified login experience to nearly all AlmaLinux websites and properties.  We are happy to announce the launch of https://accounts.almalinux.org!

[AlmaLinux Accounts](https://accounts.almalinux.org) will give you a single account to use across the array of sites and services offered by AlmaLinux!  In addition it eases the process of onboarding new contributors through centralized groups and permissions.

## Why?
Introducing our Single Sign-On (SSO) system offers numerous benefits for both users and the AlmaLinux OS Foundation. SSO enhances security, streamlines access, and simplifies user management across our ecosystem. With a single set of credentials, users can seamlessly navigate all AlmaLinux websites and services. This unified login experience ultimately boosts productivity, fosters collaboration, and provides a more cohesive and personalized experience for our community.

## Software Stack
In the spirit of FOSS, it was only natural for us to stick with a free and open-source software stack. The chosen components should be familiar to anyone who has dealt with directory management or SSO in the Enterprise Linux space.  We took inspiration from Fedora's account system for some components.

We have chosen the following FOSS components to power our SSO:

- [FreeIPA](https://www.freeipa.org) for directory and user management.
- [Noggin](https://github.com/fedora-infra/noggin), a web front-end for user self-service. We've been doing work in the Fedora project to get noggin and its dependencies added to EPEL 9. This will benefit anyone looking to deploy noggin on RHEL 9 or RHEL 9 compatible distros. <sup>1</sup>
- [Keycloak](https://www.keycloak.org/), an OpenID Connect system to sit between applications and LDAP.  We've started contributing to a playbook mostly maintained by RHEL engineers to help ease the deployment of Keycloak on EL distros. <sup>2</sup>

## What About My Existing Account(s)?
We have a transition plan for the next few weeks to get all systems fully supporting our [AlmaLinux Accounts](https://accounts.almalinux.org) and all existing accounts transitioned into the system, or otherwise integrated.

### chat.almalinux.org (Mattermost)
chat.almalinux.org is the single largest standalone user database we have to transition.  Luckily this is a very easy and painless task for us as well as users.

After you've created your [AlmaLinux Account](https://accounts.almalinux.org), navigate to the `Profile -> Security` section in Mattermost.

![Step 1 of converting MatterMost account to use AlmaLinux Accounts](/blog-images/almalinux-accounts-mattermost-step1.png)

From here click on `Edit` next to `Sign-in Method` and then `Switch to Using AD/LDAP` and you can link your new AlmaLinux account.  *Keep in mind that once you link your account you will always use your AlmaLinux account to sign in to chat.almalinux.org.*

![Step 2 of converting MatterMost account to use AlmaLinux Accounts](/blog-images/almalinux-accounts-mattermost-step2.png)

![Step 3 of converting MatterMost account to use AlmaLinux Accounts](/blog-images/almalinux-accounts-mattermost-step3.png)

![Step 4 of converting MatterMost account to use AlmaLinux Accounts](/blog-images/almalinux-accounts-mattermost-step4.png)

This last step has slightly confusing wording.  It appears as though it is asking for your email password, but it is not.  Do NOT enter your email password.  It in fact wants your current Mattermost password for your *email-based* login.

1. Your current Mattermost account password.
2. Your [AlmaLinux Account](https://accounts.almalinux.org) username and password.

### bugs.almalinux.org

All existing users on bugs.almalinux.org have been imported as AlmaLinux Accounts.  You can gain access to the account by requesting a password reset at https://accounts.almalinux.org/forgot-password/ask using your username.

### git.almalinux.org

git.almalinux.org was originally setup with only GitHub as an authentication source.  This is now disabled and you must use your AlmaLinux Account to log in.

If you wish to recover your previous git.almalinux.org account send an email to account-merge@almalinux.org from the address tied to your GitHub and AlmaLinux accounts and we can tie them together for you.

### lists.almalinux.org

lists.almalinux.org has been tied into [AlmaLinux Accounts](https://accounts.almalinux.org) for a few weeks now.  Existing lists accounts can be linked to AlmaLinux Accounts seamlessly.

Login option for new accounts:

![Step 1 of associating lists.almalinux.org account with AlmaLinux Accounts](/blog-images/almalinux-accounts-lists-step1.png)

Tie your existing account to your AlmaLinux Account at https://lists.almalinux.org/accounts/social/connections/:

![Step 2 of associating lists.almalinux.org account with AlmaLinux Accounts](/blog-images/almalinux-accounts-lists-step2.png)

### pes.almalinux.org
The Package Evolution Service (PES) will be updated with OIDC support, and subsequently AlmaLinux Account support soon.

### build.almalinux.org
The AlmaLinux Build System (ALBS) will be updated with OIDC support, and subsequently AlmaLinux Account support soon.

### Other
There are various other services used by contributors which are mostly tied into AlmaLinux Accounts already with a few to follow soon.

## Frequently Asked Questions
**Q:** I configured 2FA/OTP at https://accounts.almalinux.org but *service/site XYZ* does not have a field for my OTP on the login page.  
**A:** All sites tied to [AlmaLinux Accounts](https://accounts.almalinux.org) support your 2FA/OTP.  Simply add it to the end of your password in the password field when logging in.  For example if your password is `hunter2` and your OTP is `123456` you would enter `hunter2123456` into the password field.

**Q:** Where should I go for help?  
**A:** The [Infrastructure Channel on Mattermost](https://chat.almalinux.org/almalinux/channels/infrastructure),
[IRC](https://web.libera.chat/#almalinux-infrastructure), [mailing list](https://lists.almalinux.org/mailman3/lists/infra.lists.almalinux.org/).

---

<sup>1</sup> *https://bodhi.fedoraproject.org/updates/FEDORA-EPEL-2023-b0e8a9d618*  
*https://bodhi.fedoraproject.org/updates/FEDORA-EPEL-2023-cfcb055a9f*  
*https://bodhi.fedoraproject.org/updates/FEDORA-EPEL-2023-fdfb8a6342*  
*https://bodhi.fedoraproject.org/updates/FEDORA-EPEL-2023-3b54948adb*  
*https://bodhi.fedoraproject.org/updates/FEDORA-EPEL-2023-46e518d693*  
*https://bodhi.fedoraproject.org/updates/FEDORA-EPEL-2023-607e3d35c7*  
*https://bodhi.fedoraproject.org/updates/FEDORA-EPEL-2023-6215554ad9*  
*https://bugzilla.redhat.com/show_bug.cgi?id=2174923*

<sup>2</sup> *https://github.com/ansible-middleware/keycloak/pull/73*
