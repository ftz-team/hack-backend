from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import tree

from .managers import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=1000, default='', blank=True, null=True, unique=True)
    email = models.EmailField(blank=True, null=True)
    first_name = models.CharField(max_length=1000, default='', blank=True, null=True)
    last_name = models.CharField(max_length=1000, default='', blank=True, null=True)

    age = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    city = models.CharField(max_length=1000, default='', blank=True, null=True)
    # main_application 

    # system
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        if self.first_name is not None and self.last_name is not None:
            return self.first_name + self.last_name
        return ''

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_superuser


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # values


class Event(models.Model):
    name = models.CharField(max_length=1000, default='', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    team = models.ManyToManyField(User, related_name='event_team', blank=True)