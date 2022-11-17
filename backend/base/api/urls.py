from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('leagues/', views.GetLeagues),
    path('league/<str:pk>/', views.GetLeague),
    path('teams/', views.GetTeams),
    path('team/<str:pk>/', views.GetTeam),
    path('leagues/team/<str:pk>/', views.GetLeagueTeam),
    path('standings/<str:pk>/', views.GetStandingLeague),
    path('fixtures/', views.GetFixtures),
    path('fixtures/<str:pk>/', views.GetFixturesTeam),
    path('lineups/<str:pk>/', views.GetLineupsTeam)

]
