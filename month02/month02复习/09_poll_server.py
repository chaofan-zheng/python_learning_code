import time
from socket import *
from select import *

HOST = '0.0.0.0'
PORT = 8887
ADDR = (HOST, PORT)
tcp_socket = socket()
tcp_socket.bind(ADDR)
tcp_socket.listen(5)
# 设置无阻塞
tcp_socket.setblocking(False)
# 设置监控
p = poll()
p.register(tcp_socket, POLLIN)
# 准备好查找字典，根据events的filno返回套接字对象
map = {tcp_socket.fileno(): tcp_socket}
# 循环监控发生的IO事件
while True:
    events = p.poll()
    print(events)  # events的返回格式是[(fileno,event),(),(),...]
    for fileno, event in events:  # 拆包
        if fileno is tcp_socket.fileno():
            connfd, addr = map[fileno].accept()
            print("Connect from", addr)
            # 添加客户端连接套接字到监控列表
            connfd.setblocking(False)
            map[connfd.fileno()] = connfd  # 维护字典
            p.register(connfd, POLLIN)
        else:  # 就是connfd就绪的情况
            # 处理一个客户端的消息
            data = map[fileno].recv(1024)
            # 客户端退出
            if not data:
                p.unregister(fileno)
                map[fileno].close()
                del map[fileno]  # 从字典删除
                continue
            print(data.decode())
            map[fileno].send(b"OK")
