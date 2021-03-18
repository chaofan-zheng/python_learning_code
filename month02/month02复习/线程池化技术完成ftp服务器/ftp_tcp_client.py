"""
   查看文件库文件
      客户端: 发送请求
             接受等待响应
             根据响应处理
             OK 接收列表
             FAIL 结束

      服务端： 解析请求
              判断给出什么响应
              OK 发送文件列表
              FAIL 结束


   下载文件
   上传文件
   退出
   API：
        查看文件列表LIST##
        下载：GET##
        上传：PUSH##
        退出 Exit##
"""
import os
from socket import socket


class FTPClient:
    def __init__(self, host, port):
        self.port = port
        self.host = host
        self.ADDR = (self.host, self.port)
        self.tcp_socket = self.connect_server()
        self.handle = FTPHandle(self.tcp_socket)

    def connect_server(self):
        tcp_socket = socket()
        tcp_socket.connect(self.ADDR)
        return tcp_socket

    def show_menu(self):
        print("1) 查看文件")
        print("2) 下载文件")
        print("3) 上传文件")
        print("4) 退   出")
        print("")

    def main(self):
        while True:
            self.show_menu()
            self.handle.select_menu()


class FTPHandle:
    def __init__(self, tcp_socket):
        self.tcp_socket = tcp_socket

    def select_menu(self):
        item = input("请输入选项:")
        if item == '1':
            self.do_list()  # 查看FTP文件夹下的所有文件
        elif item == '2':
            pass
        elif item == '3':
            pass
        elif item == '4':
            pass
        else:
            print("请输入正确选项！")

    def do_list(self):
        self.tcp_socket.send(b"LIST")
        # 等待响应
        result = self.tcp_socket.recv(128)
        if result == b"OK":
            # 接收文件列表
            files = self.tcp_socket.recv(1024 * 1024)
            print(files.decode())
        else:
            print("文件库为空")


if __name__ == '__main__':
    client = FTPClient('127.0.0.1', 8000)
    client.main()
