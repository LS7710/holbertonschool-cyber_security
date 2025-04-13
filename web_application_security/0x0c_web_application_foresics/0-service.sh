#!/bin/bash

cat auth.log | grep "pam_unix" | cut -d '(' -f 2 | cut -d ')' -f 1 | cut -d ':' -f 1 | sort | uniq -c | sort -nr
