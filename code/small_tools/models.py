from django.db import models

# Create your models here.

class SmallTools(models.Model):
    """用户学习的主题"""
    #小工具名称
    name = models.CharField(max_length=200)
    #作者
    author = models.CharField(max_length=200)
    #添加时间
    date_added = models.DateTimeField(auto_now_add=True)
    #使用说明
    instruction = models.TextField()

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name