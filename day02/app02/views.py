from django.http import HttpResponse
from django.shortcuts import render
from .models import Item, Category


# Create your views here.


def get_html(req):
    return render(req,"item.html")

def create_item(req):
    #解析参数
    params = req.POST
    name = params.get("i_name")
    barcoade = params.get("i_barcode")
    cate_id = int(params.get("cate_id"))

    #创建数据
    item = Item.objects.create(
        name=name,
        barcode=barcoade,
        category_id=cate_id
    )
    return HttpResponse("创建成功了{}".format(item.name))


def select_data(req):
    #使用filter查名字
    data = Item.objects.filter(name="陈二狗")
    # data = Item.objects.filter(name__endswith="可乐")
    # print(dir(data))
    # data = data.filter(name="百事可乐")
    # data = Item.objects.filter(id_gt=3)
    # data = Item.objects.filter(id_in=[1,3])
    # data = Item.objects.exclude(name="陈二狗")
    # data = Item.objects.all().order_by("-id")
    return render(req,"items.html",{"items":data})

def get_category(req):
    cates = Category.objects.all()
    return render(req,"cates.html",{"data":cates})
#根据商品分类拿商品数据
def get_item_by_c_id(req):
    #解析get请求的c_id参数
    c_id = int(req.GET.get("c_id"))
    #获取商品数据
    items = Item.objects.filter(category_id=c_id)
    return render(req,"items.html",{"items":items})