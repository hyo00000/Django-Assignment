# Generated by Django 5.1 on 2024-09-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_todo_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='start_date',
            field=models.DateField(null=True),
        ),
    ]
