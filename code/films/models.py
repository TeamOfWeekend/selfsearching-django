from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Film(models.Model):
    """用户学习的主题"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,  # 这里应该是 User, 而不是 'User', 否则会报错
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name
