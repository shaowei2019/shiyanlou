#!/usr/bin/env python3
import sys
for i in sys.argv[1:]:
    key,value = i.split(':')
    print('ID:{} Name:{}'.format(key,value))
