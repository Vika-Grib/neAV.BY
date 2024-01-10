from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets, generics
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet

from .models import Car, Advertisment, MyUser
from .serializers import GroupSerializer, UserSerializer, CarDetailSerializer, CarListView, CarAdvertismentSerializer, \
    UserCreateSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class UserView(ModelViewSet):
    """
    API endpoint который позволяет пользователям просматривать или редактировать
    """
    queryset = MyUser.objects.all().order_by('username')  #чтобы посмотреть наших всех юзеров
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

class UserPermission(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: GenericAPIView, obj: models.Model):
        if not request.user.is_authenticated:
            return False
        if view.action in ['update', 'partial_update', 'retrieve']:
            return obj == request.user or request.user.is_staff
        else:
            return False
    def has_permission(self, request: Request, view: GenericAPIView):
        if request.method in permissions.SAFE_METHODS:
            # проверяется условие является ли метод безопасным ( get, head, options) - ctrl + по методу кликнуть
            return True
        if view.action == 'create':
            return True
        if view.action == 'list':
            return True
        elif view.action in ['update', 'partial_update', 'retrieve']:
            return True
        else:
            return False
            # для почитать - он вернет True всем, если нужно что-то делать то вернет проверку
            # является ли юзер владельцем obj.user == request.user
        # return obj.user == request.user


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint который позволяет группам просматривать или редактировать
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [UserPermission, ]

# создание машины в БД
class CarCreateView(ModelViewSet):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()

# чтобы посмотреть все объекты в базе данных
class CarListView(generics.ListAPIView):
    serializer_class = CarListView
    queryset = Car.objects.all()
    # ListAPIView обязательно принимает queryset - какие записи вынуть из БД
    #permission_classes = (IsAuthenticated, ) # если нужно, чтобы просматривать должен только авторизованный
# просмотр конкретной записи, редактирование, удаление

class CarDetailView(ModelViewSet): # RetrieveUpdateDestroyAPIView - метод позволяет редактировать, удалять и получать данные об одном объекте
    serializer_class = CarDetailSerializer # CarDetailSerializer - указываем его, потому что нужны все поля
    queryset = Car.objects.all()
    # даем разрешение редактировать только тому, кто создал запись
    permission_classes = [UserPermission, ]


class CarAdvertisment(ModelViewSet):
    serializer_class = CarAdvertismentSerializer
    queryset = Advertisment.objects.all()
    permission_classes = [UserPermission, ]


# class AdvertCreateView(generics.CreateAPIView):
#     serializer_class = CarAdvertismentSerializer
#     permission_classes = [UserPermission, ]

