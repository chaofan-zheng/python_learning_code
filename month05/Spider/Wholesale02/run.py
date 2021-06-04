from scrapy import cmdline

cmdline.execute('scrapy crawl wholesale -o wholesale.csv'.split())
