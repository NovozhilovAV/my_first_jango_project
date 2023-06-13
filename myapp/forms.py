from django import forms
import datetime

def year_choices():
    return [(r, r) for r in range(1970, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

class CarForm(forms.Form):
    brand = forms.CharField(max_length=50, label='Марка')
    model = forms.CharField(max_length=50, label='Модель')
    color = forms.CharField(max_length=30, label='Цвет', required=False)
    power = forms.IntegerField(label='Мощность (л/с)', required=False, min_value=1, max_value=600)
    year = forms.ChoiceField(label='Год выпуска', choices=year_choices, initial=current_year)
    