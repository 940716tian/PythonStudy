from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from .models import Language
from django.template import loader


def index(req):
    return render(req,"index.html")
def langs(req):
    #查询语言
    data = Language.objects.all()
    #加载模板
    html = loader.get_template("langs.html")
    print(dir(html))
    #渲染
    html_str = html.render({"langs":data})
    print(html_str)


    # return render(req,"langs.html",{"langs":data})
    return HttpResponse(html_str)

def new_index(req):
    print("被执行")
    # return HttpResponseRedirect("/app04/langsq")
    # return redirect("/app04/langsq")
    return redirect(reverse("python1806:lele"))

def myindex_with_param(req,p1):
    print(p1)
    print(type(p1))
    # 通过这个值来搜索语言数据
    try:
        lua = Language.objects.get(pk=int(p1))
        res = "{}的描述是{}".format(lua.name, lua.desc)
    except (Language.DoesNotExist,Language.MultipleObjectsReturned):
        res = "没有数据"

    return HttpResponse(res)


def myindex_with_paramv1(req,p2):
    p1 = p2
    print(p1)
    print(type(p1))
    # 通过这个值来搜索语言数据
    try:
        lua = Language.objects.get(pk=int(p1))
        res = "{}的描述是{}".format(lua.name, lua.desc)
    except (Language.DoesNotExist,Language.MultipleObjectsReturned):
        res = "没有数据"

    return HttpResponse(res)


def new_reverse(req):
    return redirect(reverse("python1806:myindex",args=(2,)))

def new_reverse01(req):
    return redirect(reverse("python1806:v1index",kwargs={"p2":3}))


def block(req):
    return render(req,"block.html")

def include(req):
    return render(req,"include.html")


def home(req):
    return render(req,"blocks.html")