# Generated by Django 4.0 on 2021-12-26 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
