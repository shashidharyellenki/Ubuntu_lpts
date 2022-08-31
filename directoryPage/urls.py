from . import views
from django.urls import path

urlpatterns=[
    path('', views.index, name='index'),
    path('<int:student_id>/', views.student, name='student'),
    path('mail', views.send_email, name='mail'),
    path('detail/<int:Units_id>/', views.details,name='details'),
    path('moredetails/<int:moredetails_id>/', views.CourseIndepthDetails, name="CourseIndepthDetails"),
    path('update_status', views.update_status, name="update_status")

    
]