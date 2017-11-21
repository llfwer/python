# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class GirlSpiderPipeline(object):
    def __init__(self):
        try:
            self.db = pymysql.connect(host="localhost", user="root", password="123456", db="test", port=3306)
            self.cur = self.db.cursor()
        except Exception as e:
            print(e)

    def __del__(self):
        try:
            self.cur.close()
            self.db.close()
        except Exception as e:
            print(e)

    def process_item(self, item, spider):
        self.save_to_mysql(item)
        print(item['name'] + ' - > 保存完毕')
        return item

    def save_to_mysql(self, item):
        sql_insert = """insert into girl(_name,_desc,_image,_link) values('%s','%s','%s','%s')"""

        try:
            self.cur.execute(sql_insert % (item['name'], item['desc'], item['image'], item['link']))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
