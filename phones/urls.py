from django.conf.urls import url
from . import views

app_name = 'phones'
urlpatterns = [
    url(r'^$', views.index, name='index')
]
