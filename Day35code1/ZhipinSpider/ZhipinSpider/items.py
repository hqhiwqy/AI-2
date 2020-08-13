# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhipinspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  # 岗位名称
    salary = scrapy.Field()  # 岗位薪资
    address = scrapy.Field()  # 工作地点
    years = scrapy.Field()  # 工作年限
    education = scrapy.Field()  # 学历要求
    company_name = scrapy.Field()  # 公司名称
    company_type = scrapy.Field()  # 公司所在行业
    company_scale = scrapy.Field()  # 公司规模
    company_finace = scrapy.Field()  # 融资情况
