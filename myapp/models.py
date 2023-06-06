from django.db import models

# Create your models here.
# Create migrations: python manage.py makemigration
# Migrate: python manage.py migrate
class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возраст')
    city = models.CharField(max_length=100, verbose_name='Город')
    is_activated = models.BooleanField(verbose_name='Активация')

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

class Car(models.Model):
    brand = models.CharField(max_length=30, verbose_name='Марка')
    model = models.CharField(max_length=30, verbose_name='Модель')
    color = models.CharField(max_length=30, verbose_name='Цвет')
    power = models.IntegerField(verbose_name='Мощность')
    year = models.IntegerField(verbose_name='Год')

    def __str__(self):
        return self.brand
        # return ' '.join([str(self.brand), str(self.model)])    # доделать, тут остановились
    class Meta:
        verbose_name = 'Машины'
        verbose_name_plural = 'Автомобили'
