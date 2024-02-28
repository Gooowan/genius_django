from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import requests

@csrf_exempt
def login(request):
    render(request, 'login.html')


@csrf_exempt
def signup(request):
    print('1')
    if request.method == 'POST':
        print('2')
        form_data = {
            'username': request.POST.get('username'),
            'role': request.POST.get('role'),
            'password': request.POST.get('password')
        }
        print('3')
        response = requests.post('http://localhost:3000/signup/', data=form_data)
        if response.status_code == 200:
            print('4')
            return HttpResponse('User Registered successfully')
        else:
            return HttpResponse(f'An error occurred: {response.text}', status=response.status_code)
    else:
        return render(request, 'signup.html')
