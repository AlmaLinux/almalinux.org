---
#Required - don't alter
type: "certification/ecosystem-catalog"

#Required
date: 2024-07-31

#Required
title: "A+ Server AS-2124BT-HNTR"

#Required
image: "/images/ec/supermicro-logo.png"

#Required
shortTitle: "Supermicro A+ Server AS-2124BT-HNTR"

#Required
provider: "Super Micro Computer, Inc."

#Optional
system: "Server"

#Optional
specsLink: "https://www.supermicro.com/en/Aplus/system/2U/2124/AS-2124BT-HNTR.cfm"

#Optional
supportLink: "https://www.supermicro.com/en/support"

#Optional - If not provided no button will be rendered
buttonLink: "https://www.supermicro.com/en/Aplus/system/2U/2124/AS-2124BT-HNTR.cfm"

# optional
key_applications:
  - Compute Intensive Applications
  - HPC, Data Center, Enterprise Server
  - Hyperscale / Hyperconverged

# The data contained here will be displayed in a key -> value table
# under overview.  If it is removed no overview section will display
overview_collection:
  - key: Tests Run By
    # valid values are "AlmaLinux OS Foundation", "<Vendor Name>", or "Community"
    value: AlmaLinux OS Foundation
  # optional
  # - key: "Certification Inherited From"
  #   value: A+ Server AS-2124BT-HNTR
  #   link: supermicro-as-2124bt-hntr
  # optional
  - key: "Test Logs"
    value: "Click here"
    link: systems/supermicro/supermicro-as-2124bt-hntr
  - key: "CPU"
    value: "2 x AMD EPYC 73F3 16-Core @ 3.50GHz (32 Cores / 64 Threads)"
  - key: "Chipset"
    value: "AMD Starship/Matisse"
  - key: "RAM"
    value: "16 x 64 GB DDR4-3200MT/s 36ASF8G72PZ-3G2E1"
  - key: "STORAGE"
    value: "960GB SAMSUNG MZ7LH960"
  - key: "NETWORK"
    value: "2 x Intel XXV710 for 25GbE SFP28"

certification_collection:
  - name: "AlmaLinux 9"
    # valid values are "official", or "community"
    certified: official
    architecture: "x86_64"
    compute:
      name: "Compute"
      level: 9.0
      features:
        - "CPU Core Performance Counters": "9.0+"
        - "CPU Scaling Governor": "9.0+"
        - "System Memory": "9.0+"
        - "Virtualization (Host)": "9.0+"
    management:
      name: "Management"
      level: 9.0
      features:
        - "Graphical Console": "9.0+"
        - "Virtual Media": "9.0+"
    network:
      name: "Network"
      level: 9.0
      features:
        - "25Gb Ethernet": "9.0+"
    storage:
      name: "Storage"
      level: 9.0
      features:
        - "SATA SSD": "9.0+"
        - "PCIe NVMe": "9.0+"
    hardware:
      name: "Hardware"
      level: 9.0
      features:
        - "AMD EPYC™ 7002 Series": "9.0+"
        - "AMD EPYC™ 7003 Series": "9.0+"

  - name: "AlmaLinux 8"
    # valid values are "official", or "community"
    certified: official
    architecture: "x86_64"
    compute:
      name: "Compute"
      level: 8.3
      features:
        - "CPU Core Performance Counters": "8.3+"
        - "CPU Scaling Governor": "8.3+"
        - "System Memory": "8.3+"
        - "Virtualization (Host)": "8.3+"
    management:
      name: "Management"
      level: 8.3
      features:
        - "Graphical Console": "8.3+"
        - "Virtual Media": "8.3+"
    network:
      name: "Network"
      level: 8.3
      features:
        - "25Gb Ethernet": "8.3+"
    storage:
      name: "Storage"
      level: 8.3
      features:
        - "SATA SSD": "8.3+"
        - "PCIe NVMe": "8.3+"
    hardware:
      name: "Hardware"
      level: 8.3
      features:
        - "AMD EPYC™ 7002 Series": "8.3+"
        - "AMD EPYC™ 7003 Series": "8.3+"

#Begin Search metadata
searchTitle: "Supermicro A+ Server AS-2124BT-HNTR"
# this is basically just tags, formatting doesn't much matter
searchDesc:
  "2U DP CloudDC with 12 hot-swap 3.5 NVMe/SAS/SATA bays and 4 PCIe 5.0 x16 slots + 2 PCIe 5.0 x16 AIOM slots
  Highly configurable 2U 4-node systems
  2-socket with 16 DIMMs or
  1-socket with 8 DIMMs per node
  Flexible storage and I/O options
  including NVMe/SATA3 and SIOM
  networking
  NO-COMPROMISE 2U 4-NODE ARCHITECTURE
  BigTwin is the 5th generation in the Supermicro® Twin Family with a multitude of
  innovations and engineering breakthroughs.
  TwinPro systems are designed for simplified deployment and maintenance, and
  assembled with the highest quality to ensure continuous operation even at maximum
  capacity.
  With AMD EPYC™ 7003 Series Processors with AMD 3D V-Cache™ Technology,
  customers in high-end enterprise, data center, HPC and Cloud Computing
  environments receive the greatest competitive advantage from data center resources
  with the Supermicro® TwinPro."
es_collection:
  # valid values Server, Component, Component Collection
  type: ["Server"]
  provider: "Super Micro Computer, Inc."
  certified-for: ["AlmaLinux 9", "AlmaLinux 8"]
  # valid values x86_64, aarch64, s390x, ppc64le, risc-v
  architecture: "x86_64"
  network: Configurable (SIOM)
  pcie-version: "4.0"
  processor-line: "Dual AMD EPYC™ 7003/7002"
  processor-brand: "AMD"
  storage: ["NVMe", "SATA", "SAS"]
---
