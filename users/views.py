from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from users.models import User

def user_detail(req, pk):
    user = get_object_or_404(User, pk=pk)
    context = {
        'user': user
    }
    return render(req, 'user_detail.html', context)