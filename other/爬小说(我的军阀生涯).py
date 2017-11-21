# -*- coding:utf-8 -*-
import re

import Utils

base_url = 'http://www.zwdu.com/book/19898/'

html = Utils.requests_get(base_url, 'gb18030')

if html is not None and html.strip() != '':
    reg = re.compile(r'<dd><a href="/book/19898/(\d+\.html)">(.*?)</a></dd>')
    req = re.findall(reg, html)

    f = open('D:\\宇宙交易平台.txt', 'a', encoding='utf-8')

    for i in req:
        chapter_url = base_url + i[0]
        title = i[1]
        chapter = Utils.load_chapter(chapter_url)
        f.write(title + '\r\n' + chapter + '\r\n')
        f.flush()
        print('下载完成 -> ' + title)

    f.close()
    print('全部下载完成!')
