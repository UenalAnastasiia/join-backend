# Generated by Django 5.0.2 on 2024-02-18 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board_status', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardstatus',
            name='name',
        ),
    ]