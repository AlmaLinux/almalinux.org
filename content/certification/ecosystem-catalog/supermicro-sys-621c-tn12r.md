---
#Required - don't alter
type: "certification/ecosystem-catalog"

#Required
date: 2024-07-31

#Required
title: "CloudDC SuperServer SYS-621C-TN12R"

#Required
image: "/images/ec/supermicro-logo.png"

#Required
shortTitle: "Supermicro CloudDC SuperServer SYS-621C-TN12R"

#Required
provider: "Super Micro Computer, Inc."

#Optional
system: "Server"

#Optional
specsLink: "https://www.supermicro.com/en/products/system/clouddc/2u/sys-621c-tn12r"

#Optional
supportLink: "https://www.supermicro.com/en/support"

#Optional - If not provided no button will be rendered
buttonLink: "https://www.supermicro.com/en/products/system/clouddc/2u/sys-621c-tn12r"

# optional
key_applications:
  - Web Server, Firewall Application
  - Data Center Optimized, Value IaaS
  - Cloud Computing, Compact Server
  - DNS & Gateway Servers, Firewall Application
  - CDN, Edge Nodes

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
    link: systems/supermicro/supermicro-sys-621c-tn12r
  - key: "CPU"
    value: "2 x Intel Xeon Gold 6444Y @ 4.00GHz (32 Cores)"
  - key: "Chipset"
    value: "Intel Device 1bce"
  - key: "RAM"
    value: "16 x 64 GB DDR5-4800MT/s MTC40F2046S1RC48BA1"
  - key: "STORAGE"
    value: "7682GB KCM6XRUL7T68 + 2000GB INTEL SSDPELKX020T8"
  - key: "NETWORK"
    value: "2 x Mellanox MT2892"

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
        - "4th Generation Intel® Xeon® Scalable Processors": "9.0+"
        - "5th Generation Intel® Xeon® Scalable Processors": "9.2+"


  - name: "AlmaLinux 8"
    # valid values are "official", or "community"
    certified: official
    architecture: "x86_64"
    compute:
      name: "Compute"
      level: 8.7
      features:
        - "CPU Core Performance Counters": "8.7+"
        - "CPU Scaling Governor": "8.7+"
        - "System Memory": "8.7+"
        - "Virtualization (Host)": "8.7+"
    management:
      name: "Management"
      level: 8.7
      features:
        - "Graphical Console": "8.7+"
        - "Virtual Media": "8.7+"
    network:
      name: "Network"
      level: 8.7
      features:
        - "25Gb Ethernet": "8.7+"
    storage:
      name: "Storage"
      level: 8.7
      features:
        - "SATA SSD": "8.7+"
        - "PCIe NVMe": "8.7+"
    hardware:
      name: "Hardware"
      level: 8.7
      features:
        - "4th Generation Intel® Xeon® Scalable Processors": "8.0+"
        - "5th Generation Intel® Xeon® Scalable Processors": "8.8+"


#Begin Search metadata
searchTitle: "Supermicro CloudDC SuperServer SYS-621C-TN12R"
searchDesc: "Key Applications
  Web Server, Firewall Application, Data Center Optimized, Value IaaS, Cloud
  Computing, Compact Server, DNS & Gateway Servers, Firewall Application,
  CDN, Edge Nodes,
  Key Features
  Dual sockets E (LGA-4677) 5th and 4th Gen Intel® Xeon® Scalable
  processors;
  16 DIMMs up to 4TB 3DS ECC DDR5-5600: RDIMM;
  4 PCIe 5.0 x8 FHHL (optional: combine into 2 PCIe 5.0 x16); 2 PCIe 5.0 x16
  FHHL; 2 PCIe 5.0 x4 NVMe M.2;
  Dual AIOM (OCP 3.0) slots with NCSI for networking, 1 dedicated IPMI LAN;
  12x 3.5/2.5 hot-swap hybrid NVMe/SATA/SAS drive bays;
  3 heavy duty fans with optimal fan speed control, 1 air shroud;
  1200W redundant Titanium level 100-240Vac and 200-240 Vdc power
  supplies;
  1 VGA, 1 COM, 2 USB 3.0 (rear);"
es_collection: 
  # valid values Server, Component, Component Collection
  type: ["Server"]
  provider: "Super Micro Computer, Inc."
  certified-for: ["AlmaLinux 9", "AlmaLinux 8"]
  # valid values x86_64, aarch64, s390x, ppc64le, risc-v
  architecture: "x86_64"
  network: Configurable (AIOM)
  pcie-version: "5.0"
  processor-line : "4th/5th Generation Intel® Xeon® Scalable Processors"
  processor-brand: "Intel"
  storage: ["NVMe", "SATA", "SAS"]
---
