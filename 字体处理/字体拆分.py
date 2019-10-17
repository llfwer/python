#!/usr/bin/python
import sys

from fontTools import subset

# 测试使用
# sys.argv = ['字体拆分.py', '.\data\Funkster.ttf']
sys.argv = ['字体拆分.py', '.\data\HARLOWSI.TTF']

if len(sys.argv) < 2:
    print("Usage : 字体拆分.py in.ttx")
    sys.exit(1)

ttx_file = sys.argv[1]
del sys.argv

ops = subset.Options()
font = subset.load_font(ttx_file, ops)

sub = subset.Subsetter(ops)
sub.populate(text='Google')
sub.subset(font)

ops.flavor = 'woff'

subset.save_font(font, '.\data\sub.woff', ops)

font.close()

# sub.woff 在 windows 上利用 FontCreator 软件导出成ttf文件 即可使用
