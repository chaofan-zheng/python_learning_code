# Scrapy settings for Wholesale project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Wholesale'

SPIDER_MODULES = ['Wholesale.spiders']
NEWSPIDER_MODULE = 'Wholesale.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Wholesale (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False
cookie = "cna=p4vBF6s8S3cCAXAObY5XttFY; cookie2=1c73ba2a52ae3b803a301ba8acb6bd00; hng=CN%7Czh-CN%7CCNY%7C156; t=254b9eeb2fb1019f5c5eb6453d03d9da; _tb_token_=e1b859e63a1ee; __cn_logon__=false; ali_ab=39.182.24.103.1618932554145.6; _csrf_token=1618932554546; xlly_s=1; tfstk=cHx1BJfIgIKUqJu4bdMU0MkswLfca9E1LA1HCU1328-QFrAA9s474_wWCKVLvaBC.; l=eBjAKrdqjB4VkEg2BO5Cnurza77tgCdb8EVzaNbMiIncC60GYbv84FKQDvzG7F-RJJXcGHLH4IVQ8KwTYUY07M3hDsSzzIC0JxH2Bef..; isg=BDExyMIU9b5JAVmqcLzalBxCQLvLHqWQ8RwUGhNDu_xaOlCMWWukYMoQXcZcxj3I"
header = {
    "accept-encoding": "gzip, deflate",
    "accept-language": "en,zh;q=0.9,zh-CN;q=0.8",
    "cache-control": "max-age=0",
    "Connection": "keep-alive",
    "cookie": "{}".format(cookie),
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
}
# Override the default request headers:
DEFAULT_REQUEST_HEADERS = header
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',

#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Wholesale.middlewares.WholesaleSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Wholesale.middlewares.WholesaleDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'Wholesale.pipelines.WholesalePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
