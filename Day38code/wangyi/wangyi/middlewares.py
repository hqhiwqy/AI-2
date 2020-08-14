import scrapy
import time


# 自定义爬虫news的下载中间件
class NewsDownloaderMiddleware:

    def process_response(self, request, response, spider):
        # 判断哪些响应对象是属于5大分类的请求返回的，如果是就对响应对象进行处理
        if response.url in spider.urls:
            brower = spider.brower
            brower.get(response.url)

            # 鼠标滚动到底部
            brower.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            brower.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            brower.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)

            # 获取携带了新闻数据的页面的html源码
            page_html = brower.page_source

            # 实例化一个新的响应对象
            new_response = scrapy.http.HtmlResponse(url=response.url, body=page_html, encoding='utf-8', request=request)
            return new_response
        else:
            return response