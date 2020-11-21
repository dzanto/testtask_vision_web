from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('registration/', views.CreateUserView.as_view()),
    path('activating_user/', views.get_token),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', views.ListUserView.as_view()),
    path('active_users/', views.ListActiveUserView.as_view()),
]