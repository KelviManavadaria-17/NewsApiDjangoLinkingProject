from django.shortcuts import render

from newsapp import urls
import requests
# Create your views here.
API_KEY = 'a85399a7f7c742d286ffb8ee88e47d48'
categories = ['business','entertainment' ,'general','health' ,'science' ,'sports' ,'technology']

def home(request ):
    
    url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2022-01-08&'
       'sortBy=popularity&'
       'apiKey=a85399a7f7c742d286ffb8ee88e47d48')

    

    response = requests.get(url)
    data = response.json()
    attribute = data['articles']
    totalResults=data['totalResults']
    context = {
        'attribute' : attribute,
        'totalResults':totalResults,
        'categories':categories
    }
    return render(request,'newsapp/home.html',context)

def category(request, k):
    url = f'https://newsapi.org/v2/top-headlines/sources?category={k}apiKey={API_KEY}'
    print(url)
    response = requests.get(url)
    data = response.json()
    attribute = data['sources']
    totalResults=data['totalResults']
    context = {
         
        'attribute' : attribute,
        'totalResults':totalResults
    }
    return render(request,'newsapp/home.html',context)


def language(request, k):
    url = f'https://newsapi.org/v2/top-headlines/sources?category={k}apiKey={API_KEY}'
    print(url)
    response = requests.get(url)
    data = response.json()
    attribute = data['articles']
    totalResults=data['totalResults']
    context = {
        'attribute' : attribute,
        'totalResults':totalResults
    }
    return render(request,'newsapp/home.html',context)


