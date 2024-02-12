# Generated by Django 4.0.6 on 2024-02-11 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.IntegerField(choices=[(1, 'Frontend'), (2, 'Backend'), (3, 'Design'), (4, 'Marketing'), (5, 'Backoffice'), (6, 'Other')], null=True),
        ),
    ]