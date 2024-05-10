from datetime import datetime
from django.contrib import messages
from django.contrib.auth import login
from django.db import models
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import Group
from django.urls import reverse
from knox.models import AuthToken
from knox.views import LoginView
from rest_framework import permissions, viewsets, generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .models import Car, Advertisment, MyUser, UsedAuto, ChatMessage
from .serializers import GroupSerializer, UserSerializer, CarDetailSerializer, CarListView, CarAdvertismentSerializer, \
    UserCreateSerializer, UsedCarListView, MessageSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from .send_tg_messages import *
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import MyUser, UsedAuto
from django.db.models import Subquery, Q, OuterRef
from .pagination import CustomPagination


@require_GET
def used_auto_list(request):
    # Получение query параметров из запроса
    brand = request.GET.get('brand')
    model = request.GET.get('model')
    year = request.GET.get('year')
    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')

    # Фильтрация данных на основе полученных параметров
    used_autos = UsedAuto.objects.all()
    if brand:
        used_autos = used_autos.filter(car__brand=brand)  # Предполагая, что есть связь с моделью Car
    if model:
        used_autos = used_autos.filter(car__model=model)  # Предполагая, что есть связь с моделью Car
    if year:
        used_autos = used_autos.filter(year=year)
    if price_min:
        used_autos = used_autos.filter(price_for_bel_rub__gte=price_min)
    if price_max:
        used_autos = used_autos.filter(price_for_bel_rub__lte=price_max)

    # Сериализация данных в JSON
    used_auto_data = list(used_autos.values('name', 'price_for_bel_rub', 'photo', 'year', 'kyzov', 'privod', 'color', 'probeg'))
    return JsonResponse({'results': used_auto_data})



@require_GET
def get_telegram_id(request):
    username = request.GET.get('username', None)
    if username is None:
        return JsonResponse({'error': 'Username is required'}, status=400)

    try:
        user = MyUser.objects.get(username=username)
        telegram_id = user.telegram_id
        return JsonResponse({'telegramId': telegram_id})
    except MyUser.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)


class UserView(ModelViewSet):
    """
    API endpoint который позволяет пользователям просматривать или редактировать
    """
    queryset = MyUser.objects.all().order_by('username')  #чтобы посмотреть наших всех юзеров
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny, ]


class UserCreateView(generics.GenericAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny, ]
    @csrf_exempt
    def post(self, request):
        serializer_class = self.get_serializer(data=request.data) #  передаем тот же наш сериалайзер, чтобы не ккофликтовала (т.к. функция и можно череез селф реализовать)
        serializer_class.is_valid(raise_exception=True)
        user = serializer_class.save()
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data, # context=self.get_serializer_context()) - все поля, содержание информации которое мы могли не видеть
            'token':  AuthToken.objects.create(user)[1]
        })

def send_tg_message(request):
    selected_items = request.session.get('users')
    if request.method == 'POST':
        date = request.POST.get('date')
        # formated_data = date.replace("T", " ")
        datetime_object = datetime.strptime(date, "%Y-%m-%dT%H:%M") if date else None

        text = request.POST.get('text')

        # получаем telegram_id выбранных пользователей
        telegram_ids = [item['telegram_id'] for item in selected_items]
        # срезаем тех, кто не привязал телегу (без telegram_id)
        filtered_tg_ids = list(filter(None, telegram_ids))

        # передаём в планировщик
        send_tg_msg(filtered_tg_ids, text, datetime_object)

        # Очищаем сессию
        request.session['selected_items'] = None
        # Добавляем уведомление об успехе на страницу админки
        messages.success(request, f'Сообщение добавлено в очередь отправки')
        # Возвращаемся на страницу админки с пользователями
        return HttpResponseRedirect('http://127.0.0.1:8000/admin/mainapp/myuser/')
    return render(request, 'admin/send_message.html')


class LoginAPI(LoginView):
    permission_classes = [permissions.AllowAny, ]
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer_class = AuthTokenSerializer(data=request.data) # класс из библиотеки встроенная
        serializer_class.is_valid(raise_exception=True)  # проверка на наличие ошибки валиндности: передали ли токен или блабла
        user = serializer_class.validated_data['user']  # задаем юзера, и передаем уже отвалидированную информацию по 'юзеру'
        print(user, '!!!!!!!!!!!!')
        login(request, user)  # функция встроеннная, чтобы залогинить юзера (запрос и параметры юзеры)
        return super(LoginAPI, self).post(request)  # super подтягивается от родителя - логинимся и делаем самомывоз этой же функции еще раз если логин не прошла



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
    permission_classes = [permissions.AllowAny, ]

# чтобы посмотреть все объекты в базе данных
class CarListView1(generics.ListAPIView):
    serializer_class = CarListView

    def get_queryset(self):
        user_id = self.request.user.id
        return Car.objects.filter(user_id=user_id)

    # ListAPIView обязательно принимает queryset - какие записи вынуть из БД
    # permission_classes = [permissions.AllowAny, ] # если нужно, чтобы просматривать должен только авторизованный
# просмотр конкретной записи, редактирование, удаление


class CarListUsed(ModelViewSet):
    serializer_class = UsedCarListView
    queryset = UsedAuto.objects.all()
    pagination_class = CustomPagination

class CarDetailView(ModelViewSet): # RetrieveUpdateDestroyAPIView - метод позволяет редактировать, удалять и получать данные об одном объекте
    serializer_class = CarDetailSerializer # CarDetailSerializer - указываем его, потому что нужны все поля
    queryset = Car.objects.all()
    # даем разрешение редактировать только тому, кто создал запись
    # permission_classes = [UserPermission, ]


class CarAdvertisment(ModelViewSet):
    serializer_class = CarAdvertismentSerializer
    def get_queryset(self):
        user_id = self.request.user.id
        return Advertisment.objects.filter(user_id=user_id)

    # permission_classes = [UserPermission, ]
    parser_classes = (MultiPartParser, FormParser) # для фото



class MyInbox(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']

        # messages = ChatMessage.objects.filter(
        #     id__in=Subquery(
        #         MyUser.objects.filter(
        #             Q(sender__reciever=user_id) |
        #             Q(reciever__sender=user_id)
        #         ).distinct().annotate(
        #             last_msg=Subquery(
        #                 ChatMessage.objects.filter(
        #                     Q(sender=OuterRef('id'), reciever=user_id) |
        #                     Q(reciever=OuterRef('id'), sender=user_id)
        #                 ).order_by('-id')[:1].values_list('id', flat=True)
        #             )
        #         ).values_list('last_msg', flat=True).order_by("-id")
        #     )
        # ).order_by("-id")
        messages = ChatMessage.objects.filter(
            Q(user_create_id=user_id) | Q(receiver_id=user_id)
        ).distinct().order_by('-date_time')

        return messages


class GetMessages(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        messages = ChatMessage.objects.filter(
            Q(user_create_id=user_id) | Q(receiver_id=user_id)
        ).distinct().order_by('-date_time')

        return messages
        # sender_id = self.kwargs['sender_id']
        # reciever_id = self.kwargs['reciever_id']
        # messages = ChatMessage.objects.filter(sender__in=[sender_id, reciever_id],
        #                                       reciever__in=[sender_id, reciever_id])

        # return messages


class SendMessages(generics.CreateAPIView):
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(user_create=self.request.user)



#######################################################################
# создать сообщение в чате или новый чат с сообщением (если чата ещё нет)
# class ChatMessageCreateView(generics.CreateAPIView):
#     queryset = ChatMessage.objects.all()
#     serializer_class = ChatMessageCreateSerializer
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request):
#         user_id = request.data.get('user_id')
#         message_text = request.data.get('text')
#
#         try:
#             user = MyUser.objects.get(id=user_id)
#         except MyUser.DoesNotExist:
#             return Response({"error": "Пользователь не найден"}, status=status.HTTP_404_NOT_FOUND)
#
#         chat = Chat.objects.filter(users__in=[self.request.user, user]).annotate(num_users=Count('users')).filter(
#             num_users=2).first()
#
#         if not chat:
#             chat = Chat.objects.create()
#             chat.users.add(self.request.user, user)
#
#         chat_message = ChatMessage.objects.create(
#             text=message_text,
#             user_create=self.request.user,
#         )
#
#         chat.messages.add(chat_message)
#
#         serializer = ChatMessageCreateSerializer(chat_message)
#         return Response({"info": "Сообщение создано",
#                          "message": serializer.data,
#                          "chat_id": chat.id,
#                          "users": [
#                              {
#                                  "id": f"{user.id}",
#                                  "username": f"{user.username}",
#                                  "photo": f"{request.build_absolute_uri(user.photo.url) if user.photo else None}"
#                              },
#                              {
#                                  "id": f"{self.request.user.id}",
#                                  "username": f"{self.request.user.username}",
#                                  "photo": f"{request.build_absolute_uri(self.request.user.photo.url) if self.request.user.photo else None}"
#                              }
#                          ]
#                          }, status=status.HTTP_201_CREATED)
#
#
# # получить список всех чатов текущего пользователя
# class ChatMessageRetrieveView(generics.ListAPIView):
#     serializer_class = ChatSerializer
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self):
#         user = self.request.user
#         return Chat.objects.filter(users=user)
#
# # обновить сообщение в чате
# class ChatMessageUpdateView(generics.RetrieveUpdateAPIView):
#     serializer_class = ChatMessageUpdateSerializer
#     permission_classes = [IsAuthenticated]
#     queryset = ChatMessage.objects.all()