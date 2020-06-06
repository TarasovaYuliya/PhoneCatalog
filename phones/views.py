from django.shortcuts import get_object_or_404, render, redirect
from .models import Subscriber, Phone
# Базовый класс для обработки страниц с формами.
from django.views.generic.edit import FormView
# Спасибо django за готовую форму регистрации.
from django.contrib.auth.forms import UserCreationForm
# Спасибо django за готовую форму аутентификации.
from django.contrib.auth.forms import AuthenticationForm
# Функция для установки сессионного ключа. По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login
# Для Log out с перенаправлением на главную
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
# Для смены пароля - форма
from django.contrib.auth.forms import PasswordChangeForm
# сообщения
from .models import Message
from datetime import datetime
# для ответа на асинхронный запрос в формате JSON
from django.http import JsonResponse
import json
# оценки
from .models import Mark
# вычисление среднего, например, средней оценки
from django.db.models import Avg


# главная страница
def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
    # создание HTML-страницы по шаблону index.html
    # с заданными параметрами latest_subscribers и message
    return render(
        request,
        "index.html",
        {
            "latest_subscribers":
                Subscriber.objects.order_by('Name')[:5],
            "message": message
        }
    )


# страница список телефонов для абонента
def detail(request, subscriber_id):
    error_message = None
    if "error_message" in request.GET:
        error_message = request.GET["error_message"]

    return render(
        request,
        "phones.html",
        {
            "subscriber": get_object_or_404(Subscriber, pk=subscriber_id),
            "error_message": error_message,
            "latest_messages": Message.objects.filter(chat_id=subscriber_id).order_by('-pub_date')[:5],
            # кол-во оценок, выставленных пользователем
            "already_rated_by_user": Mark.objects.filter(author_id=request.user.id).count(),
            # оценка текущего пользователя
            "user_rating":
                Mark.objects
                    .filter(author_id=request.user.id)
                    .filter(subscriber_id=subscriber_id)
                    .aggregate(Avg('mark'))["mark__avg"],
            # средняя по всем пользователям оценка
            "avg_mark": Mark.objects.filter(subscriber_id=subscriber_id).aggregate(Avg('mark'))["mark__avg"]
        }

    )


# базовый URL приложения, главной страницы - часто нужен при указании путей переадресации
app_url = "/phones/"


# наше представление для регистрации
class RegisterFormView(FormView):
    # будем строить на основе встроенной в django формы регистрации
    form_class = UserCreationForm
    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = app_url + "login/"
    # Шаблон, который будет использоваться при отображении представления.
    template_name = "reg/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()
        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


# наше представление для входа
class LoginFormView(FormView):
    # будем строить на основе встроенной в django формы входа
    form_class = AuthenticationForm
    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "reg/login.html"
    # В случае успеха перенаправим на главную.
    success_url = app_url

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()
        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


# для выхода - миниатюрное представление без шаблона - после выхода перенаправим на главную
class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)
        # После чего перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect(app_url)


# наше представление для смены пароля
class PasswordChangeView(FormView):
    # будем строить на основе встроенной в django формы смены пароля
    form_class = PasswordChangeForm
    template_name = 'reg/password_change_form.html'
    # после смены пароля нужно снова входить
    success_url = app_url + 'login/'

    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(PasswordChangeView, self).form_valid(form)


# функция для добавления сообщений для определенного абонента
def post(request, subscriber_id):
    msg = Message()
    msg.author = request.user
    msg.chat = get_object_or_404(Subscriber, pk=subscriber_id)
    msg.message = request.POST['message']
    msg.pub_date = datetime.now()
    msg.save()
    return HttpResponseRedirect(app_url + str(subscriber_id))


# функция, возвращающую список сообщений к абоненту в формате JSON
def msg_list(request, subscriber_id):
    # выбираем список сообщений
    res = list(
        Message.objects
            # фильтруем по id абонента
            .filter(chat_id=subscriber_id)
            # отбираем 5 самых свежих
            .order_by('-pub_date')[:5]
            # выбираем необходимые поля
            .values('author__username', 'pub_date', 'message')
    )
    # конвертируем даты в строки - сами они не умеют
    for r in res:
        r['pub_date'] = r['pub_date'].strftime('%d.%m.%Y %H:%M:%S')

    return JsonResponse(json.dumps(res), safe=False)


# функция для добавление оценки абоненту
def post_mark(request, subscriber_id):
    msg = Mark()
    msg.author = request.user
    msg.subscriber = get_object_or_404(Subscriber, pk=subscriber_id)
    msg.mark = request.POST['mark']
    msg.pub_date = datetime.now()
    msg.save()
    return HttpResponseRedirect(app_url + str(subscriber_id))


# функция, возвращающуя среднюю оценку загадки в формате JSON
def get_mark(request, subscriber_id):
    res = Mark.objects.filter(subscriber_id=subscriber_id).aggregate(Avg('mark'))

    return JsonResponse(json.dumps(res), safe=False)
