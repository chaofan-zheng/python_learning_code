# Scrapy settings for HouseInformation project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'HouseInformation'

SPIDER_MODULES = ['HouseInformation.spiders']
NEWSPIDER_MODULE = 'HouseInformation.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'HouseInformation (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

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
DEFAULT_REQUEST_HEADERS = {
    'cookie': """f=n; f=n; id58=QadTkmBr7lRNRuVBHWFaAg==; city=hz; 58home=hz; commontopbar_new_city_info=79%7C%E6%9D%AD%E5%B7%9E%7Chz; commontopbar_ipcity=hz%7C%E6%9D%AD%E5%B7%9E%7C0; 58tj_uuid=565b8c6d-ea5f-496e-9e46-881148bdce44; new_uv=1; utm_source=; spm=; init_refer=; wmda_uuid=94eeee6ecf371c102e247dcd654c63fb; wmda_new_uuid=1; wmda_visited_projects=%3B11187958619315; als=0; xxzl_deviceid=rjee4icNkU0U8pCRx%2BuXBBC1VI7NSEKsDtx%2B%2FHM0QcCNz96FEqSCCx8VsjH0xHp0; sessid=E53864F5-3CD2-4668-95E1-6E0A8FD90AEA; aQQ_ajkguid=633F93FB-B5C7-4879-9FDD-CECFDEA59A96; 58_ctid=79; is_58_pc=1; commontopbar_new_city_info=18%7C%E6%9D%AD%E5%B7%9E%7Chz; wmda_visited_projects=%3B11187958619315%3B8788302075828; new_session=0; __xsptplus8=8.1.1617686155.1617686155.1%234%7C%7C%7C%7C%7C%23%23RvKeLkQj_cDyvyxiaNXSCDycgmRjy5b-%23; ctid=79; xxzl_cid=cf020687519e4ce0a778bbc689b6cb29; xzuid=92a26c02-85d8-43d0-8eb3-6621512a8f90""",
    'user-agent': """Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"""
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'HouseInformation.middlewares.HouseinformationSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'HouseInformation.middlewares.HouseinformationDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'HouseInformation.pipelines.HouseinformationPipeline': 300,
# }

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
