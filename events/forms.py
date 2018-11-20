from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, University, RSO

class MyUserCreationForm(UserCreationForm):
    PERM_LEVELS = (
        ('Student', 'Student'),
        ('Admin', 'Admin'),
        ('Superadmin', 'Superadmin'),
    )
    
    name = forms.CharField(max_length=20)
    email = forms.EmailField()
    perm_level = forms.ChoiceField(choices=PERM_LEVELS)
    university = forms.ModelChoiceField(queryset=University.objects.all(), to_field_name='name', empty_label=None, required=False)
    rsos = forms.ModelMultipleChoiceField(queryset=RSO.objects.all(), to_field_name='name', required=False)


    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('name', 'email', 'perm_level', 'university',)