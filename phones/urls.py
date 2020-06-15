from django.conf.urls import url
from . import views

app_name = 'phones'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^password-change/', views.PasswordChangeView.as_view()),
    # отправка сообщения
    url(r'^([0-9]+)/post/$', views.post, name='post'),
    # отправка списка сообщений
    url(r'^([0-9]+)/msg_list/$', views.msg_list, name='msg_list'),
    # отправка оценки
    url(r'^([0-9]+)/post_mark/$', views.post_mark, name='post_mark'),
    # средняя оценка
    url(r'^([0-9]+)/get_mark/$', views.get_mark, name='get_mark'),
    # добавление нового абонента
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^post_phone/$', views.post_phone, name='post_phone'),
]
