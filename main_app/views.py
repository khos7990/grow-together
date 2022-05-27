from urllib import response
# import django
import requests
from .models import Plant, UserPlant
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import uuid
import boto3
import urllib.parse
from pprint import pprint

# Amazon S3 base Link
S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'grow-together'

# Create your views here.

def home(request):
    return render(request, 'home.html')

# def match(request):
#     return render(request, 'match.html')


def signup (request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
        else:
            error_message = 'Unable to complete sign up - Please Try Again'
    form = UserCreationForm
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def upload(request, user_id):
    if request.method == 'POST':
        photo_file = request.FILES.get('photo-file', None)
        api_key = '2b10P60RFzvdu9lsD1dWCHuk6u'
        organ_1 = 'organs=flower'
        if photo_file:
            s3 = boto3.client('s3')
            key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        
            try:
                s3.upload_fileobj(photo_file, BUCKET, key)   
                url = f"{S3_BASE_URL}{BUCKET}/{key}"
                encoded = urllib.parse.quote_plus(url)
                api_match = 'https://my-api.plantnet.org/v2/identify/all?api-key=' + api_key + '&images=' + encoded + '&' + organ_1
                result = requests.get(api_match)
                data = (result.json())
                match = data['bestMatch']
                first_word = match.split()[:1]
                p = Plant.objects.all().filter(scientific_name__contains=first_word[0])
                matches = Plant.objects.all().filter(light=p[0].light).exclude(scientific_name__contains=p[0])
                matched_plant = matches[:3]
                return render(request, 'upload.html', {user_id: user_id, 'result': data, 'plant': p.first(), 'matched_plant': matched_plant, 'photo': url})
            except Exception as e:
                print(e)
                print('An error occurred uploading file to S3')
    return render(request, 'upload.html')

@login_required
def myplants(request, user_id):
    if user_id == request.user.id:
        matchedplant = []
        user = User.objects.get(id = user_id)
        if user.userplant_set.all():
            for match in user.userplant_set.all():
                matchedplant.append(Plant.objects.get(scientific_name=match.matched_plant))
            return render(request, 'myplants.html', {'user':user, 'matched': matchedplant})   
    return HttpResponse('<h1> No Bueno </h1>')      
          
def matchedplant(request, user_id):
    if request.method == 'POST':
        form = (request.POST)
        user = User.objects.get(id = user_id)
        plant = Plant.objects.get(id=form['matched_plant'])
        userplant = Plant.objects.get(id=form['user_plant'])
        usermatch = UserPlant(url=form['url'], user=user, matched_plant= plant, user_plant=userplant)
        usermatch.save()
        return redirect('myplants', user_id = user_id) 

def deletematch(request, user_id):
    user = User.objects.get(id = user_id)
    if request.method == 'POST':
        for match in user.userplant_set.all():
            matchid = (match.id)
            print(matchid)
            deletematch= UserPlant.objects.get(id=matchid).delete()
            print(deletematch)
            return redirect('myplants', user_id = user_id) 

    






    









