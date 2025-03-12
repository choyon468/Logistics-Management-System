# Generated by Django 4.2.19 on 2025-03-12 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_lms_worker_custom_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='lmsworker',
            name='card',
            field=models.CharField(choices=[('visa', 'Visa'), ('mc', 'Master Card'), ('ae', 'American Express')], default='visa', max_length=10),
        ),
    ]
