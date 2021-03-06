# 4. 通过下列数据结构,实现下列功能.

#     (1).定义函数,打印所有商品信息,
#         格式：商品编号xx,商品名称xx,商品单价xx.
#     (2).定义函数,打印商品单价小于2万的商品信息
#          格式：商品编号xx,商品名称xx,商品单价xx.
#     (3).定义函数,打印所有订单中的商品信息,
#         格式：商品名称xx,商品单价:xx,数量xx.
#     (4).定义函数,查找最贵的商品(使用自定义算法,不使用内置函数)
#     (5).定义函数,根据单价对商品列表升序排列

# 商品列表
list_commodity_infos = [
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]

# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]
