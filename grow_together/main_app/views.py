import django
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def match(request):
    return render(request, 'match.html')
