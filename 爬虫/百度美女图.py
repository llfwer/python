# -*- coding:utf-8 -*-
import re

import HtmlUtils

url = 'http://www.27270.com/tag/441_2.html'


def get_girls_url():
    html = HtmlUtils.get(url, 'gb18030')

    if html is None or html.strip() == '':
        return

    reg = re.compile(r'<img alt="\w+?" src="(.*?)" width="\d+" width="\d+" height="\d+"/>')
    req = re.findall(reg, html)

    for i in req:
        print(i)


get_girls_url()
