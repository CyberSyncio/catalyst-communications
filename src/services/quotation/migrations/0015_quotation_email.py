# Generated by Django 5.1.2 on 2024-12-13 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quotation", "0014_alter_quotation_project"),
    ]

    operations = [
        migrations.AddField(
            model_name="quotation",
            name="email",
            field=models.EmailField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
