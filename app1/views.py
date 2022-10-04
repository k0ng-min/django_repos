from django.shortcuts import render

# Create your views here.
from app1.models import User


def mainlist(request):
    users = User.objects.all()
    return render(request, 'app1_main.html', {'users': users})
