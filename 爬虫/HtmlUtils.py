import sys

import chardet
import requests


def decode(html):
    guess = chardet.detect(html)
    gc = guess['encoding']
    sc = sys.getdefaultencoding()
    if gc == sc:
        return html
    return html.decode(gc, 'ignore').encode(sc)


def get(url, encoding='utf-8', headers=None):
    try:
        response = requests.get(url, headers=headers)
        response.encoding = encoding
        return response.text
    except Exception as e:
        print(e)
        return None
