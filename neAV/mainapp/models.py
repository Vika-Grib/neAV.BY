from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
# class Photo(models.Model):
#     imagename = models.TextField()
#     articleimage = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
class Car(models.Model):
    vin = models.CharField(verbose_name='Vin-номер', db_index=True, unique=True, max_length=64)
    color = models.CharField(verbose_name='Цвет', max_length=64)
    brand = models.CharField(verbose_name='Марка', max_length=64)
    CAR_TYPES = (
        (1, 'Седан'),
        (2, 'Хэчбек'),
        (3, 'Универсал'),
        (4, 'Купе'),
        (5, 'Лифтбек'),
        (6, 'Кабриолет')
    )
    car_type = models.IntegerField(verbose_name='Тип машины', choices=CAR_TYPES)
    # photo = models.ManyToManyField(Photo, related_name='photos', blank=False)
    photo = models.ImageField(verbose_name='Фото', blank=True, upload_to='photos/')
    CAR_TRANSMISSION = (
        (1, 'Робот'),
        (2, 'Механика'),
        (3, 'Автомат')
    )
    transmission = models.IntegerField(verbose_name='Коробка передач', choices=CAR_TRANSMISSION)
    ENGINE_TYPES = (
        (1, 'Дизель'),
        (2, 'Бензин'),
        (3, 'Бензин (пропан-бутан'),
        (4, 'Бензин (бутан)')
    )
    engine_type = models.IntegerField(verbose_name='Тип двигателя', choices=ENGINE_TYPES)
    DRIVE_UNITS = (
        (1, 'Полный привод'),
        (2, 'Передний привод'),
        (3, 'Задний привод')
    )
    drive_unit = models.IntegerField(verbose_name='Привод', choices=DRIVE_UNITS)
    description = models.CharField(verbose_name='Описание', max_length=1000)
    PRICES = (
        (1, 'USD'),
        (2, 'BYN')
    )
    price = models.IntegerField(verbose_name='Цена', choices=PRICES)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    # так как эта модель может быть переопределена, то нужно наследователь эту модель из джанги


class Advertisment(models.Model):
    AD_TYPES = (
        (1, 'Легковой автомобиль'),
        (2, 'Грузовик или фургон'),
        (3, 'Мототехника'),
        (4, 'Спецтехника'),
        (5, 'С/х техника'),
        (6, 'Водный транспорт'),
    )
    advert_type = models.IntegerField(verbose_name='Тип транспорта', choices=AD_TYPES)

class Advertisment_parts(models.Model):
    AD_PARTS = (
        (1, 'Запчасти, автотовары и расходники'),
        (2, 'Шины и дискин')
    )
    parts_type = models.IntegerField(verbose_name='Тип транспорта', choices=AD_PARTS)

class Light_Car(models.Model, Advertisment):
    CAR_MARKS = (
        (1, 'Alfa Romeo'),
        (2, 'Audi'),
        (3, 'BMW'),
        (4, 'Chevrolet'),
        (5, 'Chrysler'),
        (6, 'Citroen'),
    )
    light_car_type = models.IntegerField(verbose_name='Тип транспорта', choices=CAR_MARKS)

class Car_Models(models.Model):
    CAR_MODELS = ()
    light_car_model = models.IntegerField(verbose_name='Модель автомобиля', choices=CAR_MODELS)

class Year(models.Model):
    CAR_YEARS = ()
    car_year = models.IntegerField(verbose_name='Год', choices=CAR_YEARS)

