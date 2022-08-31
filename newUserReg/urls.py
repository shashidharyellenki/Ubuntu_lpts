from django.urls import path

from . import views

urlpatterns=[
    path('', views.indexx, name='indexx'),
    path('login/', views.login, name='login'),
    
]