from django.urls import path
from .views_2 import*

urlpatterns = [
    path('maglumat',maglumat,name='maglumat'),
    path('delete_item/<int:id>/<int:which>',delete_item,name='delete_item'),
    path('update/<int:id>/<int:which>',update,name="update"),
    path('create/<int:san>',creating,name="create"),
    path('rugsat/<int:id>/<int:which>',Rugsat_bermek,name="rugsat"),
]