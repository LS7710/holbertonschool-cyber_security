# 🛡️ Burp Suite - Fundamentals

## 📚 Project Overview

This project dives into the essential tools and techniques of **Burp Suite**, a powerful platform for performing security testing of web applications. It guides the learner through real-world use cases including interception, response tampering, brute-force attacks, token analysis, and privilege escalation.

> ✅ **Fully completed** — Each task was performed in a simulated web application environment using Burp Suite Community Edition.

---

## 🎯 Learning Objectives

By the end of this project, I was able to:

- Set up Burp Suite and intercept HTTPS traffic
- Install and use client-side TLS certificates
- Modify HTTP responses in real time
- Brute-force authentication with Repeater and Intruder
- Analyze tokens with Sequencer
- Manipulate Bearer tokens using Decoder

---

## 🛠️ Tools & Technologies

- **Burp Suite Community Edition**
- **Kali Linux 2023.2**
- HTTPS Proxy Configuration
- Decoder, Repeater, Intruder, Sequencer
- TLS Certificate installation
- Base64 and GZIP decoding

---

## 📁 Project Structure

```
web_application_security/
└── 0x02_burpsuite_fundamentals/
    ├── 0-flag.txt
    ├── 1-flag.txt
    ├── 2-flag.txt
    ├── 3-flag.txt
    ├── 4-flag.txt
    ├── 5-flag.txt
    ├── 6-flag.txt
```

---

## ✅ Tasks Breakdown

### 🔧 0. Getting Started with Burp Suite
- Installed and configured Burp Suite proxy
- Installed TLS CA certificate
- Found the hidden flag inside the server’s TLS certificate

---

### 🔒 1. Client-Side TLS Authentication
- Downloaded `.p12` certificate and imported it into Burp Suite
- Successfully authenticated to access restricted content and reveal the flag

---

### ✏️ 2. Modifying Page Responses
- Intercepted a response on `/task2`
- Modified JSON body to expose hidden flag content via spoofing

---

### 🔁 3. Repeater Tool Exploration
- Used Burp’s Repeater tool to brute-force login credentials
- Gained unauthorized access and extracted the flag

---

### 🔫 4. Intruder: Hidden Profiles
- Captured request with profile ID parameter
- Configured Intruder to fuzz a numeric range
- Found valid profile and retrieved its flag

---

### 🔍 5. Sequencer: Token Analysis
- Captured and analyzed multiple session tokens
- Identified skipped/valid session and hijacked it by cookie replacement
- Flag revealed after impersonating a valid session

---

### 🔓 6. Decoder: Bearer Token Escalation
- Intercepted and Base64-decoded a token
- GZIP decompressed the payload
- Changed `"admin": false` → `"admin": true`
- Re-encoded and replayed the token to escalate privilege
- Flag revealed on elevated response

---

## 🚀 Project Status

✅ **Fully Completed**  
This hands-on project offered extensive experience in using Burp Suite for security auditing and exploitation. From TLS interception to token tampering, each module reinforced critical web security concepts.

---
