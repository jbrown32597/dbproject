from django.urls import include, path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'events'
urlpatterns = [
    path('', views.WelcomeView.as_view(), name='welcome'),
    path('login/', LoginView.as_view(template_name='events/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('viewUser/<int:pk>', views.ViewUser.as_view(), name='viewUser'),
    path('universities/', views.UniversityList.as_view(), name='universities'),
    path('addUniversity/', views.AddUniversity.as_view(), name='addUniversity'),
    path('viewUniversity/<int:pk>/', views.ViewUniversity.as_view(), name='viewUniversity'),
    path('editUniversity/<int:pk>/', views.EditUniversity.as_view(), name='editUniversity'),
]