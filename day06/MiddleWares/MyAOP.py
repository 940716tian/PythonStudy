from django.http import HttpResponse, HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin


class YJMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        # name = request.GET.get("name")
        # if name == "kang":
        #     return HttpResponse("恭喜中奖")
        # elif name == "ada":
        #     return HttpResponse("特等奖")
        # elif name == "班长":
        #     return HttpResponse("咖啡")
        black_ips = []
        #获取IP
        ip = request.META.get("REMOTE_ADDR")
        print(ip)
        if ip in black_ips:
            return HttpResponseForbidden("黑名单成员 无法访问")
        else:
            return HttpResponse("可以访问")