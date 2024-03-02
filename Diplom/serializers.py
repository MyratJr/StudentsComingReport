from rest_framework import serializers
from .models import DeviceId, Talyplar
from rest_framework.exceptions import APIException


class DeviceIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceId
        fields = ('username', 'device_id')

    def create(self, validated_data):
        return DeviceId.objects.create(**validated_data)
    

class ObjectNotFoundException(APIException):
    status_code = 400


class UpdateStudentStatusSerializer(serializers.Serializer):
    device_id = serializers.CharField(max_length=255)

    def validate(self, data):
        device_id = data.get('device_id')
        try:
            device_id_query = DeviceId.objects.get(device_id=device_id)
        except DeviceId.DoesNotExist:
            raise ObjectNotFoundException("Enjamyňyz hasaba alynmadyk. Hasaba goşmak üçin ýokarky düwmä basyň")
        try:
            Talyplar.objects.get(device_id=device_id_query)
        except Talyplar.DoesNotExist:
            raise ObjectNotFoundException("Siz hasaba goşulmadyk. Administratora ýüz tutuň")
        return data