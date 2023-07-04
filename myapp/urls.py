from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('cars/', cars, name='cars'),
    path('add_cars/', add_car, name='add_car'),
    path('drivers/', drivers, name='drivers'),
    # path('contacts/<int:id>/', contacts),    # идентификатор параметра
    path('contacts/<str:id>/', contacts, name='contacts'),
    path('add_client/', add_client, name='add_client'),
    path('clients/<int:pk>', client_card, name='client_card'),
    path('clients/', clients, name='clients'),
    path('employees/', EmployeeList.as_wiew(), name='employee_list'),
    path('employees/<int:pk/>', EmployeeDetail.as_view(), name='employee_detail'),
    path('employees_form/', EmployeeCreate.as_view(), name='employee_create'),
    path('employees/<int:pk>/', EmployeeUpdate.as_view(), name='employee_update'),

]
