# Generated by Django 2.0.5 on 2018-05-22 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzarias', '0002_auto_20180522_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzaria',
            name='nome',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
