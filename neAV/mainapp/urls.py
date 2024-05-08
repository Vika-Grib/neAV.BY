from django.urls import include, path
from rest_framework import routers
from . import views
from .views import *


router = routers.DefaultRouter()
# router.register('advert', CarAdvertisment)
router.register('detail', CarDetailView)
router.register('create', CarCreateView)
router.register('used', CarListUsed)
# http://127.0.0.1:8000/api/v1/mainapp/car/used/


# urlpatterns += router.urls


urlpatterns = [
    path('all/', CarListView1.as_view()),
    path('car/advert/', CarAdvertisment.as_view({'get': 'list'})),
    path('car/', include(router.urls)),
    path('send_tg_message/', send_tg_message, name='send_tg_message'),
    path('api/v1/mainapp/car/used/filter', used_auto_list, name='used_auto_list'),

    path('get-telegram-id/', get_telegram_id, name='get_telegram_id'),  # Измененный путь для API получения telegram_id
    path('api/', include('djoser.urls')),  # Маршруты для аутентификации и регистрации пользователей

    path("my-messages/<user_id>/", views.MyInbox.as_view()),
    path("get-messages/<sender_id>/<reciever_id>/", views.GetMessages.as_view()),
    path("send-messages/", views.SendMessages.as_view()),
    # http://127.0.0.1:8000/api/v1/mainapp/send-messages/

    # Get profile
    # path("profile/<int:pk>/", views.ProfileDetail.as_view()),
    # path("search/<username>/", views.SearchUser.as_view()),

    # path('chat_message/create/', ChatMessageCreateView.as_view(), name='chat_message_create'),
    # path('chat_message/list/', ChatMessageRetrieveView.as_view(), name='chat_message_list_view'),
    # path('chat_message/update/<int:pk>', ChatMessageUpdateView.as_view(), name='chat_message_update_view'),
]







# подключаем API используя автоматическую маршрутизацию URL routing адресов
# Также мы включаем login URLs доступный для просмотра API
# http://127.0.0.1:8000/api/v1/mainapp/search/1/
# api/v1/mainapp/get-telegram-id/
# api/v1/mainapp/car/create/
# api/v1/mainapp/car/detail/4/
# api/v1/mainapp/car/advert/ тут все объявления машин
# api/v1/mainapp/car/advert/create/
# api/users/
# http://127.0.0.1:8000/api/v1/mainapp/send-messages/
# api/v1/mainapp/chat_message/create/

# app_name = 'car'
# router = routers.DefaultRouter()
# router.register(r'groups', views.GroupViewSet)
# urlpatterns += router.urls