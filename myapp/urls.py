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
    path('clients/', clients, name='clients'),

]
