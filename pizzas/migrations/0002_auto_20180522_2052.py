# Generated by Django 2.0.5 on 2018-05-22 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saborpizza',
            name='nome',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
