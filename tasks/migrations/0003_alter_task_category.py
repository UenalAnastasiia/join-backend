# Generated by Django 4.0.6 on 2024-02-11 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.IntegerField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Design', 'Design'), ('Marketing', 'Marketing'), ('Backoffice', 'Backoffice'), ('Other', 'Other')], null=True),
        ),
    ]
