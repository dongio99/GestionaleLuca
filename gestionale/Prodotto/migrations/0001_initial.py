# Generated by Django 5.0.1 on 2024-01-23 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prodotto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codice', models.CharField(max_length=255, unique=True)),
                ('nome', models.CharField(max_length=255)),
                ('produttore', models.CharField(blank=True, max_length=255)),
                ('soglia_riordino', models.IntegerField(default=-1)),
                ('categoria', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
