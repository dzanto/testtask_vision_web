from django.urls import path, include
from . import views


urlpatterns = [
    path('auth/email/', views.email_confirmation),
    path('auth/token/', views.get_token),
    path('registration/', views.CreateUserView.as_view()),
    path('users/', views.ListUserView.as_view()),
    path('active_users/', views.ListActiveUserView.as_view()),
]