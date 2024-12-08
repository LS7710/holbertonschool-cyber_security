#!/bin/bash
echo "$2  $1" | sha256sum -c - && echo "ok" || echo "fail"
