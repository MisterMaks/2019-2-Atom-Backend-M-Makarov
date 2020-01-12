from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from user_profile.models import UserProfile
from django.http import HttpResponse
from chats.models import Member

# Create your views here.
@require_http_methods(["GET", "POST"])
def user_profile(request):
    return JsonResponse({'test': 'user_profile'})


@require_http_methods(["GET", "POST"])
def contacts(request):
    return JsonResponse({'test': 'contacts'})


"""ДЗ-6"""

@login_required
@require_http_methods(["GET", "POST"])
def search_user(request, user_input=None):
    """Поиск пользователей"""
    # user_input - id, name, nick

    if user_input is None:
        return JsonResponse({"Error": "Your input is None"})

    try:
        for_user_ids = UserProfile.objects.filter(id=int(user_input))
    except ValueError:
        for_user_ids = []

    for_user_usernames = UserProfile.objects.filter(username__contains=str(user_input))
    for_user_first_names = UserProfile.objects.filter(first_name__contains=str(user_input))
    for_user_last_names = UserProfile.objects.filter(last_name__contains=str(user_input))

    result = [user for user in for_user_ids]

    for user in for_user_usernames:
        if user not in result:
            result.append(user)

    for user in for_user_first_names:
        if user not in result:
            result.append(user)

    for user in for_user_last_names:
        if user not in result:
            result.append(user)

    if len(result) == 0:
        return JsonResponse({"response": "no such users {}".format(user_input)})

    users = {
        "searched users with {}".format(user_input): [
            {
                "user_id": res.id,
                "username": res.username,
                "first_name": res.first_name,
                "last_name": res.last_name,
                "avatar": res.avatar.url if res.avatar else None
            } for res in result
        ]
    }
    return JsonResponse(users)


"""ДЗ-7"""


@login_required
@require_http_methods(["GET", "POST"])
def get_contacts(request):
    """Получение списка контактов"""

    # if pk is None:
    #     return JsonResponse({"Error": "ID is None!"})

    user = request.user
    members = Member.objects.all().filter(user=user.id)
    if len(members) == 0:
        return JsonResponse({"Error": "no contacts"})

    chats = [member.chat for member in members]
    all_chats_members = []
    for chat in chats:
        members = Member.objects.all().filter(chat=chat.id)
        all_chats_members += [member for member in members]

    contact_members = []
    for member in all_chats_members:
        contact = UserProfile.objects.all().filter(id=member.user.id)[0]
        contact_members.append(contact)
    contact_members = set(contact_members)

    response = {
        "user_id": user.id,
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "avatar": user.avatar.url if user.avatar else None,
        "contacts": [
            {
                "user_id": contact_member.id,
                "username": contact_member.username,
                "first_name": contact_member.first_name,
                "last_name": contact_member.last_name,
                "avatar": contact_member.avatar.url if user.avatar else None
            } for contact_member in contact_members
        ]
    }
    return JsonResponse(response)


def login(request):
    print(request)
    return render(request, 'login.html')


@login_required
def home(request):
    print(request.user.id)
    return render(request, 'home.html')
