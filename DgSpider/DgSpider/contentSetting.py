# -*- coding: utf-8 -*-

# Scrapy settings for DgSpider project

# 图片储存
IMAGES_STORE = 'D:\\pics\\jfss\\'

# 爬取域名
DOMAIN = 'nrsfh.com'

# 图片域名前缀
DOMAIN_HTTP = "http:"

# 随机发帖用户
CREATE_POST_USER = '37619,18441390'

# 爬虫名
SPIDER_NAME = 'DgContentSpider'

# 文章URL爬取规则XPATH
POST_TITLE_XPATH = '//div[@class="title"]'
POST_CONTENT_XPATH = '//div[@class="bodycss"]'
