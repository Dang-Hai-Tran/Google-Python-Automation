#!/usr/bin/env python3

import sys
import subprocess

with open("oldFiles.txt", mode='r') as old_file:
    old = old_file.readlines()
    new = [file.replace('jane', 'jdoe') for file in old]
    for i in range(len(old)):
        subprocess.run(['mv', f"..{old[i].strip()}", f"..{new[i].strip()}"])
