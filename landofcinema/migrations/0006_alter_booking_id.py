# Generated by Django 4.1.5 on 2023-01-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landofcinema', '0005_alter_booking_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]