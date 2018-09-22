from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index3),
    path('b/', views.index2),
    path('check_id/', views.check_id),

    path('register_member_db/',views.register_member_db),
    
]
