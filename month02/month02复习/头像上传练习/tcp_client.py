import time
from socket import *


class UploadAvatar:
    def __init__(self):
        self.tcp_socket = socket()
        self.tcp_socket.connect(('127.0.0.1', 8889))

    def upload(self):
        with open('IMG_6306.jpg', 'rb') as f:
            while True:
                content = f.read(1024)
                if not content:
                    break
                self.tcp_socket.send(content)
        time.sleep(0.1)  # 防止沾包
        self.tcp_socket.send(b'##')
        res = self.tcp_socket.recv(1024)
        print(res.decode())
        self.tcp_socket.close()


if __name__ == '__main__':
    upload_file = UploadAvatar()
    upload_file.upload()
