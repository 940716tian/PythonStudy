import os
from django import template
import logging
from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage, send_mass_mail
# Create your views here.
from django.template import loader
from .my_util import *
from django.template import loader
from django.views.decorators.csrf import csrf_exempt,csrf_protect
# 实例化一个日志对象
log = logging.getLogger("django")




def test(req):
    log.info("尼玛")
    return HttpResponse("收工")


def test_email(req):
    title = "来自Django的问候"
    msg = "今天是个好日子！"
    receivers = [
        "1181233464@qq.com",
    ]
    email_from = settings.DEFAULT_FROM_EMAIL
    send_mail(title,msg,email_from,receivers)
    return HttpResponse("OK")


def send_html(req):
    title = "天空之城"
    #要有html才行 先加载 再渲染
    #再发送邮件
    template = loader.get_template("email_templates.html")
    html = template.render({"title":"哈哈哈","url":"http://www.baidu.com"})
    receivers = [
        "1178084358@qq.com",
    ]
    email_from = settings.DEFAULT_FROM_EMAIL
    #再发送邮件
    send_mail(title,'',email_from,receivers,html_message=html)
    return HttpResponse("好了")

def file_email(req):
    message = EmailMessage
    title = "天空"
    msg = "湛蓝"
    receivers = [
        "1178084358@qq.com",
    ]
    email_from = settings.DEFAULT_FROM_EMAIL
    #实例化邮件信息
    message = EmailMessage(title,msg,email_from,receivers)
    file_path = os.path.join(settings.STATICFILES_DIRS[0],"timg.jpg")

    #加载附件路劲
    message.attach_file(file_path,"image/jpg")

    #发送邮件
    message.send()
    return HttpResponse("OJBK")


def send_many(req):

    receivers = [
        "1178084358@qq.com",
    ]
    email_from = settings.DEFAULT_FROM_EMAIL
    msg1 = ("标题","打不过我吧，哈哈哈哈",email_from,receivers[:1])
    msg2 = ("还是标题","打不过我吧，哈哈哈哈",email_from,receivers)

    #发送邮件
    send_mass_mail((msg1,msg2))
    return HttpResponse("OJB蛇皮K")

def send_verify_mail(req):
    uuid_str = get_unique_str()
    url = "http://"+req.get_host()+"/app08/verify/"+ uuid_str

    #加载模板
    template = loader.get_template("email_templates.html")
    html = template.render({"title":"欢送大家","url":url})
    title = "注册"
    user_email = "1178084358@qq.com"#应该是解析用户传过来的参数
    receivers = [
        user_email
    ]
    email_from = settings.DEFAULT_FROM_EMAIL
    send_mail(title, '', email_from, receivers, html_message=html)

    #设置缓存
    cache.set(uuid_str,user_email,settings.VERIFY_CODE_MAX_AGE)

    return HttpResponse("注册成功,请注意查收邮件")

def verify(req,code):
    # 去缓存拿数据
    email = cache.get(code)
    if email:
        #找到用户对象，然后更新用户状态字段 is_active = True save()
        return HttpResponse(email+"验证成功")
    else:
        return HttpResponse("验证无效")


# @csrf_exempt #不进行保护
@csrf_protect #添加csrf保护
def cz_api(req):
    if req.method == "GET":
        return render(req,"cz.html")
    else:
        #解析参数
        params = req.POST
        name = params.get("name")
        num = params.get("num")
        return HttpResponse("操作成功")