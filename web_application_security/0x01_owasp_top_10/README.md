# 🔐 OWASP Top 10

## 📚 Project Overview

This project is part of the **Cybersecurity Specialization (Part 1)** at Holberton School. It explores real-world web application vulnerabilities based on the **OWASP Top 10 (2021)** — a globally recognized list of the most critical security risks to web applications.

> ✅ **Fully completed** — All vulnerabilities were tested and exploited as required for educational purposes.

---

## 🎯 Learning Objectives

By the end of this project, I was able to:

- Explain the purpose of the OWASP Top 10 and its impact
- Demonstrate Broken Access Control
- Decode weakly encrypted credentials (Cryptographic Failures)
- Exploit Stored Cross-Site Scripting (XSS)
- Understand the risks associated with poor session management
- Identify vulnerable input fields and improper encoding practices

---

## 🛠️ Tools & Technologies

- **Kali Linux 2023.2**
- **curl**, **sqlmap**
- **Browser DevTools (F12)**
- **Base64/XOR decoding**
- **Manual request inspection**
- **Burp Suite/ZAP for testing**

---

## ✅ Project Requirements

- All Bash scripts must:
  - Be 2 lines long or less
  - Use `$1` for dynamic input
  - Follow Betty coding style
  - Use proper shebang (`#!/bin/bash`)
- All files must end with a newline
- Filters or scripts must be functional and demonstrate the vulnerability
- A `README.md` file is mandatory

---

## 📁 Project Structure

```
web_application_security/
└── 0x01_owasp_top_10/
    ├── 0-flag.txt
    ├── 1-xor_decoder.sh
    ├── 2-flag.txt
    ├── 3-flag.txt
    ├── 4-vuln.txt
```

---

## 🧪 Tasks Breakdown

### ✅ 0. (A1:2021) - Broken Access Control
- Manipulated predictable session IDs to hijack another user’s session
- Demonstrated insecure session management

---

### ✅ 1. (A2:2021) - Cryptographic Failures - Scripting
- Built a Bash script to decode XOR-encoded passwords (WebSphere style)
- Used to decrypt credentials in the next challenge

---

### ✅ 2. (A2:2021) - Cryptographic Failures - Catch The Flag
- Identified encrypted credentials from intercepted requests
- Used previous XOR script to decode password and sign in for the flag

---

### ✅ 3. (A3:2021) - Injection [Stored XSS] - part 1/3
- Found 3 specific user profiles to follow
- Triggered a stored XSS event and retrieved flag via triggered JS in profile

---

### ✅ 4. (A3:2021) - Injection [Stored XSS] - part 2/3
- Located the vulnerable field in profile edit form
- Injected `<script>` payload and confirmed alert on profile view
- Identified the exact input field name responsible

---

## 🚀 Project Status

✅ **Fully Completed**  
📌 This project bridges theoretical knowledge of OWASP Top 10 risks with hands-on exploitation and detection — essential for both attackers and defenders in web security.

---
