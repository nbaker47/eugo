from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404


def index(request):
    return render(request, 'index.html')

def battle(request):
    return render(request, 'battle.html')

def map(request):
    return render(request, 'map.html')

def login(request):
    return render(request, 'login.html')

def player(request):
    return render(request, 'player.html')

def lecturers(request):
    return render(request, 'lecturers.html')

def lecturerdex(request):
    return render(request, 'lecturerdex.html')

def mapmod(request):
    return render(request, 'mapmod.html')