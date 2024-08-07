---
#Required - don't alter
type: ecosystem-catalog

#Required
date: 2024-07-19T14:56:00-04:00

#Required
title: "HP Zbook Mobile Workstation HP ZBook Studio 23 Work PC"

#Required
image: "/images/ec/hp-logo.png"

#Required
shortTitle: "ZBook Studio 12"

#Required
provider: "HP Inc."

#Optional
system: "Laptop"

#Optional
specsLink: "https://www.google.com"

#Optional
supportLink: "https://www.google.com"

#Optional - If not provided no button will be rendered
buttonLink: "https://www.google.com"

# The data contained here will be displayed in a key -> value table
# under overview.  If it is removed no overview section will display
overview_collection:
- key: "CPU"
  value: "Intel Xeon"
- key: "RAM"
  value: "DDR4 4/8GB"
- key: "STORAGE"
  value: "128GB eMMC"
- key: "FEATURE"
  value: "It runs software!"



certification_collection:
  - name: "AlmaLinux 9"
    certified: 1
    architecture: "x86_64"
    compute:
      name: "Compute"
      level: 9.0
      features:
        - "CPU Core Performance Counters": "9.4+"
        - "HDMI Audio Playback": "9.4+"
        - "22 x Max Logical CPU": "9.4+"
        - "Stereo Audio Playback": "9.4+"
        - "Stereo Audio Record": "9.4+"
        - "System Controlled Scaling": "9.4+"
        - "System Memory": "9.4+"
        - "Thunderbolt 4": "9.4+"
        - "1 x USB 3 (5 Gigabit) Ports": "9.4+"
        - "1 x USB C (10 Gigabit) Ports": "9.4+"
        - "Uncore Performance Counters": "9.4+"
        - "Virtual Machine (Host)": "9.4+"
    management:
      name: "Management"
      level: 9.0
      features:
        - "Basic GPU Graphics": "9.4+"
        - "Battery Monitoring": "9.4+"
        - "Fingerprint Reader": "9.4+"
        - "LCD Backlight Control": "9.4+"
        - "Suspend on lid": "9.4+"
        - "Suspend to disk": "9.4+"
        - "Suspend to idle": "9.4+"
        - "Suspend to idle on Fn": "9.4+"
        - "Suspend to memory": "9.4+"
        - "Suspend to memory on Fn": "9.4+"
    network:
      name: "Network"
      level: 9.0
      features:
        - "Bluetooth 5.x": "9.4+"
        - "WiFi 6": "9.4+"
    storage:
      name: "Storage"
      level: 9.0
      features:
        - "M.2 NVME": "9.4+"
        - "PCIe SD Card Reader": "9.4+"

  - name: "AlmaLinux 8"
    certified: 0
    architecture: "x86_64"
    compute:
      name: "Compute"
      level: 8.0
      features:
        - "CPU Core Performance Counters": "8.4+"
        - "HDMI Audio Playback": "8.4+"
    management:
      name: "Management"
      level: 8.0
      features:
        - "Basic GPU Graphics": "8.4+"
        - "Battery Monitoring": "8.4+"
    network:
      name: "Network"
      level: 8.0
      features:
        - "Bluetooth 5.x": "8.4+"
        - "WiFi 6": "8.4+"
    storage:
      name: "Storage"
      level: 9.0
      features:
        - "M.2 NVME": "9.4+"
        - "PCIe SD Card Reader": "9.4+"


#Begin Search metadata
searchTitle: "ZBook Studio 24"
searchDesc: "The innovative ZBook, is innovative!"
es_collection: 
  type: ["CPU Collection", "Component"]
  provider: "HP Inc."
  platform: "AlmaLinux"
  certified-for: "AlmaLinux 9"
  architecture: "x64"
  network: "2 Gigabit Ethernet"
  management: "Accelerated GPU Graphics"
  compute: "CPU Pinning"
  storage: "Blu-ray"
---