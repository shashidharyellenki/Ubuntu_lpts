from . import views
from django.urls import path

urlpatterns=[
    path('', views.index, name='index'),
    path('<int:student_id>/', views.student, name='student'),
    path('mail', views.sendEmail, name='mail')

    
]