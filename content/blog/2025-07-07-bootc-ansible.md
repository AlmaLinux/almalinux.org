---
title: "Composing bootc Images with Ansible"
type: blog
author:
 name: "Isaac Beverly"
 bio: "Atomic SIG lead & HeliumOS Developer"
 image: /users/imbev.jpg
date: 2025-07-07 #TODO change date
images:
  - /blog-images/2024-04-08-secure-boot.png #TODO Update image
post:
    title: "Composing bootc images with Ansible"
    image: /blog-images/2024-04-08-secure-boot.png
---

Ansible has long existed as a popular choice for declaratively managing the configuration of AlmaLinux systems at runtime.

In contrast, Bootable Containers (bootc) is an emerging technology that builds operating system images using the same syntax and infrastructure as OCI/Docker containers. The Cloud SIG has built bootc images for AlmaLinux since [Fall 2024](/blog/2024-09-02-bootc-almalinux-heliumos/), with additional image variants maintained by the recently formed [Atomic SIG](https://wiki.almalinux.org/sigs/Atomic.html).

By using Ansible and bootc together, organizations and individuals can build easily-maintainable operating system images.

### Building bootc images

bootc images are specified using the widely adopted standard, OCI/Docker Containerfile syntax. This is functions well, but has some drawbacks when publishing a diverse array of image variants.

```Dockerfile
FROM quay.io/almalinuxorg/almalinux-bootc:10-kitten

RUN dnf update -y

# Add third-party repository:

RUN dnf install -y epel-release

# Add additional software

RUN dnf install -y tmux btop

```

Consider the above Containerfile. This is a basic example that is easy to maintain because of its minimal complexity and length.

What if you wanted to build images with packages installed to support different hardware? What if you wanted to build images with vary by workload or software versions?

This can be done by using build-args, environment variables, or calling different scripts from different Containerfiles.

Conditional execution in a Containerfile:
```Dockerfile
# ...
ARG arg
RUN if [[ -z "$arg" ]] ; then echo "Optimized for AMD" ; else echo "Optimized for NVIDIA" ; fi
```

Different Containerfile per case:
```Dockerfile
# Containerfile.A
# ...

RUN ./setup-testing-repos.sh
```

```Dockerfile
# Containerfile.B
# ...

RUN ./setup-release-repos.sh
```

These approaches work, but there is a more accessible option, one using yaml.

### Introducing Ansible to bootc

The following is an example from the official Ansible documentation. This playbook demonstrates how to install a package and enable a systemd service, specifically at run-time.

```yaml
- name: 'Update db servers'
  hosts: databases
  remote_user: root
  tasks:

  - name: 'Ensure postgresql is at the latest version'
    ansible.builtin.yum:
      name: postgresql
      state: latest

  - name: 'Ensure that postgresql is started'
    ansible.builtin.service:
      name: postgresql
      state: started
```

With a few tweaks, we can apply this playbook at bootc image build-time instead:

```Dockerfile
# Containerfile
FROM quay.io/almalinuxorg/almalinux-bootc:10-kitten

RUN dnf update -y && dnf install -y ansible-core

RUN ansible-playbook playbook.yaml
```

```yaml
# playbook.yaml
- name: 'bootc image'
  hosts: localhost
  tasks:

  - name: 'Ensure postgresql is at the latest version'
    ansible.builtin.yum:
      name: postgresql
      state: latest

  - name: 'Ensure that postgresql is started'
    ansible.builtin.service:
      name: postgresql
      state: started
```

Because of `import_playbook` and the Ansible modules `ansible.builtin.import_tasks` and `ansible.builtin.include_tasks`, it is simple to compose Ansible configuration to build a variety of images.

```yaml
# base.yaml
- name: 'Add EPEL repo'
  ansible.builtin.dnf:
    name:
      - epel-release
    state: present
```

```yaml
# nvidia.yaml
- name: 'Add NVIDIA repo'
  ansible.builtin.dnf:
    name:
      - almalinux-release-nvidia-driver
    state: present
# ...
```

```yaml
# playbook-amd.yaml
- import_playbook: base.yaml
```

```yaml
# playbook-nvidia.yaml
- import_playbook: base.yaml
- import_playbook: nvidia.yaml
```
