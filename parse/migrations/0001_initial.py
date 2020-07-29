# Generated by Django 3.0.8 on 2020-07-15 01:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='user/', validators=[django.core.validators.FileExtensionValidator(['xlsx'])])),
                ('upload_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
