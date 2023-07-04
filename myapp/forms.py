from django import forms
import datetime
from django.forms import ModelForm
from .models import *
from my_project_dj.settings import DATE_INPUT_FORMATS

def year_choices():
    return [(r, r) for r in range(1970, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

class CarForm(forms.Form):
    # работаем средствами класса forms.Form - описываем модель машины полями. создаем объект во views
    brand = forms.CharField(max_length=50, label='Марка')
    model = forms.CharField(max_length=50, label='Модель')
    color = forms.CharField(max_length=30, label='Цвет', required=False)
    power = forms.IntegerField(label='Мощность (л/с)', required=False, min_value=1, max_value=600)
    # required=False - поле не обязательно для заполнения в бд
    year = forms.ChoiceField(label='Год выпуска', choices=year_choices, initial=current_year)

class CarForm(ModelForm):
    class Meta:
        model = Car
        # fields = ['brand', 'model', 'color', 'power', 'year']
        fields = '__all__'

class ClientForm(ModelForm):
    class Meta:
        model = Client    # подключили модель
        # fields = ['name', 'last_name', 'birthday', 'city']     # поля для вывода
        # fields = '__all__'   # выведем все поля
        exclude = ['age']  # поля которые не хоти выводить
    birthday = forms.DateField(input_formats=DATE_INPUT_FORMATS, label='Дата рождения')
    # переопределили поле,в настройках(settings.py) указали как хотим заполнять дату, импортировали модуль из настроек
    # from my_project_dj.settings import DATE_INPUT_FORMATS