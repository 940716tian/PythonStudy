from django.contrib import admin

# Register your models here.

from .models import *

class EngineerAdmin(admin.ModelAdmin):

    def is_old(self):
        if self.age > 18:
            return "老人"
        else:
            return "too young,too 三炮"
    is_old.short_description = "三炮否"
# 设置显示的字段 数组里放的是我们的模型属性
    list_display = ["name","age",is_old]
#设置过滤条件
    list_filter = ["name"]

#分页
    list_per_page = 5
#搜索
    search_fields = ['name','age']
#排序
    ordering = ['-age']
#设置字段分组
    fieldsets = [
        ('基本信息', {'fields': ('name',)}),
        ('额外信息', {'fields': ('age',)})
    ]


admin.site.register(Engineer,EngineerAdmin)


