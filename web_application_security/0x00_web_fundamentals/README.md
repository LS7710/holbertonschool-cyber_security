# 🌐 Web Fundamentals

## 📚 Project Overview

This project is part of the **Cybersecurity Specialization (Part 1)** at Holberton School. It explores the foundational principles of how the web works, including HTTP communication, front-end vs back-end, and different types of vulnerabilities in modern web applications. The tasks progressively walk through exploiting Host Header Injection, XSS, SQL Injection, and Remote Code Execution (RCE).

> ✅ **Fully completed** — All tasks were explored and executed as intended.

---

## 🎯 Learning Objectives

By the end of this project, I was able to explain and demonstrate:

- How modern web applications function (Web 1.0 vs 2.0 vs 3.0)
- The roles of front-end and back-end communication
- Progressive Web Apps (PWAs)
- Differences between stateful and stateless designs
- Structured vs unstructured data
- Web application security risks (XSS, SQLi, RCE)
- Bug bounty programs and responsible disclosure

---

## 🛠️ Tools & Technologies

- **Kali Linux 2023.3**
- **curl**
- **sqlmap**
- **Python HTTP Server**
- **Browser DevTools (Firefox recommended)**

---

## ✅ Project Requirements

- All Bash scripts must:
  - Be exactly **2 lines long**
  - Start with `#!/bin/bash`
  - Use `$1`, `$2`, `$3` as arguments appropriately
  - Follow **Betty coding style**
  - Be executable
- Filters and payloads must be written as `.txt` files
- `README.md` is required at the root

---

## 📁 Project Structure

```
web_application_security/
└── 0x00_web_fundamentals/
    ├── 1-host_header_injection.sh
    ├── 2-flag.txt
    ├── 3-xss_payload.txt
    ├── 4-flag.txt
    ├── 5-ticket.txt
    ├── 6-flag.txt
    ├── 7-rce_payload.txt
    └── 8-flag.txt
```

---

## 🧪 Tasks Breakdown

### ✅ 0. Welcome
- Setup web environment and endpoint at `http://web0x00.hbtn`
- Verified connectivity using `curl` and browser

---

### ✅ 1. Can We Trust Our Hosts?
- Exploited **Host Header Injection** using `curl`
- Redirected reset link to a controlled host

---

### ✅ 2. Catch the FLAG #1
- Triggered password reset as a known user
- Captured traffic on listener to retrieve reset path
- Logged in to retrieve the flag as a **Customer**

---

### ✅ 3. Stealing Cookies from Managers is delicious!
- Created a short **XSS payload** using `<script>` and `fetch`
- Sent victim cookies to attacker-controlled host

---

### ✅ 4. Catch the FLAG #2
- Executed XSS payload on the support side
- Logged in as **Support** to retrieve the flag from response

---

### ✅ 5. Can we trust our Managers?
- Identified potential SQL Injection in ticket ID
- Saved HTTP request to `5-ticket.txt`
- Tested and exploited using `sqlmap`

---

### ✅ 6. Catch the FLAG #3
- Used dumped credentials from SQLi to login as **Admin**
- Retrieved the third flag from admin interface

---

### ✅ 7. Why would an Admin have such a function?
- Exploited poor input validation in **ping check** for **RCE**
- Payload downloads and runs `nc` binary, verifying via `-V`

---

### ✅ 8. Catch the FLAG #4
- Used reverse shell to gain root access
- Retrieved final flag from `/root` directory

---

## 🚀 Project Status

✅ **Fully Completed**  
📌 This project simulated real-world web penetration testing using industry tools and techniques. It demonstrated how layered vulnerabilities can be exploited in progression from user to admin level.

---
