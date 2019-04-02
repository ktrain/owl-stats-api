from django.contrib.auth.models import User, Group
from owlstatsapi.api.models import Team, Player, PlayerWeek
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'location', 'name', 'full_name')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'role', 'team')


class PlayerWeekSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlayerWeek
        fields = ('id', 'number', 'player', 'eliminations', 'deaths', 'healing', 'ultimates', 'final_blows')
