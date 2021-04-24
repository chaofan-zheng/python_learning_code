from scrapy import cmdline

cmdline.execute('scrapy crawl houseInformation -o HouseInformation.csv'.split())
