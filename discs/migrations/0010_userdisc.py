# Generated by Django 3.2.5 on 2021-08-03 16:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_profile_disc_bag'),
        ('discs', '0009_disc_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDisc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=50, null=True)),
                ('custom_speed', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(14), django.core.validators.MinValueValidator(1)])),
                ('custom_glide', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(1)])),
                ('custom_turn', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(-5)])),
                ('custom_fade', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('disc', models.ForeignKey(default='DELETED DISC', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='user_disc', to='discs.disc')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disc_bag', to='profiles.profile')),
            ],
        ),
    ]
