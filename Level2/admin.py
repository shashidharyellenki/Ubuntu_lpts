from django.contrib import admin

# Register your models here.
from . models import level2

class courseAdmin(admin.ModelAdmin):
    list_display= ('id', 'project_name')

admin.site.register(level2)