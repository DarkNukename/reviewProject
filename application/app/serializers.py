from rest_framework import serializers
from .models import AppDataBase

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppDataBase
        fields = "__all__"