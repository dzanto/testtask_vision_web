from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# router = DefaultRouter()
# router.register('reg', views.CreateUserView)

urlpatterns = [
    path('auth/email/', views.email_confirmation),
    path('auth/token/', views.get_token),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', views.CreateUserView.as_view()),
    path('users/', views.ListUserView.as_view()),
    path('active_users/', views.ListActiveUserView.as_view()),
]