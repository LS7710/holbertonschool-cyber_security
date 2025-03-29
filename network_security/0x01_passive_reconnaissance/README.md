# 🕵️ Passive Reconnaissance

## 📚 Project Overview

This project is part of the **Cybersecurity Specialization (Part 1)** at Holberton School and focuses on **passive reconnaissance**, the first stage in ethical hacking. It teaches how to gather intelligence about a target system or domain without directly engaging with it. Tools used include `whois`, `nslookup`, `dig`, `subfinder`, and `shodan.io`.

---

## 🎯 Learning Objectives

By the end of this project, I was able to:

- Understand DNS and how it functions
- Query WHOIS records for domain information
- Use `nslookup`, `dig`, and `subfinder` to extract DNS data
- Retrieve and analyze different DNS record types (A, MX, TXT)
- Explore and apply tools like **Shodan.io** and **DNSDumpster**
- Understand subdomain enumeration techniques
- Distinguish between **active** and **passive** reconnaissance

---

## 🛠️ Tools & Technologies

- `whois`, `awk`
- `nslookup`, `dig`
- `subfinder`
- `shodan.io`
- DNS record analysis
- Kali Linux environment

---

## ✅ Requirements

- All scripts:
  - Must be exactly 2 lines long
  - Start with `#!/bin/bash`
  - Use `$1` without quotes for domain/IP
  - End with a newline
  - Must follow **Betty coding style**
  - Must be executable
- Scripts tested on **Kali Linux**
- Markdown report required for research-based task

---

## 📁 Project Structure

```
network_security/
└── 0x01_passive_reconnaissance/
    ├── 0-whois.sh
    ├── 1-a_record.sh
    ├── 2-mx_record.sh
    ├── 3-txt_record.sh
    ├── 4-dig_all.sh
    ├── 5-subfinder.sh
    ├── holbertonschool_report.md
    ├── 100-flag.txt
    ├── 101-flag.txt
    └── 102-flag.txt
```

---

## 🧪 Tasks Breakdown

### ✅ 0. Who is it?
Use `whois` to extract registrant, admin, and tech info into CSV format.

---

### ✅ 1. A Record
Retrieve A records for a domain using `nslookup`.

---

### ✅ 2. MX Record
Retrieve MX (Mail Exchange) records using `nslookup`.

---

### ✅ 3. Check the TXT
Use `nslookup` to extract all TXT records from a domain.

---

### ✅ 4. Dig it all!
Use `dig` to return all available DNS records in the answer section only.

---

### ✅ 5. Find the sub!
Use `subfinder` to enumerate subdomains and write them to a `.txt` file in `Host,IP` format.

---

### ✅ 6. Search for us
Use **Shodan.io** to collect:
- All IP ranges for `holbertonschool.com`
- Technologies and frameworks used in subdomains  
Report findings in `holbertonschool_report.md`.

---

### 🏁 CTF Tasks – Capture the Flag

#### ✅ 7. TXT Flag
- Use `dig` with a DNS resolver (VPN-connected) to extract the flag hidden in TXT records.

#### ✅ 8. NS Flag
- Extract flag from nameservers using `dig` and DNS resolver.

#### ✅ 9. MX Flag
- Find flag in mail server records using `dig`.

---

## 🚀 Project Status

✅ **Completed** — All tasks and challenges passed with 100%  
📌 This project demonstrates real-world reconnaissance techniques used during penetration testing and red team engagements.

---
