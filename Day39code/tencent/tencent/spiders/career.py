import scrapy
import json
from tencent.items import TencentItem


class CareerSpider(scrapy.Spider):
    name = 'career'
    allowed_domains = ['careers.tencent.com']
    # start_urls = ['http://careers.tencent.com/']

    query_url = "https://careers.tencent.com/tencentcareer/api/post/Query?language=zh-cn&area=cn"
    detail_url = "https://careers.tencent.com/tencentcareer/api/post/ByPostId?language=zh-cn"

    page = 1

    def start_requests(self):
        return [self.next_request()]

    def parse(self, response):
        self.page += 1

        # print(response.text)
        posts = json.loads(response.text)['Data']['Posts']
        # print(posts)

        for value in posts:
            postId = value['PostId']
            detail_url = self.detail_url + "&postId={}".format(postId)
            yield scrapy.Request(url=detail_url, callback=self.parse_detail)

        if self.page > 2:
        # if self.page > 597:
            print('数据全部爬取完毕！')
        else:
            yield self.next_request()

    def parse_detail(self, response):
        item = TencentItem()
        data = json.loads(response.text)['Data']
        item['PostId'] = data['PostId']
        item['RecruitPostName'] = data['RecruitPostName']
        item['LocationName'] = data['LocationName']
        item['CategoryName'] = data['CategoryName']
        item['Responsibility'] = data['Responsibility']
        item['Requirement'] = data['Requirement']
        yield item

    def next_request(self):
        return scrapy.Request(url=self.query_url+'&pageIndex={}&pageSize={}'.format(self.page, 10), callback=self.parse)