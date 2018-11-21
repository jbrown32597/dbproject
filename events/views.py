from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django import forms
from .forms import MyUserCreationForm, EditUserForm, AddEventForm, AddCommentForm
from .models import University, User, Event, RSO, Comment

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
    form_class = EditUserForm

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
    fields = ['host', 'time', 'location', 'university', 'name', 'category', 'desc', 'contact_phone', 'contact_email', 'host_rso', 'event_type']

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user == self.get_object().host

class AddComment(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'events/addComment.html'
    form_class = AddCommentForm

    def get_form_kwargs(self):
        kwargs = {'initial': self.get_initial()}
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
                'request': self.request
            })
        return kwargs
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['pk'] = self.request.GET.get('pk', None)
    #     # print(self.request.GET.get('pk', None))
    #     return context

class EditComment(UserPassesTestMixin, UpdateView):
    model = Comment
    template_name = 'events/editComment.html'
    fields = ['text', 'rating']

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.pk == self.get_object().created_by.pk

class DeleteComment(UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'events/deleteComment.html'
    success_url = reverse_lazy('events:home')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.pk == self.get_object().created_by.pk

class RSOList(LoginRequiredMixin, ListView):
    model = RSO
    template_name = 'events/listRSOs.html'

class AddRSO(UserPassesTestMixin, CreateView):
    model = RSO
    template_name = 'events/addRSO.html'
    fields = ['name', 'num_students', 'university', 'admin']

    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.perm_level == 'Admin' or self.request.user.perm_level == 'Superadmin')

class ViewRSO(LoginRequiredMixin, DetailView):
    model = RSO
    template_name = 'events/viewRSO.html'

class EditRSO(UserPassesTestMixin, UpdateView):
    model = RSO
    template_name = 'events/editRSO.html'
    fields = ['name', 'num_students', 'university', 'admin']

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.pk == self.get_object().admin.pk