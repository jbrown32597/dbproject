from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class MyUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=20)


    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('name',)