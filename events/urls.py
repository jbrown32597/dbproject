from django.urls import include, path
from .views import WelcomeView
from django.contrib.auth.views import LoginView

app_name = 'events'
urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('login/', LoginView.as_view())
]