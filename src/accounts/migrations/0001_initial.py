# Generated by Django 2.2.4 on 2019-08-29 01:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default=uuid.uuid1, unique=True)),
                ('customer_type', models.CharField(blank=True, choices=[('Dispensary', 'Dispensary'), ('Grower', 'Grower'), ('Processor', 'Processor'), ('Tester', 'Tester')], max_length=30)),
            ],
            options={
                'verbose_name': 'customer',
                'verbose_name_plural': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default=uuid.uuid1, unique=True)),
                ('business_name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'vendor',
                'verbose_name_plural': 'vendors',
            },
        ),
    ]
