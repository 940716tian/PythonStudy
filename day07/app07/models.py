from django.db import models

# Create your models here.
class Engineer(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="名字"
    )
    age = models.IntegerField(
        verbose_name="年纪"
    )
    def __str__(self):
        return self.name
    class Meta:
        verbose_name="工程师"


# from tinymce.models import HTMLFiled
# class Blog(models.Model):
#     title = models.CharField(
#         max_length=30,
#     )
#     comtent = HTMLFiled()