# Generated by Django 2.2.5 on 2019-10-12 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190829_0120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='customer_type',
        ),
    ]