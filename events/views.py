from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django import forms
from .forms import MyUserCreationForm, AddEventForm
from .models import University, User, Event

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

class HomeView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'events/home.html'

class ViewUser(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'events/viewUser.html'

class EditUser(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'events/editUser.html'
    fields = ['name', 'university', 'email', 'rsos']

class UniversityList(LoginRequiredMixin, ListView):
    model = University
    template_name = 'events/listUniversities.html'

class AddUniversity(UserPassesTestMixin, CreateView):
    model = University
    template_name = 'events/addUniversity.html'
    fields = ['name', 'location', 'desc', 'num_students']

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.perm_level == 'Superadmin'

class ViewUniversity(LoginRequiredMixin, DetailView):
    model = University
    template_name = 'events/viewUniversity.html'

class EditUniversity(UserPassesTestMixin, UpdateView):
    model = University
    template_name = 'events/editUniversity.html'
    fields = ['name', 'location', 'desc', 'num_students']

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.perm_level == 'Superadmin'

class AddEvent(UserPassesTestMixin, CreateView):
    model = Event
    template_name = 'events/addEvent.html'
    form_class = AddEventForm

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.perm_level == 'Admin' or self.request.user.perm_level == 'Superadmin')

class ViewEvent(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'events/viewEvent.html'

class EditEvent(UserPassesTestMixin, UpdateView):
    model = Event
    template_name = 'events/editEvent.html'
    fields = ['host', 'time', 'location', 'name', 'category', 'desc', 'contact_phone', 'contact_email', 'host_rso', 'event_type']

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.perm_level == 'Admin' or self.request.user.perm_level == 'Superadmin')