from django.urls import path
from .views import *


urlpatterns = [
    path('', index_myapp, name='index'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('cars/', cars, name='cars'),
    path('drivers/', drivers, name='drivers'),
    # path('contacts/<int:id>/', contacts),    # идентификатор параметра
    path('contacts/<str:id>/', contacts, name='contacts'),

]
