# 🛡️ Introduction to Cybersecurity – Bash Scripting Basics

## 📚 Project Overview

This project is part of the **Cybersecurity Specialization (Part 1)** at Holberton School and serves as an introduction to core cybersecurity concepts and basic Bash scripting on Kali Linux. The tasks are designed to build familiarity with fundamental security principles, Linux command-line tools, and automation through scripting.

---

## 🎯 Learning Objectives

By completing this project, I gained the ability to explain and apply key cybersecurity concepts, including:

- What is Cybersecurity?
- The **CIA Triad**: Confidentiality, Integrity, and Availability
- Encryption fundamentals
- Risk management in cybersecurity
- Types of cybersecurity threats (e.g., viruses vs. worms)
- Social engineering techniques
- Security policies and frameworks (e.g., OWASP, NIST)
- Role of access control and multi-factor authentication (MFA)
- Network security techniques

---

## 🛠️ Technologies Used

- **Operating System**: Kali Linux 2023.2
- **Shell**: Bash
- **Tools & Commands**: `ps`, `grep`, `sha256sum`, `/dev/urandom`, `ssh-keygen`

---

## 📁 Project Structure

```
cybersecurity_basics/
└── 0x00_introduction_cybersecurity/
    ├── 0-release.sh              # Display Kali's distro ID
    ├── 1-gen_password.sh         # Generate a strong random password
    ├── 2-sha256_validator.sh     # Validate a file’s integrity via SHA-256
    ├── 3-gen_key.sh              # Generate a 4096-bit RSA SSH key pair
    └── 4-root_process.sh         # Monitor processes by a specific user
```

---

## 🧪 Tasks Breakdown

### ✅ 0. Did You Install Kali?

- **Script:** `0-release.sh`  
- **Goal:** Output the distribution ID of the current system  
- **Constraints:** One-line script, no `awk`, no `printf`

---

### ✅ 1. We Always Need Strong Passwords

- **Script:** `1-gen_password.sh`  
- **Goal:** Generate a strong alphanumeric password using `/dev/urandom`  
- **Arguments:** Password length  
- **Example:**

```bash
./1-gen_password.sh 20
# Output: MkPpprPyC3i6navUB3Lj
```

---

### ✅ 2. Verify the Integrity of a File

- **Script:** `2-sha256_validator.sh`  
- **Goal:** Compare a file’s SHA-256 hash to a known value  
- **Arguments:** Filename, Expected hash  
- **Example:**

```bash
./2-sha256_validator.sh test_file e3b0c44298fc1...
# Output: test_file: OK
```

---

### ✅ 3. We Need an SSH Key Pair!

- **Script:** `3-gen_key.sh`  
- **Goal:** Generate a 4096-bit RSA key using OpenSSH  
- **Arguments:** Output filename  
- **Output:** Creates `new_key` (private) and `new_key.pub` (public) files

---

### ✅ 4. Let's Monitor Root Activity

- **Script:** `4-root_process.sh`  
- **Goal:** List all active processes by a given user  
- **Arguments:** Username  
- **Example:**

```bash
./4-root_process.sh root
```

---

## ⚙️ Requirements & Constraints

- All scripts are written in **Bash** and run on **Kali Linux 2023.2**
- Must follow **Betty coding style**
- All scripts are **<3 lines**
- **Disallowed:** `&&`, `||`, `;`, backticks, `printf`
- **Allowed editors:** `vi`, `vim`, `emacs`

---

## 📖 References

- [OWASP Top Ten](https://owasp.org)
- [CISA](https://www.cisa.gov)
- [NIST](https://www.nist.gov)
- [SANS Institute](https://www.sans.org)
- [ISC²](https://www.isc2.org)
- [ISF](https://www.securityforum.org)

---

## 🚀 Project Status

✅ **Completed** — All tasks passed with 100%  
📌 This project lays the foundation for deeper cybersecurity exploration, including threat analysis, penetration testing, and ethical hacking.

---
