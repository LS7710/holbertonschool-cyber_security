# 🔍 Active Reconnaissance

## 📚 Project Overview

This project is part of the **Cybersecurity Specialization (Part 1)** at Holberton School. It focuses on **Active Reconnaissance** — a key phase in penetration testing where ethical hackers directly interact with target systems to discover vulnerabilities. Tasks involve service enumeration, SQL injection, manual inspection, and directory discovery using common offensive security tools.

> ✅ **Fully completed** — All tasks were successfully executed.

---

## 🎯 Learning Objectives

By the end of this project, I was able to:

- Understand what active reconnaissance is and why it matters
- Use tools like `nmap`, `sqlmap`, `gobuster`, and `Wappalyzer`
- Perform port scanning, service detection, and directory enumeration
- Conduct SQL injection to retrieve databases and dump sensitive data
- Differentiate between passive and active information gathering
- Extract hidden flags and data from websites manually and programmatically

---

## 🛠️ Tools & Technologies

- **nmap**
- **sqlmap**
- **gobuster**
- **netcat**, **telnet**, **traceroute**, **ping**
- **Wappalyzer** browser extension
- **Linux / Bash**

---

## ✅ Project Requirements

- All scripts must:
  - Be exactly **1 line long**
  - End with a newline
  - Be executable
- Use of editors: `vi`, `vim`, `emacs`
- Target machine: **cyber_netsec_0x02**
- Domain used: `active.hbtn` (mapped in `/etc/hosts`)
- Testing environment: **Kali Linux**
- `README.md` file is required at the root

---

## 📁 Project Structure

```
network_security/
└── 0x02_active_reconnaissance/
    ├── 0-ports.txt
    ├── 1-webserver.txt
    ├── 2-injectable.txt
    ├── 3-database.txt
    ├── 4-tables.txt
    ├── 5-hidden_dir.txt
    ├── 100-flag.txt
    ├── 101-flag.txt
    └── 102-flag.txt
```

---

## 🧪 Tasks Breakdown

### ✅ 0. Are there any opened Ports?
- Used `nmap` to scan top ports on `active.hbtn`
- Output saved in: `0-ports.txt`

---

### ✅ 1. Inspect the runner
- Mapped `active.hbtn` to target IP in `/etc/hosts`
- Used **Wappalyzer** to detect web server name/version
- Output saved in: `1-webserver.txt`

---

### ✅ 2. Nothing defeat Manual inspection
- Inspected site source code manually
- Found the first flag in HTML comments
- Saved in: `100-flag.txt`

---

### ✅ 3. Trypanophobia
- Discovered vulnerable URL path for SQL injection
- Output saved in: `2-injectable.txt`

---

### ✅ 4. SQLmap is an army \o/
- Used `sqlmap` to:
  - Extract database name → `3-database.txt`
  - Count tables → `4-tables.txt`

---

### ✅ 5. Injections hurt :')
- Used `sqlmap --dump` to extract table data
- Found the **second flag** from users table
- Saved in: `101-flag.txt`

---

### ✅ 6. My NAV doesn't include all my pages
- Used `gobuster` to find hidden admin panel
- Saved result in: `5-hidden_dir.txt`

---

### ✅ 7. It may look the same, but it’s not
- Located admin panel page
- Found the **third flag**
- Saved in: `102-flag.txt`

---

## 🚀 Project Status

✅ **Fully Completed**  
📌 This project helped simulate real-world web app recon using tools commonly used in ethical hacking, bug bounties, and red team engagements.

---
