# Generated by Django 4.1 on 2022-08-21 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='headline',
        ),
    ]