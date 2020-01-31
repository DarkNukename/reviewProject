from rest_framework import serializers
from .models import VacanciesDataBase

class VacanciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacanciesDataBase
        fields = "__all__"