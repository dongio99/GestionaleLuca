# Generated by Django 5.0.1 on 2024-01-23 21:32

import Magazzino.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Prodotto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magazzino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantita', models.IntegerField(validators=[Magazzino.models.validate_positive])),
                ('prodotto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Prodotto.prodotto')),
            ],
        ),
    ]
