# Generated by Django 3.1.4 on 2020-12-29 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0011_auto_20201228_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='range_from',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='column',
            name='range_to',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
