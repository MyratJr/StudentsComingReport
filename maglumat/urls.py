from django.urls import path
from .views import*

urlpatterns = [
    path('ishgarler',index_ishgarler,name="ishgarler"),
    path('ishgarler_list',ishgarler_list, name='ishgarler_list'),
    path('wezipeler',wezipeler,name='wezipeler'),
    path('wezipe_table',wezipe_table,name='wezipe_table'),
    path('wagtynda_gelenler/<str:date>',wagtynda_gelenler,name='wagtynda_gelenler'),
    path('wagtynda_gelenler_table/<str:date>',wagtynda_gelenler_table,name='wagtynda_gelenler_table'),
    path('gija_galanlar/<str:date>',gija_galanlar,name='gija_galanlar'),
    path('gija_galanlar_table/<str:date>',gija_galanlar_table,name='gija_galanlar_table'),
    path('gelmedikler/<str:date>',gelmedikler,name='gelmedikler'),
    path('gelmedikler_table/<str:date>',gelmedikler_table,name='gelmedikler_table'),
    path('barkod/<int:pk>/<int:which>',barkod,name='barkod'),
    path('',hello),
    path('hello',loginuser,name='loginuser'),
    path('logout',loguser_out,name='logging_out'),
    path('change_login',change_login,name='change_login')
]