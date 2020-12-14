# Generated by Django 3.1.4 on 2020-12-14 15:15

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
            name='Schema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('column_separator', models.CharField(max_length=2)),
                ('string_separator', models.CharField(max_length=2)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Columns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('range_from', models.IntegerField()),
                ('range_to', models.IntegerField()),
                ('order', models.IntegerField()),
                ('column_types', models.CharField(choices=[('Full name', 'Full name'), ('Job', 'Job'), ('Email', 'Email'), ('Domain name', 'Domain name'), ('Phone number', 'Phone number'), ('Company name', 'Company name'), ('Text', 'Text'), ('Integer', 'Integer'), ('Address', 'Address'), ('Date', 'Date')], max_length=12)),
                ('schema_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schemas.schema')),
            ],
        ),
    ]
