# Generated by Django 3.2.7 on 2021-11-12 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userapp', '0002_uploadmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadmodel',
            name='upload',
            field=models.ImageField(upload_to='uploads', verbose_name='Upload Confirmation'),
        ),
    ]
