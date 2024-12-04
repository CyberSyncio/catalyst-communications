# Generated by Django 5.1.3 on 2024-12-04 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0009_alter_ledger_transaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='transaction_type',
            field=models.CharField(choices=[('BUDGET_ASSIGN', 'Budget Assigned to Project'), ('TRANSFER', 'Funds Transfer'), ('CREATE_LOAN', 'Loan Created'), ('RETURN_LOAN', 'Loan Returned'), ('MISC_LOAN_CREATE', 'Miscellaneous Loan'), ('MISC_LOAN_RETURN', 'Miscellaneous Loan Return'), ('CREATE_EXPENSE', 'Expense Created'), ('MISC_EXPENSE', ' Miscellaneous Expense Created'), ('ADD_CASH', 'Added Cash'), ('INVOICE_PAYMENT', 'Invoice Paid'), ('ADD_ACC_BALANCE', 'Balance Added')], max_length=50),
        ),
    ]
