# 🔐 Linux Security Basics

## 📚 Project Overview

This project is part of the **Cybersecurity Specialization (Part 1)** at Holberton School. It introduces students to basic Linux security practices, including system monitoring, network analysis, firewall configuration, and secure file transfer. Tasks were completed using Bash scripting and tested on Kali Linux.

---

## 🎯 Learning Objectives

By the end of this project, I am able to:

- Understand what Linux is and its command-line structure
- Explain the structure of the Linux OS and its file system (FHS)
- Protect files and directories from unauthorized access
- Monitor and investigate system activity
- Securely transfer files and data using SCP
- Configure and manage firewalls using `iptables` and `ufw`
- Identify and terminate malicious processes
- Use essential security tools like `ps`, `kill`, `netstat`, `ss`, `nmap`, `lynis`, and `tcpdump`

---

## 🛠️ Tools & Technologies

- **Operating System:** Kali Linux
- **Scripting Language:** Bash
- **Security Tools:** `nmap`, `tcpdump`, `lynis`, `iptables`, `ufw`
- **Networking Tools:** `netstat`, `ss`

---

## ✅ Requirements

- All scripts must:
  - Be exactly **2 lines long**
  - Start with `#!/bin/bash`
  - Use `$1` for IP/subnet arguments
  - Avoid `&&`, `||`, `;`, backticks
  - Follow **Betty coding style**
  - Be executable
  - Be tested on **Kali Linux**
- A `README.md` file is required at the project root

---

## 📁 Project Directory Structure

```
linux_security/
└── 0x00_linux_security_basics/
    ├── 0-login.sh
    ├── 1-active-connections.sh
    ├── 2-incoming_connections.sh
    ├── 3-firewall_rules.sh
    ├── 4-network_services.sh
    ├── 5-audit_system.sh
    ├── 6-capture_analyze.sh
    └── 7-scan.sh
```

---

## 🧪 Tasks Breakdown

### ✅ 0. What secrets hold
Displays the last 5 login sessions of system users. Must be run as root or sudo.

---

### ✅ 1. Shows your Linux connections, not your social status!
Lists active TCP socket connections using `ss`, showing IPs, ports, and processes.

---

### ✅ 2. Firewall rules: Your network's first line of defense!
Allows incoming TCP connections on port 80 using firewall rules. Requires root privileges.

---

### ✅ 3. Securing your network, one rule at a time!
Displays all firewall rules in verbose mode for better insight into current configurations.

---

### ✅ 4. See what's talking, and who's listening!
Lists network services, their ports, protocols (TCP/UDP), and associated processes.

---

### ✅ 5. Where it talks, we all listen!
Initiates a full system audit using `lynis` to identify security issues and misconfigurations.

---

### ✅ 6. Your eyes and ears on the network!
Captures and analyzes 5 packets of live traffic using `tcpdump`. Useful for spotting anomalies.

---

### ✅ 7. So fast, it'll make your router sweat!
Scans a subnet using `nmap` to identify live hosts and open ports.

---

## 🏁 Project Status

✅ **Completed** — All scripts passed with a 100% score.  
📌 This project reinforces Linux-based cybersecurity practices and foundational knowledge needed for hardening systems and responding to threats.

---
