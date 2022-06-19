from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserInfo, Picture, CalendarEntry

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(UserInfo)
admin.site.register(CalendarEntry)
admin.site.register(Picture)
