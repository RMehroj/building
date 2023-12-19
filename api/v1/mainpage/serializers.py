from rest_framework import serializers

from conf.serializers import DynamicFieldsModelSerializer
from . import models


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Apartment
        fields = [
            'uuid',
            'apartment',
            'floor',
            'parking',
            'created_at',
            'update_at',
            ]


class ProjectsSerializer(DynamicFieldsModelSerializer):
    apartments = ApartmentSerializer(
        many=True, 
        read_only=True
        )
    
    class Meta:
        model = models.Projects
        fields = [
            'uuid',
            'title',
            'apartments',
            'image',
            'description',
            'finish_date',
            'created_at',
            'update_at',
            ]


class SocialnetworkSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models.SocialNetwork
        fields = [
            'title',
            'instagram',
            'telegram',
            'facebook',
        ]


class SalesOfficeSerializer(DynamicFieldsModelSerializer):
    projects = ProjectsSerializer(
        read_only=True,
        fields=["projects"],
    )
    social_network = SocialnetworkSerializer(
        read_only=True,
        fields=["social_network"],
    )
    class Meta: 
        model = models.SalesOffice
        fields = [
            'uuid',
            'projects',
            'social_network'
            'phone',
            'city',
            'location',
            'created_at',
            'update_at',
        ]


class NewsroomSerializer(serializers.Serializer):
    class Meta:
        model = models.Newsroom
        fields = [
            'uuid',
            'title',
            'description',
            'image',
            'created_at',
            'update_at',
        ]


class AboutSerializer(serializers.Serializer):
    class Meta:
        model = models.About
        fields = [
            'uuid',
            'company_name',
            'license',
            'achievements',
            'phone',
            'descrption',
            'created_at',
            'update_at',
        ]