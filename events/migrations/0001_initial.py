# Generated by Django 4.1.5 on 2023-01-14 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_event', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('poster', models.ImageField(upload_to='poster/%Y')),
                ('tech_info', models.FileField(blank=True, null=True, upload_to='tech_files')),
                ('result', models.URLField(blank=True, db_index=True)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
                ('participants', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.TextField(max_length=4)),
                ('chip', models.TextField(max_length=2)),
                ('num_chip', models.TextField(max_length=10)),
                ('agree', models.BooleanField()),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.events')),
                ('participant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
