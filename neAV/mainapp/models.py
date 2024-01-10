from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
#from django.contrib.auth import get_user_model
#User = get_user_model()

# Create your models here.
# class Photo(models.Model):
#     imagename = models.TextField()
#     articleimage = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)



class MyUser(AbstractUser):
    # date_of_birth = models.DateField()
    # height = models.FloatField()
    username = models.CharField(verbose_name='Логин', max_length=60, default='', unique=True)
    # login = models.CharField(verbose_name='Логин', max_length=30, default='')
    password = models.CharField(verbose_name='Пароль', max_length=20, default='')
    REQUIRED_FIELDS = ["password"]



class Car(models.Model):
    vin = models.CharField(verbose_name='Vin-номер', db_index=True, unique=True, max_length=64)
    color = models.CharField(verbose_name='Цвет', max_length=64, default='')
    brand = models.CharField(verbose_name='Марка', max_length=64, default='')
    CAR_TYPES = (
        (1, 'Седан'),
        (2, 'Хэчбек'),
        (3, 'Универсал'),
        (4, 'Купе'),
        (5, 'Лифтбек'),
        (6, 'Кабриолет')
    )
    car_type = models.IntegerField(verbose_name='Тип машины', choices=CAR_TYPES, default=1)
    # photo = models.ManyToManyField(Photo, related_name='photos', blank=False)

    photo = models.ImageField(verbose_name='Фото', blank=True, upload_to='photos/')

    CAR_TRANSMISSION = (
        (1, 'Робот'),
        (2, 'Механика'),
        (3, 'Автомат')
    )
    transmission = models.IntegerField(verbose_name='Коробка передач', choices=CAR_TRANSMISSION, default=1)
    ENGINE_TYPES = (
        (1, 'Дизель'),
        (2, 'Бензин'),
        (3, 'Бензин (пропан-бутан'),
        (4, 'Бензин (бутан)')
    )
    engine_type = models.IntegerField(verbose_name='Тип двигателя', choices=ENGINE_TYPES, default=1)
    DRIVE_UNITS = (
        (1, 'Полный привод'),
        (2, 'Передний привод'),
        (3, 'Задний привод')
    )
    drive_unit = models.IntegerField(verbose_name='Привод', choices=DRIVE_UNITS, default=1)
    description = models.CharField(verbose_name='Описание', max_length=1000, default='')
    PRICES = (
        (1, 'USD'),
        (2, 'BYN')
    )
    price = models.IntegerField(verbose_name='Цена', choices=PRICES, default=1)

    mileage = models.IntegerField(verbose_name='Пробег', default=1)

    SALON_MATERIALS = (
        (1, 'Искусственная кожа'),
        (2, 'Натуральная кожа'),
        (3, 'Ткань'),
        (4, 'Велюр'),
        (5, 'Алькантара'),
        (6, 'Комбинированные материалы')
    )
    salon_material = models.IntegerField(verbose_name='Материал салона', choices=SALON_MATERIALS, default=1)


    user = models.ForeignKey(MyUser, verbose_name='Пользователь', on_delete=models.CASCADE)
    # так как эта модель может быть переопределена, то нужно наследователь эту модель из джанги


class Advertisment(Car):
    AD_TYPES = (
        (1, 'Легковой автомобиль'),
        (2, 'Грузовик или фургон'),
        (3, 'Мототехника'),
        (4, 'Спецтехника'),
        (5, 'С/х техника'),
        (6, 'Водный транспорт'),
    )
    advert_type = models.IntegerField(verbose_name='Тип транспорта', choices=AD_TYPES)




class Equipment(models.Model):
    SAFETY_SYSTEMS = (
        (1, 'ABS'),
        (2, 'ESP'),
        (3, 'Антипробуксовочная'),
        (4, 'Иммобилайзер'),
        (5, 'Сигнализация')
    )
    safety_system = models.IntegerField(verbose_name='Система безопасности', choices=SAFETY_SYSTEMS)

    EXTERIERS = (
        (1, 'Легкосплавные диски'),
        (2, 'Рейлинги на крыше'),
        (3, 'Фаркоп')
    )
    exterier = models.IntegerField(verbose_name='Экстерьер', choices=EXTERIERS)

    INTERIERS = (
        (1, 'Панорамная крыша'),
        (2, 'Люк')
    )
    inetrier = models.IntegerField(verbose_name='Интерьер', choices=INTERIERS)

    HEADLIGHTS = (
        (1, 'Ксеноновые'),
        (2, 'Противотуманные'),
        (3, 'Светодиодные')
    )
    headlight = models.IntegerField(verbose_name='Фары', choices=HEADLIGHTS)

    PILLOWS = (
        (1, 'Ксеноновые'),
        (2, 'Противотуманные'),
        (3, 'Светодиодные')
    )
    pillows_safety = models.IntegerField(verbose_name='Подушки', choices=PILLOWS)

    HELPSYSTEMS = (
        (1, 'Датчик дождя'),
        (2, 'Камера заднего вида'),
        (3, 'Парктроники'),
        (3, 'Контроль мертвых зон на зеркалах')
    )
    help_system = models.IntegerField(verbose_name='Система помощи', choices=HELPSYSTEMS)

    CLIMATS = (
        (1, 'Климат-контроль'),
        (2, 'Кондиционер')
    )
    climat = models.IntegerField(verbose_name='Климат', choices=CLIMATS)

    HEATINGS = (
        (1, 'Сидений'),
        (2, 'Лобового стекла'),
        (3, 'Зеркал'),
        (2, 'Руля')
    )
    heating = models.IntegerField(verbose_name='ОБогрев', choices=HEATINGS)


class Advertisment_parts(models.Model):
    AD_PARTS = (
        (1, 'Запчасти, автотовары и расходники'),
        (2, 'Шины и дискин')
    )
    parts_type = models.IntegerField(verbose_name='Тип транспорта', choices=AD_PARTS)

class Light_Car(Advertisment):
    CAR_MARKS = (
        (1, 'Alfa Romeo'),
        (2, 'Audi'),
        (3, 'BMW'),
        (4, 'Chevrolet'),
        (5, 'Chrysler'),
        (6, 'Citroen'),
        (7, 'Dodge'),
        (8, 'Fiat')
    )
    light_car_type = models.IntegerField(verbose_name='Тип транспорта', choices=CAR_MARKS)

class Car_Models(models.Model):
    CAR_MODELS = ()
    light_car_model = models.IntegerField(verbose_name='Модель автомобиля', choices=CAR_MODELS)

class Year(models.Model):
    CAR_YEARS = ()
    car_year = models.IntegerField(verbose_name='Год', choices=CAR_YEARS)

