# SQL, NoSQL Injection

> **Status**: ✅ Project Fully Completed  
> **Track**: Cyber Security Specialization – Part 1  
> **Project**: SQL, NoSQL Injection  
> **Author**: Yosri Ghorbel  
> **Badge**: 56.14% (Fully completed, post-deadline grading)

---

## 📚 Description

This project focuses on identifying and exploiting injection vulnerabilities in both SQL and NoSQL contexts. You will explore various types of injection techniques such as time-based, blind, second-order, and union-based attacks, as well as bypassing authentication mechanisms in NoSQL environments like MongoDB.

---

## 🎯 Learning Objectives

- Understand the core concepts of SQL and NoSQL injection.
- Identify vulnerable input fields and endpoints.
- Extract database metadata, table names, and sensitive data.
- Exploit blind and second-order injection.
- Perform login bypass and user enumeration through NoSQL injection.
- Understand how to prevent such attacks.

---

## 🧰 Tools Used

- Kali Linux
- Burp Suite
- Browser Dev Tools
- cURL
- JSON Manipulation
- Manual payload crafting (No `sqlmap` allowed)

---

## ✅ Tasks

### 0. SQLi - Basic Injection Discovery
- **Goal**: Identify parameters vulnerable to SQL Injection.
- **File**: `0-vuln.txt`

---

### 1. SQLi - Extracting Database Information
- **Goal**: Retrieve database version and list of tables.
- **File**: `1-flag.txt`

---

### 2. SQLi - Data Exfiltration from a Specific Table
- **Goal**: Exfiltrate sensitive information using UNION-based SQLi.
- **File**: `2-flag.txt`

---

### 3. SQLi - Time-Based Blind Injection
- **Goal**: Use sleep functions to verify blind SQLi through timing.
- **File**: `3-flag.txt`

---

### 4. SQLi - Second-Order Blind Injection
- **Goal**: Inject payload at registration to be executed during login.
- **File**: `4-flag.txt`

---

### 5. NoSQLi - Discovering Injection Vulnerabilities
- **Goal**: Discover a non-harmful but vulnerable endpoint.
- **File**: `5-vuln.txt`

---

### 6. NoSQLi - Bypassing Login via Injection
- **Goal**: Login bypass using `{"$ne": null}` or similar payloads.
- **File**: `6-flag.txt`

---

### 7. NoSQLi - Enumerating for Profit
- **Goal**: Enumerate accounts, acquire at least 1 HBTNc coin, and get the flag.
- **File**: `7-flag.txt`

---

## 📝 Requirements

- All scripts must be exactly one line.
- Tested in **Kali Linux**.
- Must follow Betty style (where applicable).
- Use proper input validation and secure coding practices.

---

## 📁 Repository Info

- **Repo**: `holbertonschool-cyber_security`
- **Directory**: `web_application_security/0x03_sql_nosql_injection`

---

## 🚀 Conclusion

This project provided hands-on experience with both SQL and NoSQL injection vectors in a controlled lab environment. Through various creative challenges, it highlights the risks of poor input validation and insecure coding practices, and reinforces the need for proper security testing techniques.

---

