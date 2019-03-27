from django.contrib.auth.models import User, Group
from owlstatsapi.api.models import Role, Team, Player, PlayerWeek
from rest_framework import viewsets
from owlstatsapi.api.serializers import UserSerializer, GroupSerializer, \
    RoleSerializer, TeamSerializer, PlayerSerializer, PlayerWeekSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RoleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows roles to be viewed or edited.
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerWeekViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows weeks to be viewed or edited.
    """
    queryset = PlayerWeek.objects.all()
    serializer_class = PlayerWeekSerializer
