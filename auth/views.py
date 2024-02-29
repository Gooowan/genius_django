import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')