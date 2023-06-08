# Generated by Django 4.1.7 on 2023-06-04 20:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0003_order_comment_table_status_alter_table_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="last_update_timestamp",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="submit_timestamp",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
