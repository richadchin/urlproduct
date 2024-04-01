from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create', views.create, name="create"),
    path('<str:pk>', views.search, name="search")
]