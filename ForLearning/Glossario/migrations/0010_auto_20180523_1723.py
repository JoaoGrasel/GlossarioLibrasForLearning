# Generated by Django 2.0.5 on 2018-05-23 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Glossario', '0009_auto_20180523_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinal',
            name='temas',
            field=models.ManyToManyField(to='Glossario.Tema'),
        ),
    ]