#!/bin/bash

cat logs.txt | cut -d ' ' -f 1 | sort | uniq -c | sort -nr | head -n 1 | awk '{print $1}'
