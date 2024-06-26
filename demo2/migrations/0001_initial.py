# Generated by Django 5.0.6 on 2024-06-13 18:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=500)),
                ('phone', models.CharField(max_length=500)),
                ('adres', models.CharField(max_length=500)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=500)),
                ('category', models.CharField(choices=[('лекарство', 'лекарство'), ('медицинское изделие', 'медицинское изделие')], verbose_name='Категория')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('production_date', models.DateTimeField(auto_now_add=True)),
                ('manufacturer', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('klient', models.CharField(max_length=500)),
                ('tovar', models.CharField(max_length=1000)),
                ('number', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.EmailField(blank=True, max_length=500, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата продажи')),
                ('pay', models.CharField(choices=[('Наличный', 'Наличный'), ('Безналичный', 'Безналичный')], verbose_name='Вид оплаты')),
                ('status', models.CharField(choices=[('Выполнен', 'Выполнен'), ('В работе', 'В работе'), ('Новый', 'Новый')], verbose_name='Статус заказа')),
                ('sotrudnik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo2.customers')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_date', models.DateTimeField(auto_now_add=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('old_status', models.CharField(choices=[('Выполнен', 'Выполнен'), ('В работе', 'В работе'), ('Новый', 'Новый')])),
                ('new_status', models.CharField(choices=[('Выполнен', 'Выполнен'), ('В работе', 'В работе'), ('Новый', 'Новый')])),
                ('number_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo2.order')),
            ],
        ),
    ]
