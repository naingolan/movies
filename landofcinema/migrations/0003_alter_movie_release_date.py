# Generated by Django 4.1.5 on 2023-01-19 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landofcinema', '0002_movie_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
