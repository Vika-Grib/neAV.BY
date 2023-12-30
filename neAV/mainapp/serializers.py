from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import Car, Advertisment, MyUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ['name', 'login', 'password']


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


class CarAdvertismentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisment
        fields = '__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

