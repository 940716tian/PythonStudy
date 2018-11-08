from django.db import models

# Create your models here.
class IdCard(models.Model):
    num = models.CharField(
        max_length=20,
        verbose_name="身份证编号"
    )
    addr = models.CharField(
        max_length=20,
        default="当地派出所"
    )
    class Meta:
        verbose_name = "身份证类"

class Person(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="人名"
    )
    idcard = models.OneToOneField(
        IdCard,
        on_delete=models.PROTECT
    )
    def __str__(self):
        return self.name


# class Grade(models.Model):
#     name = models.CharField(
#         max_length=20,
#
#     )
#     def __str__(self):
#         return self.name
#
# class Stu(models.Model):
#     name = models.CharField(
#         max_length=30,
#     )
#     grade = models.ForeignKey(
#         Grade,
#     )
#     def __str__(self):
#         return self.name

class Author(models.Model):
    name = models.CharField(
        max_length=20
    )
    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(
        max_length=20
    )
    author = models.ManyToManyField(
        Author
    )
    def __str__(self):
        return self.name