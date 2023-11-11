from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import*
from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()

{'aman':'aman'}
{'myrat':'12mn09zx'}
{'kuwwat':'3edx4rfc'}


class Posts(admin.ModelAdmin):
    search_fields=['at']

    class Meta:
        model=Talyplar
        
admin.site.site_header = 'Administration'

class CustomUserAdmin(UserAdmin):
    list_filter=()
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Toparlar)
admin.site.register(Talyplar,Posts)
admin.site.register(Talyp_Gunler)