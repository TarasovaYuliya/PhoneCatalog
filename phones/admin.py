from django.contrib import admin
from .models import Phone, Subscriber
from .models import Message, Mark

admin.site.register(Subscriber)
admin.site.register(Phone)
admin.site.register(Message)
admin.site.register(Mark)
