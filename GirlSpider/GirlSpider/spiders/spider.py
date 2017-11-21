# -*-coding:utf-8-*-
from scrapy.spiders import CrawlSpider

from GirlSpider.items import GirlSpiderItem


class ListSpider(CrawlSpider):
    # 爬虫名称
    name = "girl"
    # 设置下载延时
    download_delay = 1
    # 允许域名
    allowed_domains = ["www.360doc.com"]
    # 开始URL
    start_urls = [
        "http://www.360doc.com/content/13/0728/11/2262479_303088135.shtml"
    ]

    # 解析内容函数
    def parse(self, response):
        info_list = response.selector.xpath('//ul[@class="paixulist"]')

        for index, info in enumerate(info_list):
            item = GirlSpiderItem()
            item['name'] = info.xpath('li/a/text()')[0].extract()
            item['desc'] = info.xpath('li/img/@alt')[0].extract()
            item['image'] = info.xpath('li/img/@src')[0].extract()
            item['link'] = info.xpath('li/a/@href')[0].extract()
            yield item
