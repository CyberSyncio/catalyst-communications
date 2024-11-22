# Generated by Django 5.1.2 on 2024-11-19 16:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0013_alter_project_budget_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('BUDGET_ASSIGN', 'Budget Assigned to Project'), ('TRANSFER', 'Funds Transfer')], max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('source', models.CharField(blank=True, max_length=255, null=True)),
                ('destination', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.project')),
            ],
        ),
    ]
