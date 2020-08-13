# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo


class ZhipinspiderPipeline:

    def process_item(self, item, spider):

        # return item
        print(item)
        # print("岗位名称：{}".format(item['name']))

        # # 链接MongoDB数据库
        # client = pymongo.MongoClient("127.0.0.1", 27017)
        #
        # # 指定数据库
        # db = client.zhipin
        #
        # # 指定集合
        # collection = db.job
        #
        # # 插入文档到集合
        # collection.insert_one(dict(item))
