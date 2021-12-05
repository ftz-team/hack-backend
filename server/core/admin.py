from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email')


@admin.register(Application)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user')


@admin.register(Event)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Stage1)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Stage2)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Stage3)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Stage4)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')