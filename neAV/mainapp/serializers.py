from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import Car


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarListView(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'vin', 'user')