from django.db import models
from django.utils import timezone


class Schema(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.TextField()
    column_separator = models.CharField(max_length=2)
    string_separator = models.CharField(max_length=2)


class Columns(models.Model):
    schema_id = models.ForeignKey(Schema, on_delete=models.CASCADE)
    name = models.TextField()
    range_from = models.IntegerField()
    range_to = models.IntegerField()
    order = models.IntegerField()

    FULL_NAME = 'Full name'
    JOB = 'Job'
    EMAIL = 'Email'
    DOMAIN_NAME = 'Domain name'
    PHONE_NUMBER = 'Phone number'
    COMPANY_NAME = 'Company name'
    TEXT = 'Text'
    INTEGER = 'Integer'
    ADDRESS = 'Address'
    DATE = 'Date'

    COLUMN_TYPE_CHOICES = [
        (FULL_NAME, 'Full name'),
        (JOB, 'Job'),
        (EMAIL, 'Email'),
        (DOMAIN_NAME, 'Domain name'),
        (PHONE_NUMBER, 'Phone number'),
        (COMPANY_NAME, 'Company name'),
        (TEXT, 'Text'),
        (INTEGER, 'Integer'),
        (ADDRESS, 'Address'),
        (DATE, 'Date')
    ]
    column_types = models.CharField(
        max_length=12,
        choices=COLUMN_TYPE_CHOICES
    )

