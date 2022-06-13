from dataclasses import fields
from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post", "date"]
        labels = {
            "username": "Your Name",
            "user_email": "Your Email",
            "text": "Your Comment"
        }