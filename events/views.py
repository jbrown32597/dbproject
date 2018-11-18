from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from .forms import MyUserCreationForm

# Create your views here.
class WelcomeView(TemplateView):
    template_name = 'events/welcome.html'

class RegistrationView(FormView):
    template_name = 'events/register.html'
    form_class = MyUserCreationForm
    
    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect('events:welcome')