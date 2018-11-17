from django.urls import include, path
from .views import WelcomeView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'events'
urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('login/', LoginView.as_view(template_name='events/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='events/logout.html'), name='logout'),
]