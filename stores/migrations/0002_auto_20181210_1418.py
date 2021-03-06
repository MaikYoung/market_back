# Generated by Django 2.0.9 on 2018-12-10 14:18

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='work_days',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)]), blank=True, help_text='Separate using a comma', null=True, size=None),
        ),
    ]
