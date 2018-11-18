from django.urls import include, path
from .views import WelcomeView, RegistrationView, HomeView, UniversityList, AddUniversity, EditUniversity
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'events'
urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('login/', LoginView.as_view(template_name='events/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('home/', HomeView.as_view(), name='home'),
    path('universities/', UniversityList.as_view(), name='universities'),
    path('addUniversity/', AddUniversity.as_view(), name='addUniversity'),
    path('editUniversity/<int:pk>/', EditUniversity.as_view(), name='editUniversity'),
]