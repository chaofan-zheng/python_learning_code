"""
练习2： 拷贝一个目录
假设目录下有若干普通文件,需要编写程序
将该目录拷贝一份，注意拷贝过程中需要
多文件同时拷贝（使用进程池完成）

os.mkdir("FTP")
os.listdir("/home/tarena/FTP")
"""
import os
import time
from multiprocessing import Pool


class FolderCopier:
    def __init__(self, old_folder_path, new_folder_name):
        """
        旧文件夹路径需指定相对路径，新建文件夹指定当前目录下。
        """
        self.new_folder_name = new_folder_name
        self.old_folder_path = old_folder_path
        try:
            os.mkdir(self.new_folder_name)  # 制作新文件夹,如果文件夹已经存在会报错
        except:
            pass
        self.old_size = self.total_size(self.old_folder_path)

    def total_size(self, dir):  # 获取目录下的文件大小
        res = 0
        for file in os.listdir(dir):
            res += os.path.getsize(dir + '/' + file)
        return res

    def copy(self, filename):
        old_file = open(f'{self.old_folder_path}/{filename}', 'rb')
        new_file = open(f'{self.new_folder_name}/{filename}', 'wb')  # 如果既有图片也有txt，就都以二进制打开
        while True:
            content = old_file.read(1024)
            if not content:
                break
            new_file.write(content)
        old_file.close()
        new_file.close()

    def main(self):
        pool = Pool()
        file_list = os.listdir(self.old_folder_path)
        for file_name in file_list:
            pool.apply_async(self.copy, args=(file_name,))

        pool.close()
        # 计算并显示文件大小
        copysize = 0
        while copysize < self.old_size:
            copysize = self.total_size(self.new_folder_name)
            percentage = (copysize / self.old_size) * 100
            print('%s--已拷贝--%.2f' % (time.ctime(), percentage))

        pool.join()


if __name__ == '__main__':
    folder_copier = FolderCopier('FTP', 'MYFTP')
    folder_copier.main()
