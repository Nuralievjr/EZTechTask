# Generated by Django 3.1.7 on 2021-03-03 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210303_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='fill_type',
        ),
    ]
