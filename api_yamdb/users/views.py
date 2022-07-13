from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status, views #filters,  serializers, 
from .serializers import (UserSerializer,)
from .permissions import IsAdminStaffUser
from rest_framework.decorators import action


User = get_user_model()


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdminStaffUser, )
    search_fields = ('username',)
    lookup_field = 'username'

    @action(
        methods=['get'],
        detail=False,
        url_path='me',
        url_name='me',
        permission_classes = [
            permissions.IsAuthenticated
        ]
    )
    def user_get_self_profile(self, request):
        # вытаскиваем юзера
        user = request.user
        # передаем сериализатору юзера
        serializer = self.get_serializer(instance=user)
        if self.request.method == 'GET':
            return Response(data=serializer.data, status=status.HTTP_200_OK)

    @action(
        methods=['patch'],
        detail=False,
        url_path='me',
        url_name='me',
        permission_classes = [
            permissions.IsAuthenticated
        ]
    )
    def user_patch_self_profile(self, request):
        user = request.user
        if self.request.method == 'PATCH':
            serializer = self.get_serializer(instance=user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save(role=user.role, partial=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)





class RegistrationView(views.APIView):
    pass


class CodeConfirmView(viewsets.ModelViewSet):
    pass