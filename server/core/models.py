from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import tree

from .managers import UserManager

@receiver(post_save, sender='core.Application')
def create_chapters(sender, instance=None, created=False, **kwargs):
    if created:
        stage1 = Stage1(application=instance, status=0)
        stage2 = Stage2(application=instance, status=0)
        stage3 = Stage3(application=instance, status=0)
        stage4 = Stage4(application=instance, status=0)
        stage1.save()
        stage2.save()
        stage3.save()
        stage4.save()


# @receiver(post_save, sender='core.Stage3')
# def create_chapters(sender, instance=None, created=False, **kwargs):
#     if not created:
#         if instance.status == 3:



class User(AbstractBaseUser):
    username = models.CharField(max_length=1000, default='', blank=True, null=True, unique=True)
    email = models.EmailField(blank=True, null=True)
    tg = models.CharField(max_length=1000, default='', blank=True, null=True)
    first_name = models.CharField(max_length=1000, default='', blank=True, null=True)
    last_name = models.CharField(max_length=1000, default='', blank=True, null=True)

    age = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    city = models.CharField(max_length=1000, default='', blank=True, null=True)
    main_application = models.ForeignKey('core.Application', on_delete=models.CASCADE, related_name='main_app', null=True, blank=True)

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
            return self.first_name + ' ' + self.last_name
        return ''

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_superuser


class Event(models.Model):
    name = models.CharField(max_length=1000, default='', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    team = models.ManyToManyField(User, related_name='event_team', blank=True)
    contract_example = models.FileField(blank=True, null=True)


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def stage1(self):
        return Stage1.objects.get(application=self)

    @property
    def stage2(self):
        return Stage2.objects.get(application=self)

    @property
    def stage3(self):
        return Stage3.objects.get(application=self)

    @property
    def stage4(self):
        return Stage4.objects.get(application=self)
    
    @property
    def current_stage(self):
        stages = [self.stage1, self.stage2, self.stage3, self.stage4]
        for i in range(1, 4):
            if stages[i-1].status == 3 and stages[i].status != 3:
                return stages[i].name
            else:
                return stages[0].name


class Stage1(models.Model):
    name = models.CharField(max_length=1000, default='Подача заявки')
    application = models.ForeignKey(Application, on_delete=models.CASCADE, blank=True, null=True)
    STATUS_CODES = [
        (1, 'Не отправлено'),
        (2, 'На рассмотрении'),
        (3, 'Принято'),
        (4, 'Отклонено'),
    ]
    status = models.IntegerField(choices=STATUS_CODES)
    expirience = models.TextField(blank=True, null=True)
    video = models.FileField(blank=True, null=True)


class Stage2(models.Model):
    name = models.CharField(max_length=1000, default='Медицинские документы')
    application = models.ForeignKey(Application, on_delete=models.CASCADE, blank=True, null=True)
    STATUS_CODES = [
        (1, 'Не отправлено'),
        (2, 'На рассмотрении'),
        (3, 'Принято'),
        (4, 'Отклонено'),
    ]
    status = models.IntegerField(choices=STATUS_CODES)
    medical_cert = models.FileField(blank=True, null=True)


class Stage3(models.Model):
    name = models.CharField(max_length=1000, default='Подписание договора')
    application = models.ForeignKey(Application, on_delete=models.CASCADE, blank=True, null=True)
    STATUS_CODES = [
        (1, 'Не отправлено'),
        (2, 'На рассмотрении'),
        (3, 'Принято'),
        (4, 'Отклонено'),
    ]
    status = models.IntegerField(choices=STATUS_CODES)
    contract = models.FileField(blank=True, null=True)


class Stage4(models.Model):
    name = models.CharField(max_length=1000, default='Камчатка!')
    application = models.ForeignKey(Application, on_delete=models.CASCADE, blank=True, null=True)
    STATUS_CODES = [
        (1, 'Не отправлено'),
        (2, 'На рассмотрении'),
        (3, 'Принято'),
        (4, 'Отклонено'),
    ]
    status = models.IntegerField(choices=STATUS_CODES)