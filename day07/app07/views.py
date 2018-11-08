from django.core.cache import cache ,caches
from django.core.paginator import Paginator
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
# cache_heihei = caches.get["heihei"]
from .models import Engineer
# Create your views here.
PER_PAGE = 6

@cache_page(30)
def get_data(req):
# 假装在拼命搜索数据  超级耗时
    import time
    time.sleep(5)
# 解析参数
    page_num = req.GET.get("page")
#查出所有数据
    data = Engineer.objects.all()
#实例化一个分页器
    paginator = Paginator(data,PER_PAGE)
    page = None
#通过来传过来的页码 获得page对象
    try:
        page = paginator.page(page_num)
#把page对象里的数据 我们读取出来 然后返回给前端（前端需要有个页面）
        result = page.object_list
    except:
        result = []
    res = {"data":result,
           "page_range":paginator.page_range,
           "page":page,
           "page_count":paginator.num_pages #总页码
}
    return render(req,"data.html",res)


def my_cache_test(req):
    #看缓存有没有数据
    res = cache.get("data")
    # res = cache_heihei.get("data")
    if res:
        print("有缓存")
        return JsonResponse(res)
    else:
        #查询model
        data = Engineer.objects.all()
        #把对象转成字典 model_to_dict()
        # model_to_dict()
        # c_data = [model_to_dict(i) for i in data]
        c_data = []
        print("被执行")
        for i in data:
            c_data.append(model_to_dict(i))

        #设置缓存
        result = {"my_data":c_data}
        cache.set("data",result,30)
        # cache_heihei.set("data",result,30)

        #返回数据给前端
        return JsonResponse(result)