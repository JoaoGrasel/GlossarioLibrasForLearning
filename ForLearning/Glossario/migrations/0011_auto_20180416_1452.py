# Generated by Django 2.0.3 on 2018-04-16 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Glossario', '0010_auto_20180416_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinal',
            name='postado',
            field=models.BooleanField(default=False),
        ),
    ]
