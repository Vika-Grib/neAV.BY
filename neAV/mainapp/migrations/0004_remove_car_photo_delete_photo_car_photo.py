# Generated by Django 4.2.8 on 2023-12-27 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_car_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='photo',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AddField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Фото'),
        ),
    ]
