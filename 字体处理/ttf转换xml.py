#!/usr/bin/python

import sys

from fontTools import ttx

# 测试使用
sys.argv = ['ttf转换xml.py', '.\data\Funkster.ttf', '.\data\Funkster.xml']

if len(sys.argv) < 3:
    print("Usage : ttf转换xml.py in.ttx out.xml")
    sys.exit(1)

ttx_file = sys.argv[1]
xml_file = sys.argv[2]
del sys.argv

font = ttx.TTFont(ttx_file)
font.saveXML(xml_file)

font.close()
