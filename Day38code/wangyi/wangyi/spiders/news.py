import scrapy
from selenium import webdriver
from wangyi.items import WangyiItem


class NewsSpider(scrapy.Spider):
    name = 'news'
    # allowed_domains = ['news.163.com']
    start_urls = ['http://news.163.com/']

    # chromedriver 驱动文件，这里需要换成你自己电脑里的驱动文件路径
    chrome_driver = "D:/PCDownload/chromedriver_win32/chromedriver"

    urls = []  # 定义需要爬取的分类url

    # 实例化一个浏览器对象
    brower = webdriver.Chrome(executable_path=chrome_driver)

    def parse(self, response):
        li_list = response.xpath('//div[@class="ns_area list"]/ul/li')
        for index in [3, 4, 6, 7, 8]:
            li = li_list[index]
            new_url = li.xpath('./a/@href').extract_first()
            self.urls.append(new_url)
            # 根据这5大类对应的url进行发送请求
            yield scrapy.Request(url=new_url, callback=self.parse_news)

    # 用来解析每一个分类对应的新闻数据（目前只能解析新闻标题）
    def parse_news(self, response):
        div_list = response.xpath('//div[@class="ndi_main"]/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()

            item = WangyiItem()
            item['title'] = title
            # 根据新闻详情页url进行发送请求
            yield scrapy.Request(url=detail_url, callback=self.parse_news_detail, meta={"data": item})

    def parse_news_detail(self, response):
        item = response.meta['data']

        if response.xpath('//div[@id="endText"]'):
            content = response.xpath('//div[@id="endText"]').extract_first()
        elif response.xpath('//div[@id="content"]'):
            content = response.xpath('//div[@id="content"]').extract_first()

        item['content'] = content

        yield item

    def close(self, spider):
        print("---------爬虫整体结束---------")
        # 爬虫结束后，记得关闭浏览器对象
        self.brower.quit()