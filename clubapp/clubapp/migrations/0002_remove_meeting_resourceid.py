# Generated by Django 2.2 on 2019-05-16 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='resourceid',
        ),
    ]