# Generated by Django 4.2.4 on 2023-10-06 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='duedate',
        ),
    ]