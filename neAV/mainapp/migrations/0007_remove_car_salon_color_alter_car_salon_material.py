# Generated by Django 4.2.8 on 2024-01-04 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_myuser_alter_car_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='salon_color',
        ),
        migrations.AlterField(
            model_name='car',
            name='salon_material',
            field=models.IntegerField(choices=[(1, 'Искусственная кожа'), (2, 'Натуральная кожа'), (3, 'Ткань'), (4, 'Велюр'), (5, 'Алькантара'), (6, 'Комбинированные материалы')], default=1, verbose_name='Материал салона'),
        ),
    ]
