from django import forms
from .models import Comment, Post


class PostBlog(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title","body","image","status","tags"]


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
