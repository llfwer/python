#!/usr/bin/python

import sys

from fontTools import ttx

# 测试使用
# sys.argv = ['查看ttf信息.py', '.\data\Funkster.ttf']
# sys.argv = ['查看ttf信息.py', '.\data\Funkster.xml']
sys.argv = ['查看ttf信息.py', '.\data\emoji.ttf']

if len(sys.argv) < 2:
    print("Usage : 查看ttf信息.py in.ttx")
    sys.exit(1)

ttx_file = sys.argv[1]
del sys.argv

font = None

if ttx_file.endswith('ttf'):
    font = ttx.TTFont(ttx_file)
elif ttx_file.endswith('xml'):
    font = ttx.TTFont()
    font.importXML(ttx_file)

if font is None:
    sys.exit(1)

print('=======GlyphOrder======== ')
order_ = font['GlyphOrder']
if hasattr(order_, 'glyphOrder'):
    orderArr = order_.glyphOrder
    print('order 0 ', orderArr[0])
    print('order 1 ', orderArr[1])
    print('order 2 ', orderArr[2])
    print('order 3 ', orderArr[3])

print('=======head======== ')
head_ = font['head']
print('tableVersion ', head_.tableVersion)
print('magicNumber %#x' % head_.magicNumber)
print('flags ', head_.flags)

print('=======hhea======== ')
hhea_ = font['hhea']
print('tableVersion %#x' % hhea_.tableVersion)
print('ascent ', hhea_.ascent)
print('descent ', hhea_.descent)

print('=======maxp======== ')
maxp_ = font['maxp']
print('tableVersion %#x' % maxp_.tableVersion)
print('numGlyphs ', maxp_.numGlyphs)
print('maxPoints ', maxp_.maxPoints)

print('=======hmtx======== ')
hmtx_ = font['hmtx']
print('notdef ', hmtx_.metrics['.notdef'])
print('uni0020 ', hmtx_.metrics['uni0020'])
print('uni0021 ', hmtx_.metrics['uni0021'])

font.close()
