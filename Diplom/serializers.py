from rest_framework import serializers
from .models import DeviceId, Talyplar
from django.shortcuts import get_object_or_404


class DeviceIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceId
        fields = ('username', 'device_id')

    def create(self, validated_data):
        return DeviceId.objects.create(**validated_data)
    

class UpdateStudentStatusSerializer(serializers.Serializer):
    device_id = serializers.CharField(max_length=255)

    def validate(self, data):
        device_id = data.get('device_id')
        device_id_query = get_object_or_404(DeviceId, device_id=device_id)
        if not Talyplar.objects.filter(device_id=device_id_query).exists():
            raise serializers.ValidationError("Invalid device_id: You not member of us.")
        return data