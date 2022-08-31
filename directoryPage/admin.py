from django.contrib import admin

# Register your models here.
from . models import Student, Course, Units, Units_content, Enrollments

class courseAdmin(admin.ModelAdmin):
    list_display= ('id', 'Name', 'Tags')
    list_display_links= ('Name' ,'Tags')
    list_filter= ('Name',)
admin.site.register(Course, courseAdmin)

class StudentCardAdmin(admin.ModelAdmin):
    list_display= ('id','Name','Email','acadamicYear','specalization')
    list_display_links=('Name',)
    list_filter=('specalization','acadamicYear')
admin.site.register(Student, StudentCardAdmin)


class UnitsAdmin(admin.ModelAdmin):
    list_display= ('id', 'Name')
    list_display_links=('Name',)
    list_filter= ('Name',)
admin.site.register(Units,UnitsAdmin)

class Units_contentAdmin(admin.ModelAdmin):
    list_display= ('id', 'Name')
    list_display_links=('Name',)
    list_filter= ('Name',)
admin.site.register(Units_content, Units_contentAdmin)

class EnrollmentAdmin(admin.ModelAdmin):
    list_display= ('id', 'StudentKey')
admin.site.register(Enrollments, EnrollmentAdmin)