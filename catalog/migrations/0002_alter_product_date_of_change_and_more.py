# Generated by Django 4.2.1 on 2023-05-28 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_of_change',
            field=models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name='дата создания'),
        ),
    ]
