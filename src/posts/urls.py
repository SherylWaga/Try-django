from django.conf.urls import url 
from django.urls import path
from django.contrib import admin

from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create', views.post_create, name='post_create'),
    path('<int:id>', views.post_detail, name='detail'),
    path('update', views.post_update, name='post_update'),
    path('delete', views.post_delete, name='post_delete'),
   
]