# Generated by Django 5.0.6 on 2024-06-23 18:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0003_rooms_roombooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='availability',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='rooms',
            name='room_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rooms',
            name='room_type',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
