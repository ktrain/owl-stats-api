from django.contrib.auth.models import User, Group
from owlstatsapi.api.models import Team, Player, PlayerWeek
from rest_framework import mixins, viewsets
from rest_framework.permissions import BasePermission, SAFE_METHODS, \
    IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from owlstatsapi.api.serializers import UserSerializer, GroupSerializer, \
    TeamSerializer, PlayerSerializer, PlayerWeekSerializer


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser|IsAuthenticated&ReadOnly, )


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAdminUser|IsAuthenticated&ReadOnly, )


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class PlayerWeekViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weeks to be viewed or edited.
    """
    queryset = PlayerWeek.objects.all().order_by('-number')
    serializer_class = PlayerWeekSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
