"""
练习3：上传头像的练习
假设客户端需要将自己的头像上传给服务端
请编写程序完成该工作，在服务端以当前日期
保存为jpg格式   2020-12-10.jpg

客户端： 读文件   发送文件内容
服务端： 接收文件内容   写入本地
"""
from socket import *


class UploadAvatar:
    def __init__(self):
        self.tcp_socket = socket()
        self.tcp_socket.bind(('127.0.0.1', 8889))
        self.tcp_socket.listen(5)
        self.conndf, self.addr = self.tcp_socket.accept()

    def upload_file(self, filename):
        with open(f'./images/{filename}.jpg', 'wb') as f:
            while True:
                data = self.conndf.recv(1024)
                if data == b'##':  # 以##作为传完的标志
                    break
                f.write(data)
        self.conndf.send('传输完成'.encode())
        self.conndf.close()
        self.tcp_socket.close()


if __name__ == '__main__':
    upload_avatar = UploadAvatar()
    upload_avatar.upload_file(upload_avatar.addr)
