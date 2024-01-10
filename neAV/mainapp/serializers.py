from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import Car, Advertisment, MyUser

# user = serializers.HiddenField(default=serializers.CurrentUserDefault())

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # по запросу чтобы не могли посмотреть пароль
    def create(self, data):
        user = MyUser(username=data['username'])
        user.set_password(data['password'])
        user.save()
        return user



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CarDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # становится скрытое поле юзера, то есть только авторизованный пользователь
    # будет давать свои объявления и их редактировать и hidden убирает строку с user в Rest
    class Meta:
        model = Car
        fields = '__all__'


class CarListView(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('brand', 'car_type', 'color')


class CarAdvertismentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Advertisment
        fields = '__all__'
    def create(self, data):
        advert = Advertisment(advert_type = data['advert_type'])
        advert.user = data['user']
        advert.brand = data['brand']
        advert.car_type = data['car_type']
        advert.color = data['color']
        advert.description = data['description']
        advert.mileage = data['mileage']
        advert.drive_unit = data['drive_unit']
        advert.engine_type = data['engine_type']
        advert.photo = data['photo']
        advert.price = data['price']
        advert.salon_material = data['salon_material']
        advert.transmission = data['transmission']
        advert.vin = data['vin']
        advert.save()
        return advert


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

