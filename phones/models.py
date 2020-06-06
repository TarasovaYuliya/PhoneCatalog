from django.db import models
# встроенная модель пользователя нужна для авторов сообщений
from django.contrib.auth.models import User
# тип "временная зона" для получения текущего времени
from django.utils import timezone


class Subscriber(models.Model):
    Name = models.CharField(max_length=255)
    RegDate = models.DateTimeField('date published')
    Address = models.CharField(max_length=255)


class Phone(models.Model):
    IdSubscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    PhoneNumber = models.CharField(max_length=30)


class Message(models.Model):
    chat = models.ForeignKey(Subscriber, verbose_name='Чат под абонентом', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    message = models.TextField('Сообщение')
    pub_date = models.DateTimeField('Дата сообщения', default=timezone.now)


class Mark(models.Model):
    subscriber = models.ForeignKey(Subscriber, verbose_name='Абонент', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    mark = models.IntegerField(verbose_name='Оценка')
    pub_date = models.DateTimeField('Дата оценки', default=timezone.now)
