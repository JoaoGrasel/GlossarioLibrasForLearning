# Generated by Django 2.0.3 on 2018-04-13 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Glossario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinal',
            name='postado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sinal',
            name='descricao',
            field=models.TextField(),
        ),
    ]