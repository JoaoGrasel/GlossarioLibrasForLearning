# Generated by Django 2.0.4 on 2018-05-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Glossario', '0010_auto_20180523_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='glossario',
            name='postado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tema',
            name='postado',
            field=models.BooleanField(default=False),
        ),
    ]
