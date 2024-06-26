from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.conf import settings

#from django.contrib.auth import get_user_model
#User = get_user_model()

# Create your models here.
# class Photo(models.Model):
#     imagename = models.TextField()
#     articleimage = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)



class MyUser(AbstractUser):
    username = models.CharField(verbose_name='Логин', max_length=60, default='', unique=True)
    # login = models.CharField(verbose_name='Логин', max_length=30, default='')
    # token = models.CharField(verbose_name='Токен', max_length=100, default='', editable=False)
    password = models.CharField(verbose_name='Пароль', max_length=20, default='')

    is_telegram_use = models.BooleanField(blank=True, default=False, verbose_name="Telegram привязан")
    telegram_id = models.CharField(max_length=12, blank=True, default="", verbose_name="Telegram id")

    REQUIRED_FIELDS = ["password"]


def upload_to(instance, filename):
    return 'photos/{filename}'.format(filename=filename)


class Message(models.Model):
    text = models.TextField(verbose_name="Текст сообщения", null=True)
    date_time = models.DateTimeField(verbose_name="Дата отправки", default=datetime.now(), blank=True, null=True)
    message_id = models.CharField(max_length=100, verbose_name="id сообщения", default="", blank=True)
    status = models.BooleanField(verbose_name="Статус отправки", default=True)

    def __str__(self):
        return f"[{self.date_time}] {self.text[:50]}"

    class Meta:
        verbose_name = "Сообщение в telegram"
        verbose_name_plural = "Сообщения в telegram"


class Car(models.Model):
    vin = models.CharField(verbose_name='Vin-номер', db_index=True, unique=True, max_length=64)
    color = models.CharField(verbose_name='Цвет', max_length=64, default='')
    brand = models.CharField(verbose_name='Марка', max_length=64, default='')
    model = models.CharField(verbose_name='Модель', max_length=64, default='')
    CAR_TYPES = (
        ('1', 'Седан'),
        ('2', 'Хэчбек'),
        ('3', 'Универсал'),
        ('4', 'Купе'),
        ('5', 'Лифтбек'),
        ('6', 'Кабриолет')
    )
    car_type = models.CharField(verbose_name='Тип машины', choices=CAR_TYPES, default='1', max_length=5)
    # photo = models.ManyToManyField(Photo, related_name='photos', blank=False)

    photo = models.ImageField(verbose_name='Фото', blank=True, upload_to=upload_to, null=True)

    CAR_TRANSMISSION = (
        (1, 'Робот'),
        (2, 'Механика'),
        (3, 'Автомат')
    )
    transmission = models.CharField(verbose_name='Коробка передач', choices=CAR_TRANSMISSION, default='1', max_length=10)
    ENGINE_TYPES = (
        (1, 'Дизель'),
        (2, 'Бензин'),
        (3, 'Бензин (пропан-бутан)'),
        (4, 'Бензин (бутан)')
    )
    engine_type = models.CharField(verbose_name='Тип двигателя', choices=ENGINE_TYPES, default='1', max_length=10)
    DRIVE_UNITS = (
        (1, 'Полный привод'),
        (2, 'Передний привод'),
        (3, 'Задний привод')
    )
    drive_unit = models.CharField(verbose_name='Привод', choices=DRIVE_UNITS, default='1', max_length=5)
    description = models.CharField(verbose_name='Описание', max_length=1000, default='')
    PRICES = (
        ('1', 'USD'),
        ('2', 'BYN')
    )
    price_type = models.CharField(verbose_name='Цена', choices=PRICES, default='1', max_length=5)
    price = models.IntegerField(verbose_name='Цена', default=1)

    mileage = models.IntegerField(verbose_name='Пробег', default=1)

    SALON_MATERIALS = (
        (1, 'Искусственная кожа'),
        (2, 'Натуральная кожа'),
        (3, 'Ткань'),
        (4, 'Велюр'),
        (5, 'Алькантара'),
        (6, 'Комбинированные материалы')
    )
    salon_material = models.CharField(verbose_name='Материал салона', choices=SALON_MATERIALS, default='1', max_length=10)

    user = models.ForeignKey(MyUser, verbose_name='Пользователь', on_delete=models.CASCADE)
    # так как эта модель может быть переопределена, то нужно наследователь эту модель из джанги

class UsedAuto(models.Model):
    name = models.CharField(max_length=64)
    price_for_bel_rub = models.CharField(max_length=64)
    price_for_usd = models.CharField(max_length=64)
    photo = models.CharField(max_length=64)
    year = models.CharField(max_length=64)
    kpp = models.CharField(max_length=64)
    volume = models.CharField(max_length=64)
    type_engine = models.CharField(max_length=64)
    probeg = models.CharField(max_length=64)
    kyzov = models.CharField(max_length=64)
    privod = models.CharField(max_length=64)
    color = models.CharField(max_length=64)
    power = models.CharField(max_length=64)
    comment = models.CharField(max_length=64)
    addcat_id = models.CharField(default='1', max_length=64)
    telegram_id = models.CharField(verbose_name='Телеграм_id',default='365034577', max_length=15)


class Advertisment(Car):
    AD_TYPES = (
        ('1', 'Легковой автомобиль'),
        ('2', 'Грузовик или фургон'),
        ('3', 'Мототехника'),
        ('4', 'Спецтехника'),
        ('5', 'С/х техника'),
        ('6', 'Водный транспорт'),
    )
    advert_type = models.CharField(verbose_name='Тип транспорта', choices=AD_TYPES, max_length=5, default='1')


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
        ('1', 'Alfa Romeo'),
        ('2', 'Audi'),
        ('3', 'BMW'),
        ('4', 'Chevrolet'),
        ('5', 'Chrysler'),
        ('6', 'Citroen'),
        ('7', 'Dodge'),
        ('8', 'Fiat')
    )
    light_car_type = models.CharField(verbose_name='Легковые автомобили', choices=CAR_MARKS, max_length=20)

class Moto(Advertisment):
    MOTO_MARKS = (
        ('1', 'Appollo'),
        ('2', 'Aprilia'),
        ('3', 'BMW'),
        ('4', 'BRP'),
        ('5', 'CFMOTO'),
        ('6', 'Ducati')
    )
    moto_type = models.CharField(verbose_name='Мототехника', choices=MOTO_MARKS, max_length=20)


class Car_Models(models.Model):
    CAR_MODELS = ()
    light_car_model = models.IntegerField(verbose_name='Модель автомобиля', choices=CAR_MODELS)

class Year(models.Model):
    CAR_YEARS = ()
    car_year = models.IntegerField(verbose_name='Год', choices=CAR_YEARS)



class ChatMessage(models.Model):
    user_create = models.ForeignKey(MyUser, verbose_name="Отправитель", on_delete=models.CASCADE, blank=True, null=True, related_name="created_chat_messages")  # Уникальное имя обратного отношения
    receiver = models.ForeignKey(MyUser, verbose_name="Получатель", on_delete=models.CASCADE,
                                 related_name="received_chat_messages", blank=True, null=True)

    status = models.BooleanField(verbose_name="статус прочтения получателем", default=False)
    text = models.TextField(verbose_name="Текст сообщения")
    date_time = models.DateTimeField(verbose_name="Дата отправки", auto_now_add=True)


    def __str__(self):
        return f"{self.user_create} - {self.receiver}"

    class Meta:
        verbose_name = "Сообщение в чате"
        verbose_name_plural = "Сообщения в чате"



# class Chat(models.Model):
#     users = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Пользователи чата")
#
#     def __str__(self):
#         user_names = ", ".join(user.username for user in self.users.all())
#         return f"Чат между: {user_names}"
#
#     class Meta:
#         verbose_name = "Чат"
#         verbose_name_plural = "Чаты"
#
# class Message(models.Model):
#     chat = models.ForeignKey(Chat, null=True, on_delete=models.CASCADE, verbose_name="Чат")
#     sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Отправитель", null=True)
#     message = models.TextField(verbose_name="Сообщение", null=True)
#     timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Время отправки", null=True)
#
#     def __str__(self):
#         return f"Сообщение от {self.sender.username} в {self.timestamp}"
#
#     class Meta:
#         ordering = ['timestamp']
#         verbose_name = "Сообщение"
#         verbose_name_plural = "Сообщения"





#
# class Chat(models.Model):
#     users = models.ManyToManyField(MyUser, verbose_name="Пользователи чата")
#     messages = models.ManyToManyField(ChatMessage, verbose_name="сообщения", blank=True)
#
#     def __str__(self):
#         return f"чат [{self.id}]"
#
#     class Meta:
#         verbose_name = "Чат"
#         verbose_name_plural = "Чаты"

    # @property
    # def sender_profile(self):
    #     sender_profile = Profile.objects.get(user=self.sender)
    #     return sender_profile
    # @property
    # def reciever_profile(self):
    #     reciever_profile = Profile.objects.get(user=self.reciever)
    #     return reciever_profile