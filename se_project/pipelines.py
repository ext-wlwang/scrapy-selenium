# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy import Item
import pymongo



class SeProjectPipeline:
    def process_item(self, item, spider):
        return item


class MongoDBPipeline(object):
    """
    将item写入MongoDB
    """

    @classmethod
    def from_crawler(cls, crawler):
        cls.DB_URL = crawler.settings.get('MONGO_DB_URI', 'mongodb://wangweiliang:9eTmHHpk@192.168.10.105:32771/')
        cls.DB_NAME = crawler.settings.get('MONGO_DB_NAME', 'crawler_test')
        return cls()

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.DB_URL)
        self.db = self.client[self.DB_NAME]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection = self.db[spider.name]
        post = dict(item) if isinstance(item, Item) else item
        collection.insert_one(post)
        return item
