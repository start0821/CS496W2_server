from django.conf.urls import include
from django.urls import path

from . import views


app_name = "gallary"
urlpatterns=[
    path('',views.index, name='index'),
    path('<int:pk>/',views.detail, name='detail'),
]
