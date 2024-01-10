from django.urls import include, path
from rest_framework import routers
from . import views
from .views import *


router = routers.DefaultRouter()
router.register('advert', CarAdvertisment)
router.register('detail', CarDetailView)
router.register('create', CarCreateView)
# urlpatterns += router.urls


urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('all/', CarListView.as_view()),
    path('car/', include(router.urls))
    # path('car/advert/create/', AdvertCreateView.as_view()),
    # path('users/all/', UserView.as_view()),
    # path('users/create/', UserCreateView.as_view())
]

# app_name = 'car'
# router = routers.DefaultRouter()
# router.register(r'groups', views.GroupViewSet)
# urlpatterns += router.urls

# подключаем API используя автоматическую маршрутизацию URL routing адресов
# Также мы включаем login URLs доступный для просмотра API
# api/v1/mainapp/car/create/
# api/v1/mainapp/all/
# api/v1/mainapp/car/detail/4/
# api/v1/mainapp/car/advert/ тут все объявления машин
# api/v1/mainapp/car/advert/create/
# api/v1/mainapp/users/all/
# api/v1/mainapp/users/create/