from django.db.models import Avg, Sum, Q, F
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Humen


def get_data(req):
    #聚合函数 money>10050
    humens = Humen.objects.filter(money__gt=10050)
    # avg_age = humens.aggregate(Avg("age"))
    avg_age = humens.aggregate(Sum("age"))
    print(avg_age)
    # return HttpResponse("OK")
    return HttpResponse(avg_age.get("age__sum"))

def get_data_by_q(req):
    #获取查询条件
    # data = Humen.objects.filter(Q(age__lt=10) | Q(money__gt=10050))
    # data = Humen.objects.filter(id__lt=10,age__gt=10)
    data = Humen.objects.filter(Q(id__lt=10) & Q(age__gt=10))
    return render(req,"humens.html",{"humens":data})

def get_data_by_f(req):
    #获取条件查询 找出自己年纪大于自己编号的数据
    data = Humen.objects.filter(age__gt=F("id"))
    res = Humen.new_objects.create_girl("曹蒹")
    print(res)
    return render(req,"humens.html",{"humens":data})



def delete_humen(req):
    #解析参数
    param = req.GET
    h_id = param.get("h_id")
    h_id = int(h_id)
    #数据查询
    # obj = Humen.objects.get(pk=h_id)
    #删除
    # obj.delete()
    objs = Humen.objects.filter(id__lt=h_id)#条件批量删除
    objs.delete()
    return HttpResponse("删除成功")

#数据的更新
def update_humen(req):
    #解析参数
    new_name = req.GET.get("name")
    #拿到数据集合的第一个
    # obj=Humen.objects.all().first()
    # obj.name = new_name
    # obj.save

    res = Humen.objects.filter(id=10)
    data = {
        "name":new_name,
        "age":1000
    }
    # res.update(name=new_name,age=1)
    res.update(**data)
    return HttpResponse("OK")

