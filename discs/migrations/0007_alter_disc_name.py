# Generated by Django 3.2.5 on 2021-08-03 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discs', '0006_alter_disc_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disc',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
