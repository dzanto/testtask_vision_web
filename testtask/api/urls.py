from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # регистрация пользователей
    path('registration/', views.CreateUserView.as_view()),
    # активация пользователя
    path('activating_user/', views.get_token),
    # получение JWT токена
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # список всех пользователей
    path('users/', views.ListUserView.as_view()),
    # список активированных пользователей
    path('active_users/', views.ListActiveUserView.as_view()),
]