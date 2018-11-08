from django.conf.urls import url

from app05plus.views import index, register, mylogin

from app05plus.views import mylogout

urlpatterns = [
    url(r"^newindex01$",index),
    url(r"^register01$",register,name="register"),
    url(r"^mylogin01$",mylogin,name="mylogin"),
    url(r"^logout$",mylogout),
]