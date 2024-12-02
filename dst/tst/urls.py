from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', list, name='listcourse'),
    path('update/<str:pk>/', updatelist.as_view(), name='update'),
    path('src/', search, name='search'),
    path('del/<str:pk>/', delete.as_view(), name='del')
]
