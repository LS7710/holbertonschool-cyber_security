#!/bin/bash
sudo find / -type d -perm -0002 -print -exec chmod o-w {} +
