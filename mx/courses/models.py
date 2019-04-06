from django.db import models

# Create your models here.
from datetime import datetime


class Course(models.Model):
    """
    物品表设计

    """
    name = models.CharField(max_length=50, verbose_name='物品名')
    desc = models.CharField(max_length=300, verbose_name="物品描述")
    detail = models.TextField(verbose_name="物品详情")
    students = models.IntegerField(default=0, verbose_name='使用人数')
    fav_nums = models.IntegerField(default=0, verbose_name='剩余数量')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = "物品"
        verbose_name_plural = verbose_name


