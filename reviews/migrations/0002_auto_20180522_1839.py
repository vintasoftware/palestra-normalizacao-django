# Generated by Django 2.0.5 on 2018-05-22 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzarias', '0002_auto_20180522_1636'),
        ('pizzas', '0001_initial'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reviewpizza',
            unique_together={('sabor', 'pizzaria')},
        ),
    ]