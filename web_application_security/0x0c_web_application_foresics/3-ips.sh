#!/bin/bash

grep "Accepted password for" auth.log | grep -oP 'from \K[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | sort | uniq | wc -l
