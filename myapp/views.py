from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requesrs):
    return HttpResponse('<h1>Main page</h1>')

def index_myapp(requests):
    return HttpResponse('<h1>Myapp Page</h1>')
def about(requests):     # функциональный метод
    return HttpResponse('about site, plies')
# request потому как мы отправляем запрос на сайт

def login(requests):
    return HttpResponse('<h2>Page login !!!</h2>')

def contacts(requests, id):
    url_id = id
    name = requests.GET.get('name')
    age = requests.GET.get('age')
            # requests.POST.get('password')    # для примера запроса
    get_params = {'name': name, 'age': age}
    # return HttpResponse(f'<h1>Page Contacts</h1>, id = {id}')
    # return HttpResponse(f'<h1>Page Contacts</h1>, id = {id}, name = {name}, age = {age}')
    return HttpResponse(f'<h1>Page Contacts</h1>, url_params_id = {url_id}, get_params - {get_params}')

