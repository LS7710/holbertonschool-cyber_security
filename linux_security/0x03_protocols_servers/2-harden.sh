#!/bin/bash
sudo find / -xdev -type d -perm -0002 -print -exec chmod o-w {} +
