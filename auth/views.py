import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import requests

@csrf_exempt
def login(request):
    render(request, 'login.html')


@csrf_exempt
def signup(request):
    print(10)
    if request.method == 'POST':
        print(20)
        data = json.loads(request.body)
        form_data = {
            'username': data.get('username'),
            'role': data.get('role'),
            'password': data.get('password')
        }
        print(form_data)
        headers = {'Content-Type': 'application/json'}
        response = requests.post('http://localhost:3000/saveuser/', data=json.dumps(form_data), headers=headers)
        # if response.status_code == 200:
        #     return JsonResponse({'message': 'User Registered successfully'})
        # else:
        #     return JsonResponse({'message': f'An error occurred: {response.text}'}, status=response.status_code)
    else:
        return render(request, 'signup.html')