from django.forms import model_to_dict
from .models import Stu
from django.http import JsonResponse, QueryDict
from django.views.generic import View
from .mysingal import action


class StuAPI(View):


    def get(self,req):
        #返回所有学生的信息
        # 1.拿到学生信息
        data = Stu.objects.all()
        stus = [model_to_dict(i) for i in data]
        result = {
            "code":1,
            "msg":"OK",
            "data":stus,
        }
        return JsonResponse(result)

    def post(self,req):
        # 解析参数
        params = req.POST
        name = params.get("name")
        age = params.get("age")
        try:
            age = int(age)
        except TypeError as e:
            result = {
                "code":2,
                "msg":"年纪是数字类型",
                "data":None
            }
            return JsonResponse(result)
        # 创建对象
        stu = Stu.objects.create(
            name=name,
            age=age,
        )
        # 返回结果
        result = {
            "code":1,
            "msg":"created",
            "data":model_to_dict(stu)
        }
        return JsonResponse(result)

    def delete(self,req):
        # 解析参数
        params = QueryDict(req.body)
        id = int(params.get("s_id"))
        # 查询数据
        stu = Stu.objects.get(pk=id)
        stu.delete()
        return JsonResponse({
            "code":1,
            "msg":"delered",
            "data":id,
        })



class TestAPI(View):
    def post(self,req):
        param = req.POST
        name = param.get("name")
        age = int(param.get("age"))
        stu = Stu()
        stu.name = name
        stu.age = age
        stu.save()
# 自定义信号的使用
        action.send(sender="班长",hehe="赵兄托我办点事")
        return JsonResponse({"msg":"OJBK"})
