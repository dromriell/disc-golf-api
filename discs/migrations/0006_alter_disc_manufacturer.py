# Generated by Django 3.2.5 on 2021-08-03 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discs', '0005_auto_20210801_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disc',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='discs.manufacturer'),
        ),
    ]
