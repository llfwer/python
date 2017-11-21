import os
import re
import sys
import urllib
import urllib.request
import zlib

import chardet
import requests
from bs4 import BeautifulSoup


def decode(html):
    guess = chardet.detect(html)
    gc = guess['encoding']
    sc = sys.getdefaultencoding()
    if gc == sc:
        return html
    return html.decode(gc, 'ignore').encode(sc)


def unzip(html, response):
    gzipped = response.headers.get('Content-Encoding')  # 查看是否服务器是否支持gzip
    if gzipped:
        html = zlib.decompress(html, 16 + zlib.MAX_WBITS)  # 解压缩，得到网页源码
    return html


def write_to_file(path, text, mode):
    f = open(path, mode, encoding='utf-8')
    f.write(text)
    f.close()


def urllib_get(url, refer=None):
    try:
        request = urllib.request.Request(url)

        request.add_header('Accept-encoding', 'gzip')  # 默认以gzip压缩的方式得到网页内容
        if not (refer is None):
            request.add_header('Referer', refer)

        response = urllib.request.urlopen(request)
        html = response.read()

        if html is None or html.strip() == '':
            return None

        html = unzip(html, response)

        return decode(html)
    except Exception as e:
        print(e)
        return None


def requests_get(url, encoding='utf-8', headers=None):
    try:
        response = requests.get(url, headers=headers)
        response.encoding = encoding
        return response.text
    except Exception as e:
        print(e)
        return None


def load_chapter(base_path, url, title):
    if not os.path.exists(base_path):
        os.makedirs(base_path, exist_ok=True)

    html = requests_get(url, 'gb18030')

    if html is None or html.strip() == '':
        return

    soup = BeautifulSoup(html, 'html.parser')
    content_tag = soup.find_all(class_='yd_text2')

    if not content_tag:
        return

    if not len(content_tag):
        return

    content = content_tag[0].text

    write_to_file(base_path + title + '.txt', title + '\n' + content, 'w')

    print('下载完成 -> ' + title)


def load_wo_de_jun_fa_sheng_ya():
    base_url = 'http://www.88dushu.com/xiaoshuo/21/21450/'

    html = requests_get(base_url, 'gb18030')

    if html is None or html.strip() == '':
        return

    # 过滤目录
    reg = re.compile(r'<li><a href="(\d+\.html)">(.*?)</a></li>')
    req = re.findall(reg, html)

    for i in req:
        chapter_url = base_url + i[0]
        title = i[1]
        load_chapter('D:\我的军阀生涯\\', chapter_url, title)


class ChineseToDigits:
    def __init__(self):
        self.dict = {'零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8,
                     '九': 9, '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000}

    def chinese2digits(self, uchars_chinese):
        total = 0
        r = 1  # 表示单位：个十百千...
        for i in range(len(uchars_chinese) - 1, -1, -1):
            val = self.dict.get(uchars_chinese[i])
            if val >= 10 and i == 0:  # 应对 十三 十四 十*之类
                if val > r:
                    r = val
                    total = total + val
                else:
                    r = r * val
                    # total =total + r * x
            elif val >= 10:
                if val > r:
                    r = val
                else:
                    r = r * val
            else:
                total = total + r * val
        return total


def join_text():
    folder = 'D:\\我的军阀生涯'

    if not os.path.exists(folder):
        return

    text_file_list = os.listdir(folder)

    digits = ChineseToDigits()
    file_dict = {}

    for i in text_file_list:
        reg = re.compile(r'第(.*?)章')
        result = re.findall(reg, i.title())
        if not len(result):
            continue
        file_dict.update({digits.chinese2digits(result[0]): i})

    print('文件排序完成')

    target_file = open('D:\\我的军阀生涯.txt', 'w', encoding='utf-8')

    for k, v in file_dict.items():
        text_path = os.path.join(folder, v)
        with open(text_path, encoding='utf-8') as f:
            target_file.write(f.read())
            target_file.flush()
            f.close()
        print('文件合并完成 -> ' + v)
    target_file.close()


def selenium_chrome():
    import time
    from selenium import webdriver

    # 引入chromedriver.exe
    chromedriver = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver

    driver = webdriver.Chrome(chromedriver)
    driver.get("http://www.baidu.com")

    driver.find_element_by_id("kw").clear()
    driver.find_element_by_id("kw").send_keys("Python")
    driver.find_element_by_id("su").click()
    time.sleep(5)
    driver.quit()


def load_chapter(url):
    html = requests_get(url, 'gb18030')

    if html is None or html.strip() == '':
        return None

    soup = BeautifulSoup(html, 'html.parser')
    content_tag = soup.find_all(id='content')

    if not content_tag:
        return None

    if not len(content_tag):
        return None

    return content_tag[0].text
