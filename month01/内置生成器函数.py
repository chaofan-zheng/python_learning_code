list01 = ['a', 'b', 'c', 'd']
for item in enumerate(list01):
    print(item)
# 作用，把索引和元素组合成元组返回

list02 = ['e', 'f', 'g', 'k']
for item in zip(list01,list02):
    print(item)
iterator = iter(list02)
print(iterator.__next__())

with open('生成器.py','r') as f:
    print(f.__next__())

