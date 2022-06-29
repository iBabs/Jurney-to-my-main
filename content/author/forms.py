from django import forms
from .models import Post

class PostForms(forms):
    class Meta:
        model = Post
        fields =[
            'writter',
            'text'
        ]