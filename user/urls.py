from django.conf.urls import include
from rest_framework import routers
from django.urls import path

from . import views


app_name = "user"
urlpatterns=[
    path('',views.new, name='new'),
    # url(r'',)
]
