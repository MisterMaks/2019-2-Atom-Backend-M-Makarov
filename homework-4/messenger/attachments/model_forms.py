from django import forms
from attachments.models import Attachment


class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ('chat', 'user', 'url', 'key')
