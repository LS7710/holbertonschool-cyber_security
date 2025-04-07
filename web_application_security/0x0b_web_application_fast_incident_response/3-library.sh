#!/bin/bash

attacker_ip=$(cat logs.txt | cut -d ' ' -f 1 | sort | uniq -c | sort -nr | head -n 1 | awk '{print $2}')

cat logs.txt | grep "^$attacker_ip " | cut -d '"' -f 6 | sort | uniq -c | sort -nr | head -n 1 | awk '{$1=""; print $0}' | sed 's/^ *//'
