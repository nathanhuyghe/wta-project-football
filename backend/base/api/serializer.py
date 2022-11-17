from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from base.models import League, Team, Standings, Fixtures, Lineups


class LeagueSerializer(ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class StandingsSerializer(ModelSerializer):
    class Meta:
        model = Standings
        fields = '__all__'


class FixturesSerializer(ModelSerializer):
    class Meta:
        model = Fixtures
        fields = '__all__'


class LineupsSerializer(ModelSerializer):
    class Meta:
        model = Lineups
        fields = '__all__'
