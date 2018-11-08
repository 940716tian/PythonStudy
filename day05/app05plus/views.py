from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def index(req):
    user = req.user
    uname = user.username if user.username else "游客"
    return render(req,"new_index.html",{"user_name":uname})
def register(req):
    if req.method == "GET":
        return render(req,"register.html")
    else:
        params = req.POST
        name = params.get('name')
        pwd = params.get('pwd')
        confirm_pwd = params.get("confirm_pwd")
        if pwd and len(pwd) >= 4 and pwd == confirm_pwd:
            # 继续校验用户是否存在
            if not User.objects.filter(username=name).exists():
                # 创建用户
                user = User.objects.create_user(username=name,password=pwd)
                return redirect(reverse("Day05:mylogin"))
            else:
                return HttpResponse("用户已存在")
        else:
                return HttpResponse("账号或密码有误")

def mylogin(req):
    if req.method == "GET":
        return render(req,"mylogon.html")
    else:
        params = req.POST
        name = params.get("name")
        pwd = params.get("pwd")
        if len(name) == 0 or len(pwd) == 0:
            return HttpResponse("不能为空")
        #校验用户
        user = authenticate(username=name,password=pwd)
        if user is None:
            return HttpResponse("账号或密码错误")
        else:
            #用户登录
            login(req,user)
            return redirect("/app05plus/newindex01")


def mylogout(req):
    logout(req)
    return redirect("/app05plus/newindex01")