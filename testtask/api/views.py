from rest_framework import permissions, filters
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.generics import get_object_or_404
from django.contrib.auth import get_user_model
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from random import choice
from string import ascii_letters
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ListUserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ListActiveUserView(ListAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


@api_view(['POST'])
@permission_classes([AllowAny])
def email_confirmation(request):
    email = request.data.get('email')
    if not email:
        return Response(status.HTTP_400_BAD_REQUEST)

    user = User.objects.get_or_create(email=email)[0]
    if not user.username:
        user.username = 'User_' + ''.join(
            choice(ascii_letters) for i in range(6))
    username = user.username

    user.save()
    code = default_token_generator.make_token(user)

    send_mail(
        subject='Ваш код аутентификации в Yamdb',
        message='Сохраните код! Он понадобится вам для получения токена.\n'
                f'confirmation_code:\n{code}\n'
                f'username: {username}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )
    return Response({"message": "код был отправлен на указанную почту: "
                                f"{email}"}, status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def get_token(request):
    email = request.data.get('email')
    user = get_object_or_404(User, email=email)
    code = request.data.get('confirmation_code')
    if default_token_generator.check_token(user, code):
        refresh = RefreshToken.for_user(user)
        tokens = {'refresh': str(refresh),
                  'access': str(refresh.access_token)}
        return Response(tokens, status.HTTP_200_OK)

    return Response({"message": "неверный код подтверждения."},
                    status.HTTP_400_BAD_REQUEST)