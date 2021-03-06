from django.db import models

class BaseModel(models.Model):
    """抽象模型基类"""
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True,verbose_name="更新时间")
    is_delete = models.BooleanField(default=False,verbose_name="删除标记")
    # 数据无价，我们不会真正的删除，只会用一个删除标记

    class Meta:
        # 说明是一个抽象类模型
        abstract = True