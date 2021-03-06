# Generated by Django 2.0.5 on 2018-05-22 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('tem_lactose', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SaborPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('ingredientes', models.ManyToManyField(related_name='pizzas', to='pizzas.Ingrediente')),
            ],
        ),
    ]
