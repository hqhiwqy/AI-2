import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sun.items import SunItem
import urllib.parse

class PoliticalSpider(CrawlSpider):
    name = 'political'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'id=1&page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        node_list = response.xpath('//ul[@class="title-state-ul"]/li')
        for li in node_list:
            no = li.xpath('./span[@class="state1"]/text()').extract_first()
            title = li.xpath('./span[@class="state3"]/a/text()').extract_first()
            detail_href = li.xpath('./span[@class="state3"]/a/@href').extract_first()
            # print(detail_href)
            full_detail_href = urllib.parse.urljoin(response.url, detail_href)
            # print(full_detail_href)
            # scrapy.Request(full_detail_href, callback=self.parse_detail)
            item = SunItem()
            item['no'] = no
            item['title'] = title
            yield scrapy.Request(full_detail_href, callback=self.parse_detail, meta={"data": item})

    def parse_detail(self, response):
        item = response.meta['data']
        item['content'] = response.xpath('//div[@class="details-box"]/pre/text()').extract_first()
        return item