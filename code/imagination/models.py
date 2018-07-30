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
    name = models.CharField(max_length=20)
    # 学校编号，不能为空，在表中具有唯一值
    collegeId = models.IntegerField(null=False, unique=True)
    # 学校地址
    address = models.TextField(blank=True, max_length=200)
    # 学校级别
    level = models.IntegerField(choices=COLLEGE_LEVELS, verbose_name='学校级别', null=False)
    # 校园面积
    area = models.PositiveIntegerField(null=True)
    # 学院数量
    academyNum = models.PositiveIntegerField()

    class Meta:
        # 本类不是抽象基类
        abstract = False
        # 所属应用，在setting中未添加应用时使用
        # app_label = 'imagination'
        # 映射的数据表名
        db_table = 'imagination_collegeInfo'
        # 定义按哪个字段值排列，以获得模型的开始或结束记录
        # get_latest_by = 'collegeId'
        # manage.py命令行工具是否管理本模型
        managed = True
        # 按照某外键引用的关系排序
        # order_with_respect_to = ''
        # 默认排序字段，可设置多个，默认降序，如果升序需在前面加“-”号
        ordering = ['collegeId']
        # 模型操作权限，默认为add、change、delete
        default_permissions = ('add', 'change', 'delete')
        # 本模型及所有继承自本模型的子模型是否为代理模型
        # proxy = True
        # 定义底层数据库所必须具备的特性，如下：只将本模型声称在满足gis_enabled特性的数据库中
        # required_db_features = ['gis_enabled']
        # 定义底层数据库的类型，比如SQLite、MySQL、Oracle。若定义本属性，模型智能在其声明的数据库中被维护
        # required_db_vendor = 'MySQL'
        # 设置不重复的字段组合，必须唯一，可以多个组合
        # unique_together = (('name', 'collegeId'),)
        # 定义联合索引的字段，可以设置多个
        index_together = [['name', 'collegeId'], ]
        # 指明一个易于理解和表述的单数形式的对象名称
        verbose_name = 'collegeInfo'
        # 指明一个易于理解和表述的附属形式的对象名称，若不指定，在类名后加s
        verbose_name_plural = 'collegeInfos'


    def __str__(self):
        return self.name


class AcademyInfo(models.Model):
    """大学学院模型"""
    # 所属学校
    collegeInfo = models.ForeignKey(CollegeInfo, on_delete=models.CASCADE,)
    # 学院名称
    name = models.CharField(max_length=20)
    # 学院编号，不能为空，在表中具有唯一值
    academyId = models.IntegerField(null=False, unique=True)
    # 包含的专业数量
    majorNum = models.PositiveIntegerField()

    class Meta:
        # 按照某外键引用的关系排序
        # order_with_respect_to = ''
        # 默认排序字段，可设置多个，默认降序，如果升序需在前面加“-”号
        ordering = ['academyId']
        # 定义联合索引的字段，可以设置多个
        index_together = [['name', 'academyId'], ]
        # 指明一个易于理解和表述的单数形式的对象名称
        verbose_name = 'academyInfo'
        # 指明一个易于理解和表述的附属形式的对象名称，若不指定，在类名后加s
        verbose_name_plural = 'academyInfos'

    def __str__(self):
        return self.name


class MajorInfo(models.Model):
    """大学专业模型"""
    # 所属学院
    academyInfo = models.ForeignKey(AcademyInfo, on_delete=models.CASCADE,)
    # 学院名称
    name = models.CharField(max_length=20)
    # 学院编号，不能为空，在表中具有唯一值
    majorId = models.IntegerField(null=False, unique=True)
    # 包含的专业数量
    gradeNum = models.PositiveIntegerField()

    class Meta:
        # 按照某外键引用的关系排序
        # order_with_respect_to = ''
        # 默认排序字段，可设置多个，默认降序，如果升序需在前面加“-”号
        ordering = ['majorId']
        # 定义联合索引的字段，可以设置多个
        index_together = [['name', 'majorId'], ]
        # 指明一个易于理解和表述的单数形式的对象名称
        verbose_name = 'majorInfo'
        # 指明一个易于理解和表述的附属形式的对象名称，若不指定，在类名后加s
        verbose_name_plural = 'majorInfos'

    def __str__(self):
        return self.name


class GradeInfo(models.Model):
    """大学年级模型"""
    # 所属专业
    majorInfo = models.ForeignKey(MajorInfo, on_delete=models.CASCADE,)
    # 年级编号，不能为空，在表中具有唯一值
    gradeId = models.IntegerField(null=False, unique=True)
    # 包含的班级数量
    classsNum = models.PositiveIntegerField()

    class Meta:
        # 按照某外键引用的关系排序
        # order_with_respect_to = ''
        # 默认排序字段，可设置多个，默认降序，如果升序需在前面加“-”号
        ordering = ['gradeId']
        # 指明一个易于理解和表述的单数形式的对象名称
        verbose_name = 'gradeInfo'
        # 指明一个易于理解和表述的附属形式的对象名称，若不指定，在类名后加s
        verbose_name_plural = 'gradeInfos'

    def __str__(self):
        return self.gradeId


class ClasssInfo(models.Model):
    """大学班级模型"""
    # 所属年级
    gradeInfo = models.ForeignKey(GradeInfo, on_delete=models.CASCADE,)
    # 班级编号，不能为空，在表中具有唯一值
    classsId = models.IntegerField(null=False, unique=True)
    # 包含的学生数量
    studentNum = models.PositiveIntegerField()

    class Meta:
        # 按照某外键引用的关系排序
        # order_with_respect_to = ''
        # 默认排序字段，可设置多个，默认降序，如果升序需在前面加“-”号
        ordering = ['classsId']
        # 指明一个易于理解和表述的单数形式的对象名称
        verbose_name = 'classsInfo'
        # 指明一个易于理解和表述的附属形式的对象名称，若不指定，在类名后加s
        verbose_name_plural = 'classsInfos'

    def __str__(self):
        return self.classsId


class StudentInfo(models.Model):
    """大学生模型"""
    # 所属班级
    classsInfo = models.ForeignKey(ClasssInfo, on_delete=models.CASCADE,)
    # 学号，不能为空，在表中具有唯一值
    studentId = models.IntegerField(null=False, unique=True)
    # 姓名
    name = models.CharField(max_length=20)
    # 姓名拼音
    namePinYin = models.CharField(max_length=20)
    # 身份证号
    idCardNum = models.CharField(max_length=20)
    # 年龄
    age = models.IntegerField()
    # 入学年份
    year_in_college = models.DateTimeField()
    # 身高
    height = models.IntegerField()
    # 体重
    weight = models.IntegerField()
    # 腰围
    bust = models.IntegerField()
    # 腰围
    waist = models.IntegerField()
    # 臀围
    hips = models.IntegerField()
    # 爱好
    hobbies = models.CharField(max_length=200)
    # 婚姻状态
    married = models.BooleanField()

    class Meta:
        # 按照某外键引用的关系排序
        # order_with_respect_to = ''
        # 默认排序字段，可设置多个，默认降序，如果升序需在前面加“-”号
        ordering = ['studentId']
        # 定义联合索引的字段，可以设置多个
        index_together = [['name', 'studentId'], ]
        # 指明一个易于理解和表述的单数形式的对象名称
        verbose_name = 'studentInfo'
        # 指明一个易于理解和表述的附属形式的对象名称，若不指定，在类名后加s
        verbose_name_plural = 'studentInfos'

    def __str__(self):
        return self.name
