from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def about(requests):     # функциональный метод
    return HttpResponse('about site, plies')
# request потому как мы отправляем запрос на сайт

def login(requests):
    return HttpResponse('<h2>Page login !!!</h2>')

def contacts(requests):
    return HttpResponse('<h1>Page Contacts</h1>')