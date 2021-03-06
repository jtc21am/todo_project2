# Generated by Django 3.2.12 on 2022-04-26 18:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myToDo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='Date & Time Stamp'),
        ),
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.TextField(help_text='Note regarding selected task'),
        ),
        migrations.AlterField(
            model_name='note',
            name='task',
            field=models.ForeignKey(help_text='Attach a note for this task', on_delete=django.db.models.deletion.CASCADE, to='myToDo.todoitem'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='tag',
            field=models.CharField(help_text='Tag for this Task', max_length=50),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='complete',
            field=models.BooleanField(default=False, help_text='Is Task completed or not'),
        ),
        migrations.AlterField(
            model_name='todotags',
            name='tag',
            field=models.ForeignKey(help_text='Attach', on_delete=django.db.models.deletion.CASCADE, to='myToDo.tags'),
        ),
    ]
