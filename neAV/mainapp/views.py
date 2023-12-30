from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets, generics

from .models import Car, Advertisment, MyUser
from .serializers import GroupSerializer, UserSerializer, CarDetailSerializer, CarListView, CarAdvertismentSerializer, \
    UserCreateSerializer


class UserView(generics.ListAPIView):
    """
    API endpoint который позволяет пользователям просматривать или редактировать
    """
    queryset = MyUser.objects.all().order_by('name')  #чтобы посмотреть наших всех юзеров
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint который позволяет группам просматривать или редактировать
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# создание машины в БД
class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer

# чтобы посмотреть все объекты в базе данных
class CarListView(generics.ListAPIView):
    serializer_class = CarListView
    queryset = Car.objects.all()
    # ListAPIView обязательно принимает queryset - какие записи вынуть из БД

# просмотр конкретной записи, редактирование, удаление
class CarDetailView(generics.RetrieveUpdateDestroyAPIView): # RetrieveUpdateDestroyAPIView - метод позволяет редактировать, удалять и получать данные об одном объекте
    serializer_class = CarDetailSerializer # CarDetailSerializer - указываем его, потому что нужны все поля
    queryset = Car.objects.all()


class CarAdvertisment(generics.ListAPIView):
    serializer_class = CarAdvertismentSerializer
    queryset = Advertisment.objects.all()


class AdvertCreateView(generics.CreateAPIView):
    serializer_class = CarAdvertismentSerializer

