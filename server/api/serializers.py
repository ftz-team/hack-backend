from django.db.models import fields
from rest_framework import serializers

from core.models import *

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class Stage1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Stage1
        fields = '__all__'


class Stage2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Stage2
        fields = '__all__'


class Stage3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Stage3
        fields = '__all__'


class Stage4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Stage4
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    stage1 = Stage1Serializer()
    stage2 = Stage2Serializer()
    stage3 = Stage3Serializer()
    stage4 = Stage4Serializer()
    user = UserSerializer()
    current_stage = serializers.ReadOnlyField()
    class Meta:
        model = Application
        fields = '__all__'


class CreateApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'