# 🌐 Nmap Live Host Discovery

## 📚 Project Overview

This project is part of the **Cybersecurity Specialization (Part 1)** at Holberton School. It introduces various host discovery techniques using **Nmap**, focusing on scanning subnetworks to detect live hosts through multiple protocols including ARP, ICMP, TCP, and UDP.

> ✅ **Fully completed** — All tasks successfully executed.

---

## 🎯 Learning Objectives

By the end of this project, I was able to explain and perform:

- What is Nmap and how it works
- How to enumerate targets in a subnetwork
- How to perform different types of Nmap ping scans:
  - ARP scan
  - ICMP Echo
  - ICMP Timestamp
  - ICMP Address Mask
  - TCP SYN Ping
  - TCP ACK Ping
  - UDP Ping
- The difference between each scan type
- How to scan for live hosts efficiently using Nmap options
- How to capture service/version info from open ports

---

## 🛠️ Tools & Technologies

- **Kali Linux**
- **Nmap**
- Bash scripting

---

## ✅ Project Requirements

- All scripts:
  - Must be exactly **2 lines long**
  - Must begin with `#!/bin/bash`
  - Must end with a newline
  - Must use `$1` for subnetwork input **(without quotes)**
  - Must follow **Betty style**
  - Must be executable
- Root/sudo privileges required for most scans
- `README.md` file is mandatory

---

## 📁 Project Structure

```
network_security/
└── 0x04_nmap_live_hosts_discovery/
    ├── 0-arp_scan.sh
    ├── 1-icmp_echo_scan.sh
    ├── 2-icmp_timestamp_scan.sh
    ├── 3-icmp_address_mask_scan.sh
    ├── 4-tcp_syn_ping.sh
    ├── 5-tcp_ack_ping.sh
    ├── 6-udp_ping_scan.sh
    └── 100-flag.txt
```

---

## 🧪 Tasks Breakdown

### ✅ 0. Will arp be enough?
- ARP Scan using Nmap (`-PR`)
- Only works within the same subnetwork

---

### ✅ 1. Host, do you hear me?
- ICMP Echo scan (`-PE`)
- Basic ping discovery across a subnet

---

### ✅ 2. Time always matter
- ICMP Timestamp scan (`-PP`)

---

### ✅ 3. Sometimes we need Masks!
- ICMP Address Mask scan (`-PM`)

---

### ✅ 4. SYN Scan me
- TCP SYN Ping scan (`-PS`)
- Scans for hosts responding on ports 22, 80, and 443

---

### ✅ 5. Are you privileged enough to scan me?
- TCP ACK Ping scan (`-PA`)
- Also scans ports 22, 80, and 443

---

### ✅ 6. UDP is our last hope
- UDP Ping scan (`-PU`)
- Scans ports 53, 161, 162

---

### ✅ 7. Simple Catch, is it mimicked?
- Capture the flag challenge
- Use UDP scan over ports 200–300 to retrieve version info and discover the hidden flag

---

## 🚀 Project Status

✅ **Fully Completed**  
📌 This project builds essential skills in network discovery and reconnaissance using Nmap — a cornerstone tool in the cybersecurity field.

---
