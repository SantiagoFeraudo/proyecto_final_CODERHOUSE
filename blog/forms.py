from django import forms
from blog.models import Comment

class PostCommentForm(forms.ModelForm):
    content = forms.CharField(label='Ingrese su comentario.')

    class Meta:
        model = Comment 
        fields = ['content']

