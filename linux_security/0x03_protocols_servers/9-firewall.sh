#!/bin/bash
sudo iptables -P INPUT DROP && sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -P FORWARD DROP && sudo iptables -P OUTPUT ACCEPT
