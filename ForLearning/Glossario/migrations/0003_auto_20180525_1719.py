# Generated by Django 2.0.5 on 2018-05-25 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Glossario', '0002_remove_perfil_contatos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='nome_empresa',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='telefone',
        ),
        migrations.AddField(
            model_name='perfil',
            name='curso',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='universidade',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
