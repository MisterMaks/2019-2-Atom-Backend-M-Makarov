from user_profile.views import user_profile, contacts, search_user
from user_profile.views import get_contacts
from django.urls import path

urlpatterns = [
    path('user_profile/', user_profile, name='user_profile'),
    path('contacts/', contacts, name='contacts'),

    # ДЗ-6
    path('search_user/', search_user, name='search_user'),
    path('search_user/<str:user_input>', search_user, name='search_user'),

    # ДЗ-7
    path('get_contacts/', get_contacts, name='get_contacts'),
    # path('get_contacts/<int:pk>', get_contacts, name='get_contacts'),
]
