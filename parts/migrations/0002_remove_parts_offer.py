# Generated by Django 3.1.1 on 2020-10-03 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parts',
            name='offer',
        ),
    ]
