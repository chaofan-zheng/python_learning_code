"""
客户端退出不影响服务端
"""

from socket import *

ADDR = ("127.0.0.1", 9999)
# 创建udp套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

mark = True
while mark:
    msg = input("<<")
    if msg == "##":
        print("会话结束")
        udp_socket.close()
        mark = False
    else:
        n = udp_socket.sendto(msg.encode(), ADDR)
        print(f"向服务器发送了{n}字节的信息")
        data, addr = udp_socket.recvfrom(2048)
        print("从服务器收到了：", data.decode())
