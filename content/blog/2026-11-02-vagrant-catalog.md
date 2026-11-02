---
title: "AlmaLinux Vagrant boxes have a new home: vagrant.almalinux.org"
type: blog
author:
  name: "Yuriy Kohut"
  bio: "Cloud SIG member"
  image: /users/yuriy-kohut.jpg
date: 2026-11-02
images:
  - /blog-images/2026/2026-11-02-vagrant-catalog-boxes.png
post:
  title: "HashiCorp is shutting down the HCP Vagrant registry on December 31, 2026. All AlmaLinux Vagrant boxes, old and new, are now served from our own catalog at vagrant.almalinux.org. Here's how to switch."
  image: /blog-images/2026/2026-11-02-vagrant-catalog-boxes.png
---

HashiCorp is retiring the HCP Vagrant registry (formerly Vagrant Cloud), the service that has hosted the `almalinux/*` Vagrant boxes since 2021. To keep the boxes available, AlmaLinux now runs its own Vagrant box catalog at **[vagrant.almalinux.org](https://vagrant.almalinux.org)**. It has every version that was ever published to HCP, plus all new releases. The box names stay the same: you only need to tell Vagrant where to find them.

## What is changing, and when

According to [HashiCorp's end-of-life notice](https://developer.hashicorp.com/hcp/docs/vagrant/hcp-vagrant-eol):

- **October 1, 2026**: HCP stopped accepting new boxes and new versions of existing boxes. AlmaLinux releases built after that date are not on HCP; they are only in our catalog.
- **November 2, 2026**: HCP Vagrant support ends.
- **December 31, 2026**: the registry shuts down. From then on, `vagrant box add almalinux/9` or `vagrant up` with `config.vm.box = "almalinux/9"` will fail unless Vagrant is pointed at our catalog.

## How to use the catalog

Set the `VAGRANT_SERVER_URL` environment variable, then use the boxes by name, exactly as before:

```bash
export VAGRANT_SERVER_URL=https://vagrant.almalinux.org
vagrant init almalinux/10
vagrant up
```

To make a project independent of the environment, set the catalog in its `Vagrantfile` instead:

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "almalinux/10"
  config.vm.box_server_url = "https://vagrant.almalinux.org"
end
```

If both are set, `VAGRANT_SERVER_URL` takes precedence. The `Vagrantfile` setting is the better choice for CI jobs that run `sudo vagrant up`, because `sudo` drops most environment variables.

Vagrant reads box metadata from the catalog, downloads the box file from AlmaLinux's own storage, and verifies its SHA-256 checksum, the same way it did with HCP.

## Boxes you already have

A box that was added from HCP remembers HCP as the place to check for updates, even after you set `VAGRANT_SERVER_URL`. `vagrant box outdated` and `vagrant box update` will report such a box as up to date, although newer versions are in the catalog, and they will fail entirely once HCP shuts down.

To switch an installed box to the catalog, add it again with the catalog set, then remove the old versions:

```bash
export VAGRANT_SERVER_URL=https://vagrant.almalinux.org
vagrant box add almalinux/9 --provider libvirt
vagrant box prune --name almalinux/9
```

Use your own box name and provider (`virtualbox`, `vmware_desktop`, `parallels`, `libvirt` or `hyperv`). From then on, `vagrant box update` checks the catalog. Running VMs are not affected; they keep using the box they were created from.

## What is in the catalog

The catalog has the same six boxes as HCP, with the full version history, from AlmaLinux OS 8.3 (February 2021) to the latest releases:

| Box                             | x86_64 (amd64)                       | ARM64 (aarch64)               |
| ------------------------------- | ------------------------------------ | ----------------------------- |
| `almalinux/10`                  | libvirt, VirtualBox, VMware, Hyper-V | VirtualBox, VMware, Parallels |
| `almalinux/10-x86_64_v2`        | libvirt, VirtualBox, VMware, Hyper-V | -                             |
| `almalinux/9`                   | libvirt, VirtualBox, VMware, Hyper-V | VirtualBox, VMware, Parallels |
| `almalinux/8`                   | libvirt, VirtualBox, VMware, Hyper-V | -                             |
| `almalinux/10-kitten`           | libvirt, VirtualBox, VMware, Hyper-V | VirtualBox, VMware, Parallels |
| `almalinux/10-kitten-x86_64_v2` | libvirt, VirtualBox, VMware, Hyper-V | -                             |

The releases made after HCP closed are already there, including AlmaLinux OS 9.8 `9.8.20261005`, AlmaLinux OS 10.2 `10.2.20261012`, AlmaLinux OS Kitten `10.20261019.0` and AlmaLinux OS 8.10 `8.10.20261026`. The new VirtualBox boxes for ARM64 hosts, such as Apple silicon Macs, are also only available from the catalog. New releases are added automatically by our build pipeline once their tests pass.

Open [vagrant.almalinux.org](https://vagrant.almalinux.org) in a browser to see every box, version, provider and architecture, with box sizes and ready-to-copy usage instructions.

## What's next?

If you maintain Vagrantfiles, CI jobs or documentation that use `almalinux/*` boxes, please switch them to the catalog before December 31. The AlmaLinux projects that use Vagrant in their own CI are being switched as well.

Questions, problems or feedback about the catalog are welcome in [cloud-images issue #363](https://github.com/AlmaLinux/cloud-images/issues/363), in the [~sigcloud channel](https://chat.almalinux.org/almalinux/channels/sigcloud) on chat.almalinux.org, or at [bugs.almalinux.org](https://bugs.almalinux.org).

If you want to stay up to date, follow us on [our forum](https://almalinux.discourse.group/), [Reddit](https://www.reddit.com/r/AlmaLinux/), [X](https://twitter.com/AlmaLinux), [Mastodon](https://fosstodon.org/@almalinux/), [LinkedIn](https://www.linkedin.com/company/80320905/), and [YouTube](https://www.youtube.com/channel/UCt9lpkqUPp1FUEi9uqVlPQA).
