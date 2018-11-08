from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app03plus.models import Person, IdCard# Stu, Grade


def get_idcard_by_humen(req):
    #有个人
    humen = Person.objects.get(pk=1)
    #访问身份证数据
    num = humen.idcard.num
    return HttpResponse(num)

#一对一关系的反向查询
def get_humen_by_idcard(req):
    idcard = "111111"
    obj = IdCard.objects.get(num=idcard)
    #类名小写
    humen_name = obj.person.name
    return HttpResponse(humen_name)

#跨关系查询 查人 身份证的签发单位是潢川的
def get_humen_by_addr(req):
    obj = Person.objects.filter(idcard__addr="潢川")
    print(obj)
    return HttpResponse("OK")


def delete_humen(req):
    # humen = Person.objects.get(id=1)
    # humen.delete()
    IdCard.objects.get(id=1).delete()
    return HttpResponse("删除ID为1的人")

# #通过学生拿到班级数据
# def get_grade_by_stu(req):
#     stu = Stu.objects.get(id=1)
#     return HttpResponse(stu.grade.name)
#
# #通过班级拿到学生数据
# def get_stu_by_grade(req):
#     grade = Grade.objects.get(id=1)
#
#     #学生类名小写set.all()
#     stus = grade.stu_set.all()
#     # stus = grade.stu_set.filter(id=1)
#     return HttpResponse(stus)