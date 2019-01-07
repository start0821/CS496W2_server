from django.conf.urls import include
from rest_framework import routers
from django.urls import path

from . import views


app_name = "contact"
urlpatterns=[
    path('',views.index, name='index'),
    path('<int:pk>/',views.detail, name='detail'),
    # url(r'',)
]
