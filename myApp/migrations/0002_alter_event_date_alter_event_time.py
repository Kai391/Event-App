# Generated by Django 4.0 on 2021-12-26 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='Time',
            field=models.CharField(max_length=100),
        ),
    ]