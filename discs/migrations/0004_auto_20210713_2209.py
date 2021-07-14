# Generated by Django 3.2.5 on 2021-07-14 02:09

import discs.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discs', '0003_disc_plastic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('established', models.IntegerField(default=2021, validators=[discs.models.max_year_validator, django.core.validators.MinValueValidator(1900)])),
                ('location', models.CharField(max_length=25)),
                ('is_defunct', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='disc',
            name='manufacturer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='discs.manufacturer'),
        ),
    ]