---
#Required - don't alter
type: "certification/ecosystem-catalog"

#Required
date: 2026-02-06

#Required
title: "Fsas Technologies PRIMERGY RX4770 M8 Rack Server"

#Required
image: "/images/ec/fsas-logo.svg"

#Required
shortTitle: "PRIMERGY RX4770 M8 Rack Server"

#Required
provider: "Fsas Technologies"

#Optional
system: "Server"

#Optional
specsLink: "https://eu.fsastech.com/eu/products-services/primergy-servers/primergy-rx4770-m8/"

#Optional
supportLink: "https://support.ts.fujitsu.com/index.asp?ld=us"

#Optional - If not provided no button will be rendered
buttonLink: "https://eu.fsastech.com/eu/products-services/primergy-servers/primergy-rx4770-m8/"

# optional
key_applications:
  - Backend Operations
  - Virtualization
  - Databases

# The data contained here will be displayed in a key -> value table
# under overview.  If it is removed no overview section will display
overview_collection:
  - key: Tests Run By
    # valid values are "AlmaLinux OS Foundation", "<Vendor Name>", or "Community"
    value: Fsas Technologies
  # optional
  # - key: "Certification Inherited From"
  #   value: A+ Server AS-2124BT-HNTR
  #   link: supermicro-as-2124bt-hntr
  # optional
  - key: "Test Logs"
    value: "Click here"
    link: systems/fsas-technologies/primergy-rx4770-m8
  - key: "CPU"
    value: "4 x Intel Xeon 6788P @ 3.80GHz (344 Cores / 688 Threads)"
  - key: "Chipset"
    value: "Intel Ice Lake IEH"
  - key: "RAM"
    value: "4 x 64 GB DDR5-6400MT/s Micron"
  - key: "STORAGE"
    value: "960GB Micron_7450_MTFDKBA960TFR"
  - key: "NETWORK"
    value: "Intel I210 + 2 x Intel I350"

certification_collection:
  - name: "AlmaLinux 9"
    # valid values are "official", or "community"
    certified: official
    architecture: "x86_64"
    compute:
      name: "Compute"
      level: 9.0
      features:
        - "CPU Core Performance Counters": "9.6+"
        - "CPU Scaling Governor": "9.6+"
        - "System Memory": "9.6+"
        - "Virtualization (Host)": "9.6+"
    management:
      name: "Management"
      level: 9.0
      features:
        - "Graphical Console": "9.6+"
        - "Virtual Media": "9.6+"
    network:
      name: "Network"
      level: 9.0
      features:
        - "25Gb Ethernet": "9.6+"
    storage:
      name: "Storage"
      level: 9.0
      features:
        - "SATA SSD": "9.6+"
        - "PCIe NVMe": "9.6+"

#Begin Search metadata
searchTitle: "Fsas Technologies PRIMERGY RX4770 M8"
# this is basically just tags, formatting doesn't much matter
searchDesc:
  "Quad-socket x86 system providing superior levels of scalability and reliable performance in a 3U chassis
  Ideal for business-critical workloads, large-scale virtualization, and in-memory databases
  Boost performance with Intel® Xeon® 6 Processors with P-cores (up to 86 P-cores per CPU)
  Address large data sets with up to 64 DIMMs with DDR5 DIMM with up to 6,400 MT/s
  Scale capacity with up to 24x 2.5” storage drives, 10x PCIe 5.0 slots, and support for M.2 hot plug module"
es_collection:
  # valid values Server, Component, Component Collection
  type: ["Server"]
  provider: "Fsas Technologies"
  certified-for: ["AlmaLinux 9"]
  # valid values x86_64, aarch64, s390x, ppc64le, risc-v
  architecture: "x86_64"
  network: Onboard, OCP v3
  pcie-version: "5.0"
  processor-line: "Dual Intel® Xeon® 6"
  processor-brand: "Intel"
  storage: ["NVMe", "SATA", "SAS"]
---
