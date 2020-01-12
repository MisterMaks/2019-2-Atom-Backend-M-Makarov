from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from messages.model_forms import MessageForm
from messages.models import Message
from chats.models import Chat, Member
from user_profile.models import UserProfile
from attachments.models import Attachment
from attachments.model_forms import AttachmentForm
from django.views.decorators.csrf import csrf_exempt
from django.core.files.images import ImageFile
import magic

# Create your views here.
@csrf_exempt
@login_required
@require_http_methods(["POST"])
def upload_file(request):
    print(request.POST)
    attachment_form = AttachmentForm(request.POST)

    if attachment_form.is_valid():
        attachment = attachment_form.save()
        print(attachment.chat_id)
        chat = Chat.objects.all().filter(id=attachment.chat_id)[0]
        # user = UserProfile.objects.all().filter(id=request.user.id)[0]
        user = request.user
        message = Message.objects.create(chat=chat, user=user, content="Вложение")
        attachment.message = message
        attachment.image = ImageFile(open(attachment.key, 'rb'))
        attachment.type_attachment = magic.from_buffer((open(attachment.key, 'rb')).read(), mime=True)
        attachment.save()

        members = Member.objects.all().filter(chat=attachment.chat_id).exclude(user=user.id)
        for member in members:
            if member.new_messages is None:
                member.new_messages = 0
            member.new_messages += 1
            member.save()

        user_member = Member.objects.all().filter(user=user.id, chat=attachment.chat_id)[0]
        user_member.new_messages = 0
        user_member.last_read_message = message
        user_member.save()

        chat = Chat.objects.all().filter(id=message.chat_id)[0]
        chat.last_message = message
        chat.save()

        response = {
            "response": "attachment sent",
            "user_id": message.user_id,
            "chat_id": message.chat_id,
            "added_at": message.added_at,
            "content": message.content,
            "attachment_key": attachment.key
        }

        return JsonResponse(response)
    return JsonResponse({"errors": attachment_form.errors}, status=400)


@login_required
@require_http_methods(["GET", "POST"])
def download_file(request, key=None):
    if key is None:
        return JsonResponse({"Error": "key is None!"})
    attachment_url = Attachment.objects.filter(key=key)[0].image.url
    print(attachment_url)
    response = "<img src='{}'>".format(attachment_url)
    return HttpResponse(response)


