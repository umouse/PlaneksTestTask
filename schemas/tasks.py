import csv

from django.conf import settings
from faker import Faker
from fake_csv.celery import app

@app.task
def generate_data_task(dataset_id):
    from schemas.models import Schema, DataSet, Column

    fake = Faker()

    dataset = DataSet.objects.filter(id=dataset_id).first()
    if not dataset:
        return
    schema = Schema.objects.filter(id=dataset.schema_id).first()
    columns = Column.objects.filter(schema=schema.id).values()
    delimeter = schema.column_separator
    quotechar = schema.string_character

    row_number = dataset.rows
    header = []
    all_rows = []
    for column in columns:
        header.append(column["name"])

    for row in range(row_number):
        raw_row = []
        for column in columns:
            column_type = column["column_type"]
            if column_type == Column.FULL_NAME:
                data = fake.name()
            elif column_type == Column.JOB:
                data = fake.job()
            elif column_type == Column.EMAIL:
                data = fake.email()
            elif column_type == Column.DOMAIN_NAME:
                data = fake.domain_name()
            elif column_type == Column.PHONE_NUMBER:
                data = fake.phone()
            elif column_type == Column.COMPANY_NAME:
                data = fake.company()
            elif column_type == Column.TEXT:
                data = fake.text()
            elif column_type == Column.INTEGER:
                data = fake.random_int()
            elif column_type == Column.ADDRESS:
                data = fake.address()
            elif column_type == Column.DATE:
                data = fake.date()
            else:
                data = None
            raw_row.append(data)
        all_rows.append(raw_row)

    with open(f'{settings.MEDIA_ROOT}schema_{schema.id}dataset_{dataset_id}.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=delimeter, quotechar=quotechar, quoting=csv.QUOTE_ALL)
        writer.writerow(header)
        writer.writerows(all_rows)

        dataset.status = dataset.Status.READY
        dataset.save()

