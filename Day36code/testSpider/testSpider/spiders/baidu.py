import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        with open('baidu.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
