# Generated by Django 4.2.8 on 2023-12-30 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_remove_car_photo_delete_photo_car_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisment',
            fields=[
                ('car_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mainapp.car')),
                ('advert_type', models.IntegerField(choices=[(1, 'Легковой автомобиль'), (2, 'Грузовик или фургон'), (3, 'Мототехника'), (4, 'Спецтехника'), (5, 'С/х техника'), (6, 'Водный транспорт')], verbose_name='Тип транспорта')),
            ],
            bases=('mainapp.car',),
        ),
        migrations.CreateModel(
            name='Advertisment_parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parts_type', models.IntegerField(choices=[(1, 'Запчасти, автотовары и расходники'), (2, 'Шины и дискин')], verbose_name='Тип транспорта')),
            ],
        ),
        migrations.CreateModel(
            name='Car_Models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('light_car_model', models.IntegerField(choices=[], verbose_name='Модель автомобиля')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('safety_system', models.IntegerField(choices=[(1, 'ABS'), (2, 'ESP'), (3, 'Антипробуксовочная'), (4, 'Иммобилайзер'), (5, 'Сигнализация')], verbose_name='Система безопасности')),
                ('exterier', models.IntegerField(choices=[(1, 'Легкосплавные диски'), (2, 'Рейлинги на крыше'), (3, 'Фаркоп')], verbose_name='Экстерьер')),
                ('inetrier', models.IntegerField(choices=[(1, 'Панорамная крыша'), (2, 'Люк')], verbose_name='Интерьер')),
                ('headlight', models.IntegerField(choices=[(1, 'Ксеноновые'), (2, 'Противотуманные'), (3, 'Светодиодные')], verbose_name='Фары')),
                ('pillows_safety', models.IntegerField(choices=[(1, 'Ксеноновые'), (2, 'Противотуманные'), (3, 'Светодиодные')], verbose_name='Подушки')),
                ('help_system', models.IntegerField(choices=[(1, 'Датчик дождя'), (2, 'Камера заднего вида'), (3, 'Парктроники'), (3, 'Контроль мертвых зон на зеркалах')], verbose_name='Система помощи')),
                ('climat', models.IntegerField(choices=[(1, 'Климат-контроль'), (2, 'Кондиционер')], verbose_name='Климат')),
                ('heating', models.IntegerField(choices=[(1, 'Сидений'), (2, 'Лобового стекла'), (3, 'Зеркал'), (2, 'Руля')], verbose_name='ОБогрев')),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_year', models.IntegerField(choices=[], verbose_name='Год')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.CharField(default='', max_length=1000, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='car',
            name='drive_unit',
            field=models.IntegerField(choices=[(1, 'Полный привод'), (2, 'Передний привод'), (3, 'Задний привод')], default=1, verbose_name='Привод'),
        ),
        migrations.AddField(
            model_name='car',
            name='engine_type',
            field=models.IntegerField(choices=[(1, 'Дизель'), (2, 'Бензин'), (3, 'Бензин (пропан-бутан'), (4, 'Бензин (бутан)')], default=1, verbose_name='Тип двигателя'),
        ),
        migrations.AddField(
            model_name='car',
            name='mileage',
            field=models.IntegerField(default=1, verbose_name='Пробег'),
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.IntegerField(choices=[(1, 'USD'), (2, 'BYN')], default=1, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='car',
            name='salon_color',
            field=models.IntegerField(choices=[(1, 'Искусственная кожа'), (2, 'Натуральная кожа'), (3, 'Ткань'), (4, 'Велюр'), (5, 'Алькантара'), (6, 'Комбинированные материалы')], default=1, verbose_name='Цвет салона'),
        ),
        migrations.AddField(
            model_name='car',
            name='salon_material',
            field=models.IntegerField(choices=[(1, 'Полный привод'), (2, 'Передний привод'), (3, 'Задний привод')], default=1, verbose_name='Материал салона'),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission',
            field=models.IntegerField(choices=[(1, 'Робот'), (2, 'Механика'), (3, 'Автомат')], default=1, verbose_name='Коробка передач'),
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(default='', max_length=64, verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_type',
            field=models.IntegerField(choices=[(1, 'Седан'), (2, 'Хэчбек'), (3, 'Универсал'), (4, 'Купе'), (5, 'Лифтбек'), (6, 'Кабриолет')], default=1, verbose_name='Тип машины'),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(default='', max_length=64, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/', verbose_name='Фото'),
        ),
        migrations.CreateModel(
            name='Light_Car',
            fields=[
                ('advertisment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mainapp.advertisment')),
                ('light_car_type', models.IntegerField(choices=[(1, 'Alfa Romeo'), (2, 'Audi'), (3, 'BMW'), (4, 'Chevrolet'), (5, 'Chrysler'), (6, 'Citroen'), (7, 'Dodge'), (8, 'Fiat')], verbose_name='Тип транспорта')),
            ],
            bases=('mainapp.advertisment',),
        ),
    ]
