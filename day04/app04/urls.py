from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r"^index$",index),
    url(r"^langs$",langs,name="lele"),
    url(r"^newindex$",new_index),
    url(r"^myindex/(\d+)$",myindex_with_param,name="myindex"),
    url(r"^v1_index/(?P<p2>\d+)$",myindex_with_paramv1,name="v1index"),
    url(r"^newreverse$",new_reverse),
    url(r"^newreverse01$",new_reverse01),
    url(r"^block$",block),
    url(r"^include$",include),
    url(r"^block01$",home),

]