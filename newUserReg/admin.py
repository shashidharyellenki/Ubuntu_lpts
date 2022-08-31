

from django.contrib import admin

# Register your models here.
from . models import Register
class RegisterAdmin(admin.ModelAdmin):
    list_display= ('id', 'FirstName', 'LastName', 'email')
    list_display_links= ('FirstName' ,)
    list_filter= ('email',)
admin.site.register(Register,RegisterAdmin)