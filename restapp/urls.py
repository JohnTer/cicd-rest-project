from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path(r'car/', views.CarView.as_view(), name='car'),
    path(r'driver/', views.DriverView.as_view(), name='driver')
]