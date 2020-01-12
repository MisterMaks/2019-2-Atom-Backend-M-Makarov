from django import forms
from chats.models import Chat


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('topic',)

