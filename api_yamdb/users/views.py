from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from api_yamdb.permissions import IsAdminStaffUser
from api_yamdb.settings import EMAIL_HOST_USER

from .serializers import (MeSerializer, UserCodeConfirm, UserRegistration,
                          UserSerializer)

User = get_user_model()


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminStaffUser, )
    pagination_class = LimitOffsetPagination
    search_fields = ('username',)
    lookup_field = 'username'

    @action(
        methods=['get', 'patch'],
        detail=False,
        url_path='me',
        url_name='me',
        permission_classes=(
            permissions.IsAuthenticated,
        )
    )
    def get_self_profile(self, request):
        user = get_object_or_404(User, username=request.user)
        if request.method == 'GET':
            serializer = MeSerializer(user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PATCH':
            serializer = MeSerializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save(role=user.role)
            return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def user_registration(request):
    serializer = UserRegistration(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    email = serializer.validated_data.get('email')
    new_user = User.objects.create(
        username=username,
        email=email,
        is_active=False
    )
    confirmation_code = default_token_generator.make_token(user=new_user)

    send_mail(
        subject='Confirmation code',
        message=f'Here is your confirmation code {confirmation_code}',
        from_email=EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=True
    )

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def user_confirmation_code(request):
    serializer = UserCodeConfirm(data=request.data)
    if 'username' in request.data:
        user = get_object_or_404(User, username=request.data['username'])
    if not serializer.is_valid():
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    confirmation_code = serializer.validated_data.get('code_confirm')

    if not default_token_generator.check_token(user, confirmation_code):
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    user.is_active = True
    user.save()
    token = AccessToken.for_user(user=user)

    return Response(
        {'token': str(token)},
        status=status.HTTP_200_OK
    )
