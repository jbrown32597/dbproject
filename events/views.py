from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from .forms import MyUserCreationForm
from .models import University

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
        return redirect('events:home')

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'events/home.html'

class UniversityList(LoginRequiredMixin, ListView):
    model = University
    template_name = 'events/listUniversities.html'

class AddUniversity(LoginRequiredMixin, CreateView):
    model = University
    template_name = 'events/addUniversity.html'
    fields = ['name', 'location', 'desc', 'num_students']

class EditUniversity(LoginRequiredMixin, UpdateView):
    model = University
    template_name = 'events/editUniversity.html'
    fields = ['name', 'location', 'desc', 'num_students']