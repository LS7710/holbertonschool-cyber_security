#!/bin/bash
subfinder -d "$1" -silent | xargs -I {} sh -c 'echo -n "{},"; dig +short {} | tail -n1' > "$1.txt"
