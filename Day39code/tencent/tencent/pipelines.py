# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo
from itemadapter import ItemAdapter


class TencentPipeline:
    def process_item(self, item, spider):
        # 连接到MongoDB数据库服务器
        client = pymongo.MongoClient('127.0.0.1', 27017)

        # 指定数据库
        db = client.tencent

        # 指定集合
        news_collection = db.career

        # 插入文档
        news_collection.insert_one(dict(item))
