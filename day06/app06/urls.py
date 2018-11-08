from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r"^login$",my_login,name="login"),
    url(r"^get_prize$",get_prize),
    url(r"^create_book",create_book_v1),
    url(r"^create_book_v2$",create_book_v2),
    url(r"^img$",get_confirm_code),
    url(r"^mylogin$",my_login),
    url(r"^slogin$",slogin),
]