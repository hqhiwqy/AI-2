# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    PostId = scrapy.Field()
    RecruitPostName = scrapy.Field()
    LocationName = scrapy.Field()
    CategoryName = scrapy.Field()
    Responsibility = scrapy.Field()
    Requirement = scrapy.Field()
