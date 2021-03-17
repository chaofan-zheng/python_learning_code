from socket import *

ADDR = ('127.0.0.1', 8888)


class QueryWord:
    def __init__(self):
        self.udp_socket = socket(AF_INET, SOCK_DGRAM)

    def find_word(self):
        """得到单词，并返回解释"""
        while True:
            word = input('请输入要查询的单词')
            if not word:
                break
            self.udp_socket.sendto(word.encode(), ADDR)  # 需要用byte传输
            data, addr = self.udp_socket.recvfrom(1024)
            print(data.decode())


if __name__ == '__main__':
    q = QueryWord()
    q.find_word()
