#!/usr/bin/python
import sys

from fontTools import ttx

# 测试使用
sys.argv = ['创建ttx.py', '.\data\\test.ttf']

if len(sys.argv) < 2:
    print("Usage : 创建ttx.py out.ttx")
    sys.exit(1)

ttx_file = sys.argv[1]
del sys.argv

font = ttx.TTFont()

font.save(ttx_file)

font.close()
