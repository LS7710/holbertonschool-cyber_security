#!/bin/bash
sestatus | awk '/SELinux status/ {print}'
