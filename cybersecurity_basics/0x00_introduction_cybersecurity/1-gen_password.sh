#!/bin/bash
head -c 100 /dev/urandom | tr -cd '[:alnum:]' | head -c "$1"
