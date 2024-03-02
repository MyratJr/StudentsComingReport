from django.urls import path, include
from .views_2 import*
from rest_framework import routers


urlpatterns = [
    # path('diplom',diplom,name='diplom'),
    path('delete_item/<int:id>',delete_item,name='delete_item'),
    path('update/<int:id>/<int:which>',update,name="update"),
    path('create/<int:san>',creating,name="create"),
    path('create_device/', DeviceIdCreateView.as_view(), name='create_device_id'),
    path('update_status/', UpdateStudentStatusView.as_view(), name='update_student_status'),
]