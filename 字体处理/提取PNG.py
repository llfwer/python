#!/usr/bin/python

import sys

from fontTools import ttx

# 测试使用
sys.argv = ['提取PNG.py', '.\data\Funkster.ttf']

if len(sys.argv) < 2:
    print("Usage : 提取PNG.py in.ttf")
    sys.exit(1)

ttx_file = sys.argv[1]
del sys.argv

font = ttx.TTFont(ttx_file)

if font is None:
    sys.exit(1)

print(font.keys())

font.close()
