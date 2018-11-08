from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class MyUser(AbstractUser):
    phone = models.CharField(
        max_length=13,
        verbose_name="手机号"
    )
    #如果是追加的字段 我们需要设置null=true 或者default
    age = models.IntegerField(
        verbose_name="年纪",
        null=True,
    )


class Book(models.Model):
    name = models.CharField(
        max_length=40,
    )
    icon = models.ImageField(
        upload_to="icons",
        null=True
    )
    icon_url = models.CharField(
        max_length=251,
        null = True
    )


