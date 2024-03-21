from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Advertisment, MyUser, Message
from django.contrib.auth.admin import UserAdmin
from .forms import *
from django.utils.translation import gettext_lazy as _
from django.db.models import QuerySet

# Register your models here.
class AdvertismentAdmin(admin.ModelAdmin):
    list_display = ('advert_type', )
    search_fields = ('advert_type', )
    # list_editable = ('advert_type', )
    list_filter = ('advert_type', )


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('phone', 'username', 'email', 'photo', 'password1', 'password2'),
    #     }),
    # )
    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     (_('Personal info'), {'fields': ('email', 'phone', 'photo', 'telegram_id', 'is_telegram_use')}),
    #     (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    #     (_('Important dates'), {'fields': ('last_login',)}),
    # )
    list_display = ('username', 'password')
    search_fields = ('username', )
    ordering = ('username',)

    actions = ['send_tg_message']

    @admin.action(description='Отправить сообщение в telegram')
    def send_tg_message(self, request, queryset: QuerySet):
        selected_items = queryset.values()
        # Создание нового массива объектов, содержащего только
        # ключи: "id", "username", "telegram_id" и "is_telegram_use"
        # этот подход позволяет также отправлять админов
        # (т.к. в составе их объекта есть time_delta
        users = [
            {
                "id": obj["id"],
                "username": obj["username"],
                "telegram_id": obj["telegram_id"],
                "is_telegram_use": obj["is_telegram_use"]
            } for obj in selected_items]
        request.session['users'] = list(users)
        return HttpResponseRedirect(reverse('send_tg_message'))


# @admin.register(Messaging) - либо декоратор, либо register внизу как стоит сейчас
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'id', 'short_text', 'status')
    search_fields = ('date_time', 'text')
    readonly_fields = ('date_time', 'message_id', 'status')

    # часть текста сообщения
    def short_text(self, obj):
        return obj.text[:100]
    short_text.short_description = "Сокращённый текст"
    # todo - добавить действие отправки отложенных рассылок сейчас

async def broadcast(text, recipients):
    api_token = '6724758298:AAGsEf6wbprcz1KhH_eMeft9RPr9i0UbBJs'
    # Initialize bot and dispatcher
    bot = Bot(token=api_token)
    for recipient in recipients:
        await bot.send_message(chat_id=recipient, text=text)


admin.site.register(Advertisment, AdvertismentAdmin)

