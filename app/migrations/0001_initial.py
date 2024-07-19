# Generated by Django 5.0.6 on 2024-07-18 03:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('disponible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Colores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('disponible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Condicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('disponible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('disponible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('disponible', models.BooleanField()),
                ('categoria', models.ForeignKey(default='None', on_delete=django.db.models.deletion.PROTECT, to='app.categoria')),
                ('colores', models.ForeignKey(default='None', on_delete=django.db.models.deletion.PROTECT, to='app.colores')),
                ('condicion', models.ForeignKey(default='None', on_delete=django.db.models.deletion.PROTECT, to='app.condicion')),
                ('marca', models.ForeignKey(default='None', on_delete=django.db.models.deletion.PROTECT, to='app.marca')),
            ],
        ),
    ]
