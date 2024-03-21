from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    User들을 보거나 편집할 수 있는 API endpoint
    """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    Group들을 보거나 편집할 수 있는 API endpoint
    """
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

