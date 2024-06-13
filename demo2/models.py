from django.db import models


class Customers(models.Model):
    fio = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    phone = models.CharField(max_length=500)
    adres = models.CharField(max_length=500)
    registration_date = models.DateTimeField(auto_now_add=True)


class Products(models.Model):
    STATUSORDER_CHOICES5 = [
        ('лекарство', 'лекарство'),
        ('медицинское изделие', 'медицинское изделие'),
    ]

    article = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    category = models.CharField(choices=STATUSORDER_CHOICES5, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    production_date = models.DateTimeField(auto_now_add=True)
    manufacturer = models.CharField(max_length=500)
    country = models.CharField(max_length=500)


class Order(models.Model):
    STATUSORDER_CHOICES = [
        ('Наличный', 'Наличный'),
        ('Безналичный', 'Безналичный'),
    ]

    STATUSORDER_CHOICES2 = [
        ('Выполнен', 'Выполнен'),
        ('В работе', 'В работе'),
        ('Новый', 'Новый'),
    ]

    klient = models.CharField(max_length=500)
    sotrudnik = models.ForeignKey(Customers, on_delete=models.CASCADE)
    tovar = models.CharField(max_length=1000)
    number = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата продажи')
    pay = models.CharField(choices=STATUSORDER_CHOICES, verbose_name='Вид оплаты')
    status = models.CharField(choices=STATUSORDER_CHOICES2, verbose_name='Статус заказа')


class History(models.Model):
    STATUS_CHOICES = [
        ('Выполнен', 'Выполнен'),
        ('В работе', 'В работе'),
        ('Новый', 'Новый'),
    ]

    change_date = models.DateTimeField(auto_now_add=True)
    number_order = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    old_status = models.CharField(choices=STATUS_CHOICES)
    new_status = models.CharField(choices=STATUS_CHOICES)