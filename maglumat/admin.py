from django.contrib import admin
from .models import*

{'aman':'aman'}
{'myrat':'12mn09zx'}

class Posts(admin.ModelAdmin):
    search_fields=['at']

    class Meta:
        model=Talyplar

admin.site.register(del_info_gun)
admin.site.register(Toparlar)
admin.site.register(Talyplar,Posts)
admin.site.register(Talyp_Gunler)