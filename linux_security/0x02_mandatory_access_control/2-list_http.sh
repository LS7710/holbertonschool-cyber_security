#!/bin/bash
semanage port -l | awk '/http/'
