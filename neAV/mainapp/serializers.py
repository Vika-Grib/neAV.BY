from django.contrib.auth.models import Group
from knox.models import AuthToken
from rest_framework import serializers
from .models import Car, Advertisment, MyUser, UsedAuto, ChatMessage, Chat


# user = serializers.HiddenField(default=serializers.CurrentUserDefault())


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'password']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'password'] # '__all__' - все поля в нашем ресте по моделям, которые встроены в формочку
        extra_kwargs = {'password': {'write_only': True}}  # по запросу чтобы не могли посмотреть пароль

    def create(self, data):
        user = MyUser.objects.create_user(data['username'], data['password'])
        # user = MyUser(username=data['username'])
        # user.set_password(data['password'])
        # token = AuthToken.objects.create(user)[1]  # создаем токен для юзера
        # user.token = token
        # user.save()
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CarDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # становится скрытое поле юзера, то есть только авторизованный пользователь
    # будет давать свои объявления и их редактировать и hidden убирает строку с user в rest
    class Meta:
        model = Car
        fields = '__all__'


class CarListView(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('brand', 'model', 'color', 'car_type', 'car_year', 'price')

class UsedCarListView(serializers.ModelSerializer):
    class Meta:
        model = UsedAuto
        fields = '__all__'


class CarAdvertismentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    photo = serializers.ImageField(required=False)
    class Meta:
        model = Advertisment
        fields = '__all__'
    def create(self, data):
        advert = Advertisment(advert_type = data['advert_type'])
        advert.user = data['user']
        advert.brand = data['brand']
        advert.model = data['model']
        advert.car_type = data['car_type']
        advert.color = data['color']
        advert.description = data['description']
        advert.mileage = data['mileage']
        advert.drive_unit = data['drive_unit']
        advert.engine_type = data['engine_type']
        advert.photo = data['photo']
        advert.price = data['price']
        advert.price_type = data['price_type']
        advert.salon_material = data['salon_material']
        advert.transmission = data['transmission']
        advert.vin = data['vin']
        advert.save()
        return advert


class MessageSerializer(serializers.ModelSerializer):
    user_create = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'  # или любое другое поле модели MyUser
    )
    class Meta:
        model = ChatMessage
        fields = '__all__'
        depth = 2

    def to_representation(self, instance):
        """
        Переопределение метода to_representation для изменения глубины вложенности.
        """
        # Если это POST запрос, уменьшить глубину
        if self.context.get('request', {}).method == 'POST':
            # Для POST запросов устанавливаем depth = 0, что означает нет вложенности
            return super(MessageSerializer, self).to_representation(instance)

        # Для всех остальных типов запросов использовать полную глубину
        representation = super(MessageSerializer, self).to_representation(instance)
        return representation



# class UserInfoRetrieveSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MyUser
#         fields = (
#             'id',
#             'username',
#         )
#
# class ChatMessageCreateSerializer(serializers.ModelSerializer):
#     user_create = UserInfoRetrieveSerializer(read_only=True)
#     class Meta:
#         model = ChatMessage
#         fields = '__all__'
#         read_only_fields = [
#             'user_create'
#         ]
#
# class ChatMessageRetrieveSerializer(serializers.ModelSerializer):
#     user_create = UserInfoRetrieveSerializer()
#     class Meta:
#         model = ChatMessage
#         fields = '__all__'
#
# class ChatMessageUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ChatMessage
#         fields = '__all__'
#         read_only_fields = [
#             'date_time',
#             'user_create',
#         ]
#
#     def update(self, instance, validated_data):
#         # убираем ключи со значениями None из словаря
#         for key, value in list(validated_data.items()):
#             if value is None:
#                 del validated_data[key]
#
#         instance.text = validated_data.get('text', instance.text)
#         instance.status = validated_data.get('status', instance.status)
#
#         instance.save()
#         return instance
#
#
# class ChatSerializer(serializers.ModelSerializer):
#     users = UserInfoRetrieveSerializer(many=True)
#     messages = ChatMessageRetrieveSerializer(many=True)
#     class Meta:
#         model = Chat
#         fields = '__all__'
#         read_only_fields = [
#             'users'
#         ]
#
#     # исключаем текущего пользователя из выводимого списка пользователей чата
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         request = self.context.get('request', None)
#
#         if request and request.user:
#             current_user_id = request.user.id
#             data['users'] = [user for user in data['users'] if user['id'] != current_user_id]
#
#         return data
#
