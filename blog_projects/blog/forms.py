from django import forms
from django.contrib.auth.forms import UserCreationForm, User

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author', 'title', 'body'
        ]
