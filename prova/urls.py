
from django.urls import path

from .views import view_prova
from .views import resultado

urlpatterns = [
    path('', view_prova),
    path('resultado', resultado, name='resultado'),
]

