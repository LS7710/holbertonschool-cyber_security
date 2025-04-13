#!/bin/bash

tail -n 1000 auth.log | grep "Accepted password for" | awk '{for(i=1;i<=NF;i++){if($i=="from"){print $(i+1)}}}' | sort | uniq | wc -l
