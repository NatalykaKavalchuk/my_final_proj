# Generated by Django 4.1.5 on 2023-01-15 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='agree',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='chip',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='distance',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='num_chip',
        ),
    ]
