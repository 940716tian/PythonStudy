"""day01 URL Configuration

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

from app01.views import hello, inter

from app01.views import home

from app01.views import get_humen

from app01.views import hehe

from app01.views import make_friends

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello$', hello),
    url(r'^myinter/', inter),
    url(r'^home/',home ),
    url(r'^humen/',get_humen ),
    url(r'^mygod$',hehe ),
    url(r'^girl/',make_friends ),



]
