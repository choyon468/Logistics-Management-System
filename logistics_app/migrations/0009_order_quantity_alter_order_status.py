# Generated by Django 4.2.19 on 2025-03-08 22:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics_app', '0008_merge_20250307_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Received', 'Received'), ('In-Transit', 'In Transit'), ('Delivered', 'Delivered')], default='Received', max_length=50),
        ),
    ]
