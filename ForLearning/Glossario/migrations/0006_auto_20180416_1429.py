

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Glossario', '0005_auto_20180416_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinal',
            name='arquivo_video',
            field=models.FileField(upload_to='Glossario/static/Glossario/videos'),
        ),
    ]
