from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from users.models import User

def user_detail(req, pk):
    user = get_object_or_404(User, pk=pk)
    return HttpResponse(user)