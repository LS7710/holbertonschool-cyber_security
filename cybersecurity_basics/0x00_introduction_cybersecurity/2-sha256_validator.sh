#!/bin/bash
if echo "$2  $1" | sha256sum -c --status; then echo "$1: OK"; else echo "$1: FAIL"; fi
