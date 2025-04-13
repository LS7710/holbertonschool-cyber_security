#!/bin/bash

cat auth.log | grep "sshd" | grep "Accepted password" | awk '{for(i=1;i<=NF;i++){if($i=="from"){print $(i+1)}}}' | sort | uniq | wc -l
