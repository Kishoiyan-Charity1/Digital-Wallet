# Generated by Django 4.0.6 on 2022-08-25 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0008_rename_loan_type_loan_loan_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='Card_name',
            new_name='card_name',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='Card_number',
            new_name='card_number',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='Card_status',
            new_name='card_status',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='Date_issued',
            new_name='date_issued',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='Expiry_date',
            new_name='expiry_date',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='Security_code',
            new_name='security_code',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='Signature',
            new_name='signature',
        ),
        migrations.RenameField(
            model_name='loan',
            old_name='Due_date',
            new_name='due_date',
        ),
        migrations.RenameField(
            model_name='loan',
            old_name='Interest',
            new_name='interest',
        ),
        migrations.RenameField(
            model_name='loan',
            old_name='Interest_rate',
            new_name='interest_rate',
        ),
        migrations.RenameField(
            model_name='loan',
            old_name='Loan_status',
            new_name='loan_status',
        ),
        migrations.RenameField(
            model_name='loan',
            old_name='Payment_date',
            new_name='payment_date',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='Message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='reward',
            old_name='Points',
            new_name='points',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='destination',
            new_name='account_destination',
        ),
    ]
