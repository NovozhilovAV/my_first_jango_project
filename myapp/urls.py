from django.urls import path
from .views import *

app_name = 'myapp'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contacts/<str:id>/', contacts, name='contacts'),
    # path('contacts/<int:id>/', contacts),    # идентификатор параметра

    path('login/', login, name='login'),

    path('cars/', cars, name='cars'),
    path('drivers/', drivers, name='drivers'),
    path('clients/', clients, name='clients'),

    path('add_car/', add_car, name='add_car'),
    path('add_client/', add_client, name='client_add'),
    path('add_driver/', add_driver, name='driver_add'),
    path('clients/<int:pk>', client_card, name='client_card'),

    # указываем путь, и вызывве его как представление as_view()
    path('employees/', EmployeeList.as_view(), name='employee_list'),
    path('employees/<int:pk>/', EmployeeDetail.as_view(), name='employee_detail'),
    path('employees_form/', EmployeeCreate.as_view(), name='employee_form'),
    path('employees/<int:pk>/', EmployeeUpdate.as_view(), name='employee_update'),

    path('orders/', OrderList.as_view(), name='order_list'),
    path('order_form/', OrderCreate.as_view(), name='order-form'),

    path('cars/search', car_search, name='car-search'),

]
