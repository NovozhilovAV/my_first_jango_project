from django.urls import path
from .views import about, login, contacts, index_myapp


urlpatterns = [
    path('', index_myapp),
    path('about/', about),
    path('login/', login),
    # path('contacts/<int:id>/', contacts),    # идентификатор параметра
    path('contacts/<str:id>/', contacts),
]
