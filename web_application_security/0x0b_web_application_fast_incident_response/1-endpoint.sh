#!/bin/bash

cat logs.txt | cut -d '"' -f 2 | cut -d ' ' -f 2 | sort | uniq -c | sort -nr | head -n 1 | awk '{print $2}'
