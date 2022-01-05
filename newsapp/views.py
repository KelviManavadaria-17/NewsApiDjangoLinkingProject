from django.shortcuts import render

from newsapp import urls
import requests
# Create your views here.
API_KEY = 'a85399a7f7c742d286ffb8ee88e47d48'

def home(request):
    url = f'https://newsapi.org/v2/everything?q=keyword&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    attribute = data['articles']
    totalResults=data['totalResults']
    context = {
        'attribute' : attribute,
        'totalResults':totalResults
    }
    return render(request,'newsapp/home.html',context)