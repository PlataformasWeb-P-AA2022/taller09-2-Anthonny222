# Generated by Django 4.0.5 on 2022-06-15 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('futbolec', '0002_rename_c_equipos_equipos_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='usu_twitter',
            new_name='twitter',
        ),
    ]