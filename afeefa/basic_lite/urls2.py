from django.urls import path,include
from .views import *

urlpatterns=[
    path("",home,name="home"),
    path("insert/",insert,name="insert"),
    path("select/",select,name="select"),
]