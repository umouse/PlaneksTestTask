from django.contrib import admin
from schemas.models import Schema, Column

admin.site.register(Schema)
admin.site.register(Column)
