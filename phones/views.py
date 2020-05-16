from django.shortcuts import get_object_or_404, render, redirect
from .models import Phone


# главная страница
def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
    # создание HTML-страницы по шаблону index.html
    # с заданными параметрами latest_phones и message
    return render(
        request,
        "index.html",
        {
            "latest_phones":
                Phone.objects.order_by('-Name')[:5],
            "message": message
        }
    )


