# Generated by Django 3.2.7 on 2021-11-23 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0005_auto_20211117_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadconfirmationmodel',
            name='payment_method',
            field=models.CharField(choices=[('ussd', 'USSD'), ('deposit', 'Deposit'), ('POS', 'POS_Transfer')], default=None, max_length=50, verbose_name='Mode of Payment'),
            preserve_default=False,
        ),
    ]
