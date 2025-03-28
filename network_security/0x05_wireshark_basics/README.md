# 🧪 Wireshark Basics

## 📚 Project Overview

This project is part of the **Cybersecurity Specialization (Part 1)** at Holberton School and introduces learners to **Wireshark**, a powerful packet capture and network protocol analysis tool. The tasks focus on creating filters that detect specific types of network traffic typically generated by various Nmap scan types and ARP sweeps.

> ✅ **Fully completed** — All packet filter tasks were successfully built and tested.

---

## 🎯 Learning Objectives

By the end of this project, I was able to:

- Understand what Wireshark is and how it’s used in cybersecurity
- Analyze network packets and extract valuable data
- Create precise Wireshark filters for:
  - IP Protocol scans
  - TCP SYN, FIN, and Connect() scans
  - UDP port scans and sweeps
  - ICMP echo sweeps
  - ARP scans
- Detect reconnaissance activity using packet-level evidence

---

## 🛠️ Tools & Technologies

- **Wireshark**
- **Nmap**
- **ARP-scan**
- **Kali Linux**

---

## ✅ Project Requirements

- All filters:
  - Must be exactly **2 lines long**
  - Must end with a newline
  - Must be saved as `.txt` files
- Target packets must be captured manually using the corresponding Nmap/ARP command
- Wireshark must be installed and configured to capture as a non-root user (via `usermod -aG wireshark $USER`)
- `README.md` file is mandatory

---

## 📁 Project Structure

```
network_security/
└── 0x05_wireshark_basics/
    ├── 0-ip_scan.txt
    ├── 1-tcp_syn.txt
    ├── 2-tcp_connect_scan.txt
    ├── 3-tcp_fin.txt
    ├── 4-tcp_ping_sweep.txt
    ├── 5-udp_port_scan.txt
    ├── 6-udp_ping_sweep.txt
    ├── 7-icmp_ping_sweep.txt
    └── 8-arp_scanning.txt
```

---

## 🧪 Tasks Breakdown

### ✅ 0. IP protocol scan
- Filter to capture traffic from Nmap’s `-sO` scan (IP protocol scan)

---

### ✅ 1. TCP SYN scan
- Detects packets from Nmap’s `-sS` scan (half-open TCP scan)

---

### ✅ 2. TCP Connect() scan
- Captures Nmap traffic using full TCP handshake (`-sT` scan)

---

### ✅ 3. TCP FIN scan
- Detects FIN flag-only scans from Nmap’s `-sF` mode

---

### ✅ 4. TCP ping sweeps
- Captures TCP SYN and ACK ping sweeps with `-sn -PS/-PA` options

---

### ✅ 5. UDP port scan
- Detects responses to UDP scans (`-sU`), typically seen as ICMP “port unreachable”

---

### ✅ 6. UDP ping sweeps
- Captures outgoing UDP packets in ping sweep mode (`-sn -PU`)

---

### ✅ 7. ICMP ping sweep
- Captures ICMP Echo Requests generated by `-sn -PE` scans

---

### ✅ 8. ARP scanning
- Detects broadcast ARP requests made using tools like `arp-scan -l`

---

## 🚀 Project Status

✅ **Fully Completed**  
📌 This project provided foundational experience in analyzing network traffic and detecting reconnaissance techniques — essential for intrusion detection and network defense.

---
