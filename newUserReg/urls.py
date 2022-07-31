from . import views
from django.urls import path

urlpatterns=[
    path('', views.indexx, name='indexx')
]