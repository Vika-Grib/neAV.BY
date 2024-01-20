from django.contrib import admin
from .models import Advertisment, MyUser


# Register your models here.
class AdvertismentAdmin(admin.ModelAdmin):
    list_display = ('advert_type', )
    search_fields = ('advert_type', )
    # list_editable = ('advert_type', )
    list_filter = ('advert_type', )

class MyUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Advertisment, AdvertismentAdmin)
admin.site.register(MyUser, MyUserAdmin)

