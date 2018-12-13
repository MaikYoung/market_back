# Generated by Django 2.0.9 on 2018-12-10 14:11

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('lat', models.DecimalField(decimal_places=6, default=Decimal('0'), max_digits=10)),
                ('lng', models.DecimalField(decimal_places=6, default=Decimal('0'), max_digits=10)),
                ('adress', models.TextField()),
                ('schedule_open', models.IntegerField()),
                ('schedule_close', models.IntegerField()),
                ('work_days', models.CharField(choices=[('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THU', 'Thursday'), ('FRI', 'Friday'), ('SAT', 'Saturday'), ('SUN', 'Sunday')], max_length=20)),
                ('is_closed', models.BooleanField(default=True)),
                ('twitter', models.CharField(max_length=200)),
                ('facebook', models.CharField(max_length=200)),
                ('instagram', models.CharField(max_length=100)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]