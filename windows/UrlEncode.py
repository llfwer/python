# coding:utf-8

import sys
import urllib
from urllib import parse


def main(argv=None):
    if argv is None:
        argv = sys.argv
    if argv[1] is not None:
        print(urllib.parse.quote(argv[1]))


if __name__ == '__main__':
    main()
