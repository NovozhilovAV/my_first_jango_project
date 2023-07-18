from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
# Create migrations: python manage.py makemigration
# Migrate: python manage.py migrate

class Driver(models.Model):
    firstname = models.CharField(max_length=100, verbose_name='Имя')
    lastname = models.CharField(max_length=100, verbose_name='Фамилия', default='')
    birthday = models.DateField(verbose_name='Дата рождения', default=date.today)
    city = models.CharField(max_length=100, verbose_name='Город', null=True)
    passport = models.CharField(max_length=15, verbose_name='Паспорт', null=False, unique=True)
    email = models.EmailField(verbose_name='Эл. почта', unique=True)
    is_activated = models.BooleanField(verbose_name='Активация', default=True)

    def __str__(self):
        return ' '.join[str(self.firstname), str(self.lastname)]

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'
        ordering = ['lastname', '-birthday']    # -birthday обратная сортировка
        unique_together = (
            ('firstname', 'lastname', 'passport'),
        )

# class Car(models.Model):
#     brand = models.CharField(max_length=30, verbose_name='Марка')
#     model = models.CharField(max_length=30, verbose_name='Модель')
#     color = models.CharField(max_length=30, verbose_name='Цвет')
#     power = models.IntegerField(verbose_name='Мощность')
#     year = models.IntegerField(verbose_name='Год')
#
#     def __str__(self):
#         return self.brand
#         # return ' '.join([str(self.brand), str(self.model)])    # доделать, тут остановились
#     class Meta:
#         verbose_name = 'Машина'
#         verbose_name_plural = 'Автомобили'


class Client(models.Model):
    firstname = models.CharField(max_length=30, verbose_name='Имя')
    lastname = models.CharField(max_length=30, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    age = models.IntegerField(verbose_name='Возраст', null=True)
    city = models.CharField(max_length=30, verbose_name='Город')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Эл. почта')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' '.join[str(self.firstname), str(self.lastname)]

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Employee(models.Model):
    # Выбираем образование из списка сотрудника
    edu_choises = [('midle', 'среднее'),
                   ('high', 'высшее'),
                   ('professional', 'профессиональное'),
    ]

    firstname = models.CharField(max_length=50, verbose_name='Имя')
    lastname = models.CharField(max_length=50, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    position = models.CharField(max_length=50, verbose_name='Должность')
    education = models.CharField(max_length=30, choices=edu_choises)

    def __str__(self):
        return ' '.join([str(self.firstname), str(self.lastname)])
    #  переопределяем для вывода имя и фамилии

    def get_absolute_url(self):
        return reverse('employee_list')
    # ссылка для перехода к описанию сотрудника
    # получаем адрес по абсолютному имени пути

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class CarBrand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Car(models.Model):
    colors = (
        ('черный', 'черный'),
        ('белый', 'белый'),
        ('желтый', 'желтый'),
        ('красный', 'красный'),
        ('зеленый', 'зеленый'),
        ('синий', 'синий'),
    )

    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE, related_name='cars', verbose_name='Марка')
    model = models.CharField(max_length=30, verbose_name='Модель')
    color = models.CharField(max_length=20, choices=colors, null=False)
    power = models.IntegerField(verbose_name='Мощность')
    year = models.IntegerField(verbose_name='Год')
    image = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return ' '.join([str(self.brand), str(self.model)])

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        ordering = ['year', 'model']
        # отображение будет от самого старшего года по возростанию,
        # знак - перед полем -означает обратный порядок


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING, related_name='cars', verbose_name='Машина')
    driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING, related_name='car', verbose_name='Водитель')
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, related_name='car', verbose_name='Клиент')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ' '.join([str(self.id), str(self.client)])

    def get_absolute_url(self):
        return reverse('myapp:order_list')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'