#!/usr/bin/env python3

import sys
params = sys.argv[1:]

if len(params) == 0:
    print("none")
else:
    print(f"parameters: {len(params)}")
    for word in params:
        print(f"{word}: {len(word)}")
