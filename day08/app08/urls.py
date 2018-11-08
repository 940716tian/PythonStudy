from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r"^easy_send$",test_email),
    url(r"^html_send$",send_html),
    url(r"^file_send$",file_email),
    url(r"^many_send$",send_many),
    url(r"^register$",send_verify_mail),
    url(r"^verify/(.*)",verify),
    url(r"^test$",test),
    url(r"^cz$",cz_api)


]