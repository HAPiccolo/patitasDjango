# Generated by Django 5.1 on 2024-09-03 01:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adoptante',
            fields=[
                ('id_adoptate', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=200)),
                ('edad', models.CharField(max_length=2)),
                ('dni', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
                ('dni', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id_especie', models.IntegerField(primary_key=True, serialize=False)),
                ('especie', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Adopciones',
            fields=[
                ('id_adopciones', models.IntegerField(primary_key=True, serialize=False)),
                ('id_adoptante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.adoptante')),
                ('id_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id_mascota', models.IntegerField(primary_key=True, serialize=False)),
                ('estado', models.BinaryField(default=1)),
                ('id_adopciones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.adopciones')),
                ('id_especie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.especie')),
            ],
        ),
        migrations.CreateModel(
            name='Caracteristicas',
            fields=[
                ('id_caracteristica', models.IntegerField(primary_key=True, serialize=False)),
                ('edad', models.CharField(max_length=2)),
                ('discapacidad', models.CharField(max_length=500)),
                ('raza', models.CharField(max_length=50)),
                ('sexo', models.CharField(choices=[('macho', 'Macho'), ('hembra', 'Hembra')], default='Macho', max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_ingreso', models.DateTimeField()),
                ('foto', models.ImageField(upload_to='')),
                ('id_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mascotas')),
            ],
        ),
        migrations.AddField(
            model_name='adopciones',
            name='id_mascota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.mascotas'),
        ),
    ]
