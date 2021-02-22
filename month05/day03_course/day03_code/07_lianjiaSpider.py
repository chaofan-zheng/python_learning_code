"""
【1】链家二手房爬虫
    # 注意: 一切以响应内容为准
	1.1> 官网地址：进入链家官网，点击二手房 : https://bj.lianjia.com/ershoufang/
	1.2> 目标 : 抓取100页的二手房源信息，包含房源的：
    	名称
    	地址
    	户型、面积、方位、是否精装、楼层、年代、类型
    	总价
    	单价
    1.3> 数据处理
    	将数据分别存入：MySQL、MongoDB、csv文件中

【2】抓取快代理网站免费高匿代理，并测试是否可用来建立自己的代理IP池
    https://www.kuaidaili.com/free/
"""

class LianjiaSpider:
    def __init__(self):
        self.url = 'https://bj.lianjia.com/ershoufang/'
    def get_html(self):