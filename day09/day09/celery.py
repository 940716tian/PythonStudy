from __future__ import absolute_import #绝对路径导入
import os
from celery import Celery
from django.conf import settings

#设置系统的环境配置用的是Django的
os.environ.setdefault("DJANGO_SETTING_MODULE", "day09.settings")

#实例化celery
app = Celery(__name__)

app.conf.timezone = "Asia/Shanghai"

#指定celery的配置来源 用的是项目的配置文件settings.py
app.config_from_object("django.conf:settings")

#让celery 自动去发现我们的任务（task）,你需要在app目录下 新建一个叫tasks.py（一定不要写错）文件
app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)





