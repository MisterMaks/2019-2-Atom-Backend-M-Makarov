from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from messages.model_forms import MessageForm
from messages.models import Message
from chats.models import Chat, Member
from user_profile.models import UserProfile
from attachments.models import Attachment
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
@login_required
@require_http_methods(["POST"])
def send_message(request):
    """Отправка сообщения"""
    # request.POST

    message_form = MessageForm(request.POST)

    if message_form.is_valid():
        message = message_form.save()
        # message.user = UserProfile.objects.filter(id=request.user.id)[0]
        user = request.user
        message.user = user
        message.save()

        members = Member.objects.all().filter(chat=message.chat_id).exclude(user=user.id)
        for member in members:
            if member.new_messages is None:
                member.new_messages = 0
            member.new_messages += 1
            member.save()

        user_member = Member.objects.all().filter(user=user.id, chat=message.chat_id)[0]
        user_member.new_messages = 0
        user_member.last_read_message = message
        user_member.save()

        chat = Chat.objects.all().filter(id=message.chat_id)[0]
        chat.last_message = message
        chat.save()

        response = {
            "response": "message sent",
            "user_id": request.user.id,
            "chat_id": message.chat_id,
            "added_at": message.added_at,
            "content": message.content
        }
        return JsonResponse(response)
    return JsonResponse({"errors": message_form.errors}, status=400)


@csrf_exempt
@login_required
@require_http_methods(["POST"])
def read_message(request):
    """Чтение сообщения"""
    # request.POST.keys() = [user_id, chat_id]

    """
    if request.POST.user_id is None or request.POST.chat_id is None:
        return JsonResponse({"Error": "ID/s is None!"})
    """

    user = request.user
    member = Member.objects.all().filter(user=user.id, chat=request.POST["chat_id"])
    if len(member) == 0:
        return JsonResponse({"Error": "Member does not exist"})
    member = member[0]
    member.new_messages = 0

    last_message = Message.objects.all().filter(chat=request.POST["chat_id"]).order_by('-added_at')[0]

    member.last_read_message = last_message
    member.save()
    return JsonResponse({"response": "message read"})




