# Generated by Django 2.0.5 on 2018-06-07 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Glossario', '0008_auto_20180606_1718'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='membro',
            new_name='glossarios',
        ),
        migrations.RenameField(
            model_name='perfil',
            old_name='responsavel',
            new_name='glossarios_responsavel',
        ),
    ]