from rest_framework import serializers
from .models import Apartment, Projects


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ['uuid', 'apartment', 'floor', 'parking', 'created_at', 'update_at']


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['title', 'apartments', 'image', 'description', 'finish_date', 'created_at', 'update_at']

