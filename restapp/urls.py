from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    #path(r'car', views.index),
    path(r'car/', views.MyView.as_view(), name='car'),
]