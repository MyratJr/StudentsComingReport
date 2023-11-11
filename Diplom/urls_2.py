from django.urls import path
from .views_2 import*

urlpatterns = [
    path('diplom',diplom,name='diplom'),
    path('delete_item/<int:id>',delete_item,name='delete_item'),
    path('update/<int:id>/<int:which>',update,name="update"),
    path('create/<int:san>',creating,name="create"),
]