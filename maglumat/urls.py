from django.urls import path
from .views import*

urlpatterns = [
    path('talyplar',index_talyplar,name="talyplar"),
    path('talyplar_list',talyplar_list, name='talyplar_list'),
    path('toparlar',toparlar,name='toparlar'),
    path('topar_table',topar_table,name='topar_table'),
    path('wagtynda_gelenler',wagtynda_gelenler,name='wagtynda_gelenler'),
    path('wagtynda_gelenler_table/<str:date>/<str:category>',wagtynda_gelenler_table,name='wagtynda_gelenler_table'),
    path('gija_galanlar',gija_galanlar,name='gija_galanlar'),
    path('gija_galanlar_table/<str:date>/<str:category>',gija_galanlar_table,name='gija_galanlar_table'),
    path('gelmedikler',gelmedikler,name='gelmedikler'),
    path('gelmedikler_table/<str:date>/<str:category>',gelmedikler_table,name='gelmedikler_table'),
    path('barkod/<int:pk>/<int:which>',barkod,name='barkod'),
    path('',hello),
    path('hello',loginuser,name='loginuser'),
    path('logout',loguser_out,name='logging_out'),
    path('change_login',change_login,name='change_login')
]