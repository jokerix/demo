from django.db import models

# Create your models here.
from users.models import UserProfile
from courses.models import Course
from datetime import datetime


class UserAsk(models.Model):
    """
    账务管理表

    """
    total = models.CharField(max_length=20, verbose_name='资金')
    spend = models.CharField(max_length=20, verbose_name='支出')
    remaining = models.CharField(max_length=20, verbose_name='剩余')


class UserCourse(models.Model):
    """
    用户使用表

    """
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name="物品", on_delete=models.CASCADE)

    # add_time = models.DateTimeField(datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户使用"
        verbose_name_plural = verbose_name
