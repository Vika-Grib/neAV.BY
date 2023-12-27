from django.urls import include, path
from rest_framework import routers
from . import views
from .views import *

app_name = 'car'
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# подключаем API используя автоматическую маршрутизацию URL routing адресов
# Также мы включаем login URLs доступный для просмотра API
# api/v1/mainapp/car/create/
# api/v1/mainapp/all/
# api/v1/mainapp/car/detail/1

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('car/create/', CarCreateView.as_view()),
    path('all/', CarListView.as_view()),
    path('car/detail/<int:pk>/', CarDetailView.as_view()),
]

urlpatterns += router.urls