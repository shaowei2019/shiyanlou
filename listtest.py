#!/usr/bin/env python3
import sys
big = []
small = []
for arg in sys.argv[1:]:
    if len(arg) > 3:
        big.append(arg)
    else:
        small.append(arg)
print(' '.join(small))
print(' '.join(big))
