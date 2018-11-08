
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect
import json

# Create your views here.
def youxi(req):
    return render(req,"2048.html")


def json_test(req):
    data = {
        "code":1,
        "msg":"OK",
        "data":[1,24,5],
    }
    # print(dir(req))
    # print("请求方法",req.method)
    # print("host",req.get_host())
    # print("GET",req.GET)
    # print("POST",req.POST)
    # print("FILES",req.FILES)
    # print(("META",req.META))
    return JsonResponse(data)
    return HttpResponse(json.dumps(data))
    # json.load() 将json 数据转化成对应的数据结构

def test_res(req):
    # 实例化
    response = HttpResponse()
    # 设置返回内容
    response.content = "哈哈"
    # 设置状态码
    response.status_code = 404

    response.write("我是write写的")
    response.flush()

    response.content = "清除缓存"
    return response


def mylogin(req):
    if req.method =="GET":
        return render(req,"login.html")
    elif req.method == "POST":
        # 做登录的操作
        pass
    #     解析参数 名字和密码
        params = req.POST
        name = params.get("umame")
        pwd = params.get("pwd")
    #假设有校验 并且也通过了
    #登录 重定向到首页
        response = redirect("/app05/index")
    #设置cookie
        response.set_cookie("user",name,max_age=30)
    # 也设置session
        req.session['pwd']=pwd
        req.session.set_expiry(30)
        return response
    else:
        return HttpResponseNotAllowed("访问不允许")


#首页
def index(req):
    #读一个请求对象的cookie 拿出叫user的字段对应的值
    u_name = req.COOKIES.get("user")
    #获取session
    res = req.session.get('pwd')
    print("session的结果",res)
    #判断是否拿到，如果没拿到 那么使用游客
    return render(req,"index.html",{"user_name":u_name})


def mylogout(req):
    response = redirect("/app05/index")
    response.delete_cookie("user")
    del req.session['pwd']
    return response
