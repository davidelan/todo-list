# Generated by Django 4.2.14 on 2024-08-10 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_todo_list_list_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo_list',
            name='list_id',
        ),
    ]
