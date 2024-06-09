from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body', 'image', 'media_link', 'is_public', 'password')

        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blog title...'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title tag for this post...'}),
            'author': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'media_link': forms.URLInput(attrs={'class': 'form-control'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),

        }