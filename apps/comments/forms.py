from django import forms
from apps.comments.models import Comment


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('product', 'user')