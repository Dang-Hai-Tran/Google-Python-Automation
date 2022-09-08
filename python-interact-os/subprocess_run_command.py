#!/usr/bin/env python3

import subprocess

result = subprocess.run(["ls", "-lA"], capture_output=True)
print(result.returncode)
print(result.stdout.decode())
