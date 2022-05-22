import re
from urllib import response
import django
import requests
from .models import Plant
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
import uuid
#import boto3
import urllib.parse
from pprint import pprint
import json

# testing amazon s3
S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'bucketnamecat'

# Create your views here.

def home(request):
    return render(request, 'home.html')

def match(request):
    return render(request, 'match.html')

def signup (request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('registration/test.html')
        else:
            error_message = 'Unable to complete sign up - Please Try Again'
    form = UserCreationForm
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def test(request, user_id):
    if request.method == 'POST':
        api_key = '2b10P60RFzvdu9lsD1dWCHuk6u'
        organ_1 = 'organs=flower'
        form =(request.POST['image'])
        encoded = urllib.parse.quote_plus(form)
        url = 'https://my-api.plantnet.org/v2/identify/all?api-key=' + api_key + '&images=' + encoded + '&' + organ_1
        result = requests.get(url)
        data = (result.json)
        return render(request, 'api.html', {'result': data})
    else:
        return render(request,'api.html')
    












