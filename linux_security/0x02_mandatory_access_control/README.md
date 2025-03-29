# 0x04. Content Discovery

## Description

This project focuses on the **Content Discovery** phase of web application penetration testing. You'll utilize tools like **Gobuster**, **ffuf**, and **Burp Suite**, as well as manual OSINT techniques, to uncover hidden files, directories, subdomains, and even past versions of web apps. The project emphasizes identifying overlooked or intentionally hidden content that might contain sensitive information, misconfigurations, or security flaws.

---

## Learning Objectives

You should be able to explain the following without Google:

- What is content discovery?
- Why is content discovery important?
- How directory brute-forcing works.
- Tools: Gobuster, Burp Suite, OWASP ZAP, DirBuster, ffuf.
- How to use wordlists in brute-forcing.
- How to find hidden directories and files.
- What is fuzzing in web security.
- OSINT techniques (e.g., Wayback Machine, Wappalyzer).
- DNS enumeration techniques (zone transfers, brute-force).
- HTTP header inspection.

---

## Tools & Techniques

- **Manual Analysis**: `robots.txt`, `sitemap.xml`, `favicon.ico`, HTTP headers.
- **Burp Suite**: For request inspection and manipulation.
- **Gobuster**: `dir`, `dns`, `fuzz`, and `tftp` modes.
- **ffuf**: Fast subdomain and path fuzzing.
- **Wayback Machine**: Historical view of websites.
- **OSINT tools**: For fingerprinting, stack discovery, and archived content.
- **cURL**: To check headers or response behavior.
- **Wappalyzer**: For identifying technologies used.

---

## Tasks Overview

| Task | Name | Points | Status |
|------|------|--------|--------|
| 0 | Manual Discovery – Sitemap / robots.txt | 4 pts | ✅ To Do |
| 1 | Manual Discovery – Check HTTP Headers | 6 pts | ✅ To Do |
| 2 | Manual Discovery – Identify Frontend Vendor | 4 pts | ⚠️ Correction |
| 3 | OSINT – Wayback Machine & Past Roles | 4 pts | ⚠️ Correction |
| 4 | Gobuster – Directory Brute-Forcing | 6 pts | ✅ To Do |
| 5 | Gobuster – DNS Mode for Subdomains | 6 pts | ✅ To Do |
| 6 | ffuf – Subdomain Fuzzing | 7 pts | ✅ To Do |
| 7 | Gobuster – Fuzz Mode | 6 pts | ✅ To Do |
| 8 | Gobuster – TFTP Mode Brute-Force | 6 pts | ✅ To Do |

---

## Status

- **Completion**: 10.61%  
- **Date**: March 29, 2025
- **Note**: All tasks are being worked on in order. Some minor corrections needed but progress is steady.

---

## Repository

**GitHub**: [holbertonschool-cyber_security](https://github.com/holbertonschool-cyber_security)  
**Directory**: `web_application_security/0x04_content_discovery`

