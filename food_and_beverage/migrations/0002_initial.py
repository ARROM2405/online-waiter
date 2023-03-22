# Generated by Django 4.1.7 on 2023-03-17 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('food_and_beverage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='order',
            field=models.ManyToManyField(to='orders.order'),
        ),
        migrations.AddField(
            model_name='beverage',
            name='order',
            field=models.ManyToManyField(to='orders.order'),
        ),
    ]
