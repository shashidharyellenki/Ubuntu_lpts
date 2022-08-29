from . import views
from django.urls import path

urlpatterns=[
    path('<int:projects_id>/', views.details, name='details'),
   

    
]