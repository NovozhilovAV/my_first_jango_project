from django.shortcuts import render
from django.http import HttpResponse
# from .forms import AddPostForm
# Create your views here.

menu = [{'title': 'О Сайте', 'url_name': 'about'},
        {'title': 'Машины парка', 'url_name': 'cars'},
        {'title': 'Водители парка', 'url_name': 'drivers'},
        {'title': 'Клиенты', 'url_name': 'clients'},
        ]

def index(request):
    return HttpResponse('<h1>Main page - Главная страница функции index</h1>')

def index_myapp(request):
    # return HttpResponse('<h1>MyApp Page</h1>')
    title = 'Моя главная страница'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/index.html', context=context)
    # render - отрисовывает страницу. с параметрами
    # myapp/index.html - указывает путь к файлу

def about(request):     # функциональный метод
    title = 'О Сайте'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/about.html', context=context)
    # return HttpResponse('About site, plies')
    # request потому как мы отправляем запрос на сайт

def cars(request):
    title = 'Машины'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/cars.html', context=context)


def drivers(request):
    title = 'Водители'
    context = {'title': title, 'menu': menu}
    return render(request, 'myapp/drivers.html', context=context)


def login(request):
    return HttpResponse('<h2>Page login !!!</h2>')

def contacts(request, id):
    url_id = id
    name = request.GET.get('name')
    age = request.GET.get('age')
            # request.POST.get('password')    # для примера запроса
    get_params = {'name': name, 'age': age}
    # return HttpResponse(f'<h1>Page Contacts</h1>, id = {id}')
    # return HttpResponse(f'<h1>Page Contacts</h1>, id = {id}, name = {name}, age = {age}')
    return HttpResponse(f'<h1>Page Contacts</h1>, url_params_id = {url_id}, get_params - {get_params}')

