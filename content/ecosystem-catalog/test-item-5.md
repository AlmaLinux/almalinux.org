---
#Required - don't alter
type: ecosystem-catalog

#Required
date: 2024-07-19T15:15:00-04:00

#Required
title: "HP ZBook Firefly 14 G10 Mobile Workstation"

#Required
image: "/images/ec/hp-logo.png"

#Required
shortTitle: "ZBook Firefly 14 G10"

#Required
provider: "HP Inc."

#Required
system: "Laptop"

#Optional
specsLink: "https://www.hp.com/us-en/shop/pdp/hp-zbook-firefly-14-g10-mobile-workstation-pc"
#Optional
supportLink: "https://support.hp.com/us-en/product/hp-zbook-firefly-14-inch-g10-mobile-workstation-pc/38882334"

#Optional
buttonLink: "https://www.hp.com/us-en/shop/pdp/hp-zbook-firefly-14-g10-mobile-workstation-pc"

#Overview
overview_collection:
- key: "CPU"
  value: "Intel Core i5/i7"
- key: "RAM"
  value: "Up to 64GB DDR5"
- key: "STORAGE"
  value: "Up to 2TB PCIe Gen4 NVMe SSD"
- key: "GPU"
  value: "Intel Iris Xe Graphics"

certification_collection:
- name: "AlmaLinux 9"
  certified: 1
  architecture: "x86_64"
  compute:
    name: "Compute"
    level: 9.0
    features:
      - "CPU Core Performance Counters": "9.4+"
      - "OpenGL 4.6": "9.4+"
      - "OpenCL 3.0": "9.4+" 
  management:
    name: "Management"
    level: 9.0
    features:
      - "Basic GPU Graphics": "9.4+"
      - "Battery Monitoring": "9.4+"
      - "Fingerprint Reader": "9.4+"
  network:
    name: "Network"
    level: 9.0
    features:
      - "Wi-Fi 6E": "9.4+"
      - "Bluetooth 5.3": "9.4+"

#Begin Search metadata
searchTitle: "ZBook Firefly 14 G10"
searchDesc: "The HP ZBook Firefly 14 G10, a powerful and portable mobile workstation for professionals on the go."
es_collection: 
  type: ["Laptop", "Mobile Workstation"]
  provider: "HP Inc."
  platform: "AlmaLinux"
  certified-for: "AlmaLinux 9"
  architecture: "x64"
  network: "Wi-Fi 6E"
  management: "Fingerprint Reader"
  compute: "Intel Core i5/i7"
  storage: "PCIe Gen4 NVMe SSD"
---