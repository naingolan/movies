# Generated by Django 4.1.5 on 2023-01-19 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landofcinema', '0003_alter_movie_release_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Theatre',
            new_name='Theater',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='theatre',
            new_name='theater',
        ),
        migrations.RenameField(
            model_name='screen',
            old_name='theatre',
            new_name='theater',
        ),
    ]