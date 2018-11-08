"""day02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app02.views import get_html, create_item, select_data, get_category, get_item_by_c_id

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^item/', get_html),
    url(r'^add_item$', create_item),
    url(r'^items$', select_data),
    url(r'^cates/',get_category ),
    url(r'^my_cate_items$',get_item_by_c_id ),

]
