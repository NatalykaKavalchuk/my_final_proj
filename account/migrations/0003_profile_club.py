# Generated by Django 4.1.5 on 2023-03-15 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_alter_profile_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="club",
            field=models.CharField(default="без клуба", max_length=100, null=True),
        ),
    ]
