#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=nt "$1" && john --show --format=nt "$1" | tail -n +2 | awk -F: '{print $2}' > 5-password.txt
