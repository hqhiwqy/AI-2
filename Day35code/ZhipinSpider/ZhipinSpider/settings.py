# Scrapy settings for ZhipinSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ZhipinSpider'

SPIDER_MODULES = ['ZhipinSpider.spiders']
NEWSPIDER_MODULE = 'ZhipinSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'ZhipinSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 指定爬虫不遵守爬虫协议
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;'
              'q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'user-agent:': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/84.0.4147.105 Safari/537.36',
    'cookie': '_zp__pub__=; sid=sem_pz_bdpc_dasou_title; __zp__pub__=; __g=sem_pz_bdpc_dasou_title; Hm_lvt_'
              '194df3105ad7148dcf2b98a91b5e727a=1597045844,1597112154; lastCity=100010000; _'
              '_c=1597112154; __l=l=%2Fwww.zhipin.com%2'
              'Fc100010000%2F%3Fquery%3Dpython%26page%3D3&r=https%3A%2F%2Fwww.baidu.com%2'
              'Fother.php%3Fsc.0s00000gPalJQ2RB6IQ4YzK4-J5o0RRKk5xL4tSkoPhjMiup_'
              '6gzcAz7lbj01ljcpUJKPZLZBIjPuI4Ic9dQFe3P6eQ8WfTrueXpXx9CPsgHNFo3lC4S9tP_'
              '9NI233BsK5oaTPpfOmLmzJc638vTpxMj733GTvuJ6cunTWUGkmYndtlRLCaVC6CegrRB-kJ6d'
              '8gmaNk30EyCr79HrIeeMtPyJwaa.7D_NR2Ar5Od663rj6t8AGSPticrtXFBPrM-kt5QxIW94UhmLmry6S9'
              'wiGyAp7BEIu80.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYqmhq1Tqpkko60IgP-T-qYXgK-5H00mywxI'
              'Z-suHY10ZIEThfqmhq1Tqpkko60ThPv5HD0IgF_gv-b5HDdnHbYnjnYnHn0UgNxpyfqnHcLPWTLn'
              'j00UNqGujYknjm3P10vPfKVIZK_gv-b5HDkPHnY0ZKvgv-b5H00pywW5Nwj0APzm1Ykrjfkr0%26ck%3D7'
              '603.1.126.376.161.379.168.301%26dt%3D1597112148%26wd%3Dboss%25E7%259B%25B4%25E8%'
              '2581%2598%26tpl%3Dtpl_11534_22836_18980%26l%3D1519403413%26us%3DlinkName%253D%2525'
              'E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%252'
              '5A8-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%'
              '253DBOSS%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252'
              '580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%25'
              '25BC%25258C%2525E6%252588%252591%2525E8%2525A6%252581%2525E8%2525B7%25259F%2525E'
              '8%252580%252581%2525E6%25259D%2525BF%2525E8%2525B0%252588%2525EF%2525BC%252581%2526l'
              'inkType%253D&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title; __'
              'a=94696129.1597045844.1597045844.1597112154.36.2.21.21; Hm_lpvt_194df3105ad7'
              '148dcf2b98a91b5e727a=1597113561; __zp_stoken_'
              '_=a32daC0NXWGldInEjOnlDfhM4TlNkbStIUjludl5sIRlnKB17BU4zSjgxfyhSDC9HQXZCEwZ%2'
              'FZH4weGQNMW47XkB8CBpeXhAZCnAqdxkBNghhEXEjCjNTQhAeKUIoFAkMA08HbBxfT1V4PGE%3D'

}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'ZhipinSpider.middlewares.ZhipinspiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'ZhipinSpider.middlewares.ZhipinspiderDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 配置使用 Piplines
ITEM_PIPELINES = {
   'ZhipinSpider.pipelines.ZhipinspiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
