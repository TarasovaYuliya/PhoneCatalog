from django.db import models


class Phone(models.Model):
    Name = models.CharField(max_length=255)
    RegDate = models.DateTimeField('date published')
    Address = models.CharField(max_length=255)
    PhoneNumber = models.CharField(max_length=30)

