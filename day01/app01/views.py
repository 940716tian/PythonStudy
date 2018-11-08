from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app01.models import Humen


def hello(requset):
    return HttpResponse("胡佳乐你好！！")

def inter(req):
    return HttpResponse("<h1>万万没想到，啦啦啦啦！</h1>")

def home(req):
    return render(req,"index.html")

def get_humen(req):
    data = Humen.objects.all()
    print(data)
    return render(req,"humen.html",{"humen":data})
def hehe(req):
    params = req.GET
    # print(params)
    print(params["data"])
    print(params.get("msg"))
    return HttpResponse("呵呵")

def make_friends(req):
    param = req.GET
    name = param.get("name")
    yz = int(param.get("yz"))
    age = int(param.get("age"))
    money = int(param.get("money"))
    if money >= 1000 and yz >= 80 and age >= 18 and age <22:
        return HttpResponse("不错呦")
    elif yz > 80 and yz >= 80 and age >= 18 and money <1000:
        return HttpResponse("好人呀")
    else:
        return HttpResponse("呵呵")