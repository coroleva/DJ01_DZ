from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def data(request):
    return HttpResponse("<a href='URL_адрес'> ссылка </a>")


def test(request):
    return HttpResponse("<h5>Это страница <h2>TEST</h2>проекта на Django</h5>")