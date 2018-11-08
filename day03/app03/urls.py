from django.conf.urls import url

from app03.views import get_data, get_data_by_q, get_data_by_f, delete_humen, update_humen

urlpatterns = [
    url(r"^getdata$",get_data),
    url(r"^qdata$",get_data_by_q),
    url(r"^fdata$",get_data_by_f),
    url(r"^del_humen$",delete_humen),
    url(r"^update$",update_humen),
]