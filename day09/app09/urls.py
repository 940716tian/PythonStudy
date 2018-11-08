from django.conf.urls import url
from .views import *

urlpatterns = [
     url(r"^first$",first),
     url(r"^test_task$",test_task),
     url(r"^stu01$",stu_view),
 ]