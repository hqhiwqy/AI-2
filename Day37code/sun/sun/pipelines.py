# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class SunPipeline:
    def process_item(self, item, spider):
        client = pymongo.MongoClient('127.0.0.1', 27017)

        db = client.sun

        political_collection = db.political

        political_collection.insert_one(dict(item))
