# Generated by Django 4.1.7 on 2023-04-05 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("staff", "0001_initial"),
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="table",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="orders",
                to="orders.table",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="waiter",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="order",
                to="staff.waiter",
            ),
        ),
    ]
