from django.contrib import admin
from .models import*

class Posts(admin.ModelAdmin):
    search_fields=['at']

    class Meta:
        model=Ishgarler

admin.site.register(del_info_gun)
admin.site.register(Wezipeler)
admin.site.register(Ishgarler,Posts)
admin.site.register(Rugsatlar)
admin.site.register(Isgar_Gunler)
admin.site.register(Kurslar)
admin.site.register(Dinleyjiler)
admin.site.register(Dinleyji_Gunler)

# nginx for store media files