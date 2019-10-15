# Generated by Django 2.2.5 on 2019-10-12 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20190903_2103'),
    ]

    operations = [
        migrations.CreateModel(
            name='DogBreed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, unique=True)),
                ('type', models.CharField(blank=True, choices=[('Companion', 'Companion'), ('Mixed', 'Mixed'), ('Guard', 'Guard'), ('Hunting', 'Hunting'), ('Pastoral', 'Pastoral'), ('Sled', 'Sled'), ('Other', 'Other')], max_length=60)),
            ],
        ),
        migrations.RenameField(
            model_name='product',
            old_name='is_aux',
            new_name='is_dog',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='type',
        ),
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='dogs', to='catalog.DogBreed'),
        ),
    ]