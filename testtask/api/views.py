from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.generics import get_object_or_404
from django.shortcuts import get_list_or_404
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        username = request.data.get('username')
        email = request.data.get('email')
        user = get_object_or_404(User, username=username)
        code = default_token_generator.make_token(user)

        send_mail(
            subject='Ваш код аутентификации',
            message='Сохраните код! Он понадобится вам для получения токена.\n'
                    f'confirmation_code:\n{code}\n'
                    f'username: {username}',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class ListUserView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ListActiveUserView(ListAPIView):
    queryset = get_list_or_404(User, is_active=True)
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


@api_view(['POST'])
@permission_classes([AllowAny])
def get_token(request):
    email = request.data.get('email')
    user = get_object_or_404(User, email=email)
    code = request.data.get('confirmation_code')
    if default_token_generator.check_token(user, code):
        user.is_active = True
        user.save()
        return Response({"message": "Аккаунт активирован"}, status.HTTP_200_OK)

    return Response({"message": "неверный код подтверждения."},
                    status.HTTP_400_BAD_REQUEST)
