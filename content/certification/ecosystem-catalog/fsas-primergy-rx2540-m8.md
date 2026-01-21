---
#Required - don't alter
type: "certification/ecosystem-catalog"

#Required
date: 2026-01-20

#Required
title: "Fsas Technologies PRIMERGY RX2540 M8 Rack Server"

#Required
image: "/images/ec/fsas-logo.svg"

#Required
shortTitle: "PRIMERGY RX2540 M8 Rack Server"

#Required
provider: "Fsas Technologies"

#Optional
system: "Server"

#Optional
specsLink: "https://eu.fsastech.com/eu/products-services/primergy-servers/primergy-rx2540-m8/"

#Optional
supportLink: "https://support.ts.fujitsu.com/index.asp?ld=us"

#Optional - If not provided no button will be rendered
buttonLink: "https://eu.fsastech.com/eu/products-services/primergy-servers/primergy-rx2540-m8/"

# optional
key_applications:
  - AI
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
    link: systems/fsas-technologies/primergy-rx2540-m8
  - key: "CPU"
    value: "2 x Intel Xeon 6760P @ 3.80GHz (128 Cores / 256 Threads)"
  - key: "Chipset"
    value: "Intel Ice Lake IEH"
  - key: "RAM"
    value: "2 x 32 GB DDR5-6400MT/s Micron"
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
        - "CPU Core Performance Counters": "9.4+"
        - "CPU Scaling Governor": "9.4+"
        - "System Memory": "9.4+"
        - "Virtualization (Host)": "9.4+"
    management:
      name: "Management"
      level: 9.0
      features:
        - "Graphical Console": "9.4+"
        - "Virtual Media": "9.4+"
    network:
      name: "Network"
      level: 9.0
      features:
        - "25Gb Ethernet": "9.4+"
    storage:
      name: "Storage"
      level: 9.0
      features:
        - "SATA SSD": "9.4+"
        - "PCIe NVMe": "9.4+"

#Begin Search metadata
searchTitle: "Fsas Technologies PRIMERGY RX2540 M8"
# this is basically just tags, formatting doesn't much matter
searchDesc:
  "Dual-socket x86 server that delivers new levels of performance and sustainability without compromise, in an optimized 2U chassis
  Ideal for collaboration, AI applications, business processing, graphics rendering or in-memory databases
  Boost performance with Intel® Xeon® 6 Processors with P-cores (up to 86 P-cores per CPU)
  Maximize in-memory performance with 32 DIMM modules (up to 8TB DDR5 @6,400 or 8,000 MT/s)
  Scale to meet demands with 12x 3.5” or up to 24x 2.5” storage devices and support for 2x GPU cards"
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
