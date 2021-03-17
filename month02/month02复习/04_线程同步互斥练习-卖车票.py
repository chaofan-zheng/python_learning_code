"""
练习1
现在有500车票，记为T1 -- T500
共有10个窗口同时买票 W1--W10
模拟卖票过程
卖出一张则打印W1 ----- T200
卖出后要隔0.1s才能出下一张
"""
import time
from threading import Thread

tick_list = [f'T{i}' for i in range(1, 501)]


def sell_tickets(wn):
    while tick_list:
        time.sleep(0.1)
        # ticket = tick_list.pop(0)
        ticket = tick_list[0]
        del tick_list[0]
        print(f'{ticket}---{wn}')


def main():
    jobs = []
    for i in range(1, 11):
        wn = f'W{i}'
        thread = Thread(target=sell_tickets, args=(wn,))
        thread.start()
        jobs.append(thread)
    [job.join() for job in jobs]


main()
