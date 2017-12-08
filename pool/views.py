from django.shortcuts import render, redirect


# Create your views here.


def index(request):
    return render(request, 'pool/base.html')


def games(request):
    return render(request, 'pool/games.html')
