# Generated by Django 3.2.5 on 2021-08-03 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discs', '0007_alter_disc_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disc',
            name='color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='disc',
            name='disc_class',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='disc',
            name='img_alt',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='disc',
            name='plastic',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
