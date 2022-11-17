from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from base.models import League, Lineups, Team, Standings, Fixtures
from .serializer import LeagueSerializer, LineupsSerializer, StandingsSerializer, TeamSerializer, FixturesSerializer
from django.core.cache import cache
import redis
import json

r = redis.StrictRedis(host='wta-project-football.redis.cache.windows.net', port=6380,
                      password='Icn6WhS5WIGXXssIb5NJ32Dzq09Z0cpmjAzCaORFVgU=', ssl=True)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/leagues/',
        'GET /api/league/:leagueid',
        'GET /api/teams/',
        'GET /api/team/:teamid/',
        'GET /api/leagues/team/:leagueid/',
        'GET /api/standings/:leagueid/',
        'GET /api/fixtures/',
        'GET /api/fixtures/:teamid/',
        'GET /api/lineups/:teamid/'

    ]
    return Response(routes)


@api_view(['GET'])
def GetLeagues(request):
    if r.get('leagues'):
        leagues = r.get('leagues')
        return Response(json.loads(leagues))
    else:
        leagues = League.objects.all()
        serializer = LeagueSerializer(leagues, many=True)
        r.set('leagues', json.dumps(serializer.data))
        return Response(serializer.data)


@api_view(['GET'])
def GetLeague(request, pk):
    if r.get('league' + pk):
        league = r.get('league' + pk)
        return Response(json.loads(league))
    else:
        league = League.objects.get(id=pk)
        serializer = LeagueSerializer(league, many=False)
        print(serializer.data)
        r.set('league' + pk, json.dumps(serializer.data))
        return Response(serializer.data)


@ api_view(['GET'])
def GetTeams(request):
    if r.get('teams'):
        teams = r.get('teams')
        return Response(json.loads(teams))
    else:
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        r.set('teams', json.dumps(serializer.data))
        return Response(serializer.data)


@ api_view(['GET'])
def GetTeam(request, pk):
    if r.get('team' + pk):
        team = r.get('team' + pk)
        return Response(json.loads(team))
    else:
        team = Team.objects.get(id=pk)
        serializer = TeamSerializer(team, many=False)
        r.set('team' + pk, json.dumps(serializer.data))
        return Response(serializer.data)


@ api_view(['GET'])
def GetLeagueTeam(request, pk):
    if r.get('leagueteam' + pk):
        team = r.get('leagueteam' + pk)
        return Response(json.loads(team))
    else:
        team = Team.objects.filter(league=pk)
        serializer = TeamSerializer(team, many=True)
        r.set('leagueteam' + pk, json.dumps(serializer.data))
        return Response(serializer.data)


@ api_view(['GET'])
def GetStandingLeague(request, pk):
    if r.get('standingleague' + pk):
        standing = r.get('standingleague' + pk)
        return Response(json.loads(standing))
    else:
        standing = Standings.objects.filter(league=pk)
        serializer = StandingsSerializer(standing, many=True)
        r.set('standingleague' + pk, json.dumps(serializer.data))
        return Response(serializer.data)


@ api_view(['GET'])
def GetFixtures(request):
    if r.get('fixtures'):
        fixtures = r.get('fixtures')
        return Response(json.loads(fixtures))
    else:
        fixtures = Fixtures.objects.all()
        serializer = FixturesSerializer(fixtures, many=True)
        r.set('fixtures', json.dumps(serializer.data))
        return Response(serializer.data)


@ api_view(['GET'])
def GetFixturesTeam(request, pk):
    if r.get('fixture' + pk):
        fixtures = r.get('fixture' + pk)
        return Response(json.loads(fixtures))
    else:
        fixtures = Fixtures.objects.filter(Q(home_team=pk) | Q(away_team=pk))
        serializer = FixturesSerializer(fixtures, many=True)
        r.set('fixture' + pk, json.dumps(serializer.data))
        return Response(serializer.data)


@ api_view(['GET'])
def GetLineupsTeam(request, pk):
    if r.get('lineupsteam' + pk):
        team = r.get('lineupsteam' + pk)
        return Response(json.loads(team))
    else:
        team = Team.objects.get(id=pk)
        line = Lineups.objects.filter(team=team)
        serializer = LineupsSerializer(line, many=True)
        r.set('lineupsteam' + pk, json.dumps(serializer.data))
        return Response(serializer.data)
