from chats.views import chat_list, chat_page
from chats.views import create_personal_chat as cpc
from chats.views import get_chat_list as gcl
from chats.views import get_chat_page as gcp
from chats.views import create_chat
from django.urls import path

urlpatterns = [
    path('chat_list/', chat_list, name='chat_list'),
    path('chat_list/<int:pk>/', chat_list, name='chat_list'),

    path('chat_page/', chat_page, name='chat_page'),
    # ДЗ-6
    path('create_personal_chat/', cpc, name='create_personal_chat'),

    path('get_chat_list/', gcl, name='get_chat_list'),
    # path('get_chat_list/<int:pk>', gcl, name='get_chat_list'),
    # ДЗ-7
    # path('get_chat_page/', gcp, name='get_chat_page'),
    # path('get_chat_page/<int:userid>/', gcp, name='get_chat_page'),
    path('get_chat_page/<int:chatid>/', gcp, name='get_chat_page'),

    path('create_chat/', create_chat, name='create_chat')
]
