# Generated by Django 4.0.5 on 2022-06-15 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('futbolec', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='C_equipos',
            new_name='Equipos',
        ),
        migrations.RenameField(
            model_name='campeonato',
            old_name='nombre_c',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='equipo',
            old_name='nombre_e',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='jugador',
            old_name='nombre_j',
            new_name='nombre',
        ),
    ]
