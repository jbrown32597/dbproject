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
    path('viewUser/<int:pk>/', views.ViewUser.as_view(), name='viewUser'),
    path('editUser/<int:pk>/', views.EditUser.as_view(), name='editUser'),
    path('universities/', views.UniversityList.as_view(), name='universities'),
    path('addUniversity/', views.AddUniversity.as_view(), name='addUniversity'),
    path('viewUniversity/<int:pk>/', views.ViewUniversity.as_view(), name='viewUniversity'),
    path('editUniversity/<int:pk>/', views.EditUniversity.as_view(), name='editUniversity'),
    path('addEvent/', views.AddEvent.as_view(), name='addEvent'),
    path('viewEvent/<int:pk>/', views.ViewEvent.as_view(), name='viewEvent'),
    path('editEvent/<int:pk>/', views.EditEvent.as_view(), name='editEvent'),
    path('addComment/', views.AddComment.as_view(), name='addComment'),
    path('editComment/<int:pk>/', views.EditComment.as_view(), name='editComment'),
    path('deleteComment/<int:pk>/', views.DeleteComment.as_view(), name='deleteComment'),
    path('RSOs/', views.RSOList.as_view(), name='RSOs'),
    path('addRSO/', views.AddRSO.as_view(), name='addRSO'),
    path('viewRSO/<int:pk>/', views.ViewRSO.as_view(), name='viewRSO'),
    path('editRSO/<int:pk>/', views.EditRSO.as_view(), name='editRSO'),
]