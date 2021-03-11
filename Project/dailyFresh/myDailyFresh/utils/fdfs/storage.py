from django.conf import settings
from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client


class FDFStorage(Storage):
    def __init__(self, client_conf=None, base_url=None):
        if not client_conf:
            client_conf = settings.FDFS_CLIENT_CONF
        self.client_conf = client_conf
        if not base_url:
            base_url = settings.FDFS_URL
        self.base_url = base_url

    def _open(self, name, mode='rb'):
        """打开文件时使用"""
        pass

    def _save(self, name, content):
        """保存文件时使用"""
        # name 你上传的文件的名字
        # content 包含你上传文件的内容的File对象
        # _save应该是返回被保存文件的真实名称，（通常是传进来的name,但是如果储存需要修改文件名称，则返回新的名称来代替）

        # 创建一个fdfs_client对象
        client = Fdfs_client(self.client_conf)  # 路径是要相对于django项目的路径

        # 上传文件到fdfs系统中
        res = client.upload_by_buffer(content.read())
        # upload by buffer 是上传文件内容的意思，所以content需要.read()
        # res 返回内容：
        # {
        #     'Group name': group_name,
        #     'Remote file_id': remote_file_id,
        #     'Status': 'Upload successed.',
        #     'Local file name': '',
        #     'Uploaded size': upload_size,
        #     'Storage IP': storage_ip
        # } if success else None
        if res.get('Status') != 'Upload successed.':
            raise Exception('上传文件至fdfs失败')
        # 获取返回的文件id
        filename = res.get('Remote file_id')  # group1/.....
        return filename

    def exists(self, name):
        """Returns True if a file referenced by the given name already exists in the storage system, or False if the name is available for a new file."""
        # django 判断文件名是否可用
        return False  # 代表就是可用的新文件

    def url(self, name):
        """返回文件路径"""
        # url函数用于返回django根据路径找文件的作用
        # name是存储在mysql的文件名称，也就是上面的filename
        return self.base_url + name  # nginx 域名+端口号
