from messages.views import send_message
from messages.views import read_message
from django.urls import path

urlpatterns = [
    # ДЗ-7
    path('send_message/', send_message, name='send_message'),

    path('read_message/', read_message, name='read_message'),
]
