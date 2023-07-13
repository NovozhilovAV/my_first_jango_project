from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .forms import CarForm, ClientForm, DriverForm
from .models import *
import datetime
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from .filters import CarFilter
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator
# from .forms import AddPostForm
# Create your views here.

menu = [{'title': 'О Сайте', 'url_name': 'about'},
        {'title': 'Машины парка', 'url_name': 'cars'},
        {'title': 'Водители парка', 'url_name': 'drivers'},
        {'title': 'Клиенты', 'url_name': 'clients'},
        {'title': 'Сотрудники', 'url_name': 'employee_list'},
        {'title': 'Заказы', 'url_name': 'order_list'},
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


def contacts(request, id):
    url_id = id
    name = request.GET.get('name')
    age = request.GET.get('age')
            # request.POST.get('password')    # для примера запроса
    get_params = {'name': name, 'age': age}
    # return HttpResponse(f'<h1>Page Contacts</h1>, id = {id}')
    # return HttpResponse(f'<h1>Page Contacts</h1>, id = {id}, name = {name}, age = {age}')
    return HttpResponse(f'<h1>Page Contacts</h1>, url_params_id = {url_id}, get_params - {get_params}')


def cars(request, cars=None):
    title = 'Машины'
    # cars = Car.objects.all()
    f = CarFilter(request.GET, queryset=Car.objects.all())
    if not request.GET.get('query'):
        cars = Car.objects.all()

    # context = {'title': title, 'menu': menu, 'cars': cars}
    context = {'title': title, 'menu': menu, 'cars': cars, 'filter': f}
    return render(request, 'myapp/cars.html', context=context)


def drivers(request):
    title = 'Водители'
    drivers = Driver.objects.all()
    context = {'title': title, 'menu': menu, 'objects': drivers}
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


# @staff_member_required
def add_car(request):
    if request.method == 'GET':
        title = 'Добавить машину'
        form = CarForm    # обьект формы. пустая - из файла forms
        context = {'title': title, 'menu': menu, 'form': form}
        return render(request, 'myapp/car_add.html', context=context)

    if request.method == 'POST':
        carform = CarForm(request.POST, request.FILES)
        if carform.is_valid():
            # car = Car()
            # car.brand = carform.cleaned_data['brand']
            # car.model = carform.cleaned_data['model']
            # car.color = carform.cleaned_data['color']
            # car.power = carform.cleaned_data['power']
            # car.year = carform.cleaned_data['year']
            carform.save()  # сохроняем форму
            # return render(request, 'myapp/car_add.html', {'titel': titel})  # и выводим форму
        return cars(request)


def clients(request):
    title = 'Клиенты'
    clients = Client.objects.all()   # 19:25
    context = {'title': title, 'menu': menu, 'clients': clients}
    return render(request, 'myapp/clients.html', context=context)

def add_driver(request):
    if request.method == 'GET':
        title = 'Добавить Водителя'
        form = DriverForm()
        context = {'title': title, 'menu': menu, 'form': form}
        return render(request, 'myapp/driver_add.html', context=context)

    if request.method == 'POST':
        driverform = DriverForm(request.POST)
        if driverform.is_valid():
            driverform.save()
            return drivers(request)


def add_client(request):
    # return render(request, 'myapp/client_add.html')
    title = 'Добавить клиента'  # заголовок страницы
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)    # 19:48
            age = datetime.date.today().year - form.cleaned_data['birthday'].year
            instance.age = age
            instance.save()
            # form.save()    # сохроняем форму
            # return render(request, 'myapp/client_add.html', {'title': title})    # и выводим форму
            return clients(request)
    else:
        form = ClientForm()    # создаем объект формы- пустой- метод гет

    context = {'title': title, 'menu': menu, 'form': form}

    return render(request, 'myapp/client_add.html', context=context)
    # отрисовка страницы для гет запроса


def car_detail(request, pk):
    car = Car.objects.get(pk=pk)
    title = 'Car detail'
    context = {'object': car, 'title': title}

    return render(request, 'main/car_detail.html', context=context)


def client_card(request, pk):
    title = 'Client information'
    # client = Client.objects.get(pk=pk)
    client = get_object_or_404(Client, pk=pk)
    context = {'menu': menu, 'title': title, 'client': client}

    # @login_required
    # def clients(request):
    #     title = 'Клиенты'
    #     clients = Client.objects.all()
    #     paginator = Paginator(clients, 2)  # Show 25 contacts per page.
    # page_number = request.GET.get("page")
    #     page_obj = paginator.get_page(page_number)
    #     context = {'title': title, 'menu': menu, 'clients': clients, 'page_obj': page_obj}

    return render(request, 'myapp/client_card.html', context=context)



# классовый метод определенния
class EmployeeList(ListView):
    model = Employee
    template_name = 'myapp/employee_list.html'
    context_object_name = 'employees'
    # имя передается в шаблон для преребора сотрудников

    def get_context_data(self, **kwargs):
        # получение общего контекста из родительского класса
        context = super().get_context_data(**kwargs)
        # изменение родительского контекста - добавление ключей словаря
        context['title'] = 'Сотрудники'    # заголовок
        context['count'] = Employee.objects.count()
        context['menu'] = menu
        return context

class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'myapp/employee_detail.html'
    context_object_name = 'employee'

    def get_context_data(self, **kwargs):
        # получение общего контекста из родительского класса
        context = super().get_context_data(**kwargs)
        context['title'] = 'Информация о сотруднике'    # заголовок
        context['menu'] = menu
        return context


class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'    # Все поля добавляем
    template_name = 'myapp/employee_form.html'
    # представления для создания объекта


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'    # Все поля добавляем
    template_name = 'myapp/employee_update.html'


class EmployeeDelete(DetailView):
    model = Employee
    template_name = 'myapp/delete.html'
    success_url = reverse_lazy('main:employee_list')


def car_search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        ft = Q(model__icontains=query) | Q(year__icontains=query) | Q(brand__name__contains=query)
        results = Car.objects.filter(ft)

        return cars(request, cars=results)

class OrderCreate(CreateView):
    model = Order
    fields = '__all__'
    template_name = 'myapp/order_form.html'

class OrderList(ListView):
    model = Order
    template_name = 'myapp/order_list.html'
    context_object_name = 'objects'