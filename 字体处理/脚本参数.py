#!/usr/bin/python

import sys

if len(sys.argv) < 4:
    print("Usage : 脚本参数.py param1 param2 param3...")
    sys.exit(1)

param0 = sys.argv[0]
param1 = sys.argv[1]
param2 = sys.argv[2]
param3 = sys.argv[3]
del sys.argv

print('param 0 : %s , param 1 : %s , param 2 : %s , param 3 : %s' % (param0, param1, param2, param3))
