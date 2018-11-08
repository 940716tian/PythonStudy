from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r"^data$",get_data),
    url(r"^cache$",my_cache_test),
]