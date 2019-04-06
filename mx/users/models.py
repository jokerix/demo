from django.db import models

# Create your models here.
from datetime import datetime


class UserProfile(models.Model):
    name = models.CharField(max_length=40, verbose_name='姓名', default="")
    gender = models.CharField(choices=(('male', '男'), ('female', '女')), default='female', max_length=6)
    mobile = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """
    使用人表设计
    物品表和使用人表是 一对多关系
    使用表外键引用课程表

    """
    name = models.CharField(max_length=50, verbose_name='物品名')
    course = models.CharField(max_length=40, verbose_name="使用人")
    num = models.CharField(max_length=30, verbose_name="使用数量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="借阅时间")

    class Meta:
        verbose_name = "使用者"
        verbose_name_plural = verbose_name
