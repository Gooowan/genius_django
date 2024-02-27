from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from pymongo import MongoClient
from django.http import JsonResponse

def login_view(request):
    if request.method == 'POST':
        # Get parameters from form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Connect to MongoDB
        client = MongoClient('mongodb://localhost:27017/')
        db = client['mydatabase']

        # Query MongoDB
        user = db.users.find_one({'username': username, 'password': password})

        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})