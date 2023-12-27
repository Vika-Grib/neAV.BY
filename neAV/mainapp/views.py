from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, generics

from .models import Car
from .serializers import GroupSerializer, UserSerializer, CarDetailSerializer, CarListView

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint который позволяет пользователям просматривать или редактировать
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


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