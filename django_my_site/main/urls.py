

from django.urls import path
#1
from .import views

#2 обработка перехода на 2 страницы (главную data и test)
urlpatterns = [
    path('', views.index),
    path('data', views.data),
    path('test', views.test)
]

# далее переходим на main/views для создания страниц
