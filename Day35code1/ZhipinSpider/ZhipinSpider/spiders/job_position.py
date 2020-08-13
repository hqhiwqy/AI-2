import scrapy
from ZhipinSpider.items import ZhipinspiderItem
import time


class JobPositionSpider(scrapy.Spider):
    name = 'job_position'  # 指定 Spider 名称
    allowed_domains = ['zhipin.com']  # 限制爬取的域名
    start_urls = ['http://www.zhipin.com/']  # 自动爬取的页面URL

    # 定义需要爬取的页面，这里搜索的是全国-python
    position_url = "https://www.zhipin.com/c100010000/?query=python"

    # 当前页码
    current_page = 1

    # 重写start_requests()方法，Scrapy 引擎默认会自动调用一次
    def start_requests(self):
        return [self.next_request()]

    def parse(self, response):

        # 获取当前页面下所有的招聘数据
        node_list = response.xpath('//div[@id="main"]/div/div[2]/ul/li')

        # 循环解析页面的数据
        for node in node_list:
            item = ZhipinspiderItem()
            item['name'] = node.xpath('.//div[@class="job-title"]/span[1]/a/text()').extract()[0]
            item['salary'] = node.xpath('.//div[@class="job-limit clearfix"]/span/text()').extract()[0]
            item['address'] = node.xpath('.//div[@class="job-title"]/span[2]/span/text()').extract()[0]
            item['years'] = node.xpath('.//div[@class="job-limit clearfix"]/p/text()').extract()[0]
            item['education'] = node.xpath('.//div[@class="job-limit clearfix"]/p/text()').extract()[1]
            item['company_name'] = node.xpath('.//div[@class="company-text"]/h3/a/text()').extract()[0]
            item['company_type'] = node.xpath('.//div[@class="company-text"]/p/a/text()').extract()[0]
            company = node.xpath('.//div[@class="company-text"]/p/text()').extract()
            item['company_scale'] = company[0]
            item['company_finance'] = company[1]
            yield item

        self.current_page += 1

        # 最多爬2页
        if self.current_page > 1:
            print("全部数据爬取完毕！")
        else:
            time.sleep(5)
            # 使用 yield 语句将 item 对象返回给 Scrapy 引擎。这里不能用return，因为return会导致整个方法返回，循环不能继续执行
            # 而 yield 将会创建一个生成器。
            yield self.next_request()

    def next_request(self):
        """
        请求下一页
        :return:
        """
        return scrapy.http.FormRequest(self.position_url + ("&page=%d&ka=page-%d" % (self.current_page,
                                                                                     self.current_page)),
                                       callback=self.parse)