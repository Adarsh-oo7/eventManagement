# Generated by Django 5.0.6 on 2024-06-23 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0006_remove_roombooking_cus_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='roombooking',
            name='cus_phone',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]
