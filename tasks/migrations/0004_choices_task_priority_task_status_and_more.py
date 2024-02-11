# Generated by Django 4.0.6 on 2024-02-11 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.IntegerField(choices=[(1, 'urgent'), (2, 'medium'), (3, 'low')], null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(1, 'To do'), (2, 'In progress'), (3, 'Awaiting Feedback'), (4, 'Done')], null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.IntegerField(choices=[(1, 'Frontend'), (2, 'Backend'), (3, 'Design'), (4, 'Marketing'), (5, 'Backoffice'), (6, 'Other')], null=True),
        ),
    ]
