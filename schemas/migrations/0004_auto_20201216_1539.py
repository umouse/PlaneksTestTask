# Generated by Django 3.1.4 on 2020-12-16 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0003_auto_20201216_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='column',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='column',
            name='order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='column',
            name='range_from',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='column',
            name='range_to',
            field=models.IntegerField(null=True),
        ),
    ]
