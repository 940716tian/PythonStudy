from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="分类名",
        db_column="cate_name"#改数据库字段的名字
    )
    cate_num = models.CharField(
        max_length=20,
        null= True,
        verbose_name="分类编号"
    )
    create_time = models.DateTimeField(
        auto_now_add=True,
        verbose_name="创建时间"
    )
    update_time = models.DateTimeField(
        auto_now=True,
        verbose_name="修改时间"
    )
    class Meta:
        #改数据库表的名字
        db_table = "category"


class Item(models.Model):
    name = models.CharField(
        max_length=40,
        verbose_name="商品名字"
    )
    barcode = models.CharField(
        max_length=13,
        verbose_name="条码",
        null=True
    )
    category = models.ForeignKey(
        Category,
        db_index=True,
    )
