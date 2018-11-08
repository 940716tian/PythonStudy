from django.db import models

# Create your models here.

class HumenManage(models.Manager):
    def create_girl(self,name):
        res = Humen.objects.create(
            name = name,
            age=18,
            money=12
        )
        return res

class  Humen(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True
    )
    age = models.IntegerField(
        default=1
    )
    money = models.IntegerField(
        default=0
    )
    objects = models.Manager()#类管理器

    new_objects = HumenManage()