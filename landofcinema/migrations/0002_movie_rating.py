# Generated by Django 4.1.5 on 2023-01-17 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("landofcinema", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="rating",
            field=models.FloatField(default=0.0),
        ),
    ]
