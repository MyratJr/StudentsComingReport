from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.views.static import serve as mediaserve
import debug_toolbar

urlpatterns = [
    path('',include('maglumat.urls')),
    path('',include('maglumat.urls_2')),
    path('admin', admin.site.urls),
    re_path(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
                    mediaserve, {'document_root': settings.MEDIA_ROOT})
] 

if settings.DEBUG:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]