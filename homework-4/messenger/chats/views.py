from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from chats.models import Chat, Member
from user_profile.models import UserProfile
from messages.models import Message
from attachments.models import Attachment
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@require_http_methods(["GET", "POST"])
def chat_list(request, pk=None):
    if pk != None:
        print(pk)
        # return JsonResponse({"test": "App"})
        return render(request, "chat_list.html")
    return JsonResponse({"test": "chat_list"})


@require_http_methods(["GET", "POST"])
def chat_page(request):
    return JsonResponse({"test": "chat_page"})


"""ДЗ-6"""


@csrf_exempt
@login_required
@require_http_methods(["POST"])
def create_personal_chat(request):
    """Создание персонального чата"""
    # Личный чат пользователя
    # request.POST.keys() = [user_id]

    """
    if request.POST["user_id"] is None:
        return JsonResponse({"Error": "ID is None!"})
    """

    # user = UserProfile.objects.all().filter(id=request.user.id)
    # if len(user) == 0:
    #     return JsonResponse({"Error": "User does not exist"})
    # user = user[0]
    user = request.user

    chat = Chat.objects.create(topic="Personal chat")
    member = Member.objects.create()
    member.user = user
    member.chat = chat
    chat.save()
    member.save()
    return JsonResponse({"Create_personal_chat": "Personal chat created"})


@login_required
@require_http_methods(["GET", "POST"])
def get_chat_list(request):
    """Получение списка чатов"""

    # if pk is None:
    #     return JsonResponse({"Error": "ID is None!"})

    # user = UserProfile.objects.all().filter(id=request.user.id)
    # if len(user) == 0:
    #     return JsonResponse({"Error": "User does not exist"})
    # user = user[0]
    user = request.user

    members = Member.objects.all().filter(user=user.id)
    chats = [member.chat for member in members]
    print(chats)
    if len(chats) == 0:
        response = {"user_id": user.id,
                    "username": user.username,
                    "fullname": user.first_name + " " + user.last_name,
                    "chats": None
                    }
        return JsonResponse(response)

    chats_data = []
    for chat in chats:
        if chat.last_message:
            chats_data.append({
                "chat_id": chat.id,
                "is_group_chat": chat.is_group_chat,
                "topic": chat.topic,
                "last_message_id": chat.last_message.id,
                "last_message_content": chat.last_message.content,
                "last_message_added_at": chat.last_message.added_at
            })
        else:
            chats_data.append({
                "chat_id": chat.id,
                "is_group_chat": chat.is_group_chat,
                "topic": chat.topic,
                "last_message": None,
            })

    response = {
        "user_id": user.id,
        "username": user.username,
        "fullname": user.first_name + " " + user.last_name,
        "chats": chats_data
    }
    return JsonResponse(response)


"""ДЗ-7"""


@csrf_exempt
@login_required
@require_http_methods(["GET", "POST"])
def get_chat_page(request, chatid):
    """Получение страницы чата"""

    # if userid is None or chatid is None:
    #     return JsonResponse({"Error": "userID or chatID is None!"})

    # user = UserProfile.objects.all().filter(id=request.user.id)
    # if len(user) == 0:
    #     return JsonResponse({"Error": "User_id#{} does not exist".format(userid)})
    # user = user[0]
    user = request.user

    chat = Chat.objects.all().filter(id=chatid)
    # if len(chat) == 0:
    #     return JsonResponse({"Error": "Chat_id#{} does not exist".format(chatid)})
    chat = chat[0]

    # member = Member.objects.all().filter(user=request.user.id, chat=chatid)
    # if len(member) == 0:
    #     return JsonResponse({"Error": "User#{} does not have access to Chat#{}".format(userid, chatid)})

    messages = [message for message in Message.objects.all().filter(chat=chatid)]
    messages_data = None
    # print(messages)
    if len(messages) != 0:
        messages_data = [
            {
                "message_id": message.id,
                "from_user_id": message.user.id,
                "from_user_fullname": message.user.first_name + " " + message.user.last_name,
                "content": message.content,
                "added_at": message.added_at
            } for message in messages
        ]

    attachments = [attachment for attachment in Attachment.objects.all().filter(chat=chatid)]
    attachments_data = None
    if len(attachments) != 0:
        attachments_data = [
            {
                "attachment_id": attachment.id,
                "from_id": attachment.user.id,
                "from_user_fullname": attachment.user.first_name + " " + attachment.user.last_name,
                "message_id": attachment.message,
                "type_attachment": attachment.type_attachment,
                "url": attachment.url
            } for attachment in attachments
        ]

    response = {
        "user_id": user.id,
        "chat_page_id": chatid,
        "username": user.username,
        "fullname": user.first_name + " " + user.last_name,
        "chat_id#{} topic".format(chatid): chat.topic,
        "messages": messages_data,
        "attachments": attachments_data
    }
    return JsonResponse(response)

@csrf_exempt
@login_required
@require_http_methods(["POST"])
def create_chat(request):
    """Создание чата с кем-то одним"""
    # request.POST.keys() = [friend]

    # user = UserProfile.objects.all().filter(id=request.user.id)
    # if len(user) == 0:
    #     return JsonResponse({"Error": "User does not exist"})
    # user = user[0]
    user = request.user

    print(request.body)
    friend = UserProfile.objects.all().filter(id=request.POST["friend"])
    # if len(friend) == 0:
    #     return JsonResponse({"Error": "User does not exist"})
    friend = friend[0]

    chat = Chat.objects.create(topic="{} и {}".format(user.first_name + " " + user.last_name,
                                                      friend.first_name + " " + friend.last_name))

    member_user = Member.objects.create()
    member_user.user = user
    member_user.chat = chat

    member_friend = Member.objects.create()
    member_friend.user = friend
    member_friend.chat = chat

    member_user.save()
    member_friend.save()
    chat.save()
    return JsonResponse({"Create_chat": "chat created"})
