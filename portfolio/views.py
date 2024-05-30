from django.shortcuts import render
from .models import Profile

def home(request):
    profile = Profile.objects.all()
    return render(request, 'home.html', {'projects': profile})
