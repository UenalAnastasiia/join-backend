# Generated by Django 5.0.2 on 2024-02-14 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_alter_task_priority_alter_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='color',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
