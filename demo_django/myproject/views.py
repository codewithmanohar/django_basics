from django.http import HttpResponse
from django.shortcuts import render
from users.models import User

def home(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'home.html', context)