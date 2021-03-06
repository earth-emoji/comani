# Generated by Django 2.2.4 on 2019-09-03 21:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190829_0120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='lenght',
            new_name='length',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='catalog.Product'),
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default=uuid.uuid1, unique=True)),
                ('breed', models.CharField(blank=True, max_length=255, unique=True)),
                ('type', models.CharField(blank=True, choices=[('Companion', 'Companion'), ('Mixed', 'Mixed'), ('Guard', 'Guard'), ('Hunting', 'Hunting'), ('Pastoral', 'Pastoral'), ('Sled', 'Sled'), ('Other', 'Other')], max_length=60)),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='dogs', to='catalog.Product')),
            ],
        ),
    ]
