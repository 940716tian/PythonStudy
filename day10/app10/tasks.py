from celery import task
from django.conf import settings
from django.core.cache import caches
from django.template import loader
from django.core.mail import send_mail

# 获得缓存
cache = caches["confirm"]

@task
def send_verify_mail(url,user_id,reciever):
    title = "爱鲜蜂验证"
    content = ""
    # 加载页面
    template = loader.get_template("user/email.html")
    # 渲染
    html = template.render({"url":url})

    email_from = settings.DEFAULT_FROM_EMAIL
    # 发送邮件
    send_mail(title,content,email_from,[reciever],html_message=html)

    #设置缓存
    cache.set(url.split("/")[-1],user_id,settings.VERIFY_CODE_MAX_AGE)





