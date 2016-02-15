from django import forms
from .models import ImgMessage
from django.forms import ModelForm

class ImgMessageForm(ModelForm):
    class Meta:
        model = ImgMessage
        fields = ['img', 'text']
