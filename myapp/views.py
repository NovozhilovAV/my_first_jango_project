from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .forms import CarForm

# from .forms import AddPostForm
# Create your views here.

menu = [{'title': 'О Сайте', 'url_name': 'about'},
        {'title': 'Машины парка', 'url_name': 'cars'},
        {'title': 'Водители парка', 'url_name': 'drivers'},
        {'title': 'Клиенты', 'url_name': 'clients'},
        ]

#def index(request):
#    return HttpResponse('<h1>Main page - Главная страница функции index</h1>')

def index(request):
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

@csrf_protect
def login(request):
    title = 'Войти'
    context ={'title': title, 'menu': menu}
    # return HttpResponse('<h2>Page login !!!</h2>')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse(f'Login - {username}, Password = {password}')

    if request.method == 'GET':
        return render(request, 'myapp/login.html', context=context)


def contacts(request, id):
    url_id = id
    name = request.GET.get('name')
    age = request.GET.get('age')
            # request.POST.get('password')    # для примера запроса
    get_params = {'name': name, 'age': age}
    # return HttpResponse(f'<h1>Page Contacts</h1>, id = {id}')
    # return HttpResponse(f'<h1>Page Contacts</h1>, id = {id}, name = {name}, age = {age}')
    return HttpResponse(f'<h1>Page Contacts</h1>, url_params_id = {url_id}, get_params - {get_params}')

def add_car(request):
    if request.method == 'GET':
        title = 'Добавить машину'
        form = CarForm
        context = {'title': title, 'menu': menu, 'form': form}
        return render(request, 'myapp/car_add.html', context=context)

    if request.method == 'POST':
        carform = CarForm(request.POST)
        if carform.is_valid():
            car = Car()
            car.brand = carform.cleaned_data['brand']
            car.model = carform.cleaned_data['model']
            car.color = carform.cleaned_data['color']
            car.power = carform.cleaned_data['power']
            car.year = carform.cleaned_data['year']
            car.save()
        return cars(request)
        # return render(request, 'myapp/cars.html', context=context) - так даже правильнее