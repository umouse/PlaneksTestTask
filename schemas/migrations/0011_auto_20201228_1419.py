# Generated by Django 3.1.4 on 2020-12-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0010_auto_20201222_1527'),
    ]

    operations = [
        migrations.RenameField(
            model_name='column',
            old_name='column_types',
            new_name='column_type',
        ),
        migrations.AlterField(
            model_name='column',
            name='order',
            field=models.PositiveIntegerField(null=True),
        ),
    ]