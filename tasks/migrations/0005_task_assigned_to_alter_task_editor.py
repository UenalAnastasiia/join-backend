# Generated by Django 4.0.6 on 2024-02-11 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0004_choices_task_priority_task_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editor', to=settings.AUTH_USER_MODEL),
        ),
    ]
