# Generated by Django 2.0.5 on 2018-05-22 16:10

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pizzas', '0001_initial'),
        ('pizzarias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewPizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avaliacao', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('pizzaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzarias.Pizzaria')),
                ('sabor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzas.SaborPizza')),
            ],
        ),
    ]
