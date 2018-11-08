from django.http import HttpResponse
from django.shortcuts import render
import time
from .tasks import *
# Create your views here.

def first(req):
    return HttpResponse("今天第一个函数")


def test_task(req):
    # time.sleep(5)
    # my_task.delay()
    # task2.delay(5)
    result = res_task.delay(3)
    print(dir(result))
    print(result.task_id) #获取task_id
    return HttpResponse("OJBK")


def stu_view(req):
    return render(req,"stu.html")
