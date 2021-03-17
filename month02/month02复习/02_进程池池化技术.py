from multiprocessing import Pool
from time import *
from random import random


def worker(msg, sec):
    sleep(sec)
    print(ctime(), '---', msg)


# 创建进程池
pool = Pool(4)  # 不写就代表根据计算机的性能来自动创建池 写4就是四个池子

# 将事件放到池子中
for i in range(1, 21):
    msg = "订单-%d" % i
    pool.apply_async(worker, args=(msg, random() * 3))  # 使用异步方法执行

pool.close()  # 关闭 不能加入新事件

pool.join()  # 阻塞等待进程池运行结束
