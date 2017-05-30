# log/forms.py
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from poem.models import Poem


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(
        attrs={'type': 'text', 'placeholder': 'نام کاربری ', 'class': 'form-control input-lg', 'name': 'username', 'id': 'username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(
        attrs={'type': 'password', 'placeholder': 'رمز شما', 'class': 'form-control input-lg', 'name': 'password', 'id': 'password'}))


class PoemForm(forms.ModelForm):

    class Meta:
        model = Poem
        fields = ('title', 'text', 'image','sound')
        widgets = {
            'title': forms.TextInput(attrs={'type': 'text', 'class': 'form-control parsley-validated'}),
            'text': forms.Textarea(attrs={'type': 'text', 'class': 'form-control input-lg','name':'editor1','id':'editor1','rows':'10','cols':'80'}),
            'image': forms.FileInput(attrs={'type': 'file', 'class': 'btn btn-success fileinput-button', 'name': 'picture'}),
            'sound': forms.FileInput(attrs={'type': 'file', 'class': 'btn btn-primary fileinput-button', 'name': 'picture'}),
        }
        labels = {
            'title': u'نام',
            'text' : u'توضیح' ,
            'image': u'عکس', 
            'sound': u'صدا', 
            
        }
        max_length = {
            'title': 30,
        }