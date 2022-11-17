import json
import time
from django.shortcuts import render
from django.http import HttpResponse
import requests


def home(request):
    return render(request, 'home.html')


def team(request):
    return HttpResponse('gelukt')


def createLeague(request):
    return HttpResponse('gelukt')
