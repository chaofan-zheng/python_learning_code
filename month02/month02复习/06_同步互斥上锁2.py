"""
使用2个线程，一个打印 1--52 这些数字
一个打印 A--Z 这些字母，
两个线程一起执行，要求打印出来的顺序为两个数字一个字母
12A34B ...... 5152Z
"""
from threading import Thread, Lock

lock1 = Lock()
lock2 = Lock()


def print_alpha():
    for i in range(65, 91):
        lock2.acquire()
        print(chr(i))
        lock1.release()


def print_num():
    for i in range(1, 53, 2):
        lock1.acquire()
        print(i)
        print(i + 1)
        lock2.release()


thread1 = Thread(target=print_alpha)
thread2 = Thread(target=print_num)
lock2.acquire()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
