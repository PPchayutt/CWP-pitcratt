#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
    text = sys.argv[1]
    z_count = text.count('z')

    if z_count > 0:
        print("z" * z_count)
    else:
        print("none")
else:
    print("none")
