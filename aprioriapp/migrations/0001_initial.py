# Generated by Django 4.2.7 on 2023-12-28 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.CharField(max_length=100)),
                ('item_name', models.CharField(max_length=150)),
                ('order_time', models.DateTimeField()),
                ('ccustomer', models.CharField(max_length=100)),
                ('qty', models.CharField(max_length=50)),
                ('currency', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=150)),
            ],
        ),
    ]