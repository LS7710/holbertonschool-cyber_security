#!/bin/bash
sudo iptables -P INPUT DROP && sudo iptables -A INPUT -p tcp --dport ssh -j ACCEPT
sudo iptables -A INPUT -j DROP && sudo iptables -P FORWARD DROP && sudo iptables -P OUTPUT ACCEPT
