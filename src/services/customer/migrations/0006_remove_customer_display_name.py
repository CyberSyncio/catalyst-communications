# Generated by Django 5.1.2 on 2024-11-09 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_alter_customer_currency_alter_customer_customer_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='display_name',
        ),
    ]
