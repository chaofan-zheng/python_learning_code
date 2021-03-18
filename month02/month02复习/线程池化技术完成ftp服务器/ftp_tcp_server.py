import os
import time
from multiprocessing import Pool
from socket import socket


class FTPServer:
    def __init__(self, host, port):
        self.port = port
        self.host = host
        self.address = (host, port)
        self.__sock = self.__create_sock()
        self.base_path = '../FTP'
        self.pool = Pool()

    def __create_sock(self):
        tcp_socket = socket()
        tcp_socket.bind(self.address)
        return tcp_socket

    def serve_forever(self):
        self.__sock.listen(5)
        while True:
            connfd, addr = self.__sock.accept()
            print(f'从{addr}连接')
            handle = Handle(connfd)
            self.pool.apply_async(handle.main)


class Handle:
    def __init__(self, connfd):
        self.connfd = connfd
        self.folder_path = '../FTP'

    def request(self, data):
        """根据请求类型，调用不同的函数"""
        if data == "LIST":
            self.do_list()
        elif data == "GET":
            pass
        elif data == "PUT":
            pass
        elif data == "EXIT":
            pass

    def do_list(self):
        file_list = os.listdir(self.folder_path)
        if not file_list:
            self.connfd.send(b'FAIL')
            return
        self.connfd.send(b'OK')
        time.sleep(0.1)  # 防止沾包！！！
        data = "\n".join(file_list)
        self.connfd.send(data.encode())

    def main(self):
        while True:
            data = self.connfd.recv(1024).decode()
            self.request(data)


if __name__ == '__main__':
    server = FTPServer('127.0.0.1', 8000)
    server.serve_forever()
