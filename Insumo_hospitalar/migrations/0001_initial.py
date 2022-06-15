# Generated by Django 4.0.5 on 2022-06-15 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insumo_hospitalar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=100)),
                ('Valor_custo', models.FloatField(max_length=100)),
                ('Valor_repasse', models.CharField(max_length=100)),
                ('Vencimento', models.DateField(max_length=100)),
                ('Quantidade', models.CharField(max_length=100)),
                ('Marca', models.FloatField(max_length=100)),
            ],
        ),
    ]
