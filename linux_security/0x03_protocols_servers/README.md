# Protocols and Servers - Cybersecurity Project

## 🧠 Description

This project explores essential protocols and services in network security, including NFS, SMTP, SNMP, and firewall configurations. It focuses on auditing, hardening, and analyzing Linux servers using security tools and bash scripting.

---

## 🛠️ Tasks & Objectives

### 0. Analyze iptables Rules
- Display all current `iptables` rules with line numbers.
- ✅ Tool: `iptables`

### 1. Audit SSH Configuration
- Identify non-standard SSH settings in `/etc/ssh/sshd_config`.
- ✅ Tool: `grep`, `cat`

### 2. Harden Linux Server
- Detect world-writable directories and restrict their permissions.
- ✅ Tool: `find`, `chmod`

### 3. Identify Common Vulnerabilities
- Perform a system audit using **Lynis** to uncover unpatched security issues.
- ✅ Tool: `lynis`

### 4. Check for NFS Vulnerabilities
- Scan for open and publicly accessible NFS shares on the network.
- ✅ Tool: `showmount`

### 5. Audit SNMP Configuration
- Locate SNMP settings that expose community strings like `public`.
- ✅ Tool: `grep` or `cat` on `snmpd.conf`

### 6. Examine SMTP Server Settings
- Verify if the SMTP server uses STARTTLS or other encryption mechanisms.
- ✅ Tool: `grep` or config inspection

### 7. Simulate DoS Attack on HTTP Server
- Launch a basic DoS attack using `hping3` to simulate flooding traffic.
- ✅ Tool: `hping3`

### 8. Check for Weak SSL/TLS Ciphers
- Use `nmap` to identify SSL/TLS ciphers and flag any weak configurations.
- ✅ Tool: `nmap --script ssl-enum-ciphers`

### 9. Implement Basic Firewall Rules
- Set `iptables` rules to block all traffic except SSH (port 22).
- ✅ Tool: `iptables`

---

## 📚 Learning Outcomes

- Analyze and secure core Linux services and ports.
- Detect and mitigate common protocol-based vulnerabilities.
- Utilize tools like `iptables`, `lynis`, `nmap`, and `hping3`.
- Harden systems using security best practices and scripting.

---

## 🧰 Tools Used

- `iptables`
- `lynis`
- `nmap`
- `hping3`
- `showmount`
- `grep`, `find`, `chmod`

---

## ✅ Result

**Project badge earned: 100% 🏅**  
Mastered defensive scripting, protocol hardening, and system auditing.

---

## Author

**Maroua – Cybersecurity Track | C#23**
