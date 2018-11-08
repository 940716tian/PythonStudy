from django.urls import reverse
from io import BytesIO

import os

import random
from django.conf import settings
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .myutil import get_unique_str,get_random_color
# Create your views here.
from .models import Book



def my_login(req):
    if req.method == "GET":
        return render(req,"login.html")
    else:
        #解析参数
        params = req.POST
        user_info = params.get("user_info")
        pwd = params.get("pwd")

        print(pwd)
        #认证
        user = authenticate(username=user_info,password=pwd)
        #判断是否校验成功
        if user:
            login(req,user)
            return HttpResponse("登录成功")
        else:
            return HttpResponse("有错误")





def get_prize(req):
    # 生成一个随机数
    num = random.randint(1,100)
    if num > 90:
        return HttpResponse("奖金一万元")
    else:
        return HttpResponse("酱油一瓶")






def create_book_v1(req):
    if req.method == "GET":
        book = Book.objects.all().first()
        # print("可以")

        #拼接图片的网络端口
        icon_url = "http://{}/static/uploads/{}".format(
            req.get_host(), # 获取访问的域名加端口
            book.icon.url   # 图片的路径字符串
        )
        # print("还可以")
        return render(req,"mybook.html",{"book_name":book.name,"icon":icon_url})
    #
    # 解析参数
    name = req.POST.get("name")
    myfile = req.FILES.get("icon")

    #实例化一个数据
    book = Book.objects.create(
        name = name,
        icon = myfile
    )
    return HttpResponse("OK")


def create_book_v2(req):
    if req.method == "GET":
        return render(req,"mybook.html")
    else:
        #拿到参数
        name =req.POST.get("name")
        myfile = req.FILES.get("icon")

        #文件路径
        filename = get_unique_str() + "."+ myfile.name.split(".")[-1]
        filepath = os.path.join(settings.MEDIA_ROOT,"filename")
        f = open(filepath,"wb")

        for i in myfile.chunks():
            f.write(i)
        return HttpResponse("OK")



def get_confirm_code(req):
    from PIL import Image,ImageDraw,ImageFont
    from io import BytesIO

    #实例化一块画布
    img_size = (150,70)
    img_color = get_random_color()
    img = Image.new("RGB",img_size,img_color)

    #实例化一个画笔
    draw = ImageDraw.Draw(img)
    code_xy = (20,20)
    # code_color = get_random_color()


    #实例化一个字体
    font_path = os.path.join(settings.STATICFILES_DIRS[0],"fonts/ADOBEARABIC-BOLD.OTF")
    font_size = 35
    font = ImageFont.truetype(font_path,font_size)

    # #画一个字母
    # draw.text(code_xy,"L",font=font,fill = code_color)

    soure = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    #用来保存 我们生成的随机数字
    res = ""
    for i in range(4):
        # 随机出一个字母
        code_color = get_random_color()
        index = random.randint(0,len(soure))
        my_str = soure[index]
        res += my_str
        draw.text((20+30*i,20),my_str,fill=code_color,font=font)

    # 画点
    for i in range(100):
        x = random.randint(0,150)
        y = random.randint(0,70)
        draw.point((x,y),fill=get_random_color())
        draw.line((20,65),fill=(255,255,255),width=50)

    buf = BytesIO()
    #保存
    img.save(buf,"png")
    del draw

    #保存的session
    req.session["verify_code"] = res
    return HttpResponse(buf.getvalue(),content_type="image/png")


def my_login(req):
    if req.method == "GET":
        return render(req,"mylogin.html")
    else:
        code = req.POST.get("code")
        server_code = req.session.get("verify_code")
        #将入户传入的和系统session保存的字符都转入小写然后作比较
        if code and len(code) > 0 and code.lower() == server_code.lower():
            return HttpResponse("OK")
        else:
            return HttpResponse("NO OK")



def slogin(req):
    if req.method == "GET":
        return render(req,"slogin.html")
    else:
        #解析参数
        params = req.POST
        user_info = params.get("user_info")
        pwd = params.get("pwd")

        print(pwd)
        #认证
        user = authenticate(username=user_info,password=pwd)
        #判断是否校验成功

        code = req.POST.get("code")
        server_code = req.session.get("verify_code")
        if user and code and len(code) > 0 and code.lower() == server_code.lower():
            login(req,user)
            return redirect(reverse("/create_book/"))
        else:
            return HttpResponse("有错误")