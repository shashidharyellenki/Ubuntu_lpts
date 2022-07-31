from django.contrib import admin

# Register your models here.
from . models import StudentCard, course
class courseAdmin(admin.ModelAdmin):
    list_display= ('id', 'courseName', 'status', 'continousCredits')
    list_display_links= ('courseName' ,)
    list_filter= ('courseName',)
admin.site.register(course, courseAdmin)

class StudentCardAdmin(admin.ModelAdmin):
    list_display= ('id','Name','Email','acadamicYear','specalization')
    list_display_links=('Name',)
    list_filter=('specalization','acadamicYear')
admin.site.register(StudentCard, StudentCardAdmin)

