from django.db import models

# Create your models here.


COLLEGE_LEVELS = (
    (1, '双一流'),
    (2, '一本'),
    (3, '二本'),
    (4, '三本'),
)


# 自定义管理器
class CollegeInfoManager(models.Manager):
    def get_query_set(self):
        # 调用父类方法
        return super(CollegeInfoManager, self).get_query_set()

class CollegeInfo(models.Model):
    """大学信息模型"""
    # 管理器定义
    objects = models.Manager()  # 默认的管理器
    college_objects = CollegeInfoManager()  # 自定义管理器
    # 学校名称
    name = models.CharField()
    # 学校编号，不能为空，在表中具有唯一值
    id = models.IntegerField(null=False, unique=True)
    # 学校地址
    address = models.TextField()
    # 学校级别
    level = models.IntegerField(choices=COLLEGE_LEVELS, verbose_name='学校级别', null=False)
    # 校园面积
    area = models.PositiveIntegerField()
    # 学院数量
    academyNum = models.PositiveIntegerField()

    class Meta:
        # 本类不是抽象基类
        abstract = False
        # 所属应用
        app_label = 'imagination'
        # 映射的数据表名
        db_table = 'imagination_collegeInfo'
        # 定义按哪个字段值排列，以获得模型的开始或结束记录
        get_latest_by = id
        # manage.py命令行工具是否管理本模型
        managed = True


    def __str__(self):
        return self.name

