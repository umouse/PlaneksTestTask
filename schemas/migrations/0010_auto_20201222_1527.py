# Generated by Django 3.1.4 on 2020-12-22 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0009_auto_20201222_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='status',
            field=models.CharField(choices=[('Ready', 'Ready'), ('Processing', 'Processing')], max_length=15),
        ),
    ]