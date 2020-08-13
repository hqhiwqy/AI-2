# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    no = scrapy.Field()  # 问题编号
    title = scrapy.Field()  # 问题标题
    content = scrapy.Field()  # 问题的内容
