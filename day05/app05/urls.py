from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r"^yx$",youxi),
    url(r"^myjson$",json_test),
    url(r"^res$",test_res),
    url(r"^mylogin01$",mylogin,name="mylogin"),
    url(r"^index01$",index,name="index"),
    url(r"^mylogout$",index,name="mylogout")
]
