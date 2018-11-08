from django.conf.urls import  url
from .views import *

urlpatterns = [
    url(r"^get_card$",get_idcard_by_humen),
    url(r"^get_humen$",get_humen_by_idcard),
    url(r"^get_humen01$",get_humen_by_addr),
    url(r"^delete_humen$",delete_humen),
    # url(r"^get_grade$",get_grade_by_stu),
    # url(r"^get_stu$",get_stu_by_grade),
]